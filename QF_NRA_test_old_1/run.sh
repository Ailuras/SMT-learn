#！/bin/bash
time_t=$2
solver=$3
function testAll() {
    for file in $@/*;do 
        echo --------------------------------------------------
        start=$[$(date +%s%N)/1000000]
        if [ "$solver"x = "cvc5"x ]; then
            timeout $time_t bash run_cvc5.sh $file
        fi
        if [ "$solver"x = "z3"x ]; then
            z3 $file -T:$time_t
        fi
        end=$[$(date +%s%N)/1000000]
        take=$(( end - start ))
        echo $file : ${take} ms.
    done
}
# echo 2
testAll $1