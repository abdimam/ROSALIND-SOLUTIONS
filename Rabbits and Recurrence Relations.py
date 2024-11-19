#This might not be the best solution to demostrate dynamic programming but it is still in its spirit!

def rabbit_maker(n, k):
    #what we will do is initiating a vector/list that repressents the initial state of the rabbits, that is one pair of litter.
    rabbitNkids = [0,1] #[adult, kids], these are counted as PAIRS

    #now, we know the logic behind these rabbits/litters, let a month pass and all pairs of litters will be adults, while all pairs of adults will each to their own make a pair of litter
    for i in range(1, n+1):
        newborn = rabbitNkids[0] * k #we multiply the second element with k which is the parameter for how many pairs litter one pair of rabbits can make
        newadults = rabbitNkids[1]

        rabbitNkids[0] += newadults #because adults never die, we just add all new adults here
        rabbitNkids[1] = newborn
    print(rabbitNkids[0])

def validate_parameters(n, k):
    if not isinstance(n, int) and isinstance(k, int):
        raise ValueError(f"One of the parameters given are not integers. N: {n}. k: {k}")
    if n and k < 0:
        raise ValueError(f"One of the parameters are negative, we cant have negative pairs of rabbits, nor can they give birth to negative amount of litter")
    
def main():
    n = int(input("PLease give the amount of rabbit pairs: "))
    k = int(input("PLease give the amount of pair of litter that are born: "))

    validate_parameters(n, k)
    rabbit_maker(n, k)


if __name__ == "__main__":
    main()
