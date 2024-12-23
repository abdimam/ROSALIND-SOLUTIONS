#This problem can be easly solved by just using for loops and checking each element/base against the corresponding base and counting each time we find a mismatch.
#Obviously this approach is not computationally optimal
#I figured that refering to a hashmap might be a good solution to avoid the potential chain of "if" statements

#we take sequence s and t
def st_countmismatch(s,t ): 

    point_mutations = 0

    for character_s,character_t in zip(s,t):
        if character_s != character_t:
            point_mutations += 1
    print(f"The amount of point mutation found: {point_mutations}")

def validate_st(s,t): #We are making sure that the inputed string is actually a DNA sequence and correctly formated, or else we will raise an error
    for character_s,character_t in zip(s,t):
        if character_s not in {"A", "C", "G", "T"}:
            raise ValueError(f"Invalide nucleotide: {character_s}")
        if character_t not in {"A", "C", "G", "T"}:
            raise ValueError(f"Invalide nucleotide: {character_t}")

def main():
    s = input("Please give the first sequence:  ")
    t = input("Please give the second input     ")
    validate_st(s,t)
    st_countmismatch(s,t)

if __name__ == "__main__":
    main()
