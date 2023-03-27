package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
    "unicode"
)

func main() {
    // Prompt user to enter a string
    fmt.Print("Enter a DNA sequence: ")
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    input := scanner.Text()

    // Convert input to uppercase
    
    input = strings.ToUpper(input)

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
    fmt.Println("Result: ", output)
}
