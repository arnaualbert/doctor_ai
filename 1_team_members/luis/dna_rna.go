package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func ReplaceLetterWithU(input string, letter string) string {
    // Check if input contains only A, T, G, C
    for _, char := range input {
        if !strings.ContainsAny(string(char), "ATGC") {
            return "Invalid input! Please enter a DNA sequence containing only A, T, G, and C."
        }
    }

    // Replace all occurrences of the letter with "U"
    output := strings.ReplaceAll(input, letter, "U")

    // Add a line break every 50 characters
    var builder strings.Builder
    for i, char := range output {
         builder.WriteRune(char)
        if (i+1)%50 == 0 {
             builder.WriteString("\n")
        }
    }
    output = builder.String()

    // Return the result
    return output
}

func main() {
    // Get input and output file names and letter to be replaced from command-line arguments
    if len(os.Args) < 2 {
        fmt.Println("Please enter an input file name as a command-line argument.")
        os.Exit(1)
    }
    inputFileName := os.Args[1]

    // Open the input file
    inputFile, err := os.Open(inputFileName)
    if err != nil {
        fmt.Println("Error opening input file:", err)
		panic(err)
    }
    defer inputFile.Close()

    // Create the output file
    outputFileName := strings.TrimSuffix(inputFileName, ".fasta") + "_modified.fasta"
    outputFile, err := os.Create(outputFileName)
    if err != nil {
        fmt.Println("Error creating output file:", err)
		panic(err)
    }
    defer outputFile.Close()

    // Parse the input FASTA file
    scanner := bufio.NewScanner(inputFile)
    var header, sequence string
    for scanner.Scan() {
        line := scanner.Text()
        if strings.HasPrefix(line, ">") {
            // Found a header line
            if len(sequence) > 0 {
                // Write the previous sequence to the output file
                outputSequence := ReplaceLetterWithU(sequence, "T")
                fmt.Fprintln(outputFile, header)
                fmt.Fprintln(outputFile, outputSequence)
            }
            header = line
            sequence = ""
        } else {
            // Found a sequence line
            sequence += line
        }
    }

    // Write the last sequence to the output file
    outputSequence := ReplaceLetterWithU(sequence, "T")
    fmt.Fprintln(outputFile, header)
    fmt.Fprintln(outputFile, outputSequence)

    // Check for errors during parsing
    if err := scanner.Err(); err != nil {
        fmt.Println("Error parsing input file:", err)
		panic(err)
    }

    // Print a success message
    fmt.Println("FASTA sequence has been modified and written to", outputFileName)
}