from words import words
import random
import pyperclip

number_of_lines = int(
    input("Enter the number of lines of para you want ")) * 21

print(
    "Here is your Prargraph and it is already copied to you clipboard use it! Have a Good Day Hommie")

para=" ".join(random.choices(words, k=number_of_lines))

pyperclip.copy(para)
print("\n \n",para,"\n")