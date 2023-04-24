package main

import (
	"fmt"
	"os"
)

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

	// seq1 := "CGGCGGCGCGCGCGGCGCCGGCGGCGCGCGCGGCGCCGGCGGCGCGCGCGGCGCCGGCGGCGCGCGCGGCGC"
	// seq2 := "CGCGCGCTAACGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCG"
	// alignedSeq1, alignedSeq2, score := globalAlignment(seq1, seq2)

	// Example usage
	alignedSeq1, alignedSeq2, score := globalAlignment(os.Args[1], os.Args[2])

	// Print the alignment
	fmt.Println("Aligned sequence 1:", alignedSeq1)
	fmt.Println("Aligned sequence 2:", alignedSeq2)
	fmt.Println("Alignment score:", score)

	// Create the file
	file, err := os.Create("result.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	// Escribimos en el archivo
	// fmt.Fprintln(file, "Aligned sequence 1:", alignedSeq1)
	// fmt.Fprintln(file, "Aligned sequence 2:", alignedSeq2)
	// fmt.Fprintln(file, "Alignment score:", score)
}
