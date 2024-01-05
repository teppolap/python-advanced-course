import threading
import time

def test_heavy_computing(idx):
    print('->test_heavy_computing('+str(idx)+')')
    time.sleep(10)
    print('<-test_heavy_computing('+str(idx)+')')

def start_threads(f, N):
    threads = []

    def target_function(idx):
        f(idx)

    for idx in range(N):
        thread = threading.Thread(target=target_function, args=(idx,))
        thread.start()
        threads.append(thread)

    return threads

def wait_threads(th_list):
    for thread in th_list:
        thread.join()

# Testauskoodi
if __name__ == "__main__":
    thread_count = 5
    thread_list = start_threads(test_heavy_computing, thread_count)
    wait_threads(thread_list)

    print("Kaikki säikeet ovat valmistuneet.")

