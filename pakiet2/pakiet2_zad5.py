def is_palindrome(x):
    return x.lower().replace(" ", "") == x[::-1].lower().replace(" ", "")

print(is_palindrome("alA "))