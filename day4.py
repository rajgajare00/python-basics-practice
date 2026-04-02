# Day 4 - List & Dictionary Practice
# Raj Gajare | Prime 2.0

# 1. list operations:
number=[5,8,3,9,4,6,35,78,46,7,3]
print("Original list:",number)
print("Sorste list:",sorted(number))
print("Reversed list:",number[::-1])
print("Max:",max(number))
print("Min:",min(number))
print("Sum:",sum(number))

# 2. list comprehension:
squares=[x**2 for x in number]
print("Squares of the numbers in the list:",squares)

# 3. Dictionary operations:
Student={
    "name":"Raj Gajare",
    "branch":"AI & DS",
    "year":"2nd",
    "Leetcode_streek":150
}
print("Student Info:")
for key, value in Student.items():
    print(f"{key}: {value}")    
    
    
# 4. word counter
def word_counter(sentence):
    words=sentence.split()
    count={}
    for word in words:
        word.lower()
        count[word]=count.get(word,0)+1
    return count
print("word count:")
print(word_counter("This is a simple sentence with some repeated words"))