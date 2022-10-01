#！/bin/bash
# ./parallel.sh QF_NRA 1800 mathsat5 mathsat5_1
time_t=$2
solver=$3
result=$4

index=1
function parallel() {
    for folder in $@/*;do 
        # echo `ls -lR $folder | grep "^-"| wc -l`
        state=-1
        for file in $folder/*;do
            if test -f $file;then
                state=0
                break
            fi
            if test -d $file;then
                state=1
                break
            fi
        done
        if [ $state -eq 0 ];then
            # echo hh
            nohup bash run.sh $folder $time_t $solver > results/result_$result/result_$index.log 2>&1 &
            index=$[ $index + 1 ]
        fi
        if [ $state -eq 1 ];then
            parallel $folder
        fi
    done
}

if [ ! -d results/result_$result ];then
  mkdir results/result_$result
fi

parallel $1