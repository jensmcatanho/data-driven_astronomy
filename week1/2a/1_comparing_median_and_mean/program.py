def list_stats(stats):
    n = len(stats)
    mean = sum(stats) / n
    median = 0
    
    stats.sort()
    mid = n // 2
    if n % 2 == 0:
        median = (stats[mid - 1] + stats[mid]) / 2
    else:
        median = stats[mid]
    
    return median, mean

if __name__ == '__main__':
    # Test Case 1
    print(list_stats([1.3, 2.4, 20.6, 0.95, 3.1]))
    
    # Test Case 2
    print(list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7]))

    #Test Case 3
    print(list_stats([1.5]))