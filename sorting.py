#sorting algorithm 
# get user input 
data = []
responce = ''


while responce != 'q':
    responce = input("Numbers: (if you want to look sort press 'q') ")
    if responce != 'q':
        data.append(responce)
        data.sort()

print('\n')
print("Sorting data is: " , data)



