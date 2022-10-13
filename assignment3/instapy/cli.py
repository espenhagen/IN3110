"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = io.read_image(file)

    if scale != 1:
        # Resize image by scaling factor, if provided
        image = Image.fromarray(image)
        image = image.resize((image.width // scale, image.height // scale))
        image = np.asarray(image)

    # Get the filter function
    filter_function = instapy.get_filter(filter= filter, implementation= implementation)

    # Apply the filter
    filtered = filter_function(image)

    if out_file:
        # save the file
        io.write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    parser.add_argument("-i", "--implementation", default= "python", help="The implementation")
    parser.add_argument("-f", "--filter", default= "color2gray", help="Select filter type")
    parser.add_argument("-sc", "--scale", type= int, default= 1, help="Scale factor to resize image")

    # parse arguments and call run_filter
    argv = parser.parse_args()
    run_filter(file=argv.file, out_file=argv.out, implementation=argv.implementation, filter=argv.filter, scale=argv.scale)
