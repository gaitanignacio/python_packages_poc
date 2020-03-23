from Queue import Queue
from threading import Thread
from time import sleep

def do_stuff(q):
  while True:
    print("Checkig for stuff")
    sleep(0.2)
    if not q.empty():
        print("There is work to do")      
        x,y = q.get()
        print(y)
        q.task_done()

q = Queue(maxsize=0)

worker = Thread(target=do_stuff, args=(q,))
worker.setDaemon(True)
worker.start()

for x in range(100):
  q.put(['1',x])
  sleep(1)

#q.join()