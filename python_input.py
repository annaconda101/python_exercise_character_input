from char_input.char_input import StringChallenge

text_input = input("Enter your string here: ")
sc = StringChallenge()
print sc.get_reversed_string(text_input)
