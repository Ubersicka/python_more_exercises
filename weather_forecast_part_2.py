celsium = float(input())

if celsium < 5:
    print('unknown')
elif celsium <= 11.9:
    print("Cold")
elif celsium <= 14.9:
    print('Cool')
elif celsium <= 20:
    print('Mild')
elif celsium <= 25.9:
    print('Warm')
elif celsium <= 35:
    print('Hot')
else:
    print('unknown')
