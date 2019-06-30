listofnumber = [1,2,3,4,5,6,7]

def forloopwithbreak():
    for number in listofnumber:
        if number%2 == 0:
            print("even number found")
            break
    else:
        print("even number not found")


def forloopwithpass():
    """doc string"""
    for number in listofnumber:
        """doc string"""
        if number%2 == 0:
            continue
        print(number, ' ')

print(forloopwithpass())

response = input("enter response")
print(response)

response = None
