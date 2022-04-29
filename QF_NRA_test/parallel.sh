#！/bin/bash
time_t=$2

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
            nohup bash run.sh $folder $time_t > result/result_$index.log 2>&1 &
            index=$[ $index + 1 ]
        fi
        if [ $state -eq 1 ];then
            parallel $folder
        fi
    done
}

parallel $1