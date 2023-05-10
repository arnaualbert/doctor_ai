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
func globalAlignment(seq1 string, seq2 string, gapOpen int, gapExtend float64, matrix [][]int) (string, string, int) {
	m, n := len(seq1), len(seq2)

	// Inicializar la matriz de puntuación y la matriz de rutas
	scoreMatrix := make([][]int, m+1)
	for i := range scoreMatrix {
		scoreMatrix[i] = make([]int, n+1)
	}
	routeMatrix := make([][]int, m+1)
	for i := range routeMatrix {
		routeMatrix[i] = make([]int, n+1)
	}

	// Inicializar las variables de gap
	// var gapOpening bool
	var gapExtendScore float64
	var gapOpenScore int

	if gapOpen == 0 {
		// gapOpening = false
		gapExtendScore = gapExtend
		gapOpenScore = 0
	} else {
		// gapOpening = true
		gapExtendScore = float64(gapOpen) + gapExtend
		gapOpenScore = gapOpen
	}

	// Llenar la primera fila y la primera columna con las penalizaciones por gap
	for i := 1; i <= m; i++ {
		scoreMatrix[i][0] = gapOpenScore
		routeMatrix[i][0] = 1
	}
	for j := 1; j <= n; j++ {
		scoreMatrix[0][j] = gapOpenScore
		routeMatrix[0][j] = 2
	}

	// Calcular la puntuación de cada celda en la matriz de puntuación
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			print(seq1[i-1])
			print("\n")
			print(seq2[j-1])
			matchScore := matrix[seq1[i-1]-'A'][seq2[j-1]-'A']
			diagonalScore := scoreMatrix[i-1][j-1] + matchScore
			upScore := scoreMatrix[i-1][j] + int(gapExtendScore)
			leftScore := scoreMatrix[i][j-1] + int(gapExtendScore)
			maxScore := max(diagonalScore, upScore, leftScore)
			if maxScore == diagonalScore {
				routeMatrix[i][j] = 3
			} else if maxScore == upScore {
				routeMatrix[i][j] = 1
			} else {
				routeMatrix[i][j] = 2
			}
			scoreMatrix[i][j] = maxScore
		}
	}

	// Reconstruir los alineamientos
	align1, align2 := "", ""
	i, j := m, n
	for i > 0 || j > 0 {
		if routeMatrix[i][j] == 3 {
			align1 = string(seq1[i-1]) + align1
			align2 = string(seq2[j-1]) + align2
			i--
			j--
		} else if routeMatrix[i][j] == 1 {
			align1 = string(seq1[i-1]) + align1
			align2 = "-" + align2
			i--
		} else {
			align1 = "-" + align1
			align2 = string(seq2[j-1]) + align2
			j--
		}
	}

	return align1, align2, scoreMatrix[m][n]
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
	alignedSeq1, alignedSeq2, score := globalAlignment(seq1, seq2, int(gap_open), gap_extend, blosum62)

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
