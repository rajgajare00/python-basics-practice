# my python journey day-3
# Raj Gajare | Prime2.0
# problem -1 : WAP to reverse the string
def reverse_string(s):
    return s[::-1]
# taking user input
str=input("Enter any string:")
reversed=reverse_string(str)
print("reversed string is:",reversed)
 

# problem -2 : WAP to check if the string is palindrome or not
def palindrome(s):
    if(s==s[::-1]):
        return True
    else: 
        return False
palin=input("Enter a string to check palindrome or not:")
is_palindrome=palindrome(palin)
if(is_palindrome):
    print("The given string "+palin+" is a palindrome")
else:
    print("The given string "+palin+" is not a palindrome")


# problem -3 : WAP to count the number of vowels in a string
def count_vowels(s):
    count=0
    s.Lower()
    for char in s:
        if char in 'aeiou':
            count+=1
    return count
vowel_string=input("Enter a string to count the number of vowels:")
vowel_count=count_vowels(vowel_string)
print("The number of vowels in the given string is:",vowel_count)

