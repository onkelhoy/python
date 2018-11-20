class ArrayList (ListClass):
    __array = []
    __size = 0
    def __init__(self):
        self.__array = [None] * 10
        self.__size = 0

    # adding the value
    def add (self, value):
        if self.__size >= len(self.__array):
            self.resize()

        self.__array[self.__size] = value
        self.__size += 1

    def size (self):
        return self.__size

    # Resizing the array : copy & replace
    def resize(self):
        temp = [None] * self.__size * 2
        for i in range (0, self.__size):
            temp[i] = self.__array[i]

        self.__array = temp

    def get (self, index):
        if index >= self.__size:
            raise IndexError('Trying to access whats is not there!')
        return self.__array[index]




l = ArrayList()
l.add(1)
print l.size()
