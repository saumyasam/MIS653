# Author: Saumya Padhi
# Week 5 MSBA Exercise

def char_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
result = char_count("Midland is getting colder")
print(result)  