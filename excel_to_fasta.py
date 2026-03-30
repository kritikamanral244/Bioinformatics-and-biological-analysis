from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
import pandas as pd
import sys


def load_data(excelfile):
    df = pd.read_excel(excelfile)
    print(f"Total rows loaded: {len(df)}")
    return df


def clean_data(df, id_col, seq_col):
    df = df.dropna(subset=[id_col, seq_col])
    df[seq_col] = df[seq_col].astype(str).str.replace(" ", "").str.upper()
    df = df[df[seq_col] != ""]
    df = df.drop_duplicates(subset=[id_col])
    df = df.drop_duplicates(subset=[seq_col])
    return df


def convert_to_fasta(df, id_col, seq_col, output="uniprot_sequences.fasta"):
    records = []
    for _, row in df.iterrows():
        rec = SeqRecord(Seq(row[seq_col]), id=str(row[id_col]), description="")
        records.append(rec)
    with open(output, "w") as f:
        SeqIO.write(records, f, "fasta")
    return records


if __name__ == "__main__":
    excelfile = sys.argv[1]
    id_col = "Entry"
    seq_col = "Sequence"

    df = load_data(excelfile)
    total = len(df)

    df = clean_data(df, id_col, seq_col)
    records = convert_to_fasta(df, id_col, seq_col)

    print(f"Unique sequences kept: {len(records)}")
    print(f"Rows removed:          {total - len(records)}")
    print(f"Output: uniprot_sequences.fasta")
```


