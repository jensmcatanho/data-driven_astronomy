from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def mean_fits(files):
    if len(files) == 0:
        return []

    datasets = []

    for file in files:
        hdulist = fits.open(file)
        datasets.append(hdulist[0].data)
        hdulist.close()

    result = np.mean(datasets, axis=0)
    return result

def run_test(files):
    data = mean_fits(files)
    
    if len(data) > 0:
        print(data[100, 100])

        plt.imshow(data.T, cmap=plt.cm.viridis)
        plt.colorbar()
        plt.show()

if __name__ == '__main__':
    # Test Case 1
    print("Test Case #1")
    run_test(['image0.fits', 'image1.fits', 'image2.fits'])
    
    # Test Case 2
    print("Test Case #2")
    run_test(['image0.fits', 'image1.fits', 'image3.fits'])
    
    # Test Case 3
    print("Test Case #3")
    run_test(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])

    # Additional Test Case 1
    print("Additional Test Case #1")
    run_test([])