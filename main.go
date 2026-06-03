package main

// My solutions are housed in the my_solutions folder but I have moved this to another repo called dsa_practice

import (
	"fmt"
	//dsa_practice/arrays/two-sum"
	//"dsa_practice/strings/length-of-last-word"
	//"dsa_practice/strings/roman_to_integer"
	//"ddsa_practice/arrays/missing_number"
	//"dsa_practice/arrays/search_insert_position"
	"dsa_practice/arrays/build_array_from_permutation"
)

// func main() {
// 	nums := []int{2, 7, 5, 9, 11}
// 	target := 9

// 	fmt.Println(twosum.TwoSumA(nums, target))
// 	fmt.Println(twosum.TwoSumB(nums, target))
// }

// func main() {
// 	inputA := "Hello World"
// 	inputB := "   fly me   to   the moon  "
// 	inputC := "luffy is still joyboy"
// 	fmt.Println(lengthoflastword.LengthOfLastWordA(inputA))
// 	fmt.Println(lengthoflastword.LengthOfLastWordA(inputB))
// 	fmt.Println(lengthoflastword.LengthOfLastWordB(inputC))
// }

// func main() {
// 	s1 := "III"
// 	s2 := "LVIII"
// 	s3 := "MCMXCIV"
// 	fmt.Println(romantointeger.RomanToInt(s1))
// 	fmt.Println(romantointeger.RomanToInt(s2))
// 	fmt.Println(romantointeger.RomanToInt(s3))
// }

// func main() {
// 	numsA := []int{3,0,1}
// 	numsB := []int{0,1}
// 	numsC := []int{9,6,4,2,3,5,7,0,1}
// 	fmt.Println(missingnumber.MissingNumberA(numsA))
// 	fmt.Println(missingnumber.MissingNumberA(numsB))
// 	fmt.Println(missingnumber.MissingNumberA(numsC))
// 	fmt.Println(missingnumber.MissingNumberB(numsA))
// 	fmt.Println(missingnumber.MissingNumberB(numsB))
// }

// func main() {
// 	numsA := []int{1,3,5,6}; targetA := 5
// 	numsB := []int{1,3,5,6}; targetB := 2
// 	numsC := []int{1,3,5,6}; targetC := 7
// 	fmt.Println(searchinsertposition.SearchInsertA(numsA, targetA))
// 	fmt.Println(searchinsertposition.SearchInsertA(numsB, targetB))
// 	fmt.Println(searchinsertposition.SearchInsertA(numsC, targetC))
// 	fmt.Println(searchinsertposition.SearchInsertB(numsA, targetA))
// 	fmt.Println(searchinsertposition.SearchInsertB(numsB, targetB))
// }

func main() {
	numsA := []int{0,2,1,5,3,4}
	numsB := []int{5,0,1,2,3,4}
	fmt.Println(buildarrayfrompermutation.BuildArrayA(numsA))
	fmt.Println(buildarrayfrompermutation.BuildArrayA(numsB))
	fmt.Println(buildarrayfrompermutation.BuildArrayB(numsA))
	fmt.Println(buildarrayfrompermutation.BuildArrayB(numsB))
}

