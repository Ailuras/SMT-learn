#！/bin/bash

function pre_process() {
    if test -d $@;then
        local state=-1
        for file in $@/*;do
            if test -f $file;then
                if [ $state -eq -1 ];then
                    state=0
                fi
                if [ $state -eq 1 ];then
                    state=2
                fi
            fi
            if test -d $file;then
                pre_process $file
                if [ $state -eq -1 ];then
                    state=1
                fi
                if [ $state -eq 0 ];then
                    state=2
                fi
            fi
        done
        # echo $state
        if [ $state -eq 2 ];then
            
            if [ ! -d "$@/temp" ];then
                mkdir $@/temp
            fi
            for file in $@/*;do
                if test -f $file;then
                    mv $file $@/temp
                fi
            done
        fi
    fi
}

pre_process $1