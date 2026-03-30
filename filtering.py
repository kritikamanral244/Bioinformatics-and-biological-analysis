from Bio import SeqIO
import statistics
import sys


def filter_sequences(input_file, output_file):
    records = list(SeqIO.parse(input_file, "fasta"))
    lengths = [len(record.seq) for record in records]

    min_len = min(lengths)
    max_len = max(lengths)
    mean_len = statistics.mean(lengths)

    lower = mean_len * 0.2
    upper = mean_len * 1.2

    filtered = [
        record for record in records
        if len(record.seq) != min_len
        and len(record.seq) != max_len
        and lower <= len(record.seq) <= upper
    ]

    SeqIO.write(filtered, output_file, "fasta")

    print(f"Total sequences:    {len(records)}")
    print(f"Kept:               {len(filtered)}")
    print(f"Removed:            {len(records) - len(filtered)}")
    print(f"Output: {output_file}")


if __name__ == "__main__":
    input_file = sys.argv[1]   # run as: python filter_sequences.py input.fasta output.fasta
    output_file = sys.argv[2]
    filter_sequences(input_file, output_file)