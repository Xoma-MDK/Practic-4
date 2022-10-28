import math
from multiprocessing import Queue
import multiprocessing
from datetime import datetime


def process(insert: Queue, output: Queue):
    while True:
        a, b = insert.get(), insert.get()
        powered = int(math.pow(a, b))
        summed = 0
        for i in range(powered + 1):
            summed += i
        output.put(f"{a} ^ {b} = {powered}, {summed}")


def file_writer(queue: Queue):
    while True:
        if not queue.empty():
            now = datetime.now()
            f = open(f"watch/{now.day} - {now.month} - {now.year}  {now.hour}-{now.minute}-{now.second}  --  {queue.get()}", "w+")
            f.close()


if __name__ == '__main__':
    in_queue = Queue()
    out_queue = Queue()
    multiprocessing.Process(target=file_writer, args=(out_queue, )).start()
    multiprocessing.Process(target=process, args=(in_queue, out_queue, )).start()
    while True:
        inp = input()
        in_queue.put(int(inp.split()[0]))
        in_queue.put(int(inp.split()[1]))





