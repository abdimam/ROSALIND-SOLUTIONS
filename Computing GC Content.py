#I have decided to make a "proper" parser for fasta files in this solution.
#I will ad the sample dataset as a FASTA file, it is available as "Sample_dataset_GC.FASTA"
def parser(fasta_file): #this parser will take out the sequence ID and sequence and group them together
    seq_ID = []
    sequences = [] #The idea behind these two initiated lists is that they will contain the ID respectivly the sequence, each pair having the same indices
    
    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip() #removes any whitespaces, but those are anyways not expected to be in a real FASTA file
            #The key here is to find where the > symbols are in the file, they indicate where a new sequence with a specific ID starts, if we found another one after then we know it is a new sequence unique from the last one
            if line.startswith(">"):
                seq_ID.append(line.strip(">"))
            else:
                sequences.append(line)
    return seq_ID, sequences


def GC_counter(fasta_file):
    seq_ID, sequences = parser(fasta_file)
    highest_GC = 0
    index_seq = None
    for ind, i in enumerate(sequences):
        GC = i.count("C") + i.count("G")
        seq_length = len(i)
        GC_content = GC/seq_length
        if GC_content > highest_GC:
            highest_GC = GC_content
            index_seq = ind
    print(seq_ID[index_seq])
    print(highest_GC * 100)

def main():
    fasta_file = input("Pleae give the name of the fasta file you want to use, otherwise leave this blank and we will use the sample dataset: ")
    if fasta_file == "":
        fasta_file = "Sample_dataset_GC.FASTA"
    GC_counter(fasta_file)

if __name__ == "__main__":
    main()

