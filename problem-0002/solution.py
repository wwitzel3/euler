MAX_FIB = 4000000

def fib(l,r,s):
    result = l+r
    if result <= MAX_FIB:
        if not result % 2:
            s += result
        return fib(r,result,s)
    return s

def main():
    print fib(1,1,0)

if __name__ == '__main__':
    main()

