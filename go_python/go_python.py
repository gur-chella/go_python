import ctypes
import sys
lib1 = ctypes.CDLL('./go_python.so')
lib1.go_python_func.argtypes=[ctypes.c_char_p]
#lib1.add.argtypes=[ctypes.c_int,ctypes.c_int]
#print(lib1.add(2,4))
#lib1.go_python_func.restype = ctypes.c_char_p
print lib1.string_func(b"1")
#lib1.go_python_func("hello")
#lib1.go_python_func(b"hello")
#lib1.print_to_file()