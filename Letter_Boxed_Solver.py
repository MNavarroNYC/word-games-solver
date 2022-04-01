#3-31-2022 (C) MNavarro
#A quick program that solves NYT's Letter Boxed because today's was too hard

import json

file_name = "words.txt"                #string of the file name of the dictionary
word_dict = []                         #the entire English Dictionary
side_lists = [[], [], [], []]          #list of letters on each side of the box
guess_count = 0                        #amount of guesses to win the game

#parses the text file to get a list of all of the english words
def parse_words():
  with open(file_name) as words:
    lines = words.readlines()
    for word in lines:
      if "\n" in word:
        word = word.replace("\n", "")
      word_dict.append(word)

#grabs the user input and adds it to the usable letter list
def set_side_lists():
  letters = []
  count = 0
  for i in range(0, 12):
    letter = input("Please input letter: ")
    letter.lower()
    letters.append(letter)
  for letter in letters:
    letter = letters[count]
    if count < 3:
      side_lists[0].append(letter)
      count += 1
    elif count < 6:
      side_lists[1].append(letter)
      count += 1
    elif count < 9:
      side_lists[2].append(letter)
      count += 1
    elif count < 12:
      side_lists[3].append(letter)
      count += 1

#goes through word_dict and removes words without the eligible letters
def find_eligible_words():
  eligible_words = []
  letters = []
  for side_list in side_lists:
    for letter in side_list:
      letters.append(letter)
  for word in word_dict:
    is_eligible = True
    for letter in word:
      if letter not in letters:
        is_eligible = False
    if is_eligible:
      eligible_words.append(word)

  return eligible_words

#returns the side list a letter is in
def get_current_side_list(letter):
  for side in side_lists:
    if letter in side:
      return side

#goes thru eligible words and then returns just words that comply with The Letter Boxed rules
def sort_eligible_words(eligible_words):
  result = []
  for word in eligible_words:
    word_len = len(word)
    is_usable = True
    for i in range(0, word_len):
      current_letter = word[i]
      current_side_list = get_current_side_list(current_letter)
      if i > 0:
        prev_letter = word[i - 1]
        if prev_letter in current_side_list:
          is_usable = False
      if i < word_len - 2:
        next_letter = word[i + 1]
        if next_letter in current_side_list:
          is_usable = False
    if is_usable:
      result.append(word)
  return result

#returns words from the already sorted and ascending list of words that matches the last letter of the previous guess
def get_next_word_list(last_letter, word_list):
  result = []
  for word in word_list:
    if word[0] == last_letter:
      result.append(word)
  return result

#runs the entire program and gives results in the terminal
def run():
  guess_count = int(input("Solve in how many guesses: "))
  set_side_lists()
  parse_words()
  eligible_words = find_eligible_words()
  sorted_eligible_words = sort_eligible_words(eligible_words)
  ascending_sorted_words = sorted(sorted_eligible_words, key = len, reverse = True)
  print(ascending_sorted_words)
  while guess_count > 0:
    last_letter = input("What was the last letter of the word you picked: ")
    last_letter.lower()
    print(get_next_word_list(last_letter, ascending_sorted_words))
    guess_count -= 1

run()
