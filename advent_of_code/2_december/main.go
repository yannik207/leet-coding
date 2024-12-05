package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
	file, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Create a slice of slices to hold all child slices
	motherSlice := [][]string{}

	// Use a scanner to read the file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// Create a new slice for the current line
		childSlice := []string{scanner.Text()}

		// Append the child slice to the mother slice
		motherSlice = append(motherSlice, childSlice)
	}

	// Check for errors during scanning
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	for i := range motherSlice {
		test_drive := [][]string{motherSlice[i]}
		// fmt.Printf("variable message='%v' is of type %T \n", test_drive, test_drive)
	}
}
