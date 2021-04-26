"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: This is the integer that will be process to find largest digit
	:return: The integer representing the largest digit in n
	"""
	divisor_counter = 0
	largest_n = 0
	num_y = 10
	if n < 0:
		n = abs(n)
	else:
		n = n
	return helper(n, largest_n, divisor_counter, num_y)


def helper(n, largest_n, divisor_counter, num_y):
	divisor_counter += 1
	if num_y == 0:
		return largest_n
	else:
		# Choose
		num_x = int(n / (1 * (10 ** (divisor_counter - 1))) % 10)
		num_y = int(n / (1 * (10 ** divisor_counter)) % 10)
		if num_x > largest_n:
			largest_n = num_x
		# Explore
		return helper(n, largest_n, divisor_counter, num_y)


if __name__ == '__main__':
	main()
