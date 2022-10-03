# Instapy

## Contents:

1. What is 'instapy'?
2. How to install the package 'instapy'?
3. How to run the functions from 'instapy'?
4. Functionality not yet implemented.
5. Notes to peer reviewer.

## 1: What is 'instapy'?

Instapy is a software package for python3 that provide functions that can convert
an image into a grayscale og sepia image. The package has several implementations
of the same tools, where the only difference is the speed of converting an image.
The reason for this difference in speed is different implementations under the hood.

## 2: How to install the package 'instapy'?

Instapy can be installed as a package with pip. To install instapy do:
1. Open a terminal window and navigate to the folder assignment3.
2. Run the following command in the terminal:

    python3 -m pip install .

3. Instapy is ready to use.

## 3: How to run the functions from 'instapy'?
After installing instapy with pip you can import and use the filter functions
in any python code. To import a function use the following import sentence
at the beginning of your code file:

General form:

    from instapy.module import function, function, ...

Example of use:

    from instapy.python_filters import python_color2gray

The imported function can then be applied in the code by calling, e.g:

    python_color2gray()

## 4: Functionality not yet implemented
In the package all the grayscale filters and the sepia filters are implemented
and ready to use. The package is installable with pip. However at the time of
turning in, the package is not yet complete according to the tasks
of the assignment3.
The following functionality is not implemented:
    - Timer and profiling reports.
    - Tests for image filters
    - Command-line interface

## 5: Notes to peer reviewer
Hi! Welcome to my implementation of 'instapy', and thanks for doing the peer
review. Just a few notes:
At the time of turning in the assignment I had not yet finished all the tasks.
All the filters are implemented (IN3110 version), the pyproject.toml file is
implemented, and obviously also this README-file. However tests, timing and
profiling report, and command-line interface were not implemented at the time
of turning inn assignment3. To specify, you can expect to find the
following tasks implemented:
Task 1, task 2, task 3, task 4, task 7 and task 12.

Also, if you have figured out how to use Einstein sum or any other smart
moves for implementing the numpy_color2sepia function, I would very much
appreciate some tips, code or comments on this. I did struggle with finding out
how to use einsum, and my solution is suboptimal and only partly utilize
the possiblities of numpy, I think.

Good luck with the peer reveiw assignment! ;-)
