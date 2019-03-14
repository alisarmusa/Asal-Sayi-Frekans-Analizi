import timeit

def primes(n):
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]
#---------------------------------------------------------------------------------------------------------------
begin = timeit.default_timer()

mycenter = 193
i = 1
while i < 9:
    PrimeList = primes(10 ** i)

    PrimeDiffList = []
    length = len(PrimeList) - 1
    m = 0
    while m < length:
        diff = PrimeList[m + 1] - PrimeList[m]
        PrimeDiffList.append(diff)
        m += 1

    index = PrimeDiffList.index(max(PrimeDiffList))
    print(str(10 ** i).center(mycenter))
    print("------------------------------".center(mycenter))
    result = str(PrimeList[index+1])  + " - "  + str(PrimeList[index])   + " = " + str(PrimeDiffList[index])
    print(result.center(mycenter))
    print("******************************".center(mycenter))
    i += 1

end = timeit.default_timer()
#---------------------------------------------------------------------------------------------------------------
print(str(end - begin).center(mycenter))