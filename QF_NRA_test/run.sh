#！/bin/bash
time_t=$2
function testAll() {
    for file in $@/*;do 
        echo --------------------------------------------------
        start=$[$(date +%s%N)/1000000]
        z3 $file -T:$time_t
        end=$[$(date +%s%N)/1000000]
        take=$(( end - start ))
        echo $file : ${take} ms.
    done
}
# echo 2
testAll $1