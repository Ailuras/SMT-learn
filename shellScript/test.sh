#！/bin/bash
# ./assign.sh 20161105-Sturm-MBO 1 0.0000001
# ./assign.sh QF_NRA_MBO 4 0.0000001

# sed -n '/.*QF_NIA.*/'p SMT-COMP2022singlequeryfinal.xml > output.xml

# file=../../QF_NIA/Stroeder_15__svcomp_ex2.c__p25866_terminationG_0.smt2
# filename=$(basename $file)
# echo $filename
# sed -n "/.*$filename.*/"p output.xml|wc -l

function delete() {
    for file in $@/*;do 
        if test -f $file;then
            filename=$(basename $file)
            num=$(sed -n "/.*$filename.*/"p output.xml|wc -l)
            if [ $num -eq 0 ];then
                rm -rf $file
                # echo $file
            fi
        fi
        if test -d $file;then
            delete $file
        fi
    done
}

delete ../../QF_NIA

# sed -n 's/.*declare-const \([a-z][0-9]\) Real.*/\1/p' output1.xml > output2.xml