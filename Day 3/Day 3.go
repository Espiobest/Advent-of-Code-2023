package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

var gears = make(map[[2]int][]int)

func isSymbol(point string) bool {
	return point != "." && !regexp.MustCompile(`^\d+$`).MatchString(point)
}

func checkNeighbors(lines []string, i int, num string, index int) bool {
	start := index - 1
	end := index + len(num)
	numInt, _ := strconv.Atoi(num)
	if start >= 0 {
		if lines[i][start:start+1] == "*" {
			gears[[2]int{i, start}] = append(gears[[2]int{i, start}], numInt)
		}

		if isSymbol(lines[i][start : start+1]) {
			return true
		}
	}

	if end < len(lines[i]) {
		if lines[i][end:end+1] == "*" {
			gears[[2]int{i, end}] = append(gears[[2]int{i, end}], numInt)
		}

		if isSymbol(lines[i][end : end+1]) {
			return true
		}
	}

	if start < 0 {
		start = 0
	}
	if end >= len(lines[i]) {
		end = len(lines[i]) - 1
	}

	neighboringLines := [][2]int{}
	if i > 0 {
		neighboringLines = append(neighboringLines, [2]int{-1, i - 1})
	}
	if i < len(lines)-1 {
		neighboringLines = append(neighboringLines, [2]int{1, i + 1})
	}

	for _, nl := range neighboringLines {
		direction, lineIndex := nl[0], nl[1]
		for j, symbol := range lines[lineIndex][start : end+1] {
			if isSymbol(string(symbol)) {
				if string(symbol) == "*" {
					gears[[2]int{i + direction, j + start}] = append(gears[[2]int{i + direction, j + start}], numInt)
				}
				return true
			}
		}
	}

	return false
}

func main() {
	data, err := ioutil.ReadFile("data.txt")
	lines := strings.Split(string(data), "\n")

	total := 0
	gearTotal := 0

	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	for i, line := range lines {

		re := regexp.MustCompile(`\d+`)
		numbers := re.FindAllString(line, -1)
		indices := re.FindAllStringIndex(line, -1)
		for j := 0; j <= len(numbers)-1; j++ {
			num := numbers[j]
			index := indices[j]
			if checkNeighbors(lines, i, num, index[0]) {
				num, _ := strconv.Atoi(num)
				total += num
			}
		}
	}

	for _, gear := range gears {
		if len(gear) == 2 {
			x, y := gear[0], gear[1]
			gearTotal += x * y
		}
	}

	fmt.Println("Part 1:", total)
	fmt.Println("Part 2:", gearTotal)
}
