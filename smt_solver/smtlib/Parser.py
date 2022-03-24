
import itertools
import functools
from collections import deque

import smtlib.Commands as smtcmd
from smtlib.Script import SmtlibCommand, SmtlibScript

from solver.smt_solver import smt_solver_s
from solver.formula import operator


class Cache(object):
    def __init__(self):
        self.keys = {}

    def bind(self, name, value):
        """Binds a symbol in this environment"""
        lst = self.keys.setdefault(name, [])
        lst.append(value)

    def unbind(self, name):
        """Unbinds the last binding of this symbol"""
        self.keys[name].pop()

    def get(self, name):
        """Returns the last binding for 'name'"""
        if name in self.keys:
            lst = self.keys[name]
            if len(lst) > 0:
                return lst[-1]
            else:
                return None
        else:
            return None

    def update(self, value_map):
        """Binds all the symbols in 'value_map'"""
        for k, val in iteritems(value_map):
            self.bind(k, val)

    def unbind_all(self, values):
        """UnBinds all the symbols in 'values'"""
        for k in values:
            self.unbind(k)

# EOC SmtLibExecutionCache


class tokenizer(object):
    def __init__(self, handle, interactive = False):
        if interactive:
            self.reader = self.interactive_char_iterator(handle)
            self.__col_cnt = 0
            self.__row_cnt = 0
        else:
            self.reader = itertools.chain.from_iterable(handle)
            self.__col_cnt = None
            self.__row_cnt = None

        self.generator = self.create_generator(self.reader)
        self.extra_queue = deque()
    
    def add_extra_token(self, token):
        self.extra_queue.append(token)

    def consume_maybe(self):
        if(self.extra_queue):
            return self.extra_queue.popleft()
        else:
            return next(self.generator)

    def consume(self, msg = None):
        if(self.extra_queue):
            return self.extra_queue.popleft()
        else:
            try:
                t = self.consume_maybe()
            except StopIteration:
                if(msg):
                    raise SmtlibSyntaxError()
                else:
                    raise SmtlibSyntaxError()
            return t
    
    def raw_read(self):
        return next(self.reader)

    @property
    def pos_info(self):
        if(self.__row_cnt is not None):
            return (self.__row_cnt, self.__col_cnt)
        return None

    @staticmethod
    def create_generator(reader):
        spaces = set([" ", "\n", "\t"])
        separators = set(["(", ")", "|", "\""])
        specials = spaces | separators | set([";", ""])

        try:
            c = next(reader)
            eof = False
            while not eof:
                if(c in specials):
                    if(c in spaces):
                        c = next(reader)
                    elif(c in separators):
                        if(c=="|"):
                            s = []
                            c = next(reader)
                            while(c and c != "|"):
                                if(c == "\\"):
                                    c = next(reader)
                                    if(c != "|" and c != "\\"):
                                        raise SmtlibSyntaxError()
                                s.append(c)
                                c = next(reader)
                            if(not c):
                                raise SmtlibSyntaxError()

                            yield "".join(s)
                            c = next(reader)

                        elif(c=="\""): # string start
                            s = c
                            num_quotes = 0
                            while(True):
                                c = next(reader)
                                if(not c):
                                    raise SmtlibSyntaxError()
                                if(c!="\"" and num_quotes%2!=0):
                                    break
                                s+=c
                                if(c=="\""):
                                    num_quotes += 1
                            yield s
                        else:
                            yield c
                            c = next(reader)
                    elif(c == ";"):
                        while(c and c!="\n"):
                            c = next(reader)
                        c = next(reader)
                    else: # eof
                        eof = True
                        assert(len(c)==0)
                else:
                    tk = []
                    while(c not in specials):
                        tk.append(c)
                        c = next(reader)
                    yield "".join(tk)
        except StopIteration: # read done
            return
    
    def interactive_char_iterator(self, handle):
        c = handle.read(1)
        while c:
            yield c
            c = handle.read(1)

