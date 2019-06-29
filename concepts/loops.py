listofnumber = [1,2,3,4,5,6,7]

for number in listofnumber:
    if number%2 == 0:
        print("even number found")
        break
else:
    print("even number not found")