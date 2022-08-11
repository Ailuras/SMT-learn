import os
import re
import sys

def blank(s, max_width = 12):
    new_s = str(s)
    return ''.join([' ' for _ in range(max_width - len(new_s))])

print(  "File"+ blank('12345678') + 
        " Total " + blank(' Total ', 8) +
        " sat " + blank('sat', 8) +
        " unsat " + blank('123456', 8) +
        " unkown " + blank('12345', 8) +
        " unsolved " + blank('12345', 8) +
        " Time " + blank('1234', 8)
    )
_Total = 0
_Sat = 0 
_Check_unsat = 0 
_Unsat = 0
_Unknown = 0

dir = sys.argv[1]

file_list = os.listdir(dir)
stats = []
err_files = set()
for file in file_list:
    if os.path.isdir(dir+file):
        pass
    elif(file[-4:]=='.log'):
        total = 0
        sat = 0
        time = 0
        unsat = 0
        unknown = 0
        with open(dir+file) as f:
            lines = f.readlines()
            for line in lines:
                if(line.strip() == 'sat'):
                    _Sat += 1
                    sat += 1
                elif(line.strip() == 'unsat'):
                    unsat += 1
                    _Unsat += 1
                elif(line.strip() == 'unknown'):
                    unknown += 1
                    _Unknown += 1
                elif(line.find('Split_100')!=-1 or "Split_82" in line or "Split_60" in line or "SAT_Split_100" in line):
                    _Total += 1
                    total += 1
                    nums = re.findall(r"\d+", line[line.rfind(':'):line.rfind('ms')])
                    if(len(nums) == 1):
                        time += int(nums[0])
                else:
                    nums = re.findall(r"\d+", line[line.rfind(':'):line.rfind('ms')])
                    if(len(nums) == 1):
                        time += int(nums[0])
                
        
        stats.append((file, total, sat, unsat, unknown, total-sat-unsat-unknown, time))


sorted_stats = sorted(stats, key=lambda x: (len(x[0]), x[0]))


for s in sorted_stats:
    print(  s[0] + blank(s[0]) + 
            str(s[1]) + blank(s[1], 8) + 
            str(s[2]) + blank(s[2], 8) + 
            str(s[3]) + blank(s[3], 8) + 
            str(s[4]) + blank(s[4]) + 
            str(s[5]) + blank(s[5]) + 
            str(s[6]) + blank(s[6], 8)
        )
print('Total files: %d; Sat: %d; Unsat: %d; Unsolved:%d.'%(_Total, _Sat, _Unsat,  _Total - _Sat - _Unsat))
