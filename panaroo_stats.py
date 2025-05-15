#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:43:08 2024

@author: ahmed
"""
###################################

import pandas as pd
import numpy as np
import argparse

###################################
my_parser = argparse.ArgumentParser(description='Welcome!')
#print("example: $ python panaroo_stats.py -i ./txt")



my_parser.add_argument('-i','--input_dir',
                       action='store',
                        metavar='input_dir',
                       type=str,
                       help="input_dir")

my_parser.add_argument('-p','--prefix',
                       action='store',
                        metavar='prefix',
                       type=str,
                       help="prefix")


###########################################
# Execute the parse_args() method
args = my_parser.parse_args()

###########################################
data  = args.input_dir
data = pd.read_csv(data)
#data = pd.read_csv("gene_presence_absence_panaroo.csv")
pref = args.prefix
#pref = "CA"
###################################

df = pd.DataFrame(data)

###################################

#the core genome module
df_no_na = df.dropna()
df_core = df_no_na[df_no_na.apply(lambda row: row.astype(str).str.strip().all(), axis=1)]


fcn  = df_core.columns[df_core.notna().all()].tolist()[0]

gene_list = df_core[fcn].tolist()

with open('list_of_core_genes_from_%s_genome.txt'%(fcn), 'w') as file:
    file.write('\n'.join(map(str, gene_list)))
    
df_core.to_csv('Core_genome.csv', index=False)



###################################
#let's go for the file

spp_df = df.iloc[:, 3:]

# Select columns that start with 'CA'
ca_columns = [col for col in spp_df.columns if col.startswith(pref)]

# Select columns without 'CA' prefix
other_columns = [col for col in spp_df.columns if not col.startswith(pref)]

# Filter rows where all 'CA' columns have values not present in other columns

filtered_df = spp_df[
    spp_df[ca_columns].notna().all(axis=1) & 
    spp_df[other_columns].isna().all(axis=1)
]

filtered_df.reset_index(drop=True, inplace=True)


fcn  = filtered_df.columns[filtered_df.notna().all()].tolist()[0]

gene_list = filtered_df[fcn].tolist()

with open('list_of_genes_%s_from_%s.txt'%(pref,fcn), 'w') as file:
    file.write('\n'.join(map(str, gene_list)))

final_filtered_df = df[df.apply(lambda row: row.astype(str).str.contains('|'.join(gene_list)).any(), axis=1)]

final_filtered_df.reset_index(drop=True, inplace=True)

final_filtered_df.to_csv('%s_unique_genes.csv'%(pref), index=False)

# Count occupied cells per column and store the results in a tuple
occu_cols = tuple(df[col].count() for col in df.columns)
av_occ_col = sum(occu_cols) / len(occu_cols)

print("You have a pangenome  of %d genes"%(len(df)))
print("On average, each genome has a %d genes"%(av_occ_col))
print("You have a core genome of %d genes for your input genomes"%(len(df_core)))
print("You have %d of unique genes for the %s group"%(len(gene_list),str(pref)))



