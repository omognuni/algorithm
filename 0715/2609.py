import sys

input = sys.stdin.readline

def gcd(a,b):
    while b > 0:
        a, b = b, a%b

    return a

def lcm(a,b):
    return int(a*b /gcd(a,b))

m, n = map(int, input().split())

print(gcd(m,n))
print(lcm(m,n))
# def is_prime(n):
#     if n == 1:
#         return False

#     # 제곱근까지만 확인
#     sq = int(math.sqrt(n))
    
#     for i in range(2, sq+1):
#         if n % i == 0:
#             return False
#     return True

# m, n = map(int,input().split())
# mcm = 0


# count = 1
# while True:
#     if m*count % n == 0:
#         mcm=m*count
#         break
#     else:
#         count+=1

# primes = []
# for i in range(1, 10001):
#     if is_prime(i):
#         primes.append(i)

# m_prime = []
# n_prime = []


# count = 0
# while m != 1:
    
#     if m % primes[count] == 0:
#         m = m//primes[count]
#         m_prime.append(primes[count])
#         count = 0
#     else:
#         count+=1
        

# count = 0
# while n != 1:

#     if n % primes[count] == 0:
#         n = n//primes[count]
#         n_prime.append(primes[count])
#         count = 0
#     else:
#         count += 1

# m_prime = set(m_prime)
# n_prime = set(n_prime)
# mcd = 1
# for i in list(n_prime & m_prime):
#     mcd = mcd*i


# print(mcd)
# print(mcm)

