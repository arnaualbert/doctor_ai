package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func localAlignment(seq1, seq2 string, match, mismatch, gap int) (string, string, int) {
	n := len(seq1)
	m := len(seq2)
	score := make([][]int, n+1)
	for i := range score {
		score[i] = make([]int, m+1)
	}
	maxScore := 0
	maxI := 0
	maxJ := 0
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			matchScore := score[i-1][j-1] + match
			deleteScore := score[i-1][j] + gap
			insertScore := score[i][j-1] + gap
			if seq1[i-1] != seq2[j-1] {
				matchScore = score[i-1][j-1] + mismatch
			}
			score[i][j] = max(0, max(matchScore, max(deleteScore, insertScore)))
			if score[i][j] > maxScore {
				maxScore = score[i][j]
				maxI = i
				maxJ = j
			}
		}
	}
	alignedSeq1 := ""
	alignedSeq2 := ""
	i := maxI
	j := maxJ
	for score[i][j] != 0 {
		if score[i][j] == score[i-1][j-1]+match && seq1[i-1] == seq2[j-1] {
			alignedSeq1 = string(seq1[i-1]) + alignedSeq1
			alignedSeq2 = string(seq2[j-1]) + alignedSeq2
			i--
			j--
		} else if score[i][j] == score[i-1][j-1]+mismatch || score[i][j] == score[i-1][j-1]+match {
			alignedSeq1 = string(seq1[i-1]) + alignedSeq1
			alignedSeq2 = string(seq2[j-1]) + alignedSeq2
			i--
			j--
		} else if score[i][j] == score[i-1][j]+gap {
			alignedSeq1 = string(seq1[i-1]) + alignedSeq1
			alignedSeq2 = "-" + alignedSeq2
			i--
		} else {
			alignedSeq1 = "-" + alignedSeq1
			alignedSeq2 = string(seq2[j-1]) + alignedSeq2
			j--
		}
	}
	return alignedSeq1, alignedSeq2, maxScore
}

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
	match_string := os.Args[3]
	mismatch_string := os.Args[4]
	gap_string := os.Args[5]

	match, err := strconv.Atoi(match_string)
	if err != nil {
		panic(err)
	}

	mismatch, err := strconv.Atoi(mismatch_string)
	if err != nil {
		panic(err)
	}

	gap, err := strconv.Atoi(gap_string)
	if err != nil {
		panic(err)
	}

	alignedSeq1, alignedSeq2, score := localAlignment(seq1, seq2, match, mismatch, gap)
	outputFile, err := os.Create("alignment_result.txt")
	if err != nil {
		panic(err)
	}

	fiftystring1 := splitString(alignedSeq1, 50)
	fiftystring2 := splitString(alignedSeq2, 50)
	defer outputFile.Close()
	writer := bufio.NewWriter(outputFile)
	writer.WriteString(header1 + "\n")
	writer.WriteString(fiftystring1 + "\n")
	writer.WriteString(header2 + "\n")
	writer.WriteString(fiftystring2 + "\n")
	writer.WriteString(fmt.Sprintf("Alignment score: %d\n", score))
	writer.Flush()
}
