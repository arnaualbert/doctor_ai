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

func localAlignment(seq1 string, seq2 string, match int, mismatch int, gap int, gapLeft int, gapUp int) (string, string, int, int, int, int, int) {
	n := len(seq1)
	m := len(seq2)
	score := make([][]int, n+1) // n+1
	for i := range score {
		score[i] = make([]int, m+1) // m+1
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

	gap_I := gapLeft

	gap_J := gapUp

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
			alignedSeq1 = string(seq1[i+gap_I]) + alignedSeq1
			alignedSeq2 = "-" + alignedSeq2
			i--
		} else {
			alignedSeq1 = "-" + alignedSeq1
			alignedSeq2 = string(seq2[j+gap_J]) + alignedSeq2
			j--
		}
	}

	first_seq_end := len(alignedSeq1) + i
	second_seq_end := len(alignedSeq2) + j

	first_seq := i + 1
	second_seq := j + 1

	return alignedSeq1, alignedSeq2, maxScore, first_seq, second_seq, first_seq_end, second_seq_end
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

func readFastaFile(filename string) ([]string, []string, error) {
	file, err := os.Open(filename)
	if err != nil {
		println("Error reading")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var sequences []string
	var sequence strings.Builder
	var headers []string

	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, ">") {
			headers = append(headers, line)
			if sequence.Len() > 0 {
				sequences = append(sequences, sequence.String())
				sequence.Reset()
			}
			continue
		}
		sequence.WriteString(line)
	}

	if sequence.Len() > 0 {
		sequences = append(sequences, sequence.String())
	}

	return sequences, headers, nil
}

func main() {
	file1 := os.Args[1]

	file2 := os.Args[2]

	seq1, header1, err := readFastaFile(file1)
	if err != nil {
		fmt.Printf("Error reading %s: %v\n", file1, err)
		return
	}

	seq2List, header2, err := readFastaFile(file2)
	if err != nil {
		fmt.Printf("Error reading %s: %v\n", file2, err)
		return
	}

	match_string := os.Args[3]
	mismatch_string := os.Args[4]
	gap_string := os.Args[5]
	gap_I := os.Args[6]
	gap_J := os.Args[7]

	// fmt.Println()

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

	gapI, err := strconv.Atoi(gap_I)
	if err != nil {
		panic(err)
	}

	gapJ, err := strconv.Atoi(gap_J)
	if err != nil {
		panic(err)
	}
	outputFile, err := os.Create(os.Args[8])
	i := 0
	for _, seq2 := range seq2List {

		alignedSeq1, alignedSeq2, score, locI, locJ, locfI, locfJ := localAlignment(seq1[0], seq2, match, mismatch, gap, gapI, gapJ)
		if err != nil {
			panic(err)
		}
		fiftystring1 := splitString(alignedSeq1, 50)
		fiftystring2 := splitString(alignedSeq2, 50)

		writer := bufio.NewWriter(outputFile)
		// seq_to_write := header2[i]

		writer.WriteString(fmt.Sprintf("%s %d %s %d\n", header1[0], locI, fiftystring1, locfI))
		writer.WriteString(fmt.Sprintf("%s %d %s %d\n", header2[i], locJ, fiftystring2, locfJ))
		writer.WriteString(fmt.Sprintf("Alignment score: %d\n\n", score))
		writer.Flush()
		i = i + 1

	}
	defer outputFile.Close()
}
