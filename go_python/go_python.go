package main


import "C"

import(
	"fmt"
	"time"
	"os"
)
//export add
func add(x,y int)int {
	return x+y
}
//export print_to_file
func print_to_file(){
	f1, err := os.OpenFile("/home/mantek-singh/bin/go_python/thread_file_go.txt", os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}
	defer f1.Close()
	for ;;{
		f1.WriteString("operation being done here\n")
		fi, err := os.Stat("/home/mantek-singh/bin/go_python/thread_file_go.txt")
		if err!=nil {
			panic(err)
		}
		size := fi.Size()
		fmt.Printf("The go file has size %d\n", size)
		time.Sleep(10*time.Millisecond)
	}
}

//export string_func
func string_func(x int) int{
	//fmt.Printf("x is %v",x)
	//fmt.Println(x)
	f, err := os.OpenFile("/home/mantek-singh/bin/go_python/thread_file_go.txt", os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	f.WriteString(string(x))
	//f.WriteString(x + "\n")
	return x
}





//export go_python_func
func go_python_func(id string) {
	f, err := os.OpenFile("/home/mantek-singh/bin/thread_file_go.txt", os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}

	defer f.Close()
	for dummy:=1;dummy>0 ; dummy--{
		//var x string = "operation being written here" + id + "\n"
		if _, err = f.WriteString("operation being written here " + id + "\n"); err != nil {
			panic(err)
		}
		//time.Sleep(10 * time.Millisecond)

	}

}
func main() {
	print_to_file()

}