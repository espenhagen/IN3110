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

    gray_image[:,:,0] = image[:,:,0] * 0.21
    gray_image[:,:,1] = image[:,:,1] * 0.72
    gray_image[:,:,2] = image[:,:,2] * 0.07

    sumarray = (image[:,:,0]*0.21) + (image[:,:,1]*0.72) + (image[:,:,2] * 0.07)

    gray_image[:,:,0] = sumarray
    gray_image[:,:,1] = sumarray
    gray_image[:,:,2] = sumarray


    gray_image = gray_image.astype("uint8")

    return gray_image

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

    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
        ]

    sepia_image = np.empty_like(image)

    for row in range(image.shape[0]):
        for collumn in range(image.shape[1]):

            channels = image[row][collumn]

            sepia_r = np.sum(channels * sepia_matrix[0])
            sepia_g = np.sum(channels * sepia_matrix[1])
            sepia_b = np.sum(channels * sepia_matrix[2])

            if sepia_r > 255:
                sepia_r = 255

            if sepia_g > 255:
                sepia_g = 255

            if sepia_b > 255:
                sepia_b = 255

            sepia_image[row][collumn][0] = sepia_r
            sepia_image[row][collumn][1] = sepia_g
            sepia_image[row][collumn][2] = sepia_b

    sepia_image = sepia_image.astype("uint8")

    return sepia_image
