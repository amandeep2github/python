last2last, last, limit = 0, 1, 100
#0,1,2,3,5
print(0)
while last2last + last <= limit: #0, 1,
    print(last2last + last)
    last2last, last = last, last2last+last

