package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

var cardCount = make(map[int]int)

func contains(slice []int, num int) bool {
	for _, n := range slice {
		if n == num {
			return true
		}
	}
	return false
}

func stringToIntSlice(slice []string) []int {
	var intSlice []int
	for _, s := range slice {
		n, _ := strconv.Atoi(s)
		intSlice = append(intSlice, n)
	}
	return intSlice
}

func main() {
	data, err := ioutil.ReadFile("data.txt")
	lines := strings.Split(string(data), "\n")

	total := 0
	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	for i, line := range lines {
		cardCount[i] = cardCount[i] + 1

		splits := strings.Split(strings.Split(line, ":")[1], "|")

		var winArr []int = stringToIntSlice(strings.Fields(splits[0]))
		var numArr []int = stringToIntSlice(strings.Fields(splits[1]))
		c := 0
		for _, num := range numArr {
			if contains(winArr, num) {
				c++
			}
		}
		if c > 0 {
			total += int(math.Pow(2, float64(c-1)))
		}

		for j := 0; j < c; j++ {
			cardCount[i+j+1] = cardCount[i+j+1] + cardCount[i]
		}
	}

	sum := 0
	for _, v := range cardCount {
		sum += v
	}

	fmt.Println("Part 1:", total)
	fmt.Println("Part 2:", sum)
}
