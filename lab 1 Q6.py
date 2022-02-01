# function which return reverse of a string
user =  input("enter  palindrome  word :")

result = user[::-1]

if user == result:
    print("Yes, the word is palindrome ")

else:
    print("NO, the word is not palindrome   ")   
