package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {
	// Obtener la longitud deseada de la secuencia de ADN desde los argumentos de línea de comandos
	if len(os.Args) != 2 {
		fmt.Println("Uso: go run main.go [longitud]")
		return
	}
	length, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("La longitud debe ser un número entero")
		return
	}

	// Generar una secuencia aleatoria de ADN
	rand.Seed(time.Now().UnixNano())
	dna := make([]byte, length)
	for i := 0; i < length; i++ {
		switch rand.Intn(4) {
		case 0:
			dna[i] = 'A'
		case 1:
			dna[i] = 'C'
		case 2:
			dna[i] = 'G'
		case 3:
			dna[i] = 'T'
		}
	}

	// Escribir la secuencia de ADN generada en un archivo fasta
	file, err := os.Create("dna.fasta")
	if err != nil {
		fmt.Println("Error al crear el archivo dna.fasta")
		return
	}
	defer file.Close()

	_, err = file.WriteString(">secuencia_aleatoria\n")
	if err != nil {
		fmt.Println("Error al escribir en el archivo dna.fasta")
		return
	}

	lineWidth := 80
	for i := 0; i < length; i += lineWidth {
		end := i + lineWidth
		if end > length {
			end = length
		}
		line := string(dna[i:end]) + "\n"
		_, err = file.WriteString(line)
		if err != nil {
			fmt.Println("Error al escribir en el archivo dna.fasta")
			return
		}
	}

	fmt.Println("La secuencia de ADN aleatoria ha sido escrita en el archivo dna.fasta")
}

