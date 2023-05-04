package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    // Parse the command line arguments
    if len(os.Args) != 4 {
        fmt.Println("Usage: go run splitfasta.go <input.fasta> <start> <end>")
        os.Exit(1)
    }
    start, err := strconv.Atoi(os.Args[2])
    if err != nil {
        panic(err)
    }
    end, err := strconv.Atoi(os.Args[3])
    if err != nil {
        panic(err)
    }

    // Open the input file
    inputFile, err := os.Open(os.Args[1])
    if err != nil {
        panic(err)
    }
    defer inputFile.Close()

    // Create the output file
    outputFile, err := os.Create(fmt.Sprintf("output_%d_%d.fasta", start, end))
    if err != nil {
        panic(err)
    }
    defer outputFile.Close()

    // Scan the input file line by line
    scanner := bufio.NewScanner(inputFile)
    var header string
    var seq strings.Builder
    for scanner.Scan() {
        line := scanner.Text()
        if strings.HasPrefix(line, ">") {
            // Write the previous sequence to the output file, if applicable
            if header != "" {
                writeSequenceToFile(header, seq.String(), start, end, outputFile)
                header = ""
                seq.Reset()
            }
            // Save the new header line
            header = line
        } else {
            // Build the sequence string
            seq.WriteString(line)
        }
    }
    // Write the last sequence to the output file, if applicable
    if header != "" {
        writeSequenceToFile(header, seq.String(), start, end, outputFile)
    }
}

// Helper function to write a sequence to a file if it falls within the specified start and end positions
func writeSequenceToFile(header string, seq string, start int, end int, outputFile *os.File) {
    if end <= len(seq) {
        fmt.Fprintf(outputFile, "%s\n%s\n", header, seq[start-1:end])
    }
}
