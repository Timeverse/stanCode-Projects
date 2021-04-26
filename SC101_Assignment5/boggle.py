"""
File: boggle.py
Name: Ralph Liu
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
FILTER_DICT = []
Grid_size = 4
ANS_Lst = []


def main():
	"""
	TODO:
	"""
	raw_lst = []
	input_lst = []
	for i in range(1, 5, 1):
		input_row = input(str(i) + ' row of letters: ')
		input_row = input_row.lower()
		input_row = input_row.split()
		raw_lst.append(input_row)
		for rows in range(len(raw_lst)):
			for letters in raw_lst[rows]:
				input_lst += letters
				raw_lst = []
	empty_grid = create_grid(Grid_size)
	grid_filled = fill_grid(empty_grid, input_lst)
	read_dictionary(input_lst)
	find_anagram(grid_filled)


def create_grid(grid_size):
	grid = {}
	for y in range(grid_size):
		for x in range(grid_size):
			z = (x, y)
			grid[z] = ''
	return grid


def fill_grid(grid, input_lst):
	grid.update(zip(grid, input_lst))
	return grid


def read_dictionary(input_lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	raw_dict = []  # This stores the raw imported dictionary. Structure is [['a'],['b']]
	rdy_dict = []  # Processed raw dictionary. Structure is refined as ['a', 'b']
	input_lst = list(dict.fromkeys(input_lst))
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split()
			raw_dict.append(word)

	for item in raw_dict:
		rdy_dict += item

	for word in rdy_dict:
		if len(word) >= 4:  # This filters the dictionary for words of same length as user input
			for letters in input_lst:
				if word.startswith(letters):  # This further filter words that start with each alphabet of user input
					FILTER_DICT.append(word)


def find_anagram(grid_filled):
	for x in range(Grid_size):
		for y in range(Grid_size):
			ch = grid_filled[(x, y)]
			cur_s = [ch]
			used_pos = [(x, y)]
			cur_word = ''
			find_anagram_helper(used_pos, cur_s, x, y, grid_filled, cur_word)
	print('There are ' + str(len(ANS_Lst)) + ' words in total')


def find_anagram_helper(used_pos, cur_s, x, y, grid_filled, cur_word):
	if len(cur_word) >= 4:
		if cur_word in FILTER_DICT:
			if cur_word not in ANS_Lst:
				print('Found: ' + cur_word)
				ANS_Lst.append(cur_word)
			else:
				pass
	else:
		# Choose
		for shift_y in range(y - 1, y + 2):
			for shift_x in range(x - 1, x + 2):
				if 0 <= shift_x <= 3 and 0 <= shift_y <= 3:
					if (shift_x, shift_y) not in used_pos:
						ch = grid_filled[(shift_x, shift_y)]
						cur_s.append(ch)
						used_pos.append((shift_x, shift_y))
						# Explore
						cur_word = ''
						for letters in cur_s:
							cur_word += letters
						if has_prefix(cur_word) is True:
							find_anagram_helper(used_pos, cur_s, shift_x, shift_y, grid_filled, cur_word)
						# Un-choose
						cur_s.pop()
						used_pos.pop()


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for string in FILTER_DICT:
		if string.startswith(sub_s) is True:
			return True


if __name__ == '__main__':
	main()
