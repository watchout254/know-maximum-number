import sys

print("\t\t\t🤗A warm welcome to Jawabu Program!!!!👏")
print("Feel free to know the maximum number in all the numbers you list below.....")
jibu = input("Kindly enter all the numbers: ")
jibu1 = jibu.split() #split with a space in between

count = 0 #to know the length of the list
for cup in jibu1:
    count = count+1
print(f"The length is : {count}")

for coaches in range(count):
    jibu1[coaches] = int(jibu1[coaches])

print(jibu1)

bazenga = jibu1[0]
for biggie in jibu1:
    if biggie > bazenga:
        bazenga = biggie

print(f"Maximum number is 👉 : {bazenga}")
print("Thank you Champ, you did it 😎")
