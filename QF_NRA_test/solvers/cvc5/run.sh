cvc5=cvc5/bin/cvc5
bench=$1
ulimit -t $2
# use: trywith [params..]
# to attempt a run.  Only thing printed on stdout is "sat" or "unsat", in which
# case this run script terminates immediately.  Otherwise, this function
# returns normally and prints the output of the solver to $out_file.
function trywith {
  limit=$1; shift;
  result="$({ ulimit -S -t "$limit"; $cvc5 -L smt2.6 --no-incremental --no-type-checking --no-interactive "$@" $bench; } 2>&1)"
  case "$result" in
    sat|unsat) echo "$result"; exit 0;;
    *)         echo "unknown";;
  esac

}

# use: finishwith [params..]
# to run cvc5. Only "sat" or "unsat" are output. Other outputs are written to
# $out_file.
function finishwith {
  result="$({ $cvc5 -L smt2.6 --no-incremental --no-type-checking --no-interactive "$@" $bench; } 2>&1)"
  echo "$result"
}
# cvc5 setting for QF_NIA
# trywith 420 --nl-ext-tplanes --decision=justification
# trywith 60 --nl-ext-tplanes --decision=internal
# trywith 60 --nl-ext-tplanes --decision=justification-old
# trywith 60 --no-nl-ext-tplanes --decision=internal
# trywith 60 --no-arith-brab --nl-ext-tplanes --decision=internal
# this totals up to more than 20 minutes, although notice that smaller bit-widths may quickly fail
trywith 300 --solve-int-as-bv=2 --bitblast=eager
trywith 300 --solve-int-as-bv=4 --bitblast=eager
trywith 300 --solve-int-as-bv=8 --bitblast=eager
trywith 300 --solve-int-as-bv=16 --bitblast=eager
finishwith --solve-int-as-bv=32 --bitblast=eager
#finishwith --nl-ext-tplanes --decision=internal
