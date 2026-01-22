def palindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            return "Not a Palindrome"
    return "Palindrome"

s = input()
print(palindrome(s))