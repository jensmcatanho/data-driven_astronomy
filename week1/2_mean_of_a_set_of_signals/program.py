import numpy as np

def mean_datasets(files):
    datasets = []

    for file in files:
        datasets.append(np.loadtxt(file, delimiter=','))

    result = np.mean(datasets, axis=0)
    return np.round(result, decimals=1)

if __name__ == '__main__':
    # Test Case 1
    print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

    # Test Case 2
    print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
