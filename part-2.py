# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    elif array[0] == query:
        return True

    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if text == "":
        return True
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match
def digit_match(digit_1, digit_2):
    if digit_1 == 0 and digit_2 == 0:
        return 1
    
    if digit_1 == 0 or digit_2 == 0:
        return 0
    
    count = 1 if (digit_1 % 10 == digit_2 % 10) else 0

    if digit_1 < 10 or digit_2 < 10:
        return count

    return count + digit_match(digit_1 // 10, digit_2 // 10)
