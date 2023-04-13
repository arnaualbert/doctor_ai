package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func genbankToFasta(file string) (string, error) {

	// Abrir el archivo en modo lectura
	f, err := os.Open(file)
	if err != nil {
		return "", err
	}
	defer f.Close()

	// Crear un nuevo archivo en modo escritura con extensión .fasta
	fastaFile, err := os.Create(strings.TrimSuffix(file, ".gb") + ".fasta")
	if err != nil {
		return "", err
	}
	defer fastaFile.Close()

	// Escribir la cadena en formato Fasta en el archivo
	writer := bufio.NewWriter(fastaFile)

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
				// seq += strings.ReplaceAll(line, " ", "")

			}
		}
	}

	// Crear la cadena en formato Fasta

	fasta := fmt.Sprintf(">%s\n", id)
	for i := 0; i < len(seq); i += 70 {
		end := i + 70
		if end > len(seq) {
			end = len(seq)
		}
		fasta += strings.ToUpper(seq[i:end]) + "\n"
	}

	// Escribir la cadena en formato Fasta en el archivo
	_, err = writer.WriteString(fasta)
	if err != nil {
		return "", err
	}
	writer.Flush()

	return fasta, nil
}

func main() {
	fasta, err := genbankToFasta("sequence.gb")

	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println(fasta)
	}
}
