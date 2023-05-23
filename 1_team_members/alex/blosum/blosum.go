package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var blosum62 = [26][26]int{

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

func getIndex(ch byte) int {
	return int(ch - 'A')
}

func max(nums ...int) int {
	m := nums[0]
	for _, n := range nums[1:] {
		if n > m {
			m = n
		}
	}
	return m
}

func smithWaterman(seq1, seq2 string) (int, string, string, int, int, int, int) {
	m, n := len(seq1), len(seq2)
	matrix := make([][]int, m+1)
	for i := range matrix {
		matrix[i] = make([]int, n+1)
	}

	maxScore := 0
	maxI, maxJ := 0, 0

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			score := blosum62[getIndex(seq1[i-1])][getIndex(seq2[j-1])]
			gap_Cost := os.Args[3]
			gapCost_Extend := os.Args[4]
			gapCost, err := strconv.Atoi(gap_Cost)
			if err != nil {
				panic(err)
			}
			gapCostExtend, err := strconv.Atoi(gapCost_Extend)
			if err != nil {
				panic(err)
			}

			matrix[i][j] = max(0, matrix[i-1][j-1]+score, matrix[i-1][j]-gapCost-gapCostExtend, matrix[i][j-1]-gapCost-gapCostExtend)

			if matrix[i][j] > maxScore {
				maxScore = matrix[i][j]
				maxI, maxJ = i, j
			}
		}
	}

	var alignedSeq1, alignedSeq2 []byte
	i, j := maxI, maxJ

	for i > 0 && j > 0 {
		score := blosum62[getIndex(seq1[i-1])][getIndex(seq2[j-1])]
		if matrix[i][j] == matrix[i-1][j-1]+score {
			alignedSeq1 = append(alignedSeq1, seq1[i-1])
			alignedSeq2 = append(alignedSeq2, seq2[j-1])
			i--
			j--
		} else if matrix[i][j] == matrix[i-1][j]-1 {
			alignedSeq1 = append(alignedSeq1, seq1[i-1])
			alignedSeq2 = append(alignedSeq2, '-')
			i--
		} else if matrix[i][j] == matrix[i][j-1]-1 {
			alignedSeq1 = append(alignedSeq1, '-')
			alignedSeq2 = append(alignedSeq2, seq2[j-1])
			j--
		} else {
			break
		}
	}

	first_seq_end := len(alignedSeq1) + i + 2
	second_seq_end := len(alignedSeq2) + j + 2

	first_seq := i + 2
	second_seq := j + 2

	return maxScore, string(alignedSeq1), string(alignedSeq2), first_seq, second_seq, first_seq_end, second_seq_end
}

func main() {
	file1, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}
	defer file1.Close()
	scanner1 := bufio.NewScanner(file1)
	scanner1.Scan()
	header1 := scanner1.Text()
	seq1 := ""
	for scanner1.Scan() {
		seq1 += scanner1.Text()
	}
	file2, err := os.Open(os.Args[2])
	if err != nil {
		panic(err)
	}
	defer file2.Close()
	scanner2 := bufio.NewScanner(file2)
	scanner2.Scan()
	header2 := scanner2.Text()
	seq2 := ""
	for scanner2.Scan() {
		seq2 += scanner2.Text()
	}

	outputFile, err := os.Create(os.Args[5])
	if err != nil {
		panic(err)
	}

	defer outputFile.Close()
	writer := bufio.NewWriter(outputFile)

	score, alignedSeq1, alignedSeq2, locI, locJ, locfI, locfJ := smithWaterman(seq1, seq2)
	fmt.Printf("La similitud entre las secuencias \"%s\" y \"%s\" es: %d\n", seq1, seq2, score)
	writer.WriteString(fmt.Sprintf("%s %d %s %d\n", header1, locI, alignedSeq1, locfI))
	writer.WriteString(fmt.Sprintf("%s %d %s %d\n", header2, locJ, alignedSeq2, locfJ))
	writer.WriteString(fmt.Sprintf("Alignment score: %d", score))
	writer.Flush()
}
