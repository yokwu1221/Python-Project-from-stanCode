"""
File: anagram.py
Name: Yok
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    s = input("Find anagrams for: ")
    start = time.time()
    ####################
    dict = read_dictionary(len(s))
    print("Searching...")
    find_list = []
    find_anagrams(s, "", [], find_list, dict)
    print(f"{len(find_list)} anagrams: {find_list}")
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(count):
    l = {}
    # {a:[ "apple", "ask"...], b:["back",....] }
    with open (FILE, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) == count:
                if line[0] not in l:
                    l[line[0]] = []
                    l[line[0]].append(line)
                else:
                    l[line[0]].append(line)
    return l


def find_anagrams(s, current_s, current_list, find_list, dict):
    """
    :param s: the word to find the anagram
    :return: anagram of the word
    """
    n = 0
    s_list = []
    number_list = []
    for k in s:
        s_list.append(k)
        number_list.append(n)
        n += 1

    if len(current_s) == len(s_list):
        if current_s in dict[current_s[0]] and current_s not in find_list:
            find_list.append(current_s)
            print(f"Found: {current_s}")
            print("Searching...")

    else:
        for num in number_list:
            if has_prefix(current_s, dict) is False:
                break
            ch = s[num]
            if num in current_list:
                pass
            else:
                # choose
                current_s += ch
                current_list.append(num)
                # explore
                find_anagrams(s, current_s, current_list, find_list, dict)
                # un-choose
                current_s = current_s[:-1]
                current_list.pop()


def has_prefix(sub_s, dict):
    """
    :param sub_s: the fraction of s
    :return: True or False
    """
    n = 1
    if sub_s:
        for i in range(len(dict[sub_s[0]])):
            compare = dict[sub_s[0]][i]
            if compare.startswith(sub_s):
                return True
            else:
                if i == len(dict[sub_s[0]])-1:
                    return False
    else:
        return True


if __name__ == '__main__':
    main()
