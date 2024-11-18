def DNA2RNA(s):
    u = s.replace("T", "U")
    print(u)

def validate_DNA(s):
    for char in s:
        if char not in ["A", "T", "C", "G"]:
            raise ValueError(f"The given sequence is not a valid DNA-sequence. First invalid nucleotide found: {char}")

def main():
    s = input("Please give an valid DNA sequence: ")
    validate_DNA(s)
    DNA2RNA(s)

if __name__ == "__main__":
    main() 