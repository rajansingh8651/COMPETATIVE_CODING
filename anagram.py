str1 = input("Enter first string: ").lower().replace(" ", "")
str2 = input("Enter second string: ").lower().replace(" ", "")

if sorted(str1) == sorted(str2):
    print("They are anagrams")
else:
    print("They are not anagrams")   