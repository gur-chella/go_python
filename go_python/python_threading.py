import env
from gevent import monkey
monkey.patch_all()
import gevent
import time
import os
import ctypes
#file1 = open("thread_file.txt","w")
def identifier():
	print(threading.current_thread().getName())
def huge_function(filename):
	dummy=1
       # file1 = open(filename,"w")
        while dummy:
		dummy-=1
                print filename
                #print("hello world")
		#file1.write("operation being done here\n")
		time.sleep(0.01)
                #stats = os.stat(filename)
                #print(filename, stats.st_size)
        #file1.close()

def compute_intensive():
    while(1):
        pass
x=4
lib1 = ctypes.CDLL("./go_python.so")
#t1 = gevent.spawn(lib1.print_to_file)
#t2 = gevent.spawn(compute_intensive)
threads=[]
for i in range(10):
    fname = "file" + str(i) + ".txt"
    threads.append(gevent.spawn(huge_function,fname))
#t1 = gevent.spawn(huge_function, "file1.txt")
#t2 = gevent.spawn_later(2,lib1.print_to_file)
threads.append(gevent.spawn(lib1.print_to_file))
#threads = [t1,t2]
gevent.joinall(threads)
#file1.close()
