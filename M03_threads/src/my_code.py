import threading
import concurrent.futures as cf
import time


def heavy_computing(idx):
    print('->heavy_computing('+str(idx)+')')
    time.sleep(10)
    print('<-heavy_computing('+str(idx)+')')
    return idx*idx

def start_threads(f, N):
    with cf.ThreadPoolExecutor() as executor:
        futures = []
        
        for idx in range(N):
            future = executor.submit(f, idx)
            futures.append(future)
        return futures

def wait_threads(th_list):
    results = []
    for future in th_list:
        result = future.result()
        results.append(result[1])
    return results

# Test software under this if
if __name__ == "__main__":
    N = 10

    print('None started')
    th_list = start_threads(heavy_computing, N)
    print('Wait...')
    ret = wait_threads(th_list)
    print('All futures completed')
    print(ret)

