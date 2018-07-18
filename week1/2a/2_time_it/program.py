import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
    times = []
    
    for i in range(ntrials):
        data = np.random.rand(size)
        start = time.perf_counter()
        res = func(data)
        times.append(time.perf_counter() - start)
        
    return sum(times) / ntrials

if __name__ == '__main__':
    # Test Case 1
    print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10 ** 5, 10)))

    # Test Case 2
    print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10 ** 5, 1000)))
