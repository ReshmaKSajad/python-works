# multi-therading - executing the lengthy process in a parallel way by splitting that lengthy process .
#                   instead of executing line by line,the process will execute parallelly.
#                   multi-threading helps to finish the process within few seconds than normal execution.
import threading
import time
def cal_square(num):
    print("Calculate square")
    for i in num:
        time.sleep(.4)
        print("Square =",i*i)
def cal_cube(num):
    print("Calculate cube")
    for i in num:
        time.sleep(.4)
        print("Cube =",i*i*i)
arg = [1,2,3,4,5]
t1 = threading.Thread(target = cal_square,args = (arg,))
t2 = threading.Thread(target = cal_cube,args = (arg,))
t = time.time()
# t1.start()
#t1.join()
# t2.start()
# t1.join()
t2.start()
# t2.join()
t1.start()
t1.join()
print("time taken for execution = ",time.time()-t)
print("Execution of threads finished")

