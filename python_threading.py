import env
from gevent import monkey
monkey.patch_all()
import gevent
import time
import os
#file1 = open("thread_file.txt","w")
def identifier():
	print(threading.current_thread().getName())
def huge_function(filename):
	dummy=500
        file1 = open(filename,"w")
        while True:
		dummy-=1
		file1.write("operation being done here\n")
		time.sleep(0.01)
                stats = os.stat(filename)
                print(filename, stats.st_size)
        file1.close()
x=4
t1 = gevent.spawn(huge_function,"file1.txt")
t2 = gevent.spawn(huge_function,"file2.txt")
threads = [t1,t2]
gevent.joinall(threads)
#file1.close()
