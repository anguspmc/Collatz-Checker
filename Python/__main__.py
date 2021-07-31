n = int(input())

def even(n):
    n /= 2
    return(n)

def odd(n):
    n *= 3
    n += 1
    return(n)

def collatz(n):
    if n % 2 == 0:
        n = even(n)
    else:
        n = odd(n)
    return(n)

def main(n):
    iterations = 0
    while n != 1:
        iterations += 1
        n = collatz(n)
        print(n)
    print(f"1 was reached after {iterations} iterations")

main(n)