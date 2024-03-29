package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var blosum62 = [][]int{
	{4.0, -1.0, -2.0, -2.0, 0.0, -1.0, -1.0, 0.0, -2.0, -1.0, -1.0, -1.0, -1.0, -2.0, -1.0, 1.0, 0.0, -3.0, -2.0, 0.0, -2.0, -1.0, 0.0, -4.0},
	{-1.0, 5.0, 0.0, -2.0, -3.0, 1.0, 0.0, -2.0, 0.0, -3.0, -2.0, 2.0, -1.0, -3.0, -2.0, -1.0, -1.0, -3.0, -2.0, -3.0, -1.0, 0.0, -1.0, -4.0},
	{-2.0, 0.0, 6.0, 1.0, -3.0, 0.0, 0.0, 0.0, 1.0, -3.0, -3.0, 0.0, -2.0, -3.0, -2.0, 1.0, 0.0, -4.0, -2.0, -3.0, 3.0, 0.0, -1.0, -4.0},
	{-2.0, -2.0, 1.0, 6.0, -3.0, 0.0, 2.0, -1.0, -1.0, -3.0, -4.0, -1.0, -3.0, -3.0, -1.0, 0.0, -1.0, -4.0, -3.0, -3.0, 4.0, 1.0, -1.0, -4.0},
	{0.0, -3.0, -3.0, -3.0, 9.0, -3.0, -4.0, -3.0, -3.0, -1.0, -1.0, -3.0, -1.0, -2.0, -3.0, -1.0, -1.0, -2.0, -2.0, -1.0, -3.0, -3.0, -2.0, -4.0},
	{-1.0, 1.0, 0.0, 0.0, -3.0, 5.0, 2.0, -2.0, 0.0, -3.0, -2.0, 1.0, 0.0, -3.0, -1.0, 0.0, -1.0, -2.0, -1.0, -2.0, 0.0, 3.0, -1.0, -4.0},
	{-1.0, 0.0, 0.0, 2.0, -4.0, 2.0, 5.0, -2.0, 0.0, -3.0, -3.0, 1.0, -2.0, -3.0, -1.0, 0.0, -1.0, -3.0, -2.0, -2.0, 1.0, 4.0, -1.0, -4.0},
	{0.0, -2.0, 0.0, -1.0, -3.0, -2.0, -2.0, 6.0, -2.0, -4.0, -4.0, -2.0, -3.0, -3.0, -2.0, 0.0, -2.0, -2.0, -3.0, -3.0, -1.0, -2.0, -1.0, -4.0},
	{-2.0, 0.0, 1.0, -1.0, -3.0, 0.0, 0.0, -2.0, 8.0, -3.0, -3.0, -1.0, -2.0, -1.0, -2.0, -1.0, -2.0, -2.0, 2.0, -3.0, 0.0, 0.0, -1.0, -4.0},
	{-1.0, -3.0, -3.0, -3.0, -1.0, -3.0, -3.0, -4.0, -3.0, 4.0, 2.0, -3.0, 1.0, 0.0, -3.0, -2.0, -1.0, -3.0, -1.0, 3.0, -3.0, -3.0, -1.0, -4.0},
	{-1.0, -2.0, -3.0, -4.0, -1.0, -2.0, -3.0, -4.0, -3.0, 2.0, 4.0, -2.0, 2.0, 0.0, -3.0, -2.0, -1.0, -2.0, -1.0, 1.0, -4.0, -3.0, -1.0, -4.0},
	{-1.0, 2.0, 0.0, -1.0, -3.0, 1.0, 1.0, -2.0, -1.0, -3.0, -2.0, 5.0, -1.0, -3.0, -1.0, 0.0, -1.0, -3.0, -2.0, -2.0, 0.0, 1.0, -1.0, -4.0},
	{-1.0, -1.0, -2.0, -3.0, -1.0, 0.0, -2.0, -3.0, -2.0, 1.0, 2.0, -1.0, 5.0, 0.0, -2.0, -1.0, -1.0, -1.0, -1.0, 1.0, -3.0, -1.0, -1.0, -4.0},
	{-2.0, -3.0, -3.0, -3.0, -2.0, -3.0, -3.0, -3.0, -1.0, 0.0, 0.0, -3.0, 0.0, 6.0, -4.0, -2.0, -2.0, 1.0, 3.0, -1.0, -3.0, -3.0, -1.0, -4.0},
	{-1.0, -2.0, -2.0, -1.0, -3.0, -1.0, -1.0, -2.0, -2.0, -3.0, -3.0, -1.0, -2.0, -4.0, 7.0, -1.0, -1.0, -4.0, -3.0, -2.0, -2.0, -1.0, -2.0, -4.0},
	{1.0, -1.0, 1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, -2.0, -2.0, 0.0, -1.0, -2.0, -1.0, 4.0, 1.0, -3.0, -2.0, -2.0, 0.0, 0.0, 0.0, -4.0},
	{0.0, -1.0, 0.0, -1.0, -1.0, -1.0, -1.0, -2.0, -2.0, -1.0, -1.0, -1.0, -1.0, -2.0, -1.0, 1.0, 5.0, -2.0, -2.0, 0.0, -1.0, -1.0, 0.0, -4.0},
	{-3.0, -3.0, -4.0, -4.0, -2.0, -2.0, -3.0, -2.0, -2.0, -3.0, -2.0, -3.0, -1.0, 1.0, -4.0, -3.0, -2.0, 11.0, 2.0, -3.0, -4.0, -3.0, -2.0, -4.0},
	{-2.0, -2.0, -2.0, -3.0, -2.0, -1.0, -2.0, -3.0, 2.0, -1.0, -1.0, -2.0, -1.0, 3.0, -3.0, -2.0, -2.0, 2.0, 7.0, -1.0, -3.0, -2.0, -1.0, -4.0},
	{0.0, -3.0, -3.0, -3.0, -1.0, -2.0, -2.0, -3.0, -3.0, 3.0, 1.0, -2.0, 1.0, -1.0, -2.0, -2.0, 0.0, -3.0, -1.0, 4.0, -3.0, -2.0, -1.0, -4.0},
	{-2.0, -1.0, 3.0, 4.0, -3.0, 0.0, 1.0, -1.0, 0.0, -3.0, -4.0, 0.0, -3.0, -3.0, -2.0, 0.0, -1.0, -4.0, -3.0, -3.0, 4.0, 1.0, -1.0, -4.0},
	{-1.0, 0.0, 0.0, 1.0, -3.0, 3.0, 4.0, -2.0, 0.0, -3.0, -3.0, 1.0, -1.0, -3.0, -1.0, 0.0, -1.0, -3.0, -2.0, -2.0, 1.0, 4.0, -1.0, -4.0},
	{0.0, -1.0, -1.0, -1.0, -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0, 0.0, 0.0, -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -4.0},
	{-4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0, 1.0},
}

