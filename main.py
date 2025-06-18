# Task 1
text = "Python is amazing!"

first_word = text[:6]
amazing_part = text[10:17]
reversed_text = text[::-1]

print("First word:", first_word)
print("Amazing part:", amazing_part)
print("Reversed string:", reversed_text)

# Task 2
msg = " hello, python world! "

print("Original:", repr(msg))
print("After strip():", msg.strip())
print("After capitalize():", msg.strip().capitalize())
print("After replace():", msg.strip().replace("world", "universe"))
print("After upper():", msg.strip().upper())

# Task 3
word = input("Enter a word: ").strip()
reversed_word = word[::-1]

if word.lower() == reversed_word.lower():
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"Nope, '{word}' is not a palindrome.")