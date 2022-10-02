cd solvers/cvc5/bin
ulimit -t $2
./mathsat ../../$1
cd ../../..