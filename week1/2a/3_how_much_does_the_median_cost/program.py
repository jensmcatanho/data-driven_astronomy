from astropy.io import fits
import numpy as np
import time

def median_fits(files):
    start = time.perf_counter()
    datasets = []
    size = 0
    
    for file in files:
        hdulist = fits.open(file)
        data = hdulist[0].data
        size += data.nbytes
        datasets.append(data)
        hdulist.close()
        
    result = np.median(datasets, axis=0)
    end = time.perf_counter() - start
    size /= 1024

    return result, end, size

if __name__ == '__main__':
    # Test Case 1
    result = median_fits(['image0.fits', 'image1.fits'])
    print(result[0][100, 100], result[1], result[2])
    
    # Test Case 2
    result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
    print(result[0][100, 100], result[1], result[2])