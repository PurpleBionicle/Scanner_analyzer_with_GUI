import sys

if __name__ == '__main__':
    arr = ['Радиоблок TRP-18G-1E, E-High', 'Радиоблок TRP-13G-1E, K-High', 'Радиоблок TRP-13G-1E, K-High',
           'Радиоблок TRP-23G-1E, E-High']
    variants = ['сдаю', 'беру', 'в ремонте']
    print('Напиши 1 если - сдаю')
    print('Напиши 2 если - беру')
    print('Напиши 3 если - в ремонте')
    for a in arr:
        print(f'{a} - ', end='')
        i = int(input())
        print(f'↑ {variants[i - 1]} ↑')
