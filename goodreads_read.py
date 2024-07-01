import csv
#extract read books from the csv file
with open("goodreads_library_export.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if row[22] == '1': # all books that are read have the last but one column set to one
            print(row[1])  # The 1st row(not the 0th) contains the title of the book that is read

