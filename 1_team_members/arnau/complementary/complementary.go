package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func main() {
    // Open the input file
    inputFile, err := os.Open(os.Args[1])
    if err != nil {
        panic(err)
    }
    defer inputFile.Close()

    // Create the output file
    outputFile, err := os.Create(os.Args[2])
    if err != nil {
        panic(err)
    }
    defer outputFile.Close()

    // Scan the input file line by line
    scanner := bufio.NewScanner(inputFile)
    var seq strings.Builder
    for scanner.Scan() {
        line := scanner.Text()
        if strings.HasPrefix(line, ">") {
            // Write the header line to the output file
            fmt.Fprintf(outputFile, "%s\n", line)
        } else {
            // Build the sequence string
            seq.WriteString(line)
        }
    }

    // Convert the sequence to uppercase
    seqStr := strings.ToUpper(seq.String())

    // Generate the complementary sequence
    compSeq := complement(seqStr)

    // Write the complementary sequence to the output file
    for i := 0; i < len(compSeq); i += 50 {
        end := i + 50
        if end > len(compSeq) {
            end = len(compSeq)
        }
        fmt.Fprintf(outputFile, "%s\n", compSeq[i:end])
    }
}

// Helper function to generate the complementary sequence
func complement(seq string) string {
    comp := make([]byte, len(seq))
    for i := 0; i < len(seq); i++ {
        switch seq[i] {
        case 'A':
            comp[i] = 'T'
        case 'T':
            comp[i] = 'A'
        case 'C':
            comp[i] = 'G'
        case 'G':
            comp[i] = 'C'
        }
    }
    return string(comp)
}

