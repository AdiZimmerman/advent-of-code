import argparse
from typing import Optional

def part_one(filename: str) -> int:
	res: int = 0
	with open(filename) as f:
		for line in f:
			first, second = 0, 0
			for ch in line:
				digit = int(ch) if ch.isdigit() else None
				if digit:
					if first == 0:
						first = digit
					second = digit
			res += first * 10 + second
		return res

def part_two(filename: str) -> int:
	def find_digit(line: str, pos: int) -> Optional[int]:
		"""Returns the digit representation of word from position in line or None if no valid word found."""
		for i, word in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
			if line[pos:pos+len(word)] == word:
				return i + 1
		return None

	res: int = 0
	with open(filename) as f:
		for line in f:
			first, second = 0, 0
			for i, ch in enumerate(line):
				digit = int(ch) if ch.isdigit() else find_digit(line, i)
				if digit:
					if first == 0:
						first = digit
					second = digit
			res += first * 10 + second
		return res

def test(f, filename, expected):
	actual = f(filename)
	assert expected == actual, f"{f, filename}: expected {expected}, actual {actual}"

if __name__ == "__main__":
	test(part_one, 'test1.txt', 142)
	test(part_one, 'input.txt', 54940)
	test(part_two, 'test1.txt', 142)
	test(part_two, 'test2.txt', 281)
	test(part_two, 'input.txt', 54208)
