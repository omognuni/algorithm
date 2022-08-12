'''
https://www.acmicpc.net/problem/11653
'''

def get_primes(n):

    for i in range(2,n+1):
        if n%i==0:
            n = n//i
            print(i)
            return get_primes(n)
        else:
            pass


k = int(input())

if k == 1:
    print()

else:
    get_primes(k)