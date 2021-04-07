import multiprocessing 


q = multiprocessing.Queue(5)

q.put(111)
q.put(222)
q.put(333)
q.put(444)
q.put(555)
q.put(666)


a1 = q.get()
a2 = q.get()
a3 = q.get()
print(q.full())   #  检查队列是否已满
print(q.empty())   #  检查队列是否取完
a4 = q.get()
a5 = q.get()
print(q.full())   #  检查队列是否已满
a6 = q.get()

# a6 = q.get_nowait()
# a6 = q.get(timeout=3)

print(a1)