# parse the file to SmtlibScript, which store the smtlib commands(SmtlibCommand)
# operators: operators + params -> specific format based on theories 
class SmtlibParser(object):
    def __init__(self, smt_solver=None, interactive=False, *options):
        if(smt_solver is None): self.smt_solver = smt_solver_s()
        else: self.smt_solver = smt_solver
        self.interactive = interactive

        self.cache = Cache()
        
        self.op_mgr = operator(self.smt_solver)
        # self.var_bings = self.smt_solver.var_bings
        self.operators={
            "let" : self._enter_let,
            "!" : self._enter_annotation,
            "exists" : self._enter_quantifier,
            "forall" : self._enter_quantifier,
            '+':self._operator_adapter(self.op_mgr.plus),
            '-':self._operator_adapter(self.op_mgr.minus),
            '*':self._operator_adapter(self.op_mgr.times),
            '/':self._operator_adapter(self.op_mgr.divide),
            '>':self._operator_adapter(self.op_mgr.GT),
            '<':self._operator_adapter(self.op_mgr.LT),
            '>=':self._operator_adapter(self.op_mgr.GE),
            '<=':self._operator_adapter(self.op_mgr.LE),
            '=':self._operator_adapter(self.op_mgr.EQ),
            'not':self._operator_adapter(self.op_mgr.NOT),
            'and':self._operator_adapter(self.op_mgr.AND),
            'or':self._operator_adapter(self.op_mgr.OR),
            'xor':self._operator_adapter(self.op_mgr.XOR),
            '=>':self._operator_adapter(self.op_mgr.IMPLY),
            '<->':self._operator_adapter(self.op_mgr.IFF),
            # 'ite':self._operator_adapter(self.op_mgr.ITE)
        }

        self.commands = {
            smtcmd.ASSERT : self._cmd_assert,
            smtcmd.CHECK_SAT : self._cmd_check_sat,
            smtcmd.CHECK_SAT_ASSUMING : self._cmd_check_sat_assuming,
            smtcmd.DECLARE_CONST : self._cmd_declare_const,
            smtcmd.DECLARE_FUN : self._cmd_declare_fun,
            smtcmd.DECLARE_SORT: self._cmd_declare_sort,
            smtcmd.DEFINE_FUN : self._cmd_define_fun,
            smtcmd.DEFINE_FUNS_REC : self._cmd_define_funs_rec,
            smtcmd.DEFINE_FUN_REC : self._cmd_define_fun_rec,
            smtcmd.DEFINE_SORT: self._cmd_define_sort,
            smtcmd.ECHO : self._cmd_echo,
            smtcmd.EXIT : self._cmd_exit,
            smtcmd.GET_ASSERTIONS: self._cmd_get_assertions,
            smtcmd.GET_ASSIGNMENT : self._cmd_get_assignment,
            smtcmd.GET_INFO: self._cmd_get_info,
            smtcmd.GET_MODEL: self._cmd_get_model,
            smtcmd.GET_OPTION: self._cmd_get_option,
            smtcmd.GET_PROOF: self._cmd_get_proof,
            smtcmd.GET_UNSAT_ASSUMPTIONS : self._cmd_get_unsat_assumptions,
            smtcmd.GET_UNSAT_CORE: self._cmd_get_unsat_core,
            smtcmd.GET_VALUE : self._cmd_get_value,
            smtcmd.POP : self._cmd_pop,
            smtcmd.PUSH : self._cmd_push,
            smtcmd.RESET : self._cmd_reset,
            smtcmd.RESET_ASSERTIONS : self._cmd_reset_assertions,
            smtcmd.SET_LOGIC : self._cmd_set_logic,
            smtcmd.SET_OPTION : self._cmd_set_option,
            smtcmd.SET_INFO : self._cmd_set_info,
            smtcmd.DECLARE_DATATYPE: self._cmd_declare_datatype,
            smtcmd.DECLARE_DATATYPES: self._cmd_declare_datatypes,
        }

    def fix_wrap(self, op, *args):
        try:
            return op(*args)
        except:
            raise

    def _operator_adapter(self, op):
        """Handles generic operator"""
        def res(stack, tokens, key):
            stack[-1].append(op)

        return res

    def _reset(self):
        pass

    def atom(self, token, mgr):
        # it could be a number or a string
        try:
            res = float(token)
        except ValueError:
            # check if it is a sat variable
            if(token in self.smt_solver.sat_variable):
                return self.smt_solver.sat_variable[token]
            ans = self.cache.get(token)
            if(ans is not None):
                return ans
            # a string constant
            res = token
        return res
    
    def get_expression(self, tokens):
        mgr = self.op_mgr
        stack = []

        try:
            while True:
                tk = tokens.consume_maybe()

                if(tk=="("):
                    # nested
                    while(tk=="("):
                        stack.append([])
                        tk = tokens.consume()

                    if(tk in self.operators):
                        fun = self.operators[tk]
                        fun(stack, tokens, tk)
                    else:
                        stack[-1].append(self.atom(tk, mgr))
                
                elif(tk==")"):
                    try:
                        lst = stack.pop()
                        fun = lst.pop(0)
                    except IndexError:
                        raise SyntaxError()

                    try:
                        res = fun(*lst)
                    except TypeError as err:
                        if(not callable(fun)):
                            raise NotImplementedError()
                        raise err

                    if(len(stack)>0):
                        stack[-1].append(res)
                    else:
                        return res

                else:
                    try:
                        stack[-1].append(self.atom(tk, mgr))
                    except IndexError:
                        return self.atom(tk, mgr)
        except StopIteration:
            # No more data when trying to consume tokens
            return

    def parse_atoms(self, tokens, command, min_size, max_size=None):
        """
        Parses a sequence of N atoms (min_size <= N <= max_size) consuming
        the tokens
        """
        if(max_size is None):
            max_size = min_size

        res = []
        current = None

        for _ in range(min_size):
            current = tokens.consume()
            if(current==")"):
                raise SyntaxError()
            if(current=="("):
                raise SyntaxError()
            res.append(current)
        
        for _ in range(min_size, max_size+1):
            current = tokens.consume()
            if(current==")"):
                return res
            if(current=="("):
                raise SyntaxError()
            res.append(current)

        raise SyntaxError()

    def parse_atom(self, tokens, command):
        var = tokens.consume()
        if(var=="(" or var==")"):
            raise SyntaxError()
        return var
    

    def parse_type(self, tokens, command):
        """Parses a single type name from the tokens"""
        return tokens.consume()

    def parse_params(self, tokens, command):
        """Parses a list of types from the tokens"""
        self.consume_opening(tokens, command)
        current = tokens.consume()
        res = []
        while current != ")":
            res.append(self.parse_type(tokens, command))
            current = tokens.consume()
        return res

    def consume_opening(self, tokens, current):
        try:
            p = tokens.consume_maybe()
        except StopIteration:
            raise
        if(p!="("):
            raise SyntaxError()

    def consume_closing(self, tokens, current):
        p = tokens.consume()
        if(p!=")"):
            raise SyntaxError()
    
    # get a SmtlibScript object
    def parse(self, file):
        self.smt_solver.reset()
        with open(file) as script:
            # script is a file object(.smt2)
            # return a SmtlibScript object
            self._reset() # prepare the parser
            self.LatestScript = SmtlibScript()
            for cmd in self.get_command_generator(script):
                self.LatestScript.append(cmd)
            
            # self.LatestScript.annotations = self.cache.annotations

            return self.LatestScript
        

    def get_command_generator(self, script):
        tokens = tokenizer(script, interactive=self.interactive)

        for cmd in self.get_command(tokens):
            yield cmd

        return

    def get_command(self, tokens):
        while True:
            try:
                self.consume_opening(tokens, "<main>")
            except StopIteration:
                return
            
            current = tokens.consume()
            if(current in self.commands):
                fun = self.commands[current]
                # run functions stored in self.commands
                # which returns a SmtlibCommand object
                yield fun(current, tokens)
            else:
                raise NameError()

    def _enter_let(self, stack, tokens, key):
        """Handles a let expression by recurring on the expression and
        updating the cache
        """
        self.consume_opening(tokens, "expression")
        newvals = {}
        current = "("
        self.consume_opening(tokens, "expression")
        while current != ")":
            if current != "(":
                raise PysmtSyntaxError("Expected '(' in let binding",
                                       tokens.pos_info)
            vname = self.parse_atom(tokens, "expression")
            expr = self.get_expression(tokens)
            newvals[vname] = expr
            self.cache.bind(vname, expr)
            self.consume_closing(tokens, "expression")
            current = tokens.consume()

        stack[-1].append(self._exit_let)
        stack[-1].append(newvals.keys())
        pass


    def _exit_let(self, varlist, bdy):
        """ Cleans the execution environment when we exit the scope of a 'let' """
        for k in varlist:
            self.cache.unbind(k)
        return bdy

    def _enter_annotation(self):
        pass

    def _enter_quantifier(self):
        pass

    def _cmd_assert(self, current, tokens):
        """(assert <term>)"""
        expr = self.get_expression(tokens)
        self.consume_closing(tokens, current)
        self.op_mgr.ADD(expr)
    
    def _cmd_check_sat(self, current, tokens):
        """(check-sat)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.check_sat()

    def _cmd_check_sat_assuming(self, current, tokens):
        raise NotImplementedError()

    def _cmd_declare_const(self, current, tokens):
        """(declare-const <symbol> <sort>)"""
        var = self.parse_atom(tokens, current)
        typename = self.parse_type(tokens, current)
        self.consume_closing(tokens, current)
        
        self.smt_solver.declare_const(var, typename)

    def _cmd_declare_fun(self, current, tokens):
        """(declare-fun <symbol> (<sort>*) <sort>)"""
        var = self.parse_atom(tokens, current)
        params = self.parse_params(tokens, current)
        typename = self.parse_type(tokens, current)
        self.consume_closing(tokens, current)
        self.smt_solver.declare_fun(var, params, typename)

    def _cmd_declare_sort(self, current, tokens):
        pass

    def _cmd_define_fun(self, current, tokens):
        pass

    def _cmd_define_funs_rec(self, current, tokens):
        pass

    def _cmd_define_fun_rec(self, current, tokens):
        pass

    def _cmd_define_sort(self, current, tokens):
        pass

    def _cmd_echo(self, current, tokens):
        """(echo <string>)"""
        elements = self.parse_atoms(tokens, current, 1)
        self.smt_solver.echo(elements)

    def _cmd_exit(self, current, tokens):
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.exit()

    def _cmd_get_assertions(self, current, tokens):
        """(get-assertions)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.get_assertions()

    def _cmd_get_assignment(self, current, tokens):
        """(get-assignment)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.get_assignment()

    def _cmd_get_info(self, current, tokens):
        """(get-info <info_flag>)"""
        keyword = self.parse_atoms(tokens, current, 1)
        self.smt_solver.get_info(keyword)

    def _cmd_get_model(self, current, tokens):
        """(get-model)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.get_model()

    def _cmd_get_option(self, current, tokens):
        """(get-option <keyword>)"""
        keyword = self.parse_atoms(tokens, current, 1)
        self.smt_solver.get_option(keyword)

    def _cmd_get_proof(self, current, tokens):
        """(get-proof)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.get_proof()

    def _cmd_get_unsat_assumptions(self, current, tokens):
        """(get-unsat-assumptions)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.get_unsat_assumptions()

    def _cmd_get_unsat_core(self, current, tokens):
        """(get-unsat-core)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.get_unsat_core()

    def _cmd_get_value(self, current, tokens):
        """(get-value (<term>+)"""
        params = self.parse_expr_list(tokens, current)
        self.consume_closing(tokens, current)
        self.smt_solver.get_value(params)

    def _cmd_pop(self, current, tokens):
        """(pop <numeral>)"""
        elements = self.parse_atoms(tokens, current, 0, 1)
        levels = 1
        if len(elements) > 0:
            levels = int(elements[0])
        self.smt_solver.push(levels)

    def _cmd_push(self, current, tokens):
        """(push <numeral>)"""
        elements = self.parse_atoms(tokens, current, 0, 1)
        levels = 1
        if len(elements) > 0:
            levels = int(elements[0])
        self.smt_solver.push(levels)

    def _cmd_reset(self, current, tokens):
        """(reset)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.reset()

    def _cmd_reset_assertions(self, current, tokens):
        """(reset-assertions)"""
        self.parse_atoms(tokens, current, 0)
        self.smt_solver.reset_assertions()

    def _cmd_set_logic(self, current, tokens):
        """(set-logic <symbol>)"""
        elements = self.parse_atoms(tokens, current, 1)
        name = elements[0]
        self.smt_solver.set_logic(name)

    def _cmd_set_option(self, current, tokens):
        """(set-option <option>)"""
        self.smt_solver.set_info(elements[0], elements[1])

    def _cmd_set_info(self, current, tokens):
        """(set-info <attribute>)"""
        elements = self.parse_atoms(tokens, current, 2)
        self.smt_solver.set_info(elements[0], elements[1])

    def _cmd_declare_datatype(self, current, tokens):
        raise NotImplementedError()

    def _cmd_declare_datatypes(self, current, tokens):
        raise NotImplementedError()

class SmtlibSyntaxError(SyntaxError):
    pass




# based on SMTLIB instructions, such as v2.0, v2.5, v2.6
# based on https://github.com/pysmt/pysmt