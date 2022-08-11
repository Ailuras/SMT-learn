import os
import re

def get_data(dir, label):
    instances = []
    times = []

    data = []

    tmp_data = set()

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

    instances.append(0)
    times.append(0)
    for item in data:
        if(len(item) == 0):
            continue
        if item[1] == 'sat':
            instances.append(instances[-1] + 1)
        else:
            instances.append(instances[-1])
        times.append(times[-1]+int(item[-1])/1000)

    return instances, times
        
            