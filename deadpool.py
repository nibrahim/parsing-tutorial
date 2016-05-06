
import time
import threading
import Queue

work_queue = Queue.Queue(10)


def worker():
    while True:
        try:
            work = work_queue.get_nowait()
            print "Got some work"
            if work == "EXIT":
                print "Shutting down"
                break
            work()
        except Queue.Empty:
            print "Nothing to do. Sleeping"
            time.sleep(3)
            

def task1():
    print "Hello - task 1"
    time.sleep(3)

def task2():
    print "Hello - task 2"
    time.sleep(3)

def task3():
    print "Hello - task 3"
    time.sleep(3)

# Create worker pool
pool = []
for i in range(25):
    print "spawning worker {}".format(i)
    t = threading.Thread(target = worker)
    pool.append(t)
    t.start()

print "Worker pool ready. Starting to pump in tasks"


for i in range(50):
    print "Number of items in queue {}".format(work_queue.qsize())
    print "Putting into queue {}".format(i)
    work_queue.put(task1)
    work_queue.put(task2)
    work_queue.put(task3)

print "Shutting down"

for i in pool:
    work_queue.put("EXIT")

for i in pool:
    i.join()
        

        
    


    
    

