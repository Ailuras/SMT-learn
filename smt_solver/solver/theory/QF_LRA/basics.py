from __future__ import division
    
import copy
from decimal import Decimal, getcontext

# from solver.theory.QF_LRA.RationalNumber import Rational

class RealVariable(object):
    def __init__(self, name=None, val=Decimal(0), lowerBound=None, upperBound=None):
        self.name = name
        self.lowerBound = lowerBound
        self.AppLowerBound = False
        self.realLowerBound = None
        self.upperBound = upperBound
        self.AppUpperBound = False
        self.realUpperBound = None
        self.value = val

    def lower(self):
        return self.lowerBound
    
    def upper(self):
        return self.upperBound

    def get_value(self):
        return self.value


    def violateBound(self):
        return (self.violateUpperBound() or self.violateLowerBound())

    def violateUpperBound(self):
        if(self.upperBound is None): 
            return False
        if(self.AppUpperBound):
            if(self.value >= self.realUpperBound): return True
            elif(self.value > self.upperBound): self.upperBound = self.value
            return False
        else:
            return self.value > self.upperBound

    def violateLowerBound(self):
        if(self.lowerBound is None): 
            return False
        if(self.AppLowerBound):
            if(self.value <= self.realLowerBound): return True
            elif(self.value < self.lowerBound): self.lowerBound = self.value
            return False
        else:
            return self.value < self.lowerBound

    # check whether can lower val
    def lowerLowerBound(self, val = 0):
        # can make val more lower
        val = val + self.value
        if(self.lowerBound is None): return True
        elif(self.AppLowerBound): 
            if(val <= self.realLowerBound): return False
            elif(val < self.lowerBound): self.lowerBound = val
            return True
        else: return val >= self.lowerBound 

    # check whether can upper val
    def upperUpperBound(self, val = 0):
        # can make val more upper
        val = val + self.value
        if(self.upperBound is None): return True
        elif(self.AppUpperBound): 
            if(val >= self.realUpperBound): return False
            elif(val > self.upperBound): self.upperBound = val
            return True
        else: return val <= self.upperBound 
    
    def setLowerBound(self, lower, eps=False):
        if(lower is None): self.lowerBound = None
        elif(self.lowerBound is None or lower >= self.realLowerBound): # = is important thing
            if(eps):
                self.realLowerBound = lower
                if(self.upperBound is None): self.lowerBound = self.realLowerBound + 1
                else: 
                    # upperBound has been set
                    if(self.AppUpperBound):
                        # need update
                        if(self.upperBound < self.realLowerBound):
                            self.upperBound = (self.realUpperBound + self.upperBound)/2
                    # set lowerBound
                    self.lowerBound = (self.realLowerBound + self.realUpperBound)/2
            else:
                self.realLowerBound = lower
                self.lowerBound = lower

            self.AppLowerBound = eps or self.AppLowerBound
        
        return not self.self_violation()

    def setUpperBound(self, upper, eps=False):
        if(upper is None): self.upperBound = None
        elif(self.upperBound is None or upper <= self.realUpperBound): # = is important thing
            if(eps):
                self.realUpperBound = upper
                if(self.lowerBound is None): self.upperBound = self.realUpperBound - 1
                else: 
                    # upperBound has been set
                    if(self.AppLowerBound):
                        # need update
                        if(self.lowerBound > self.realUpperBound):
                            self.lowerBound = (self.realLowerBound + self.realUpperBound)/2
                    # set lowerBound
                    self.upperBound = (self.realLowerBound + self.realUpperBound)/2
            else:
                self.realUpperBound = upper
                self.upperBound = upper

            self.AppUpperBound = eps or self.AppUpperBound

        return not self.self_violation()

    def self_violation(self):
        if(self.lowerBound is None or self.upperBound is None): return False
        else:
            if(self.AppLowerBound and self.AppUpperBound):
                return self.realLowerBound >= self.realUpperBound
            elif(self.AppLowerBound):
                return self.realLowerBound >= self.upperBound
            elif(self.AppUpperBound):
                return self.lowerBound >= self.realUpperBound
            else:
                return self.lowerBound > self.upperBound

    def setValue(self, val):
        self.value =val

    def changeValue(self, val):
        self.value += val

    def delete(self):
        self.lowerBound=None
        self.upperBound=None
        self.realLowerBound = None
        self.realUpperBound = None
        self.AppLowerBound = None
        self.AppUpperBound = None

    def is_unset(self):
        return self.lowerBound is None and self.upperBound is None

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ne__(self, other):
        return not self.value == other.value

    def __hash__(self):
        return self.name + str(self.value)

