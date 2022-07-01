#！/bin/bash
# ./assign.sh 20161105-Sturm-MBO 1 0.0000001

grep -l "(set-info :status unknown)" 20161105-Sturm-MBO/* | xargs cp -t test/
grep -l "(set-info :status sat)" 20161105-Sturm-MBO/* | xargs cp -t test/