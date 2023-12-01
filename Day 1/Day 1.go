package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	data, err := os.Open("data.txt")
	if err != nil {
		fmt.Println("File reading error", err)
		return
	}
	defer data.Close()

	re := regexp.MustCompile(`\d`)
	var total int = 0
	var total2 int = 0
	numbers := []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

	scanner := bufio.NewScanner(data)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		var line string = scanner.Text()

		digits := re.FindAllString(line, -1)

		first_digit := digits[0]
		last_digit := digits[len(digits)-1]
		index := strings.Index(line, first_digit)
		index2 := strings.LastIndex(line, last_digit)

		num, _ := strconv.Atoi(string(first_digit + last_digit))
		total += num // part 1

		for i := 0; i < len(numbers); i++ {
			cur := strings.Index(line, numbers[i])
			if cur != -1 {
				if cur < index {
					first_digit = strconv.Itoa(i + 1)
					index = cur
				}
			}
			last := strings.LastIndex(line, numbers[i])
			if last != -1 {
				if last > index2 {
					last_digit = strconv.Itoa(i + 1)
					index2 = last
				}
			}
		}

		num2, _ := strconv.Atoi(string(first_digit + last_digit))
		total2 += num2 // part 2
	}

	fmt.Println("Part 1:", total)
	fmt.Println("Part 2:", total2)
}
