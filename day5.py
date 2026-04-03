# Day 5 - Sets & Dictionary Advanced
# Raj Gajare | Prime 2.0

# Problem 1 - Set Operations

a={1, 2, 3, 4, 5}
b={2,4,6,9,10,6,3,6}
print("set a:",a)
print("set b:",b)
print("Union:",a.union(b))
print("Intersection:(a&b)",a.intersection(b))
print("Difference:",a-b)

# Problem 2 - Remove Duplicates using Set
number=[1,2,3,4,5,6,8,5,6,4,10]
unique=list(set(number))
print("\nOriginal:",number)
print("\nRemoved Duplicates:",sorted(unique))


# Problem 3 - Dictionary Advanced
students = {
    "Raj": 85,
    "Amit": 92,
    "Priya": 78,
    "Riya": 95
}
# topper
topper=max(students,key=students.get)
print("\ntopper:",topper,"with",students[topper],"marks")
# pass student with (marks>80)
passes={k:v for k,v in students.items() if v>80}
print("\npassing students:",passes)

# problem 4 -Frequency Count
sentence="priya is learning python and priya loves coding and python both"
words=sentence.split()
freq={}
for word in words:
    freq[word]=freq.get(word,0)+1

print("\n Word Frequency:")
for word ,count in sorted(freq.items()):
    print(f"{word}:{count}")