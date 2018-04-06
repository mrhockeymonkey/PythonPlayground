#!/usr/local/bin/python

from multiprocessing import Process, Queue
import os

def myfunc(*args):
    queue = args[0]
    
    word = ''
    while word != 'END':
        word = queue.get()
        if len(word) == 7:
            print(args[1], ':', os.getpid() ,":",word)


if __name__ == '__main__': 
    queue = Queue()
    p1 = Process(target=myfunc, args=(queue,'1'))
    p2 = Process(target=myfunc, args=(queue,'2'))

    p1.start()
    p2.start()

    try:
        for line in open('words.txt'):
            queue.put(line[:-1])
    except IOError as e:
        print('Trapped', e.args)
    finally:
        queue.put('END')
        queue.put('END')

    p1.join()
    p2.join()
    print("All done")
