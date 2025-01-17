def palindrome(n):
    if n == n[::-1]: 
        return True
    else:
        return False

num = input("Enter string: ")
print(palindrome(num))
  