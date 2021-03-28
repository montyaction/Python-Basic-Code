# Define is_palindrome function that one word in string as input
# and return True if it is palindrome else


# palindrome - word that read same backword as for words

# Example
# is_palindrome("madam") -----> True
# is_palindrome("naman") -----> True
# is_palindrome("hores") -----> Fales


# logci(algorithm)
# step 1 -> reverse the string
# step 2 -> compare reverse string with original string

#.....................solution....................

# def is_palindrome(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False


# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False


def is_palindrome(word):
    return word == word[::-1]

word = input("Type the 'Palindrome' word : ")
print(is_palindrome(word))
