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

/*
Global aligment function
@input string seq1
@input string seq1
@return string alignedSeq1
@return string alignedSeq1
*/
func globalAlignment(seq1 string, seq2 string, gapOpen, gapExtend float64, matrix [][]int) (string, string, int) {
	// Obtener la longitud de las secuencias
	n := len(seq1)
	m := len(seq2)

	// Inicializar la matriz de puntuaciones y las matrices de dirección
	score := make([][]int, n+1)
	traceback := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		score[i] = make([]int, m+1)
		traceback[i] = make([]int, m+1)
	}

	// Inicializar los valores de gap en la primera fila y columna
	for i := 1; i <= n; i++ {
		score[i][0] = int(gapOpen + float64(i-1)*gapExtend)
		traceback[i][0] = 1
	}
	for j := 1; j <= m; j++ {
		score[0][j] = int(gapOpen + float64(j-1)*gapExtend)
		traceback[0][j] = 2
	}

	// Llenar la matriz de puntuaciones y la matriz de dirección
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			matchScore := matrix[seq1[i-1]-65][seq2[j-1]-65]
			diagScore := score[i-1][j-1] + matchScore
			upScore := score[i-1][j] + int(gapOpen+gapExtend)
			leftScore := score[i][j-1] + int(gapOpen+gapExtend)

			// Obtener la puntuación máxima y actualizar la matriz de dirección
			maxScore := max(diagScore, upScore, leftScore)
			score[i][j] = maxScore
			if maxScore == diagScore {
				traceback[i][j] = 3
			} else if maxScore == upScore {
				traceback[i][j] = 1
			} else if maxScore == leftScore {
				traceback[i][j] = 2
			}
		}
	}

	// Obtener la puntuación de alineamiento óptima
	maxScore := score[n][m]

	// Inicializar las cadenas de alineamiento y la posición actual
	align1 := ""
	align2 := ""
	i := n
	j := m

	// Obtener los alineamientos mediante la matriz de dirección
	for i > 0 || j > 0 {
		if traceback[i][j] == 3 {
			align1 = string(seq1[i-1]) + align1
			align2 = string(seq2[j-1]) + align2
			i--
			j--
		} else if traceback[i][j] == 1 {
			align1 = string(seq1[i-1]) + align1
			align2 = "-" + align2
			i--
		} else if traceback[i][j] == 2 {
			align1 = "-" + align1
			align2 = string(seq2[j-1]) + align2
			j--
		} else {
			break
		}
	}

	return align1, align2, maxScore
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

	// Aling the ADN sequences
	alignedSeq1, alignedSeq2, score := globalAlignment(seq1, seq2, gap_open, gap_extend, blosum62)

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
