from Bio import SeqIO
import statistics as stats
import matplotlib.pyplot as plt
import sys


def calculate_stats(fasta_file):
    lengths = [len(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]

    if len(lengths) == 0:
        print("No sequences found in FASTA file.")
        return

    mean_len = stats.mean(lengths)
    std_len = stats.pstdev(lengths)
    mean_plus_3sigma = mean_len + 3 * std_len

    print(f"Number of sequences: {len(lengths)}")
    print(f"Minimum length:      {min(lengths)}")
    print(f"Maximum length:      {max(lengths)}")
    print(f"Average length:      {mean_len:.2f}")
    print(f"Standard Deviation:  {std_len:.2f}")
    print(f"Mean + 3σ:           {mean_plus_3sigma:.2f}")

    plt.figure(figsize=(10, 5))
    plt.hist(lengths, bins=50, edgecolor='black')
    plt.axvline(mean_len, linestyle='dashed', linewidth=1, label="Mean")
    plt.axvline(mean_plus_3sigma, linestyle='dashed', linewidth=1, label="Mean + 3σ")
    plt.title("Sequence Length Distribution")
    plt.xlabel("Sequence Length")
    plt.ylabel("Count")
    plt.legend()
    plt.tight_layout()
    plt.savefig("sequence_length_distribution.png", dpi=150)
    plt.show()
    print("Plot saved: sequence_length_distribution.png")


if __name__ == "__main__":
    fasta_file = sys.argv[1]
    calculate_stats(fasta_file)
```


