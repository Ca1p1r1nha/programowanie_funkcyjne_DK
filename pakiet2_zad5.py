def is_palindrome(x):
    if x.lower().replace(" ", "") == x[::-1].lower().replace(" ", ""): return True

print(is_palindrome("alA "))