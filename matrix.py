#!/usr/bin/python3

import os
import numpy

# Assign variables

# The matrix 50K x 50K values
rows = 50000
columns = 50000

# Files to store results
unsorted_file = 'matrix_unsorted.csv'
sorted_file = 'matrix_sorted.csv'

# Create an "empty" array(matrix) on disk mapped to memory to avoid high memory consumption and leak
mapped_matrix = numpy.memmap('memmapped.dat', dtype=numpy.int32, mode='w+', shape=(rows, columns))

# Broadcast randomly created array of int32 for each column in matrix
for column in range(columns):
    mapped_matrix[:, column] = numpy.random.randint(-2147483648, 2147483647, rows, dtype='int32')

# Store created matrix in CSV file
numpy.savetxt(unsorted_file, mapped_matrix, delimiter=' ', fmt='%d')

# Sort a matrix along columns with quicksort algorithm
mapped_matrix.sort(axis=0, kind='quicksort')

# Store sorted matrix in CSV file
numpy.savetxt(sorted_file, mapped_matrix, delimiter=' ', fmt='%d')

# Delete the mapped object from memory
del mapped_matrix

# Delete the dumped file of mapped object from disk
os.remove('memmapped.dat')
