#！/bin/bash
# ./assign.sh 20161105-Sturm-MBO 1 0.0000001
# ./assign.sh QF_NRA_MBO 4 0.0000001

# sed -n '/.*QF_NIA.*/'p SMT-COMP2022singlequeryfinal.xml > output.xml

# file=../../QF_NIA/Stroeder_15__svcomp_ex2.c__p25866_terminationG_0.smt2
# filename=$(basename $file)
# echo $filename
# sed -n "/.*$filename.*/"p output.xml|wc -l

ulimit -s 1048576

function scramble() {
    for file in $@/*;do 
        if test -f $file;then
            # echo $file
            ./scrambler -seed 16 < $file > ${file}.output
            rm -rf $file
            mv ${file}.output $file
        fi
        if test -d $file;then
            scramble $file
        fi
    done
}

scramble ../QF_NIA

# sed -n 's/.*declare-const \([a-z][0-9]\) Real.*/\1/p' output1.xml > output2.xml