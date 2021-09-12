
# this function transpose columns and rows
import numpy as np

# list of list which the big list is the genes and the smallest is the values
f = open('GenesAndSamples.txt', 'r')
list_data = []
for line in f:
    line = line.rstrip().split('\t')
    list_data.append(line)
f.close()

numpy_array = np.array(list_data, dtype=object)
arr_transpose = np.transpose(numpy_array)
print(arr_transpose)

transpose_files = open('Transpose_GenesAndSimples.txt','w')
for row in arr_transpose:
    for item in row:
        transpose_files.write(str(item)+'\t')
    transpose_files.write('\n')

# input the requested organ
type = "Vagina"
# create a file name
name_file_result = type + "_" + "GTEX" + ".txt"
phenotype_file = open("TcgaTargetGTEX_phenotype.txt", 'r', errors='ignore')
transpose_genes_data = open('Transpose_GenesAndSimples.txt', 'r')
result_file = open(name_file_result, 'w', errors='ignore')
for line1 in phenotype_file:
    line1 = line1.rstrip().split('\t')
    # check if the line in the file as the requested organ and also is healthy tissue
    if line1[3] == type and line1[0].startswith("GTEX"):
        # return to the start of f_geneExp file
        transpose_genes_data.seek(0)
        for line2 in transpose_genes_data:
            line2 = line2.rstrip().split("\t")
            if line2[0] == line1[0]:
                result_file.write(str(line2) + '\n')
