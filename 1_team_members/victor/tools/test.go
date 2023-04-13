package main

import (
	"fmt"
	"strings"
)

func main() {

	str := "        	Me llamo Victor      "

	fmt.Println(str)

	trimed := strings.TrimSpace(str)

	fmt.Println(trimed)

}
