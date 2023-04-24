package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	cdsSequences := extractCdsSequences(os.Args[1])

	// Create the output file
	outputFile, err := os.Create("resultado.fasta")
	if err != nil {
		panic(err)
	}
	defer outputFile.Close()

	// Write the /translation sequence in the output file
	writer := bufio.NewWriter(outputFile)
	for i, cdsSequence := range cdsSequences {
		translation := extractTranslation(cdsSequence)
		if translation != "" {
			// Write the sequence in the fasta
			header := fmt.Sprintf(">secuencia%d\n", i+1)
			fiftytranslation := splitString(translation, 50)
			writer.WriteString(header)
			writer.WriteString(fiftytranslation)
			writer.WriteString("\n")
			writer.WriteString("\n")
			writer.WriteString("\n")
		}
	}
	writer.Flush()
}

func splitString(input string, lineLength int) string {
	var output strings.Builder
	length := len(input)
	for i := 0; i < length; i += lineLength {
		end := i + lineLength
		if end > length {
			end = length
		}
		line := input[i:end]
		output.WriteString(line)
		if end < length {
			output.WriteString("\n")
		}
	}
	return output.String()
}

func extractCdsSequences(filename string) []string {
	// Open genbank file
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// Read the file line per line
	scanner := bufio.NewScanner(file)
	var cdsSequences []string
	var currentCdsSequence string
	var inCds bool
	for scanner.Scan() {
		line := scanner.Text()

		// Search the CDS line to start
		if strings.HasPrefix(line, "     CDS") {
			// If is in a CDS line it append to the list
			if inCds {
				cdsSequences = append(cdsSequences, currentCdsSequence)
			}
			// Start reading a new CDS line
			currentCdsSequence = line
			inCds = true
		} else if inCds {
			// Append the line to the current CDS sequence
			currentCdsSequence += "\n" + line
		}
	}

	//Add the last sequence to de CDS list
	if inCds {
		cdsSequences = append(cdsSequences, currentCdsSequence)
	}

	return cdsSequences
}

func extractTranslation(cdsSequence string) string {
	// Search the line that have the /translation line
	scanner := bufio.NewScanner(strings.NewReader(cdsSequence))
	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, "                     /translation=") {
			// Extraer la secuencia de /translation
			translation := strings.TrimSpace(line[34:])
			for scanner.Scan() {
				line := scanner.Text()
				if strings.HasPrefix(line, "                     ") {
					translation += strings.TrimSpace(line[21:])
				} else {
					break
				}
			}
			return translation
		}
	}

	return ""
}
