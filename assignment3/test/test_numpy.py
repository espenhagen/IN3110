from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia

import numpy.testing as nt


def test_color2gray(image, reference_gray):
    # run color2gray
    gray_image = numpy_color2gray(image)
    # check that the result has the right shape, type
    assert gray_image.shape == image.shape == reference_gray.shape
    assert type(gray_image[0][0][0]) == type(image[0][0][0]) == type(reference_gray[0][0][0])
    # assert uniform r,g,b values
    assert gray_image[0][0][0] == gray_image[0][0][1] == gray_image[0][0][2] == reference_gray[0][0][0]
    assert gray_image[-1][-1][0] == gray_image[-1][-1][1] == gray_image[-1][-1][2] == reference_gray[-1][-1][0]


def test_color2sepia(image, reference_sepia):
    # run color2sepia
    sepia_image = numpy_color2sepia(image)
    # check that the result has the right shape, type
    assert sepia_image.shape == image.shape == reference_sepia.shape
    assert type(sepia_image[0][0][0]) == type(image[0][0][0]) == type(reference_sepia[0][0][0])
    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_matrix = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131]]

    if sepia_matrix[0][0]*image[0][0][0]+sepia_matrix[0][1]*image[0][0][1]+sepia_matrix[0][2]*image[0][0][2] > 255:
        assert sepia_image[0][0][0] == 255
    else:
        assert sepia_image[0][0][0] == (sepia_matrix[0][0]*image[0][0][0]+sepia_matrix[0][1]*image[0][0][1]+sepia_matrix[0][2]*image[0][0][2]).astype("uint8") == reference_sepia[0][0][0]
    if sepia_matrix[1][0]*image[0][0][0]+sepia_matrix[1][1]*image[0][0][1]+sepia_matrix[1][2]*image[0][0][2] > 255:
        assert sepia_image[0][0][1] == 255
    else:
        assert sepia_image[0][0][1] == (sepia_matrix[1][0]*image[0][0][0]+sepia_matrix[1][1]*image[0][0][1]+sepia_matrix[1][2]*image[0][0][2]).astype("uint8") == reference_sepia[0][0][1]
    if sepia_matrix[2][0]*image[0][0][0]+sepia_matrix[2][1]*image[0][0][1]+sepia_matrix[2][2]*image[0][0][2] > 255:
        assert sepia_image[0][0][2] == 255
    else:
        assert sepia_image[0][0][2] == (sepia_matrix[2][0]*image[0][0][0]+sepia_matrix[2][1]*image[0][0][1]+sepia_matrix[2][2]*image[0][0][2]).astype("uint8") == reference_sepia[0][0][2]
