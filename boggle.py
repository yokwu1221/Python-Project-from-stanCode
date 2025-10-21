"""
File: boggle.py
Name: Yok
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	give 4 rows of letters, and find the corresponded words
	"""
	start = time.time()

	row1 = input("1 row of letters: ")
	if not check(row1, "", 0):
		print("Illegal input")
	else:
		row1_lst = row_list(row1, [], 0)
		row2 = input("2 row of letters: ")
		if not check(row2, "", 0):
			print("Illegal input")
		else:
			row2_lst = row_list(row2, [], 0)
			row3 = input("3 row of letters: ")
			if not check(row3, "", 0):
				print("Illegal input")
			else:
				row3_lst = row_list(row3, [], 0)
				row4 = input("4 row of letters: ")
				if not check(row4, "", 0):
					print("Illegal input")
				else:
					row4_lst = row_list(row4, [], 0)
					# combine 4 list into 1 list
					wd_lst = []
					wd_lst.append(row1_lst)
					wd_lst.append(row2_lst)
					wd_lst.append(row3_lst)
					wd_lst.append(row4_lst)
					fd_lst = []
					compare_lst(wd_lst, [], "", fd_lst)
					print(f"There are {len(fd_lst)} words in total.")

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(cr_word):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	l = {}
	# {a:[ "apple", "ask"...], b:["back",....] }
	with open (FILE, "r") as f:
		for line in f:
			line = line.strip()
			if len(line) >= 4:
				if line[0] == cr_word [0]:
					if line[0] not in l:
						l[line[0]] = []
						l[line[0]].append(line)
					else:
						l[line[0]].append(line)
	return l


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	dict = read_dictionary(sub_s)
	for i in range(len(dict[sub_s[0]])):
		compare = dict[sub_s[0]][i]
		if compare.startswith(sub_s):
			return True
		else:
			if i == len(dict[sub_s[0]])-1:
				return False


def compare_lst(word_lst, first_lst, cr_word, fd_lst):
	# create 4-alpha words, adding to a list
	# first_lst: first number which has been used
	# used_lst = po of word already used in cr_word
	# first alpha
	used_lst = []
	for i in range(4):
		for j in range(4):
			po = (i, j)
			if po not in first_lst:
				ch = word_lst[i][j]
				cr_word += ch
				first_lst.append(po)
				used_lst.append(po)
				next_alpha(word_lst, po, (0, 0), cr_word, fd_lst, used_lst, 0)
				cr_word = ""
				used_lst = []


def next_alpha(word_lst, po, nx_po, cr_word, fd_lst, used_lst, st):
	# find the next alpha by using the given method
	if len(cr_word) >= 4:
		if compare(cr_word) is True:
			if cr_word not in fd_lst:
				fd_lst.append(cr_word)
				print(f'Found "{cr_word}"')
				st = len(cr_word)
				(i, j) = nx_po
				for (i, j) in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
					if 0 <= i < 4 and 0 <= j < 4:
						nx_po = (i, j)
						if nx_po not in used_lst:
							ch = word_lst[i][j]
							cr_word += ch
							used_lst.append(nx_po)
							next_alpha(word_lst, po, nx_po, cr_word, fd_lst, used_lst, st)
							if len(cr_word) > st:
								cr_word = cr_word[:-1]
								used_lst.pop()

	else:
		if has_prefix(cr_word):
			if len(cr_word) == 1:
				(i, j) = po
			else:
				(i, j) = nx_po
			for (i, j) in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
				if 0 <= i < 4 and 0 <= j < 4:
					nx_po = (i, j)
					if nx_po not in used_lst:
						ch = word_lst[i][j]
						cr_word += ch
						used_lst.append(nx_po)
						next_alpha(word_lst, po, nx_po, cr_word, fd_lst, used_lst, st)
						# un-choose
						cr_word = cr_word[:-1]
						used_lst.pop()


def check(row, word, n):
	if len(row) == 7:
		if row[n].isalpha():
			ch = row[n].lower()
			word += ch
			if n == 6:
				return word
			if row[n+1] == " ":
				word += row[n+1]
				return check(row, word, n+2)
			else:
				return False
		else:
			return False
	else:
		return False


def row_list(row, lst, n):
	# put given word into a row list
	lst.append(row[n])
	if n == 6:
		return lst
	else:
		return row_list(row, lst, n+2)


def compare(cr_word):
	# if word in the compare_list is found in the dict, then add to the finding_list
	dict = read_dictionary(cr_word)
	if cr_word in dict[cr_word[0]]:
		return True
	else:
		return False

if __name__ == '__main__':
	main()
