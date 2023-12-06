package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func stringToIntSlice(slice []string) []int {
	var intSlice []int
	for _, s := range slice {
		n, _ := strconv.Atoi(s)
		intSlice = append(intSlice, n)
	}
	return intSlice
}

func main() {
	data, err := os.ReadFile("data.txt")

	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	lines := strings.Split(string(data), "\n")

	timeStr := strings.Fields(strings.Split(lines[0], ": ")[1])
	distanceStr := strings.Fields(strings.Split(lines[1], ": ")[1])

	times := stringToIntSlice(timeStr)
	distances := stringToIntSlice(distanceStr)

	total := 1

	for i, time := range times {
		count := 0
		for j := 0; j <= time; j++ {
			x := time - j
			dist := j * x
			if dist > distances[i] {
				count++
			}
		}

		if count > 0 {
			total *= count
		}
	}

	fmt.Println("Part 1:", total)

	time, _ := strconv.Atoi(strings.Join(timeStr, ""))
	distance, _ := strconv.Atoi(strings.Join(distanceStr, ""))

	total2 := 0
	for i := 0; i < time; i++ {
		x := time - i
		dist := i * x
		if dist > distance {
			total2++
		}
	}
	fmt.Println("Part 2:", total2)
}
