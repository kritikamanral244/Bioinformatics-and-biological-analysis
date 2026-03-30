# Bioinformatics-and-biological-analysis
# Sequence Data Processing & FASTA Conversion Pipeline

## Project Overview
This project focuses on processing biological sequence datasets obtained from UniProt. It includes data cleaning, FASTA conversion, sequence filtering, and statistical analysis to generate a high-quality dataset for downstream bioinformatics applications.

## Objectives
- Convert sequence data from Excel to FASTA format  
- Perform data cleaning and duplicate removal  
- Apply preprocessing techniques for sequence quality control  
- Analyze sequence length distribution using statistical methods  
- Generate a refined dataset for further analysis  

## Workflow Pipeline

Excel Dataset (UniProt)  
↓  
Data Cleaning & FASTA Conversion  
↓  
Sequence Filtering (Preprocessing)  
↓  
Statistical Analysis & Visualization  
↓  
Final Clean Dataset + Insights  

## Tools & Technologies
- Python  
- Biopython  
- Pandas  
- Matplotlib  

## 📂 Project Structure
├── excel_to_fasta.py
├── filtering.py
├── statistics_plots.py
├── requirements.txt
└── README.md
## How to Run
### Install dependencies
pip install -r requirements.txt

### Convert Excel to FASTA
python excel_to_fasta.py input.xlsx

### Filter sequences
python filtering.py uniprot_sequences.fasta filtered_sequences.fasta

### Analyze and visualize
python statistics_plots.py filtered_sequences.fasta

## Author
Kritika Manral
B.Sc (Hons) Bioinformatics  
LinkedIn: https://www.linkedin.com/in/kritika-manral-228743355
