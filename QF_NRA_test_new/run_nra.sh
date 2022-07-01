# ../build/z3 $1 -tr:nlsat_reorder -tr:nlsat -tr:nlsat_bug -tr:nlsat_verbose -tr:nlsat_proof -tr:nlsat_resolve -tr:nlsat_resolve_done\
        # -tr:nlsat_mathematica -tr:nlsat_explain
# ../build/z3 $1 -tr:nlsat_reorder -tr:nlsat  -tr:nlsat_proof -tr:nlsat_resolve \
#         -tr:nlsat_mathematica -tr:nlsat_explain
../build/z3 $1 -tr:nlsat -tr:nlsat_mathematica
# option(Z3_ENABLE_TRACING_FOR_NON_DEBUG "Enable tracing in non-debug builds." ON)
# python scripts/mk_make.py --trace