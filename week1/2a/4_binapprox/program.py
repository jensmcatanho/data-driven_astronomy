import numpy as np

def median_bins(values, B):
    mean = np.mean(values)
    std_dev = np.std(values)
    min_val = mean - std_dev
    max_val = mean + std_dev
    
    left_bin = 0
    bins = np.zeros(B)
    bin_width = 2 * std_dev / B
    
    for value in values:
        if value < min_val:
            left_bin += 1
        elif value < max_val:
            current_bin = int((value - min_val) / bin_width)
            bins[current_bin] += 1
    
    return mean, std_dev, left_bin, bins

def median_approx(values, B):
    mean, std_dev, left_bin, bins = median_bins(values, B)
    
    n = len(values)
    mid = (n + 1) / 2
    
    count = left_bin
    for b, bin_count in enumerate(bins):
        count += bin_count
        if count >= mid:
            break
    
    bin_width = 2 * std_dev / B
    median = mean - std_dev + bin_width * (b + 0.5)
    
    return median

if __name__ == '__main__':
    # Test Case 1
    print(median_bins([1, 1, 3, 2, 2, 6], 3))
    print(median_approx([1, 1, 3, 2, 2, 6], 3))

    # Test Case 2
    print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
    print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))

    # Test Case 3
    print(median_bins([0, 1], 5))
    print(median_approx([0, 1], 5))
