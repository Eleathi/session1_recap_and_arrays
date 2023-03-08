# Exercise 8
# Ask the user to input some text, and use a for-loop
#  to count the number of vowels in that text.
# You can check whether a letter is in a longer list
#  of letters using the 'in' keyword, e.g.:
#    'z' in 'xyz'
#  returns True, whereas
#    'a' in 'xyz'
#  returns False.

text = input('I want to count vowels. Please type some text for me: ')
vowels = 'aeiou'

vowel_count = 0
for letter in text:
    if letter in vowels:
            vowel_count = vowel_count + 1

if vowel_count == 1:
    print(f"Thank you. There is {vowel_count} vowel in your input.")
elif vowel_count > 1:
    print(f"Thank you. There are {vowel_count} vowels in your input.")
else:
    print(f"Oh no! There aren't any vowels in your input!")
