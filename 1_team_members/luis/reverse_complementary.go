package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type FastaRecord struct {
	Header string
	Seq    string
}

// complement returns the complement of a nucleotide
func complement(nucleotide rune) rune {
	switch nucleotide {
	case 'A':
		return 'T'
	case 'T':
		return 'A'
	case 'C':
		return 'G'
	case 'G':
		return 'C'
	default:
		return nucleotide
	}
}

// reverseComplement returns the reverse complement of a DNA sequence
func reverseComplement(sequence string) string {
	runes := []rune(sequence)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = complement(runes[j]), complement(runes[i])
	}
	return string(runes)
}

// readFastaFile reads a FASTA file and returns its records as an array of FastaRecord structs
func readFastaFile(filename string) ([]FastaRecord, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	records := []FastaRecord{}
	var current FastaRecord

	for scanner.Scan() {
		line := scanner.Text()

		if strings.HasPrefix(line, ">") {
			if current.Header != "" {
				records = append(records, current)
			}
			current = FastaRecord{Header: line}
		} else {
			current.Seq += line
		}
	}

	if current.Header != "" {
		records = append(records, current)
	}

	return records, scanner.Err()
}

// writeFastaFile writes an array of FastaRecord structs to a FASTA file
// writeFastaFile writes an array of FastaRecord structs to a FASTA file
func writeFastaFile(filename string, records []FastaRecord) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	for _, record := range records {
		fmt.Fprintln(writer, record.Header)
		complement := reverseComplement(record.Seq)
		for i := 0; i < len(complement); i += 50 {
			end := i + 50
			if end > len(complement) {
				end = len(complement)
			}
			fmt.Fprintln(writer, complement[i:end])
		}
	}
	return writer.Flush()
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run main.go <input file>")
		return
	}

	inputFile := os.Args[1]
	outputFile := os.Args[2]
	// Check file extension
	if !strings.HasSuffix(inputFile, ".fasta") && !strings.HasSuffix(inputFile, ".fa") {
		fmt.Fprintf(os.Stderr, "Error: Input file must have a .fasta or .fa extension.\n")
		os.Exit(1)
	}

	records, err := readFastaFile(inputFile)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	err = writeFastaFile(outputFile, records)
	if err != nil {
		fmt.Println("Error writing file:", err)
		return
	}

	fmt.Println("Done!")
}