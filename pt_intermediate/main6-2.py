# last in first out queue
import queue

q = queue.LifoQueue()
numbers = [ 10, 20, 30, 40, 50, 60, 70 ]
for number in numbers:
    q.put(number)

print(q.get())
print(q.get())
print(q.queue)