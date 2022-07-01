#！/bin/bash
# ./assign.sh 20161105-Sturm-MBO 1 0.0000001

cd /home/hrcarryu/QF_NRA/

for folder in `ls /home/hrcarryu/QF_NRA_old`;do
    echo $folder: `ls $folder -lR|grep "^-"|wc -l`
done

cd /home/hrcarryu/QF_NRA/

for folder in `ls /home/hrcarryu/QF_NRA`;do
    echo $folder: `ls $folder -lR|grep "^-"|wc -l`
done