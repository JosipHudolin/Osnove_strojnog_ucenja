print('Input grade (0.0-1.0):')
try:
    x = float(input())
except:
    print('There is no input!')
if x < 0 or x > 1:
    print('Invalid grade!')
else:
    if x >= 0.9:
        print('A')
    if x >= 0.8 and x < 0.9:
        print('B')
    if x >= 0.7 and x < 0.8:
        print('C')
    if x >= 0.6 and x < 0.7:
        print('D')
    if x < 0.6:
        print('F')