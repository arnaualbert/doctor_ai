package main

import (
    "fmt"
)

func needlemanWunsch(seq1, seq2 string) (int, string, string) {
    // Creamos la matriz de puntuación
    scoreMatrix := make([][]int, len(seq1)+1)
    for i := 0; i <= len(seq1); i++ {
        scoreMatrix[i] = make([]int, len(seq2)+1)
    }
    
    // Inicializamos la primera fila y columna
    for i := 0; i <= len(seq1); i++ {
        scoreMatrix[i][0] = i * -1
    }
    for j := 0; j <= len(seq2); j++ {
        scoreMatrix[0][j] = j * -1
    }
    
    // Llenamos la matriz de puntuación
    for i := 1; i <= len(seq1); i++ {
        for j := 1; j <= len(seq2); j++ {
            match := scoreMatrix[i-1][j-1]
            if seq1[i-1] == seq2[j-1] {
                match += 1
            } else {
                match -= 1
            }
            delete := scoreMatrix[i-1][j] - 1
            insert := scoreMatrix[i][j-1] - 1
            scoreMatrix[i][j] = max(match, delete, insert)
        }
    }
    
    // Obtenemos la puntuación máxima y la posición en la matriz
    maxScore := scoreMatrix[len(seq1)][len(seq2)]
    i := len(seq1)
    j := len(seq2)
    
    // Construimos los alineamientos
    alignedSeq1 := ""
    alignedSeq2 := ""
    
    for i > 0 || j > 0 {
        if i > 0 && j > 0 && scoreMatrix[i][j] == scoreMatrix[i-1][j-1] + (1 if seq1[i-1] == seq2[j-1] else -1) {
            alignedSeq1 = string(seq1[i-1]) + alignedSeq1
            alignedSeq2 = string(seq2[j-1]) + alignedSeq2
            i--
            j--
        } else if i > 0 && scoreMatrix[i][j] == scoreMatrix[i-1][j] - 1 {
            alignedSeq1 = string(seq1[i-1]) + alignedSeq1
            alignedSeq2 = "-" + alignedSeq2
            i--
        } else {
            alignedSeq1 = "-" + alignedSeq1
            alignedSeq2 = string(seq2[j-1]) + alignedSeq2
            j--
        }
    }
    
    return maxScore, alignedSeq1, alignedSeq2
}

func max(nums ...int) int {
    max := nums[0]
    for _, num := range nums[1:] {
        if num > max {
            max = num
        }
    }
    return max
}

func main() {
    seq1 := "ATCGTGAGGTAG"
    seq2 := "ATGCTGTAGGTA"
    
    score, align1, align2 := needlemanWunsch(seq1, seq2)
    
    fmt.Printf("Score: %v\n", score)
    fmt.Printf("Aligned seq1: %v\n", align1)
    fmt.Printf("Aligned seq2: %v\n", align2)
}
