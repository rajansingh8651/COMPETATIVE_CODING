text=input("Enter your sentence here : ")
vowels="aeiouAEIOU"
count=0
for char in text:
    if char in vowels:
        count=+1
print("Total number of vowels in the sentence is : ",count)