"""numpy implementation of image filters"""

from typing import Optional
import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)

    #Removed unused calculations

    sumarray = (image[:,:,0]*0.21) + (image[:,:,1]*0.72) + (image[:,:,2] * 0.07)

    gray_image[:,:,0] = sumarray
    gray_image[:,:,1] = sumarray
    gray_image[:,:,2] = sumarray

    # Moved astype function to return statement
    return gray_image.astype("uint8")

# Source reference: The following article from dyclassroom was used as
# inspiration and help for implementing the function numpy_color2sepia:
# URL: https://dyclassroom.com/image-processing-project/how-to-convert-a-color-image-into-sepia-image
def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = np.empty_like(image)

    # define sepia matrix as a numpy array
    sepia_matrix = np.array([
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
        ])

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter
    # Using numpy.dot to multiply the image- and sepia matrices
    sepia_image = image.dot(sepia_matrix.T)


    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    sepia_image = np.clip(sepia_image, 0, 255)
    
    # Moved astype function to return statement
    return sepia_image.astype("uint8")
