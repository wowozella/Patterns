
#pattern1
print('pattern1\n')
rows = 11
for i in range(1, rows):
    for j in range(-1+i, -1, -1):
        print(format(2**j, "4d"), end=' ')
    print("")
    
#pattern2
print('\npattern2\n')
rows = 6
for row in range(1, rows):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")
    
#pattern3
print('\npattern3\n')
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("\r")
    
#pattern4
print('\npattern4\n')
rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#pattern5
print('\npattern5\n')
rows = 5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#pattern6
print('\npattern6\n')
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

#pattern7
print('\npattern7\n')
rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")				 

#pattern8
print('\npattern8\n')
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")  # print number
    # line after each row to display pattern correctly
    print("")

#pattern9
print('\npattern9\n')
rows = 7
for i in range(1, rows):
    for i in range(0, i, 1):
        print(format(2 ** i, "4d"), end=' ')
    for i in range(-1 + i, -1, -1):
        print(format(2 ** i, "4d"), end=' ')
    print("")

#pattern10
print('\npattern10\n')
	