var blosum62_v2 = [][]int{
	{-1, 4, 0, 0, -2, 2, -1, -1, 0, -2, -1, 1, 0, -2, -1, 1, 0, 0, 0, -3},          // A
	{4, -1, 1, 1, -3, 0, 3, 0, -1, -3, -2, 0, -1, -3, -2, 0, 0, -1, -2, -3},        // R
	{0, 1, -1, 1, -1, 0, 0, 0, 1, -2, -1, 0, -1, -2, -2, 0, 0, 0, -2, -3},          // N
	{0, 1, 1, -1, -3, 0, 1, 0, 0, -3, -2, 0, -2, -4, -2, 0, -1, -1, -3, -4},        // D
	{-2, -3, -1, -3, 9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -2, -1, -2, -1, 1}, // C
	{2, 0, 0, 0, -3, -1, 1, 0, -1, -2, -1, 0, -1, -3, -1, 0, 0, -1, -2, -3},        // Q
	{-1, 3, 0, 1, -4, 1, -1, -1, 0, -3, -2, 1, 0, -3, -2, 1, 0, 0, -2, -4},         // E
	{-1, 0, 0, 0, -3, 0, -1, -1, -1, -2, -2, 0, -2, -3, -2, 0, -1, -1, -2, -3},     // G
	{0, -1, 1, 0, -3, -1, 0, -1, -1, -2, -1, -1, -2, -2, -2, 0, -1, 0, -2, -3},     // H
	{-2, -3, -2, -3, -1, -2, -3, -2, -2, 3, 1, -2, 1, 0, -2, -2, -1, -2, 7, -1},    // I
	{-1, -2, -1, -2, -1, -1, -2, -2, -1, 1, 5, -1, 2, 0, -1, -1, -1, -1, 0, -3},    // L
	{1, 0, 0, 0, -3, 0, 1, 0, -1, -2, -1, -1, -1, -2, -1, 0, 0, -1, -2, -3},        // K
	{0, -1, -1, -2, -1, -1, -1, -2, -2, 1, 2, -1, 5, 0, -2, -1, -1, -1, 0, -3},     // M
	{-2, -3, -2, -4, -2, -3, -3, -3, -2, 0, 0, -2, 0, 8, -3, -2, -1, -2, 2, -3},    // F
	{-1, -2, -2, -2, -3, -2, -2, -2, -2, -1, -1, -2, -1, -3, 5, -1, 0, -1, -1, -2}, // P
	{1, 0, 0, 0, -2, 0, 0, 0, 0, -2, -1, 0, -1, -2, -1, 4, 1, 0, -2, -3},           // S
	{0, 0, 0, -1, -1, 0, 0, 0, -1, -1, -1, 0, -1, -1, 0, 1, 5, 2, 0, -2},           // T
	{0, -1, 0, -1, -2, -1, 0, -1, -1, 0, 0, -1, 0, -2, -1, 0, 2, 5, -1, -2},        // W
	{0, -2, -2, -3, -1, -2, -2, -2, -2, -3, -2, -2, -1, 2, -1, -2, 0, -1, 5, -3},   // Y
	{-3, -3, -3, -4, 1, -3, -3, -3, -2, -1, -1, -3, -1, -3, -2, -3, -2, -2, -3, 4}, // V
}

