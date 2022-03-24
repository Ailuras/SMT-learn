import os
import sys

path = os.getcwd()
pl = path.split("\\",-1)

if(pl[-1]=="QF_LRA"):
    # in folder of QF_LRA
    from basics import RealVariable, calculation, constraint, l, u, v, constant_name, is_zero
else:
    # in folder of SMT_Solver
    from solver.theory.QF_LRA.basics import RealVariable, calculation, constraint, l, u, v, constant_name, is_zero

from decimal import Decimal, getcontext

import copy

prec = 8

# feasible simplex linear solver
class solver(object):
    def __init__(self):
        self.origin = {}
        self.matrix = []
        # problem variables index from 1 to inf 
        # the index of prob variable is fixed, so the order is useful for setting constraints
        self.prob_variables = [RealVariable(name='__placeholder', val=0)]
        # auxiliary variables index from -1 to -inf
        self.auxi_variables = [RealVariable(name='__placeholder', val=0)]
        # auxiliary variable map, if an appended constraint, return the index
        # map constraint to index of auxi_variables
        self.auxi_var_Maps = {}

        # map variable name to index
        self.varMaps = {}
        # map formula(calculation) to row index
        self.formulaMaps = {}
        # map formula side of constraint to literals, a one-to-list function
        self.form_lits = {}

        # the coresponding variable of matrix:
        # row for Basic variable; col for NonBasic variable
        self.rows = []
        self.cols = []

        # for incremental problems, if solved then self.solved = True
        self.solved = False
        # add history for _Recover
        self.add_history = []
        # record state: -1, unknown; 0, false; 1, true
        self.state = -1

    def reset(self):
        # self.origin = {} # don't need to delete
        self.matrix = []
        self.rows = []
        self.cols = [i for i in range(1, len(self.prob_variables))]
        self.solved = False
        self.state = -1
        
        # delete all auxiliary variables, not really delete
        # for may use next time
        self._aux_del_all()
        # this must reset, if not {(x+y): -1} may append {(x+y): 1}
        self.form_lits = {}
        self.add_history = []

    def _aux_del_all(self):
        for i in self.auxi_variables:
            self.delete(i)

    def NewAuxVar(self):
        idx=len(self.auxi_variables)
        var = RealVariable(name="__s"+str(idx))
        self.auxi_variables.append(var)
        return -idx

    def NewProVar(self, name):
        idx=len(self.prob_variables)
        var = RealVariable(name=name)
        self.prob_variables.append(var)
        self.varMaps[name]=idx
        return idx

    def get_variable(self, idx):
        if(idx<0): return self.auxi_variables[abs(idx)]
        else: return self.prob_variables[idx]

    def solve(self):
        # now only return the element take part in simplex
        cons_conf = []
        self.solved = True
        vio = self.Violation()
        while True:
            if(vio==-1): break
            i = vio
            xi = self.rows[i]
            cons_conf.append(xi)
            varxi = self.get_variable(xi)
            # if violate lowerBound, cannot violate upperBound
            # check if varxi.lowerbound > varxi.upperbound
            if(varxi.violateLowerBound()):
                j = self.selectNBVar(i, False)
                if(j==-1): 
                    self.state = 0
                    return self.make_conflicts(cons_conf), False
                self.pivotAndUpdate(i, j, l(varxi))
            elif(varxi.violateUpperBound()):
                j = self.selectNBVar(i, True)
                if(j==-1): 
                    self.state = 0
                    return self.make_conflicts(cons_conf), False
                self.pivotAndUpdate(i, j, u(varxi))
            
            vio=self.Violation()
        
        self.state = 1
        return None, True

    def make_conflicts(self, cons_confs):
        ans = []
        for i in cons_confs:
            ans += self.form_lits[i]
        return ans

    def selectNBVar(self, i, dir):
        # the rule is select the smallest index of variable
        # in this implementation, we must first choose positive variable(problem variable)
        # after it, we are able to choose a variable of negative variable(auxiliary variable) 
        #    1 2 3
        # -1 x x x
        # -2 x x x
        # -3 x x x
        # at first time, the matrix is like above.
        # the order rule is we can only choose a pair of xi(Basic),xj(NonBasic) with xi<xj
        # e.g. (-3,1) can pivot
        #    -3 2 3
        # -1  x x x
        # -2  x x x
        #  1  x x x
        # at this time, (-2, -3) is not allowed, because (-2, 2) first
        xi = self.rows[i]
        varxi = self.get_variable(xi)
        candidate={}

        change = 0
        if(dir):
            # val(x) > ux; can update with a new value
            change = u(varxi) - v(varxi)
            for j in range(len(self.cols)):
                # if(is_zero(self.matrix[i][j])): continue
                if(is_zero(self.matrix[i][j])): continue
                xj = self.cols[j]
                varxj = self.get_variable(xj)
                if((self.matrix[i][j]<0 and varxj.upperUpperBound(change/self.matrix[i][j])) or
                 (self.matrix[i][j]>0 and varxj.lowerLowerBound(change/self.matrix[i][j]))):
                    
                    candidate[xj] = j
        else:
            # val(x) < lx; can update with a new value
            change = l(varxi) - v(varxi)
            for j in range(len(self.cols)):
                # if(is_zero(self.matrix[i][j]==0)): continue
                if(is_zero(self.matrix[i][j])): continue
                xj = self.cols[j]
                varxj = self.get_variable(xj)
                if((self.matrix[i][j]>0 and varxj.upperUpperBound(change/self.matrix[i][j])) or 
                (self.matrix[i][j]<0 and varxj.lowerLowerBound(change/self.matrix[i][j]))):
                    
                    candidate[xj] = j
        
        # iff no variable can be chosen
        if(len(candidate)==0): return -1
        # else check whether is a index bigger than 0 <=> a problem variable
        probVars = {}
        for tmp in candidate:
            if(tmp>0):
                probVars[tmp]=candidate[tmp]
        
        if(len(probVars)==0):
            # not a prob variable, then choose a auxiliary variable
            # if not a auxiliary variable, it will return former
            keys = sorted(candidate.keys())
            return candidate[keys[0]]
        else:
            keys = sorted(probVars.keys())
            return probVars[keys[0]]
 
    def Violation(self):
        ans = {}
        # for i in range(len(self.rows)-1,-1,-1):
        for i in range(len(self.rows)):
            x = self.rows[i]
            if(self.get_variable(x).violateBound()):
                return i
        return -1

    def add_variable(self, name):
        cx = self.NewProVar(name)
        self.cols.append(cx)
    
    def _Recovers(self):
        # important!!!: if appending to the tableau, the former operations on it is still,
        # so it must careful about it -> function updateAppending(): just recover the matrix for self.origin, rows from self.auxi_variables
        self.state = -1
        self.rows = copy.deepcopy(self.add_history)
        self.cols = [i for i in range(1, len(self.prob_variables))]
        self.matrix = []
        for i in self.rows:
            self.matrix.append(copy.deepcopy(self.origin[i]))
            self.recover_value(i)

    def add_constraint(self, cons, lit):
        invert=(lit<0)
        # input: cons, type of constraint
        # a special case, if all zero in variables side or whole constraint
        if(self.state!=0 and cons.sat!=-1):
            # only wrong case will set the state
            if((not invert and cons.sat==0) or (invert and cons.sat==1)):
                self.state = 0
                return [lit], False
        # check if there is a variable has been appended
        formula = []
        lent = len(self.prob_variables)
        # make list with the variable order
        for i in range(1, lent):
            var = str(self.prob_variables[i]) # variable name
            if(var in cons.formula):
                formula.append(cons.formula[var])
            else:
                formula.append(0)
        cont = -cons.formula[constant_name]
        opr = cons.operator
        varsides = cons.formula.variables()
        if(varsides in self.formulaMaps):
            # the formula has set
            idx = self.formulaMaps[varsides]
            var = self.get_variable(idx)
            if(var.is_unset()):
                # have delete, but still in self.origin etc.
                self.matrix.append(copy.deepcopy(self.origin[idx]))
                self.rows.append(idx)
                self.recover_value(idx)

            if(idx not in self.form_lits):
                # for have reset, it is None
                self.form_lits[idx] = []
            self.form_lits[idx].append(lit)

            if(self.set_bound(idx, cont, opr, invert)):
                # set bound success, nothing happened
                pass
            else:
                # add constraint error:a theory implication for a set of 
                # the same formula(var side of constraint) with conflicts of setBound
                ans = []
                for i in self.form_lits[idx]:
                    ans.append(i)
                # don't need to set self.solved, because 
                return ans, False
            
            # conflicts haven't happened, return None
            return None, True

        if(self.solved): 
            self._Recovers() # reform self.matrix
            self.solved = False
        bx = self.NewAuxVar()
        self.origin[bx]=formula
        self.recover_value(bx)
        self.matrix.append(copy.deepcopy(formula))
        self.rows.append(bx)
        # add to maps
        self.formulaMaps[varsides] = bx
        # to get literals like this: self.from_lits[self.rfomulaMaps[bx]]->list of literals
        self.form_lits[bx] = []
        self.form_lits[bx].append(lit)
        self.add_history.append(bx)

        # set bound, at first, must set success!
        self.set_bound(bx, cont, opr, invert)
        
        # conflicts haven't happened, return None
        return None, True

    def recover_value(self, idx):
        # input: basic variable index
        # recover the value of var(idx)
        new_var = self.get_variable(idx)
        s = 0
        formula = self.origin[idx]
        # important!!! for incremental, if it is second or other call, we need to recover the value
        for i in range(len(self.cols)):
            s+=formula[i]*(self.get_variable(self.cols[i]).get_value())
        new_var.setValue(s)

    def set_bound(self, idx, cont, opr, invert):
        new_var = self.get_variable(idx)
        if(not invert):
            # set bound of new_var without ==
            if(opr == "<="):
                return new_var.setUpperBound(cont)
            elif(opr == "<"):
                return new_var.setUpperBound(cont, True)
            elif(opr == "="):
                # = -> <= and >=
                raise SyntaxError("operation is not supported!")
            elif(opr == ">="):
                return new_var.setLowerBound(cont)
            elif(opr == ">"):
                return new_var.setLowerBound(cont, True)
            else:
                # not equal operator
                raise SyntaxError("operation is not supported!")
        else:
            if(opr == "<="):
                return new_var.setLowerBound(cont, True)
            elif(opr == "<"):
                return new_var.setLowerBound(cont)
            elif(opr == "="):
                # not equal is not support
                raise SyntaxError("operation is not supported!")
            elif(opr == ">="):
                return new_var.setUpperBound(cont, True)
            elif(opr == ">"):
                return new_var.setUpperBound(cont)
            else:
                # ? operator
                raise SyntaxError("operation is not supported!")

    def delete(self, var = None):
        if(var is None):
            raise SyntaxError("delete nothing")
        else:
            var.delete()

    def pivot(self, i, j):
        xi = self.rows[i]
        xj = self.cols[j]
        
        lenr = len(self.matrix)
        lenc = len(self.matrix[i])

        # self.matrix[i][j] will change when updating row i
        tmp = self.matrix[i][j]

        # update the i
        for c in range(lenc):
            if(c!=j):
                self.matrix[i][c] = -self.matrix[i][c]/tmp
            else:
                self.matrix[i][c] = 1/tmp

        # update the others
        for r in range(lenr):
            if(r!=i):
                mrj=self.matrix[r][j]
                for c in range(lenc):
                    if(c!=j):
                        self.matrix[r][c] = self.matrix[r][c] + mrj*self.matrix[i][c]
                    else:
                        self.matrix[r][c] = mrj*self.matrix[i][j]

        self.rows[i]=xj
        self.cols[j]=xi
  
    def pivotAndUpdate(self, i, j, val):
        xi = self.rows[i]
        xj = self.cols[j]
        
        # theta: xi -> val, xj -> v(xj)+theta
        theta = (val-v(self.get_variable(xi)))/self.matrix[i][j]
        self.get_variable(xi).setValue(val)
        self.get_variable(xj).changeValue(theta)
        
        # update the other lines
        lent = len(self.rows)

        for it in range(lent):
            if(it != i):
                self.get_variable(self.rows[it]).changeValue(self.matrix[it][j]*theta)
        
        self.pivot(i,j)

    def get_model(self):
        # for i in self.auxi_variables:
        #     print(str(i)+" "+str(i.get_value()))
        if(self.state!=1): return None
        res = {}
        for x in self.prob_variables:
            if (str(x) != '__placeholder'): res[str(x)]=round(float(v(x)), prec)
        
        return res
                
    def parse(self, file):
        import re
        with open(file) as f:
            lines = f.readlines()

        # variable cannot start with a number, must obey for input
        item = r"(\d|\d.\d|\d\/\d)[a-zA-Z0-9]*"
        for line in lines:
            if(line[0]=="#"):
                # comment line
                continue
            elif(line.find("Real")>=0):
                # declare variable
                varlist = line[4:]
                # delete whole blanks
                varlist = varlist.replace(" ","")
                while True:
                    idx = varlist.find(",")
                    if(idx == -1): 
                        var = varlist[:-1]
                    else:
                        var = varlist[:idx]
                    # add a variable
                    self.add_variable(var)
                    varlist = varlist[idx+1:]
                    if(idx==-1): break
            elif(line.find("check-sat")!=-1):
                tmp, ans = self.solve()
                if(ans):
                    print("SAT")
                    print(self.get_model())
                else:
                    print("UNSAT")
                    print("None")
            elif(line!="\n"):
                # a formula
                cons = constraint(formula=line.replace(" ",""))
                self.add_constraint(cons, 0)


if(__name__=='__main__'):

    s = solver()
    s.parse("./test3.la")
