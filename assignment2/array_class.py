"""
Array class for assignment 2
"""

class Array:

    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.
                    The Array class can take a list as an input if the list is given as arg2.
        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        #Two-dimentional
        #self.numberOfRows, self.numberOfCollumns = self

        #One dimentional
        #Tests of types and values of the arguments:

        try:
            assert isinstance(shape, tuple)
        except AssertionError as e:
            raise TypeError("Argument 'shape' has to be of type tuple.")

        if isinstance(values[0], list):
            values = tuple(values[0])

        try:
            assert len(values) == self._tupleProduct(shape)
        except AssertionError as e:
            raise ValueError("Number of values does not fit with array shape.")

        if isinstance(values[0], bool):
            self._checkTrueArray(values,bool)

        elif isinstance(values[0], int):
            self._checkTrueArray(values, int)

        elif isinstance(values[0], float):
            self._checkTrueArray(values, float)

        else:
            raise TypeError("Values have to be of one of the types int, float or bool.")

        # All arguments are of correct type and form.
        # We can proceed with binding of the instance variables.

        self.dimentions = len(shape)
        self.numberOfRows = shape[0]
        self.shape = shape
        self.array = list(values)
        self.type = type(values[0])

    def _tupleProduct(self, tuple):
        """Calculating product of the elements in a tuple."""
        result = 1
        for element in tuple:
            result *= element
        return result

    def _checkTrueArray(self, tuple, type):
        """ Check if a tuple is a true array, that is that it contains only
		elements of one type, and that type is int, float or bool.

		Args:
			tuple (tuple) - the tuple we want to check.
			type (int, float, boolean) - the type we want the array to consist of.
		"""

        for element in tuple:
            if not isinstance(element, type):
                if isinstance(element, bool):
                    raise ValueError("All values have to be of the same type.")
                elif isinstance(element, float):
                    raise ValueError("All values have to be of the same type.")
                elif isinstance(element, int):
                    raise ValueError("All values have to be of the same type.")
                else:
                    raise TypeError("Values have to be of one of the types int, float or bool.")

            if type == int:
                if isinstance(element, bool):
                    raise ValueError("All values have to be of the same type.")

    def _appendElementToArray(self, e):
        """ Append a new element to the end of the array.

        Args:
            e (int, boolen, float) - argument have to be of same type as the other elements in the Array.
        """

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return str(self.array)


    def __getitem__(self, index):
        """Returns element on place 'index' in the4 array.

		Args:
			Index (int) - The index number of the array-element to return.

		Returns:
			obj: The object in place specified by argument 'index'.

		Throws:
			IndexError
            ValueError
        """
        try:
            return self.array[index]
        except (IndexError, TypeError) as e:
            print("Error when indexing array: ", e)
            exit()

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        if isinstance(self.array[0], bool) or isinstance(other, bool):
            return NotImplemented

        elif isinstance(other, int) or isinstance(other, float):
            newList = [item + other for item in self.array]

            return Array(self.shape, newList)

        elif isinstance(other, Array):

            if other.shape != self.shape:
                raise ValueError("Number of values does not fit with array shape.")
            else:
                newList = []
                for i in range(len(self.array)):
                    newList.append(self.array[i] + other[i])

                return Array(self.shape, newList)

        else:
            return NotImplemented

        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented



    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        if isinstance(self.array[0], bool) or isinstance(other, bool):
            return NotImplemented

        elif isinstance(other, int) or isinstance(other, float):

            return self.__add__(other * -1)

        elif isinstance(other, Array):

            if other.shape != self.shape:
                raise ValueError("Number of values does not fit with array shape.")
            else:
                newList = []
                for i in range(len(self.array)):
                    newList.append(self.array[i] - other[i])

                return Array(self.shape, newList)

        else:
            return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """

        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        if isinstance(self.array[0], bool) or isinstance(other, bool):
            return NotImplemented

        elif isinstance(other, int) or isinstance(other, float):
            newList = [item * other for item in self.array]

            return Array(self.shape, newList)

        elif isinstance(other, Array):

            if other.shape != self.shape:
                raise ValueError("Number of values does not fit with array shape.")
            else:
                newList = []
                for i in range(len(self.array)):
                    newList.append(self.array[i] + other[i])

                return Array(self.shape, newList)

        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        if isinstance(other, Array):
            if self.shape == other.shape:
                return True
            else:
                return False
        else:
            return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """
        if isinstance(other, Array):

            if self.shape == other.shape:

                matchList = []

                for i in range(len(self.array)):
                    if self.array[i] == other[i]:
                        matchList.append(True)

                    elif self.array[i] != other[i]:
                        matchList.append(False)

                return Array(self.shape, matchList)

            else:
                raise ValueError("The shape of the two arrays do not match.")

        elif isinstance(other, int):

            matchList = []

            for i in range(len(self.array)):
                if self.array[i] == other:
                    matchList.append(True)

                elif self.array[i] != other:
                    matchList.append(False)

            return Array(self.shape, matchList)

        else:
            raise TypeError("Argument 'other' have to be of type Array or int.")


    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        if isinstance(self.array[0], bool):
            return NotImplemented

        else:
            minste = self.array[0]

            for number in self.array:
                if number < minste:
                    minste = number

            return float(minste)

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """
        return float(sum(self.array) / len(self.array))
