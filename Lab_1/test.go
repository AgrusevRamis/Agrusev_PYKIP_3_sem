package main

import (
	"fmt"
	"math"
	"strconv"
)

func readNumber(prompt string) float64 {
	for {
		fmt.Print(prompt)
		var line string
		fmt.Scan(&line)

		x, err := strconv.ParseFloat(line, 64)
		if err != nil {
			fmt.Println("это не число, попробуй ещё раз")
			continue
		}
		return x
	}
}

func discriminant(a, b, c float64) float64 {
	return b*b - 4*a*c
}

func solveY(a, b, d float64) (float64, float64) {
	s := math.Sqrt(d)
	y1 := (-b + s) / (2 * a)
	y2 := (-b - s) / (2 * a)
	return y1, y2
}

func rootsX(y float64) []float64 {
	if y > 0 {
		s := math.Sqrt(y)
		return []float64{s, -s}
	}
	if y == 0 {
		return []float64{0}
	}
	return nil
}

func main() {
	a := readNumber("a = ")

	b := readNumber("b = ")
	c := readNumber("c = ")

	if a == 0 {
		for _, x := range rootsX(-c / b) {
			fmt.Println(x)
		}
		return
	}
	d := discriminant(a, b, c)
	fmt.Println("D =", d)

	if d < 0 {
		fmt.Println("корней нет")
		return
	}

	y1, y2 := solveY(a, b, d)
	fmt.Println("y1 =", y1, "y2 =", y2)

	all := rootsX(y1)
	if y2 != y1 {
		all = append(all, rootsX(y2)...)
	}

	if len(all) == 0 {
		fmt.Println("корней нет")
		return
	}

	fmt.Println("корни:")
	for _, x := range all {
		fmt.Println(x)
	}
}
