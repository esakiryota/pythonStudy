import time
import datetime
# print(time.time())
# def calc_prod():
#     product = 1
#     for i in range(1, 100000):
#         product = product*i
#     return product
#
# start_time = time.time()
# prod = calc_prod()
# end_time = time.time()
# print('計算結果は{}です。'.format(len(str(prod))))
# print('計算結果は{}秒でした。'.format(end_time - start_time))

print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(time.time()))
