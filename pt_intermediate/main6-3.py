# priority queue
# can be used in port scanning - real life project - neuralnine.com
import queue

q = queue.PriorityQueue()
q.put((2,"Hello World"))
q.put((11,99))
q.put((5,7.5))
q.put((1,True))

# print(q.queue)
# print(q.get())
# print(q.get())
# print(q.queue)

while not q.empty():
    # print(q.get())
    print(q.get()[1]) # only get the value 
