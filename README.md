# go_python
invoking a go code from python

First I wrote a small file in go that contains all the functions that i will be invoking from my python script.(refer to
https://medium.com/learning-the-go-programming-language/calling-go-functions-from-other-languages-4c7d8bcc69bf)

Then we build a .so and a header file using the command: 'go build -o go_python.so -buildmode=c-shared go_python.go'

Then, using the ctypes foreign function library, the .so file is linked in the python script. 

I wrote 2 scripts, the python_threading.py script makes 2 python threads to write in two different files. We see that the output of the two threads is interleaved, indicating that the threads run concurrently. However, the other script written in the go_python folder(with the name python_threading.py) generates some python threads and a thread that invokes the print_to_file() go function. We see that due to the limitations of the GIL in python, once the thread invoking the function written in go is executed, all the other threads get stuck for their turn indefinitely despite the heavy file i/o operations being invoked in the go function.
