package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func parseColor(game string, color string) int {
	if !strings.Contains(game, color) {
		return -1
	}
	colorStr := strings.Split(strings.Split(game, " "+color)[0], " ")
	num, _ := strconv.Atoi(colorStr[len(colorStr)-1])
	return num
}

func main() {
	data, err := os.Open("data.txt")

	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	defer data.Close()

	scanner := bufio.NewScanner(data)
	scanner.Split(bufio.ScanLines)

	var curGame int = 1
	var totalRed int = 12
	var totalGreen int = 13
	var totalBlue int = 14
	var total int = 0
	var totalProd int = 0

	for scanner.Scan() {

		var line string = scanner.Text()
		games := strings.Split(line, "; ")
		possible := true
		var maxRed, maxGreen, maxBlue int = 0, 0, 0
		for _, game := range games {
			red := parseColor(game, "red")
			blue := parseColor(game, "blue")
			green := parseColor(game, "green")
			if (red > totalRed) || (blue > totalBlue) || (green > totalGreen) {
				possible = false
			}

			maxRed = int(math.Max(float64(maxRed), float64(red)))
			maxGreen = int(math.Max(float64(maxGreen), float64(green)))
			maxBlue = int(math.Max(float64(maxBlue), float64(blue)))
		}

		if possible {
			total += curGame
		}

		totalProd += maxRed * maxGreen * maxBlue
		curGame++
	}
	fmt.Println("Part 1:", total)
	fmt.Println("Part 2:", totalProd)
}
