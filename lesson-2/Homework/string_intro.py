# name = 'Javohirbek'
# birth_year = 2002
# age = 2026 - birth_year
# print("My name is " + name + " and I am " + str(age) + " years old.")
# text = input("Enter a string: ")
# length = len(text)
# uppercase = text.upper()
# lowercase = text.lower()
# print(length)
# print(uppercase)
# print(lowercase)
# text = input("Enter a string: ")
# print(text[::-1])
#if text == text[::-1] :
 #  print("Palindrome")
# else:
  # print("Not palindrome")
# 
#text = input("Enter a string:")
# vowels = "aeiou"
# vowel_count = 0
# consonant_count = 0
# for char in text:
  #  if char.lower() in vowels:
   #     vowel_count += 1
    #else:
     #   consonant_count += 1
# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)
# text = input("Enter a string: ")
# word = input("Enter a word to search: ")
# if word in text:
  #  print("Found")
# else:
  #  print("Not found")
# sentence = input("Enter a sentence: ")
# old_word = input("Enter the old word: ")
# new_word = input("Enter the new word: ")
# result = sentence.replace(old_word, new_word)
# print(result)
# text = input("Enter a string: ")
# first_char = text[0]
# last_char = text[-1]
# print("First caracter:", first_char)
# print("Last caracter:", last_char)
# text = input("Enter a string: ")
# reversed_text = text[::-1]
# print("Reversed string:", reversed_text)
text = input("Enter a string: ")
words = text.split()
word_count = len(words)
print("Number of words:", word_count)
