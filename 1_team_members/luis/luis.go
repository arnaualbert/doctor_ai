package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)
func Transcribe(char string) (string, error) {

	// Check if input contains any non-uppercase or non-letter characters
	for _, char := range input {
		if !unicode.IsLetter(char) || !strings.ContainsAny(string(char), "ATGC") {
			fmt.Println("Invalid input! Please enter an DNA sequence without numbers, special characters or non DNA string.")
			os.Exit(1)
		}
	}

	// Replace all occurrences of "T" with "U"
	output := strings.ReplaceAll(input, "T", "U")

	// Print the result
	return output, nil
}

func main() {

	// Get DNA sequence from command-line arguments
	if len(os.Args) < 2 {
		fmt.Println("Please enter a DNA sequence as a command-line argument.")
		os.Exit(1)
	}
	input := os.Args[1]

	// Convert input to uppercase

	input = strings.ToUpper(input)


	rna, err := Transcribe(input)
    if err != nil {
        fmt.Println(err)
        return
    }

	
}
