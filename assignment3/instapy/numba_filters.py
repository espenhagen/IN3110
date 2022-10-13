"""numba-optimized filters"""
from numba import jit
import numpy as np
# Import warnings
import warnings
# Ignore warnings
warnings.simplefilter("ignore")


@jit
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform

    for row in range(image.shape[0]):
        for collumn in range(image.shape[1]):
            r = image[row][collumn][0] * 0.21
            g = image[row][collumn][1] * 0.72
            b = image[row][collumn][2] * 0.07
            grey = r + b + g
            gray_image[row][collumn][0] = grey
            gray_image[row][collumn][1] = grey
            gray_image[row][collumn][2] = grey

    # Moved astype function to return statement.
    return gray_image.astype("uint8")

# Source reference: The following article from dyclassroom was used as
# inspiration and help for implementing the function numba_color2sepia:
# URL: https://dyclassroom.com/image-processing-project/how-to-convert-a-color-image-into-sepia-image
@jit
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)

    # Iterate through the pixels
    for row in range(image.shape[0]):
        for collumn in range(image.shape[1]):
            r = image[row][collumn][0]
            g = image[row][collumn][1]
            b = image[row][collumn][2]

                # applying the sepia matrix
            sepia_r = (0.393 * r) + (0.769 * g) + (0.189 * b)
            sepia_g = (0.349 * r) + (0.686 * g) + (0.168 * b)
            sepia_b = (0.272 * r) + (0.534 * g) + (0.131 * b)

            if sepia_r > 255:
                sepia_r = 255

            if sepia_g > 255:
                sepia_g = 255

            if sepia_b > 255:
                sepia_b = 255

            sepia_image[row][collumn][0] = sepia_r
            sepia_image[row][collumn][1] = sepia_g
            sepia_image[row][collumn][2] = sepia_b

    # return image
    # Moved astype function to return statement. 
    return sepia_image.astype("uint8")
