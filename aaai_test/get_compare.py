from hashlib import new
import os
import re

def get_real_data(dir, label):
    
    data = []

    tmp_data = set()

    if os.path.isfile(dir):
        file = dir.split('/')[-1]
        file_list = [file]
        dir = './' + dir.split('/')[1] + '/'
    else:
        file_list = os.listdir(dir)
    stats = []
    for file in file_list:
        tmp_data.clear()
        if os.path.isdir(dir+file):
            pass
        elif(file[-4:]=='.log'):
            # print("Read log:",file)
            total = 0
            check_sat = 0
            time = 0
            unsat = 0
            unknown = 0
            with open(dir+file) as f:
                lines = f.readlines()
                tmp = []
                index = 0
                while index < len(lines):
                    line = lines[index]
                    if(line.strip() == "--------------------------------------------------"):
                        if(len(tmp) > 0):
                            tmp_data.add(tuple(tmp))
                        tmp.clear()
                    else:
                        tmp.append(line)
                    index += 1
                if(len(tmp) > 0):
                    tmp_data.add(tuple(tmp))

            for instance in tmp_data:
                # a instance
                data_i = []
                for line in instance:
                    if(line.strip() == 'sat'):
                        data_i.append('sat')
                    elif(line.strip() == 'unsat'):
                        data_i.append('unsat')
                    elif(line.strip() == 'unknown'):
                        data_i.append('unknown')
                    elif(line.strip() == 'Segmentation fault'):
                        data_i.append('Segmentation fault')
                    elif(len(line.strip()) == 0):
                        continue
                    elif(line.strip()[0] == '+'):
                        continue
                    elif(label in line):
                        file = line[:line.rfind(':')].strip()
                        data_i.insert(0, file)
                        nums = re.findall(r"\d+", line[line.rfind(':'):line.rfind('ms')])
                        if(len(nums) == 1):
                            data_i.append(nums[0])
                if(len(data_i) == 2):
                    data_i.insert(1, 'None')
                data.append(data_i)

    new_data = {}
    for d in data:
        if(len(d) > 0):
            new_data[d[0]] = d[1:]
    return new_data

def get_data(dir1, dir2, label):
    times = [[], []]
    times2 = [[], []]

    data1 = get_real_data(dir1, label)
    data2 = get_real_data(dir2, label)
    
    diff = []
    for d in data1.keys():
        val1 = data1[d]
        if d not in data2:
            continue
        val2 = data2[d]
        if val1[0] == "sat":
            if val2[0] == "sat":
                times[0].append(int(val1[-1])/1000)
                times[1].append(int(val2[-1])/1000)
            elif val2[0] == "None":
                if val2[0] not in diff:
                    diff.append(val2[0])
                times2[0].append(int(val1[-1])/1000)
                times2[1].append(int(val2[-1])/1000)
                
    print(diff)
    return times, times2