/*
Global aligment function
@input string seq1
@input string seq1
@return string alignedSeq1
@return string alignedSeq1
*/
func globalAlignment(seq1 string, seq2 string, gapScore int, blosum62 [][]int) (alignedSeq1, alignedSeq2 string, score int) {

	m, n := len(seq1), len(seq2)
	scoreMatrix := make([][]int, m+1)
	for i := range scoreMatrix {
		scoreMatrix[i] = make([]int, n+1)
	}

	for i := 1; i <= m; i++ {
		scoreMatrix[i][0] = scoreMatrix[i-1][0] + gapScore
	}
	for j := 1; j <= n; j++ {
		scoreMatrix[0][j] = scoreMatrix[0][j-1] + gapScore
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			match := blosum62[getIndex(seq1[i-1])][getIndex(seq2[j-1])]
			scoreMatrix[i][j] = max(scoreMatrix[i-1][j]+gapScore, scoreMatrix[i][j-1]+gapScore, scoreMatrix[i-1][j-1]+match)
		}
	}

	i, j := m, n
	for i > 0 || j > 0 {
		match := blosum62[getIndex(seq1[i-1])][getIndex(seq2[j-1])]
		if i > 0 && j > 0 && scoreMatrix[i][j] == scoreMatrix[i-1][j-1]+match {
			alignedSeq1 = string(seq1[i-1]) + alignedSeq1
			alignedSeq2 = string(seq2[j-1]) + alignedSeq2
			i--
			j--
		} else if i > 0 && scoreMatrix[i][j] == scoreMatrix[i-1][j]+gapScore {
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
func max(a, b, c int) int {
	if a >= b && a >= c {
		return a
	} else if b >= a && b >= c {
		return b
	} else {
		return c
	}
}

func getIndex(c byte) int {
	switch c {
	case 'A':
		return 0
	case 'R':
		return 1
	case 'N':
		return 2
	case 'D':
		return 3
	case 'C':
		return 4
	case 'Q':
		return 5
	case 'E':
		return 6
	case 'G':
		return 7
	case 'H':
		return 8
	case 'I':
		return 9
	case 'L':
		return 10
	case 'K':
		return 11
	case 'M':
		return 12
	case 'F':
		return 13
	case 'P':
		return 14
	case 'S':
		return 15
	case 'T':
		return 16
	case 'W':
		return 17
	case 'Y':
		return 18
	case 'V':
		return 19
	default:
		return -1
	}
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

/*
 */
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

	gap_score, err := strconv.Atoi(os.Args[3])
	if err != nil {
		gap_score = -1.0 // Valor por defecto
	}

	// Aling the ADN sequences
	alignedSeq1, alignedSeq2, score := globalAlignment(seq1, seq2, gap_score, blosum62_v2)

	// Print result in the terminal
	// fmt.Println("Aligned sequence 1:", alignedSeq1)
	// fmt.Println("Aligned sequence 2:", alignedSeq2)
	// fmt.Println("Alignment score:", score)

	// Create the result file
	fileOut, err := os.Create(os.Args[4])
	if err != nil {
		fmt.Println(err)
		return
	}
	defer fileOut.Close()

	fiftystring1 := splitString(alignedSeq1, 50)
	fiftystring2 := splitString(alignedSeq2, 50)

	// Write the aligment result in the output file
	writer := bufio.NewWriter(fileOut)

	fmt.Fprintln(writer, "Alignment score:", score)

	fmt.Fprintln(writer, ">Aligned sequence 1:")
	writer.WriteString(fiftystring1 + "\n")

	fmt.Fprintln(writer, ">Aligned sequence 2:")
	writer.WriteString(fiftystring2 + "\n")

	writer.Flush()
}
