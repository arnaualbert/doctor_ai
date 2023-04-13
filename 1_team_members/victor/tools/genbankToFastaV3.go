// Version 3
// Returns fasta with the id as name

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func addLineBreaks(s string) string {
	var b strings.Builder
	for i, r := range s {
		if (i > 0) && (i%70 == 0) {
			b.WriteRune('\n')
		}
		b.WriteRune(r)
	}
	return b.String()
}
func genbankToFasta(file string) (string, string, error) {

	// Abrir el archivo en modo lectura
	f, err := os.Open(file)
	if err != nil {
		return "", "", err
	}
	defer f.Close()

	// Leer el archivo línea por línea
	scanner := bufio.NewScanner(f)

	// Variables para almacenar el identificador, la definición y la secuencia
	var id, definition, seq string

	for scanner.Scan() {
		line := scanner.Text()

		// Extraer el identificador y la definición de la línea DEFINITION
		if strings.HasPrefix(line, "DEFINITION") {
			definition = strings.TrimSpace(strings.TrimPrefix(line, "DEFINITION"))
		}

		// Extraer el identificador de la línea LOCUS
		if strings.HasPrefix(line, "LOCUS") {
			fields := strings.Fields(line)
			id = fields[1]
		}

		// Comenzar a leer la secuencia a partir de la línea ORIGIN
		if strings.HasPrefix(line, "ORIGIN") {
			for scanner.Scan() {
				line := scanner.Text()

				// Fin del archivo
				if strings.HasPrefix(line, "//") {
					break
				}

				// Eliminar los espacios y los números de línea de la secuencia
				seq += (strings.TrimLeft(line[10:], "0123456789"))
			}
		}
	}

	// Crear un nuevo archivo en modo escritura con extensión .fasta
	fastaFile, err := os.Create(id + ".fasta")
	if err != nil {
		return "", "", err
	}
	defer fastaFile.Close()

	// Escribir la cadena en formato Fasta en el archivo
	writer := bufio.NewWriter(fastaFile)
	// Seq to upper case
	upperSeq := strings.ToUpper(seq)
	upperSeq = strings.ReplaceAll(upperSeq, " ", "")

	// Add a line break every 50 characters
	var builder strings.Builder
	for i, char := range upperSeq {
		builder.WriteRune(char)
		if (i+1)%70 == 0 {
			builder.WriteString("\n")
		}
	}
	upperSeq = builder.String()

	// Create the string with fasta format
	fasta := fmt.Sprintf(">%s %s\n%s\n", id, definition, upperSeq)

	// Escribir la cadena en formato Fasta en el archivo
	_, err = writer.WriteString(fasta)
	if err != nil {
		return "", "", err
	}
	writer.Flush()

	return fasta, fastaFile.Name(), nil
}

func main() {
	fasta, fileName, err := genbankToFasta(os.Args[1])

	if err != nil {
		fmt.Println("Error:", err, fileName)
	} else {
		fmt.Println(fasta)
		// fmt.Println("Successfuly created FASTA:", fileName)
	}
}
