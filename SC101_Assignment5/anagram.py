"""
File: anagram.py
Name:
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

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
FILTER_DICT = []              # This will store the filtered dictionary text
ANS_LST = []                  # This will store the found anagrams
SRH_Switch = 0                # This is the switch to show if a search is ongoing. 0 = No search is ongoing


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        global ANS_LST
        ANS_LST = []
        word_input = input('Find anagrams for: ')
        read_dictionary(word_input)
        if word_input == EXIT:
            break
        else:
            (find_anagrams(word_input))
            print(ANS_LST)


def read_dictionary(s):
    """
    :param s: The world inputted by the user
    """
    raw_dict = []   # This stores the raw imported dictionary. Structure is [['a'],['b']]
    rdy_dict = []   # Processed raw dictionary. Structure is refined as ['a', 'b']
    length_check = len(s)
    with open(FILE, 'r') as f:
        for line in f:
            word = line.split()
            raw_dict.append(word)

    for item in raw_dict:
        rdy_dict += item

    for word in rdy_dict:
        if len(word) == length_check:   # This filters the dictionary for words of same length as user input
            for letters in s:
                if word.startswith(letters):  # This further filter words that start with each alphabet of user input
                    FILTER_DICT.append(word)


def find_anagrams(s):
    """
    :param s: The string inputted by the user to find the anagram
    """
    current_lst = []    # This store the result of recursion
    input_lst = []      # This store the result of converting user input string into list structure
    index_lst = []      # This store the index result of recursion
    for i in s:
        input_lst.append(i)  # Converts user inputted string into list structure
    helper(input_lst, current_lst, index_lst)


def helper(input_lst, current_lst, index_lst):
    current_s = ''  # This stores the result converting recursion result back to string format
    global SRH_Switch
    for i in current_lst:
        current_s += i  # Converting recursion result back to string format
    if len(current_lst) == len(input_lst):
        if current_s in FILTER_DICT:    # Check if the recursion result matches any word in dictionary
            if current_s not in ANS_LST:    # A word is only recorded once
                print('Found:' + current_s)
                ANS_LST.append(current_s)
                SRH_Switch = 0
            else:
                pass
    else:
        if SRH_Switch == 0:
            print('Search....')  # Print message to let user know search is ongoing
            SRH_Switch = 1  # Turn on the switch as search is ongoing
        # Choose
        for index in range(len(input_lst)):
            if index not in index_lst:  # Index is here to avoid error from a word with same letters (e.g ball)
                current_lst.append(input_lst[index])
                index_lst.append(index)
                # Explore
                sub_s = ''
                for letters in current_lst:
                    sub_s += letters
                if has_prefix(sub_s) is True:
                    helper(input_lst, current_lst, index_lst)
                # Un-choose
                current_lst.pop()
                index_lst.pop()
            else:
                pass


def has_prefix(sub_s):
    """
    :param sub_s: The sub-string of recursion result
    """
    for string in FILTER_DICT:
        if string.startswith(sub_s) is True:
            return True


if __name__ == '__main__':
    main()
