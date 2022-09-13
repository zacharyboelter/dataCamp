# x = float(input('What is x? '))
# y = float(input('What is y? '))

# z = round(x / y)

# print(f'{z:.2f}')

# def main():
#     name = input("whats your name? ")
#     hello(name)

# def hello(to="World"):
#     return(f'Hello, {to}')


# print(main())



def main():
    x = int(input('What is x? '))
    print(f'x squared is {squared(x)}')

def squared(num):
    return pow(num, 2)  

main()