package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var codonTable = map[string]string{
	"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
	"CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
	"ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
	"GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
	"TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
	"CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
	"ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
	"GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
	"TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
	"CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
	"AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
	"GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
	"TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
	"CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
	"AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
	"GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

type FastaRecord struct {
	Name    string
	Content string
}


func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s input.fasta\n", os.Args[0])
        os.Exit(1)
	}
	inputFilename := os.Args[1]

	// Check file extension
	if !strings.HasSuffix(inputFilename, ".fasta") && !strings.HasSuffix(inputFilename, ".fa") {
		fmt.Fprintf(os.Stderr, "Error: Input file must have a .fasta or .fa extension.\n")
		os.Exit(1)
	}

	// Read the input FASTA file
	fastaRecords, err := readFastaFile(inputFilename)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading input FASTA file: %v\n", err)
		panic(err)
	}

	// Transcribe DNA sequences to protein sequences
	for i, record := range fastaRecords {
		fastaRecords[i].Content = dnaToProtein(record.Content)
	}

	// Write the output FASTA file
	outputFilename := strings.TrimSuffix(inputFilename, ".fasta") + "_protein.fasta"
	err = writeFastaFile(outputFilename, fastaRecords)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error writing output FASTA file: %v\n", err)
		panic(err)
	}
}

func readFastaFile(filename string) ([]FastaRecord, error) {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var records []FastaRecord
	var currentRecord FastaRecord
	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, ">") {
			// New record
			if currentRecord.Name != "" {
				records = append(records, currentRecord)
			}
			currentRecord = FastaRecord{Name: line[1:]}
		} else {
			// Validate the DNA sequence
			for _, base := range line {
				if base != 'A' && base != 'C' && base != 'G' && base != 'T' {
					return nil, fmt.Errorf("Error reading input FASTA file: Non-DNA base '%c' found in sequence", base)
				}
			}
			// Append to current record
			currentRecord.Content += line
		}
	}
	// Append the last record
	if currentRecord.Name != "" {
		records = append(records, currentRecord)
	}
	return records, scanner.Err()
}				
func dnaToProtein(dna string) string {
	var protein strings.Builder
	for i := 0; i < len(dna)-2; i += 3 {
		codon := dna[i : i+3]
		aa := codonTable[codon]
		protein.WriteString(aa)
	}
	return protein.String()
}
				
func writeFastaFile(filename string, records []FastaRecord) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	for _, record := range records {
		fmt.Fprintf(writer, ">%s\n", record.Name)

		// Add a line break after every 50 characters in the content
		content := record.Content
		for i := 0; i < len(content); i += 50 {
			end := i + 50
			if end > len(content) {
				end = len(content)
			}
			line := content[i:end]
			fmt.Fprintln(writer, line)
		}
	}
	err = writer.Flush()
	if err != nil {
		return err
	}
	return nil
}
