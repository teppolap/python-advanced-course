import threading
import concurrent.futures as cf
import time

count = 0

def external_function():
    global count
    count += 1

def external_count():
    return count

def computing5s(thr_id):
    time.sleep(5)
    external_function()
            
    return thr_id, thr_id*thr_id

def init_values(f):
    f_values = {}
    num_threads = 50

    with cf.ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_id = {executor.submit(f, i): i for i in range(num_threads)}
        for future in cf.as_completed(future_to_id):
            idx, val = future.result()
            f_values[idx] = val

    return f_values

if __name__ == "__main__":
    ret = init_values(computing5s)
    print(ret)
    print("count =", external_count())
