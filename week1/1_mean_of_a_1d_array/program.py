import numpy as np

def calc_stats(file):
    data = np.loadtxt(file, delimiter=',')
    mean = np.mean(data)
    median = np.median(data)
    return np.round(mean, decimals=1), np.round(median, decimals=1)

if __name__ == '__main__':
    # Test Case 1
    print(calc_stats('data.csv'))

    # Test Case 2
    print(calc_stats('data2.csv'))

    # Test Case 3
    print(calc_stats('data3.csv'))