from instapy.python_filters import python_color2gray, python_color2sepia


def test_color2gray(image):
    # run color2gray
    gray_image = python_color2gray(image)
    # check that the result has the right shape, type
    assert len(gray_image) == len(image)
    assert len(gray_image[0]) == len(image[0])
    assert len(gray_image[0][0]) == len(image[0][0])
    assert type(gray_image[0][0][0]) == type(image[0][0][0])
    # assert uniform r,g,b values
    assert gray_image[0][0][0] == gray_image[0][0][1] == gray_image[0][0][2]
    assert gray_image[-1][-1][0] == gray_image[-1][-1][1] == gray_image[-1][-1][2]


def test_color2sepia(image):
    # run color2sepia
    sepia_image = python_color2sepia(image)
    # check that the result has the right shape, type
    assert len(sepia_image) == len(image)
    assert len(sepia_image[0]) == len(image[0])
    assert len(sepia_image[0][0]) == len(image[0][0])
    assert type(sepia_image[0][0][0]) == type(image[0][0][0])
    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_matrix = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131]]
    if sepia_matrix[0][0]*image[0][0][0]+sepia_matrix[0][1]*image[0][0][1]+sepia_matrix[0][2]*image[0][0][2] > 255:
        assert sepia_image[0][0][0] == 255
    else:
        assert sepia_image[0][0][0] == (sepia_matrix[0][0]*image[0][0][0]+sepia_matrix[0][1]*image[0][0][1]+sepia_matrix[0][2]*image[0][0][2]).astype("uint8")
    if sepia_matrix[1][0]*image[0][0][0]+sepia_matrix[1][1]*image[0][0][1]+sepia_matrix[1][2]*image[0][0][2] > 255:
        assert sepia_image[0][0][1] == 255
    else:
        assert sepia_image[0][0][1] == (sepia_matrix[1][0]*image[0][0][0]+sepia_matrix[1][1]*image[0][0][1]+sepia_matrix[1][2]*image[0][0][2]).astype("uint8")
    if sepia_matrix[2][0]*image[0][0][0]+sepia_matrix[2][1]*image[0][0][1]+sepia_matrix[2][2]*image[0][0][2] > 255:
        assert sepia_image[0][0][2] == 255
    else:
        assert sepia_image[0][0][2] == (sepia_matrix[2][0]*image[0][0][0]+sepia_matrix[2][1]*image[0][0][1]+sepia_matrix[2][2]*image[0][0][2]).astype("uint8")
