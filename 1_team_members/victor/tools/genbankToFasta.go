// Version 4
// Returns fasta with the id as name, and file location

package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
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

	// Variables para almacenar el identificador y la secuencia
	var id, seq string

	for scanner.Scan() {
		line := scanner.Text()

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
				// seq += (strings.ToUpper(line))
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
	fasta := fmt.Sprintf(">%s\n%s\n", id, upperSeq)

	// Escribir la cadena en formato Fasta en el archivo
	_, err = writer.WriteString(fasta)
	if err != nil {
		return "", "", err
	}
	writer.Flush()

	// Obtener la ruta absoluta del archivo
	absPath, err := filepath.Abs(fastaFile.Name())
	if err != nil {
		return "", "", err
	}

	return fasta, absPath, nil
}

func main() {
	fasta, path, err := genbankToFasta(os.Args[1])

	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Archivo guardado en:", path)
		fmt.Println(fasta)
	}
}
