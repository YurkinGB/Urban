import datetime
import multiprocessing


def read_info(name):
    all_data = []
    s = 0
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                all_data.append(line)



filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.datetime.now()
#
# for name in filenames:
#     read_info(name)
#
# end = datetime.datetime.now()
#
# print(end-start)

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end = datetime.datetime.now()

    print(end-start)