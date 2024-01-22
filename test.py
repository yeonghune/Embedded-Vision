def add(a, b):
    
    return a+b
    
def sub(a, b):
    if a > b:
        c = a-b
    else:
        c =  b-a

    return c

def mul(a, b):
    c = a*b
    return c
    
def main():
    a=int(input('a='))
    print(a)
    b=int(input('b='))
    print(b)
    print(add(a, b))
    print(sub(a, b))
    print(mul(a, b))

if __name__ == "__main__":
    main()
