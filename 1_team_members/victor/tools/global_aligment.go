package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

/*
Global aligment function
@input string seq1
@input string seq1
@return string alignedSeq1
@return string alignedSeq1
*/
func globalAlignment(seq1, seq2 string) (alignedSeq1, alignedSeq2 string, score int) {
	// Initialize variables and matrices
	m, n := len(seq1), len(seq2)
	scoreMatrix := make([][]int, m+1)
	for i := range scoreMatrix {
		scoreMatrix[i] = make([]int, n+1)
	}

	// Fill first row and column
	for i := 1; i <= m; i++ {
		scoreMatrix[i][0] = scoreMatrix[i-1][0] - 1
	}
	for j := 1; j <= n; j++ {
		scoreMatrix[0][j] = scoreMatrix[0][j-1] - 1
	}

	// Fill rest of matrix
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			match := -1
			if seq1[i-1] == seq2[j-1] {
				match = 1
			}
			scoreMatrix[i][j] = max(scoreMatrix[i-1][j]-1, scoreMatrix[i][j-1]-1, scoreMatrix[i-1][j-1]+match)
		}
	}

	// Traceback to get aligned sequences and score
	i, j := m, n
	for i > 0 || j > 0 {
		match := -1
		if i > 0 && j > 0 && seq1[i-1] == seq2[j-1] {
			match = 1
		}
		if i > 0 && j > 0 && scoreMatrix[i][j] == scoreMatrix[i-1][j-1]+match {
			alignedSeq1 = string(seq1[i-1]) + alignedSeq1
			alignedSeq2 = string(seq2[j-1]) + alignedSeq2
			i--
			j--
		} else if i > 0 && scoreMatrix[i][j] == scoreMatrix[i-1][j]-1 {
			alignedSeq1 = string(seq1[i-1]) + alignedSeq1
			alignedSeq2 = "-" + alignedSeq2
			i--
		} else {
			alignedSeq1 = "-" + alignedSeq1
			alignedSeq2 = string(seq2[j-1]) + alignedSeq2
			j--
		}
	}
	score = scoreMatrix[m][n]

	return alignedSeq1, alignedSeq2, score
}

// Función para leer una secuencia de ADN de un archivo fasta
func read_fasta(filepath string) (string, error) {
	// Abrir el archivo de entrada y crear el buffer de lectura
	file, err := os.Open(filepath)
	if err != nil {
		return "", err
	}
	defer file.Close()

	reader := bufio.NewReader(file)

	// Descartar la primera línea (cabecera)
	_, err = reader.ReadString('\n')
	if err != nil {
		return "", err
	}

	// Leer la secuencia de ADN
	var seq strings.Builder
	for {
		line, err := reader.ReadString('\n')
		if err != nil || line[0] == '>' { // el archivo fasta termina o comienza otra secuencia
			break
		}
		seq.WriteString(strings.TrimSpace(line))
	}

	return seq.String(), nil
}

func max(x, y, z int) int {
	if x > y {
		if x > z {
			return x
		} else {
			return z
		}
	} else {
		if y > z {
			return y
		} else {
			return z
		}
	}
}

func main() {
	// Read the sequencs of the fasta files
	seq1, err := read_fasta(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}

	seq2, err := read_fasta(os.Args[2])
	if err != nil {
		fmt.Println(err)
		return
	}

	// Aling the ADN sequences
	alignedSeq1, alignedSeq2, score := globalAlignment(seq1, seq2)

	// Print result in the terminal
	fmt.Println("Aligned sequence 1:", alignedSeq1)
	fmt.Println("Aligned sequence 2:", alignedSeq2)
	fmt.Println("Alignment score:", score)

	// Create the result file
	fileOut, err := os.Create("aligment_result.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer fileOut.Close()

	// Write the aligment result in the output file
	writer := bufio.NewWriter(fileOut)
	fmt.Fprintln(writer, "Alignment score:", score)
	fmt.Fprintln(writer, "Aligned sequence 1:", alignedSeq1)
	fmt.Fprintln(writer, "Aligned sequence 2:", alignedSeq2)
	writer.Flush()
}
