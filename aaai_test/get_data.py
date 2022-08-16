import os
import re

def get_data(dir, label):
    instances = []
    times = []

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
        # instances.append(instances[-1]+1)
        # times.append(times[-1]+int(item[-1]))

    return instances, times
        
def get_data_new(dir, label):
    times = []
    nums = []
    num = 0
    
    if os.path.isfile(dir):
        file = dir.split('/')[-1]
        file_list = [file]
        dir = './' + dir.split('/')[1] + '/'
    else:
        file_list = os.listdir(dir)
    
    file_list = os.listdir(dir)
    for file in file_list:
        new_path = os.path.join(dir, file)
        if not os.path.isdir(new_path):
            with open(new_path) as f:
                lines = f.readlines()
                for line in lines:
                    if 'SAT_Split_100' in line:
                        run_time = int(line.split(' : ')[1][:-4])
                        times.append(run_time)
                        num += 1
                        nums.append(num)
    times.sort()
    
    # for i in range(0, 1200, 10):
    #     min_time = i
    #     max_time = (i+10)
    #     if os.path.isfile(dir):
    #         file = dir.split('/')[-1]
    #         file_list = [file]
    #         dir = './' + dir.split('/')[1] + '/'
    #     else:
    #         file_list = os.listdir(dir)
        
    #     file_list = os.listdir(dir)
    #     for file in file_list:
    #         new_path = os.path.join(dir, file)
    #         if not os.path.isdir(new_path):
    #             with open(new_path) as f:
    #                 lines = f.readlines()
    #                 for line in lines:
    #                     if 'SAT_Split_100' in line:
    #                         run_time = int(line.split(' : ')[1][:-4])
    #                         if run_time <= max_time*1000 and run_time >= min_time*1000:
    #                             num += 1
        # times.append(max_time)
        # nums.append(num)
        
            

    return times, nums
    # return nums, times