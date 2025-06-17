# Panaroo_stats
**Kindly, if you find this repo useful for your work, cite & star this repo**

**What is this script?**

[Panaroo](https://github.com/gtonkinhill/panaroo) is a great tool for graph-based  annotation. However, sometimes I need to extract some common and unique genes from a certain group of genomes for further analysis. Therefore, I developed this simple script.


**What do you need?**

a prefix in your genome's names marking the group you are interested **(Consider this before you start Panaroo analysis)**, and the Panaroo gene_presence_absence file 

*What about dependencies?*

Pandas,numpy, and argparse

Then, effortlessly, you can type in your beautiful terminal

```bash
 python panaroo_stats.py -i simple.csv -p CA_
```
"-i/--input_dir" is your path to your Panaroo CSV gene_presence_absence file

"-p/--prefix"  is your prefix of species you are interested in. For example, I am interested in bacteria whose names start with *CA_*


**What do you get?**

Currently, there are 3 files. one CSV files with the defined as the genes that are **100% (not 99.99999%)** shared among all of your columns (genomes) in your input CSV file, another CSV for **100 %** gene shared and unique for the group of bacteria that have the prefix you wrote before in the command line, and finally one txt file with these unique genes  adapted from the first column (genome) of you prefix marked genomes.
