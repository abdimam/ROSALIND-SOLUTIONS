def main():
    s = input("PLease input the DNA sequence: ")
    validate_s(s)

    count_nucl(s)


def validate_s(s): #We are making sure that the inputed string is actually a DNA sequence and correctly formated, or else we will raise an error
    for character in s:
        if character not in ["A", "C", "G", "T"]:
            raise ValueErrror(f"Invalide nucleotide: {character}")

def count_nucl(s):
    A = s.count("A")
    T = s.count("T")
    G = s.count("G")
    C = s.count("C")

    print(A, C, G, T)

if __name__ == "__main__":
    main()