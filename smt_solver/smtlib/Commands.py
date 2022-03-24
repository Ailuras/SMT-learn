# define different kind of commands accoding to different version of SMTLIB
# it is an unchangable list

"""Defines constants for the commands of the SMT-LIB"""

ASSERT='assert'
CHECK_SAT='check-sat'
CHECK_SAT_ASSUMING='check-sat-assuming'
DECLARE_CONST='declare-const'
DECLARE_FUN='declare-fun'
DECLARE_SORT='declare-sort'
DEFINE_FUN='define-fun'
DEFINE_FUN_REC='define-fun-rec'
DEFINE_FUNS_REC='define-funs-rec'
DEFINE_SORT='define-sort'
ECHO='echo'
EXIT='exit'
GET_ASSERTIONS='get-assertions'
GET_ASSIGNMENT='get-assignment'
GET_INFO='get-info'
GET_MODEL='get-model'
GET_OPTION='get-option'
GET_PROOF='get-proof'
GET_UNSAT_ASSUMPTIONS='get-unsat-assumptions'
GET_UNSAT_CORE='get-unsat-core'
GET_VALUE='get-value'
POP='pop'
PUSH='push'
RESET='reset'
RESET_ASSERTIONS='reset-assertions'
SET_INFO='set-info'
SET_LOGIC='set-logic'
SET_OPTION='set-option'

DECLARE_DATATYPE='declare-datatype'
DECLARE_DATATYPES='declare-datatypes'


SMT_LIB_2_0 = [
    SET_LOGIC,
    SET_OPTION,
    SET_INFO,
    DECLARE_SORT,
    DEFINE_SORT,
    DECLARE_FUN,
    DEFINE_FUN,
    PUSH,
    POP,
    ASSERT,
    CHECK_SAT,
    GET_ASSERTIONS,
    GET_VALUE,
    GET_MODEL,
    GET_PROOF,
    GET_UNSAT_CORE,
    GET_INFO,
    GET_OPTION,
    EXIT,
]

SMT_LIB_2_5 = SMT_LIB_2_0 + [
    CHECK_SAT_ASSUMING,
    DECLARE_CONST,
    DEFINE_FUN_REC,
    DEFINE_FUNS_REC,
    ECHO,
    GET_ASSIGNMENT,
    GET_UNSAT_ASSUMPTIONS,
    RESET,
    RESET_ASSERTIONS,
]

SMT_LIB_2_6 = SMT_LIB_2_5 + [
    DECLARE_DATATYPE,
    DECLARE_DATATYPES
]

def commands(version):
    if(version=="26"): return SMT_LIB_2_6
    elif(version=="25"): return SMT_LIB_2_5
    else: return SMT_LIB_2_0

# based on decision procedure
# based on https://github.com/pysmt/pysmt