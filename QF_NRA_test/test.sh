#！/bin/bash

function test1() {
    for file in $@/*;do 
        if test -f $file;then
            echo file
        fi
        if test -d $file;then
            echo folder
        fi
    done
}

test1 test