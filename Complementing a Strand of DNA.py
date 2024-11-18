def validate_DNA(s):
    for char in s:
        if char not in ["A", "T", "C", "G"]:
            raise ValueError(f"The given sequence is not a valid DNA-sequence. First invalid nucleotide found: {char}")

def get_complementary_strand(s):
    u = s[::-1]
    translation_table = str.maketrans("ATCG", "TAGC")
    print(u.translate(translation_table))

def main():
    s = input("Please input DNA sequence: ")
    validate_DNA(s)
    get_complementary_strand(s)
if __name__ == "__main__":
    main()
