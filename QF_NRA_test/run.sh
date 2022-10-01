#！/bin/bash
# ./run.sh test.smt2 1800 mathsat5
time_t=$2
solver=$3
yices2=solvers/yices2/yices-smt2
mathsat5=solvers/mathsat-5.6.8-linux-x86_64/bin/mathsat
function testAll() {
    if test -f $@;then
        echo --------------------------------------------------
        start=$[$(date +%s%N)/1000000]
        if [ "$solver"x = "cvc5"x ]; then
            timeout $time_t bash run_cvc5.sh $@
        fi
        if [ "$solver"x = "z3"x ]; then
            z3 $@ -T:$time_t
        fi
        if [ "$solver"x = "yices2"x ]; then
            timeout $time_t $yices2 $@
        fi
        if [ "$solver"x = "mathsat5"x ]; then
            timeout $time_t $mathsat5 $@
        fi
        end=$[$(date +%s%N)/1000000]
        take=$(( end - start ))
        echo $@ : ${take} ms.
        return
    fi
    for file in $@/*;do 
        echo --------------------------------------------------
        start=$[$(date +%s%N)/1000000]
        if [ "$solver"x = "cvc5"x ]; then
            timeout $time_t bash run_cvc5.sh $file
        fi
        if [ "$solver"x = "z3"x ]; then
            z3 $file -T:$time_t
        fi
        if [ "$solver"x = "yices2"x ]; then
            timeout $time_t $yices2 $file
        fi
        if [ "$solver"x = "mathsat5"x ]; then
            timeout $time_t $mathsat5 $file
        fi
        end=$[$(date +%s%N)/1000000]
        take=$(( end - start ))
        echo $file : ${take} ms.
    done
}
# echo 2
testAll $1