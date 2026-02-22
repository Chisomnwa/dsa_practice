package main

import (
	"fmt";
	"piscine/go-solutions"
)


func main() {
	fmt.Println(piscine.IsPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println(piscine.IsPalindrome(" "))
	fmt.Println(piscine.IsPalindrome("race a car"))
}