zero = Decimal(0.0000001)

def is_zero(cnt):
    if(abs(cnt/zero)<=1.5): return True
    else: return False

# auxiliary functions about RealVariable
def l(x):
    return x.lower()

def u(x):
    return x.upper()

def v(x):
    return x.get_value()


def make_str(var):
    if(type(var)==str): return var
    return str(var)

import re
def is_number(num):
    # can opt, for every check needs O(n) time, n - number of variables
    if(type(num)==calculation):
        for i in num:
            if(i!=constant_name and num[i]!=0):
                return False
        return True
    if(type(num)==int or type(num)==float): return True
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    num = make_str(num)
    result = pattern.match(num)
    if result:
        return True
    else:
        return False

def to_calculation(var):
    if(type(var)==calculation):
        return var
    # if it is not type of calculation, it is only a string or a constant
    new_var = calculation()
    if(is_number(var)):
        new_var[constant_name] = Decimal(var)
    else:
        if(var==""): new_var[constant_name] = Decimal(1)
        else: new_var[var] = Decimal(1)
    
    return new_var

# __constant_name is a private variable
constant_name = "__constant__"
class calculation(object):
    def __init__(self, input = None, line = None):
        # only change other type to calcultion
        if(input is not None):
            # check type of input
            self.data={}
            if(is_number(input)):self.data[constant_name]=Decimal(input)
            else:
                if(input==""):self.data[constant_name] = Decimal(1)
                else: self.data[input] = Decimal(1)
        else:
            self.data = {}
            self.data[constant_name]=0

    # like a dict
    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, val):
        self.data[key] = val

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    # for iteration
    def __iter__(self):
        return iter(self.data.keys())

    def chageValue(self, key, val):
        if(key in self.data):
            # iff have appended
            self.data[key]+=Decimal(val)
        else:
            # not appended, setValue as val
            self.setValue(key, val)

    # get variable side of calculation
    def variables(self):
        ans = calculation()
        for i in self.data:
            if(i != constant_name): ans[i] = self.data[i]
        
        return ans

    def setValue(self, key, val):
        self.data[key] = Decimal(val)
    
    def __add__(self, other):
        if(type(other)==calculation):
            self._add_calculation(other)
        else:
            # a single variable
            if(is_number(other)):
                self.chageValue(constant_name, Decimal(other))
            else:
                self.chageValue(other, 1)
        
        return self

    def _add_calculation(self, other):
        for i in other:
            self.chageValue(i, other[i])
    
    def __radd__(self, other):
        return other + self

    def __sub__(self, other):
        # self - other
        if(type(other)==calculation):
            self._sub_calculation(other)
            return self
        if(is_number(other)):
            self.chageValue(constant_name, -Decimal(other))
        else:
            self.changeValue(other, -1)
        return self
    
    def _sub_calculation(self, other):
        for i in other:
            self.chageValue(i, -other[i])

    def __rsub__(self, other):
        return other - self

    def __mul__(self, other):
        a = is_number(other)
        b = is_number(self)
        if(a or b):
            if(a and b):
                # (* 3 4)
                if(type(other)==calculation):
                    self.data[constant_name]=Decimal(other[constant_name])*self.data[constant_name]
                else:
                    self.data[constant_name]=Decimal(other)*self.data[constant_name]
            elif(a):
                # (* (+ x 1) 3)
                if(type(other)==calculation):
                    other = other[constant_name]
                for i in self.data:
                    self.data[i] = self.data[i]*Decimal(other)
            else:
                # (* 3 (+ x 1))
                cont = self.data[constant_name]
                self.data[constant_name]=Decimal(0)
                for i in other:
                    self.data[i] = other[i]*cont
        else:
            # variable mul with variable
            raise SyntaxError("variables * variables, not a linear item!")

        return self

    def __rmul__(self, other):
        return other * self

    def __truediv__(self, other):
        # not allow x/x=1
        a = is_number(other)
        b = is_number(self)
        if(a or b):
            if(a and b):
                # (/ 3 4)
                cont = None
                if(type(other)==calculation):
                    cont = Decimal(other[constant_name])
                else:
                    cont = Decimal(other)
                if(cont==0):
                    raise SyntaxError("Divided by zero!")
                
                self.data[constant_name]=self.data[constant_name]/cont
            elif(a):
                # (/ (+ x 1) 3)
                cont=None
                if(type(other)==calculation):
                    cont = Decimal(other[constant_name])
                if(cont==0):
                    raise SyntaxError("Divided by zero!")
                for i in self.data:
                    self.data[i] = self.data[i]/cont
            else:
                # (/ 3 (+ x 1))
                raise SyntaxError("variables / variables, not a linear item!")
        else:
            # variable divide with variable
            raise SyntaxError("variables / variables, not a linear item!")
        
        return self

    def __rtruediv__(self, other):
        return other / self

    def __neg__(self):
        # - self
        for i in self.data:
            self.data[i] = - self.data[i]

        return self

    def __pos__(self):
        return self

    def __len__(self):
        return len(self.data)

    def __hash__(self):
        ss = ""
        for i in self.data:
            ss += str(i) +" "+ str(self.data[i])+" "
        
        return ss.__hash__()

    def __eq__(self, other):
        return hash(self) == hash(other)
        # if(len(self.data)!=len(other)): return False

        # # length is the same, so if anyone element not in other, then they are not equal
        # for i in self.data:
        #     if(i not in other): return False
        #     if(self.data[i]!=other[i]): return False

        # return True

    def __str__(self):
        return str(self.data)
