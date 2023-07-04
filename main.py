# based off the tutorial by Corey Schafer

import multiprocessing
import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} seconds...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        results = executor.map(do_something, seconds)
        # results = [executor.submit(do_something, sec) for sec in seconds]

        for result in results:
            print(result)

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

    # processes = []

    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     processes.append(p)
    
    # for process in processes:
    #     process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
