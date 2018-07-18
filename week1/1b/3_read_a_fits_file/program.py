from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def load_fits(file):
    hdulist = fits.open(file)
    data = hdulist[0].data
    hdulist.close()
    
    arg_max = np.argmax(data, axis=None)
    max_idx = np.unravel_index(arg_max, data.shape)

    return max_idx

def run_test(file):
    bright = load_fits(file)
    print(bright)

    hdulist = fits.open(file)
    data = hdulist[0].data
    hdulist.close()

    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    # Test Case 1
    print("Test Case #1")
    run_test('image0.fits')

    # Test Case 2
    print("Test Case #2")
    run_test('image1.fits')

    # Test Case 3
    print("Test Case #3")
    run_test('image2.fits')

    # Test Case 4
    print("Test Case #4")
    run_test('image3.fits')