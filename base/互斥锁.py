from multiprocessing import Process, Lock
import time
import json
import random 


def search(i):
    with open('data','r',encoding='utf-8') as f:
        dic = json.load(f)
    print('%s 您好!余票还有:%s'%(i,dic.get('ticket_num')))
def buy(i):
    # 先查票
    with open('data','r',encoding='utf-8') as f:
        dic = json.load(f)
    # 模拟网络延迟
    time.sleep(random.randint(1,5))
    # 判断余票是否充足
    if dic.get('ticket_num') > 0:
        # 减票操作
        dic['ticket_num'] -= 1
        # 写入数据库
        with open('data','w',encoding='utf-8') as f:
            json.dump(dic,f)
        print('%s 您好!购票成功.'%i)
    else:
        print('余票不足')

def run(i,mutex):
    search(i)
    mutex.acquire()
    buy(i)
    mutex.releace()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(1,11):
        p = Process(target=run,args=(i, mutex))
        p.start()
