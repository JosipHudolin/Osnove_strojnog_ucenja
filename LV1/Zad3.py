def Average(lst):
    return sum(lst) / len(lst)

list = []
while True:
    print('Input number:')
    var = input()
    if var == 'Done':
        break
    else:
        try:
            number = float(var)
            list.append(number)
        except:
            print('Input is not a number!')

print('Number of inputs: ', len(list))
print('Average: ', Average(list))
print('Minimum: ', min(list))
print('Maximum: ', max(list))
list.sort()
print('Sorted list:')
for number in list:
    print(number)