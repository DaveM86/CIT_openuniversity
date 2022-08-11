'''
ROOTABLE - This can be used to find the largest root that is a factor of the target.
Set the target script will do the rest.

Particularly handy when trying to factorise a disciminant quickly.
'''
import math

def rootable(target, p):
    for x in range (1,p+1):
        y = x**2
        if target % y == 0:
            print(f'{y} is a root(able) factor of {target}: {x} root '+str(target/y))

def main():
    t = int(input('target: '))
    p = math.ceil(t**0.5)
    rootable(t,p)

if __name__ == '__main__':
    main()