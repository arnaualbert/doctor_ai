package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

/*
Global aligment function
@input string seq1
@input string seq1
@return string alignedSeq1
@return string alignedSeq1
*/

// func needlemanWunsch(seq1, seq2 string, blosum [][]float64, gapOpenPenalty, gapExtendPenalty, mismatchScore float64) (string, string, float64) {
// 	n := len(seq1) + 1
// 	m := len(seq2) + 1
// 	scoreMatrix := make([][]float64, n)
// 	pointerMatrix := make([][]int, n)
// 	var score float64

// 	for i := 0; i < n; i++ {
// 		scoreMatrix[i] = make([]float64, m)
// 		pointerMatrix[i] = make([]int, m)
// 	}

// 	for i := 1; i < n; i++ {
// 		scoreMatrix[i][0] = float64(i) * gapExtendPenalty
// 	}

// 	for j := 1; j < m; j++ {
// 		scoreMatrix[0][j] = float64(j) * gapExtendPenalty
// 	}

// 	for i := 1; i < n; i++ {
// 		for j := 1; j < m; j++ {
// 			match := scoreMatrix[i-1][j-1]
// 			if seq1[i-1] == seq2[j-1] {
// 				match += mismatchScore
// 			} else {
// 				match += blosum[int(seq1[i-1]-'A')][int(seq2[j-1]-'A')]
// 			}

// 			delete := scoreMatrix[i-1][j] - gapOpenPenalty
// 			insert := scoreMatrix[i][j-1] - gapOpenPenalty

// 			scoreMatrix[i][j] = math.Max(math.Max(match, delete), insert)

// 			if scoreMatrix[i][j] == match {
// 				pointerMatrix[i][j] = 1
// 			} else if scoreMatrix[i][j] == delete {
// 				pointerMatrix[i][j] = 2
// 			} else {
// 				pointerMatrix[i][j] = 3
// 			}

// 			if scoreMatrix[i][j] > score {
// 				score = scoreMatrix[i][j]
// 			}
// 		}
// 	}

// 	alignedSeq1 := ""
// 	alignedSeq2 := ""

// 	i := n - 1
// 	j := m - 1

//		for i > 0 || j > 0 {
//			if pointerMatrix[i][j] == 1 {
//				alignedSeq1 = string(seq1[i-1]) + alignedSeq1
//				alignedSeq2 = string(seq2[j-1]) + alignedSeq2
//				i--
//				j--
//			} else if pointerMatrix[i][j] == 2 {
//				alignedSeq1 = string(seq1[i-1]) + alignedSeq1
//				alignedSeq2 = "-" + alignedSeq2
//				i--
//			} else {
//				alignedSeq1 = "-" + alignedSeq1
//				alignedSeq2 = string(seq2[j-1]) + alignedSeq2
//				j--
//			}
//		}
//		print(alignedSeq1)
//		print("\n")
//		print(alignedSeq2)
//		return alignedSeq1, alignedSeq2, score
//	}
var blosum62 = [26][26]float64{
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

func needlemanWunsch(seq1, seq2 string, blosum [][]float64, gapOpenPenalty, gapExtendPenalty, matchScore, mismatchScore float64) (string, string, float64) {
	n := len(seq1) + 1
	m := len(seq2) + 1
	scoreMatrix := make([][]float64, n)
	pointerMatrix := make([][]int, n)
	var score float64

	for i := 0; i < n; i++ {
		scoreMatrix[i] = make([]float64, m)
		pointerMatrix[i] = make([]int, m)
	}

	for i := 1; i < n; i++ {
		scoreMatrix[i][0] = float64(i) * gapExtendPenalty
	}

	for j := 1; j < m; j++ {
		scoreMatrix[0][j] = float64(j) * gapExtendPenalty
	}

	for i := 1; i < n; i++ {
		for j := 1; j < m; j++ {
			match := scoreMatrix[i-1][j-1]
			if seq1[i-1] == seq2[j-1] {
				match += matchScore
			} else {
				match += mismatchScore
			}

			delete := scoreMatrix[i-1][j] - gapOpenPenalty
			insert := scoreMatrix[i][j-1] - gapOpenPenalty

			scoreMatrix[i][j] = math.Max(math.Max(match, delete), insert)

			if scoreMatrix[i][j] == match {
				pointerMatrix[i][j] = 1
			} else if scoreMatrix[i][j] == delete {
				pointerMatrix[i][j] = 2
			} else {
				pointerMatrix[i][j] = 3
			}
			if scoreMatrix[i][j] > score {
				score = scoreMatrix[i][j]
			}
		}
	}

	alignedSeq1 := ""
	alignedSeq2 := ""

	i := n - 1
	j := m - 1

	for i > 0 || j > 0 {
		println(i)
		println(j)
		if pointerMatrix[i][j] == 1 {
			alignedSeq1 = string(seq1[i-1]) + alignedSeq1
			alignedSeq2 = string(seq2[j-1]) + alignedSeq2
			i--
			j--
		} else if pointerMatrix[i][j] == 2 {
			alignedSeq1 = string(seq1[i-1]) + alignedSeq1
			alignedSeq2 = "-" + alignedSeq2
			i--
		} else {
			alignedSeq1 = "-" + alignedSeq1
			alignedSeq2 = string(seq2[j-1]) + alignedSeq2
			j--
		}
	}

	return alignedSeq1, alignedSeq2, score
}

// func max(values ...int) int {
// 	maxVal := values[0]
// 	for _, val := range values {
// 		if val > maxVal {
// 			maxVal = val
// 		}
// 	}
// 	return maxVal
// }

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
	gap_open, err := strconv.ParseFloat(os.Args[3], 64)
	if err != nil {
		gap_open = 10.0 // Valor por defecto
	}
	gap_extend, err := strconv.ParseFloat(os.Args[4], 64)
	if err != nil {
		gap_extend = 0.5 // Valor por defecto
	}
	mismatch_score, err := strconv.ParseFloat(os.Args[5], 64)
	if err != nil {
		mismatch_score = -1 // Valor por defecto
	}
	matchScore := 10.0
	// Aling the ADN sequences
	alignedSeq1, alignedSeq2, score := needlemanWunsch(seq1, seq2, blosum62, gap_open, gap_extend, mismatch_score, float64(matchScore))
	fmt.Println("The score is: ", score)
	// Print result in the terminal
	// fmt.Println("Aligned sequence 1:", alignedSeq1)
	// fmt.Println("Aligned sequence 2:", alignedSeq2)
	// fmt.Println("Alignment score:", score)

	// Create the result file
	fileOut, err := os.Create("global_alignment_result.txt")
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