# 约束的数据结构
class constraint(object):
    def __init__(self, formula = None, l = None, r = None, opr = None):
        self.formula = calculation() # type of calculation
        self.operator = None
        self.sat = -1 # -1 is unknown; 0 is false; 1 is true

        if(formula is not None):
            self._parse(formula)
        elif(opr is not None and l is not None and r is not None):
            self._make(l, r, opr)

    def _parse(self, line):
        # 4x+5y>=3
        left = calculation()
        right = calculation()
        operator = None

        # 4x or 5y or 3: variable with coefficient or constant
        item = r"-?(\d|\d.\d|\d\/\d)?[a-zA-Z0-9]+|-?(\d|\d.\d|\d\/\d)"
        # first appear first match, must >=|<=|>|<|=
        opr = r"(>=|<=|>|<|=)" 
        operator = re.search(opr, line).group()
        if(operator=="="): raise SyntaxError("= is not support")
        rig = False
        while(True):
            ans = re.search(item, line)
            if(ans is None): break
            if(rig):
                # in right side
                items = ans.group()
                right = right + self._split_cv(items)
            else:
                # in left side
                items = ans.group()
                left = left + self._split_cv(items)
            line = line[ans.span()[1]:]
            if(line.find(operator)==0):
                # to right side
                rig = True

        self._make(left, right, operator)

    def _split_cv(self, s):
        # split coefficient and variable
        cof = r"^-?(\d|\d.\d|\d\/\d)|-?"

        cr = re.search(cof, s)
        c = cr.group()
        if(c==""): c = 1 # e.g. x
        elif(c=="-"): c = -1 # e.g. -x
        else: pass # e.g. 2x -> 2
        vr = s[cr.span()[1]:] # e.g. 2x -> x

        return to_calculation(vr)*Decimal(c)
                
    def _make(self, left, right, opr):
        left = to_calculation(left)
        right = to_calculation(right)

        self.formula = self.formula + left
        self.formula = self.formula - right

        self.operator = opr

        # check special case: constraint compare
        special = is_number(self.formula)
        if(special):
            number = self.formula[constant_name]
            ans = 1
            if(self.operator==">="):
                ans = (number >= 0)
            elif(self.operator==">"):
                ans = (number > 0)
            elif(self.operator=="<"):
                ans = (number < 0)
            elif(self.operator=="<="):
                ans = (number <= 0)
            else:
                ans = (number==0)
            self.sat = int(ans)
        

    def __eq__(self, other):
        # the same, formula and operator
        if(self.formula==other.formula and self.operator==other.operator): return True
        # pos == neg neg
        if(self.formula==-other.formula):
            if(self.operator==">" and other.operator=="<="): return True
            if(self.operator==">=" and other.operator=="<"): return True
            if(self.operator=="<" and other.operator==">="): return True
            if(self.operator=="<=" and other.operator==">"): return True
            return False

    def __hash__(self):
        s = ""
        for i in self.formula:
            s += str(i)+" "
        s += self.operator
        return s.__hash__()

    def __str__(self):
        s = ""
        for i in self.formula:
            if(i!=constant_name): s += str(self.formula[i])+str(i) + " "
            else: s += str(self.formula[i]) + " "
        s += self.operator + " 0" 
        return s