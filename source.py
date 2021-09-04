from collections import OrderedDict
import csv
from statistics import mean
def calculate_averages(input_file_name, output_file_name):
    average= []
    lname= []
    with open(input_file_name, newline= '') as f: 
        reader= csv.reader(f)
        for row in reader: 
            name = row[0]
            lname.append(name)
            these_grades = list()
            for grade in row[1:]:
               these_grades.append(float(grade))
            avg = str(mean(these_grades))
            average.append(avg)
    f.close()
    combine= OrderedDict(zip(lname, average))
    with open(output_file_name, 'w', newline= '') as file:
        writer = csv.writer(file, delimiter=',')
        for k,v in combine.items():
            writer.writerow([k , v])
    file.close()
def calculate_sorted_averages(input_file_name, output_file_name):
    average= []
    lname= []
    with open(input_file_name, newline= '') as f: 
        reader= csv.reader(f)
        for row in reader: 
            name = row[0]
            lname.append(name)
            these_grades = list()
            for grade in row[1:]:
               these_grades.append(float(grade))
            avg = mean(these_grades)
            average.append(avg)
    f.close()
    combine= OrderedDict(zip(lname, average))
    combine= list(combine.items())
    combine = sorted(combine, key=lambda x: (x[1], x[0]))
    combine= OrderedDict(combine)
    with open(output_file_name, 'w', newline= '') as file:
        writer = csv.writer(file, delimiter=',')
        for k,v in combine.items():
            writer.writerow([k , v])
    file.close()
def calculate_three_best(input_file_name, output_file_name):
    average= []
    lname= []
    with open(input_file_name, newline= '') as f: 
        reader= csv.reader(f)
        for row in reader: 
            name = row[0]
            lname.append(name)
            these_grades = list()
            for grade in row[1:]:
               these_grades.append(float(grade))
            avg = mean(these_grades)
            average.append(avg)
    f.close()
    combine= OrderedDict(zip(lname, average))
    combine= list(combine.items())
    combine = sorted(combine, key=lambda x: (-x[1], x[0]))
    combine= OrderedDict(combine)
    three= []
    for i in list(combine.items()):
       three.append(i)
    combine= three[0:3]
    combine= OrderedDict(combine)
    
    with open(output_file_name, 'w', newline= '') as file:
        writer = csv.writer(file, delimiter=',')
        for k,v in combine.items():
            writer.writerow([k , v])
    file.close()
def calculate_three_worst(input_file_name, output_file_name):
    average= []
    with open(input_file_name, newline= '') as f: 
        reader= csv.reader(f)
        for row in reader: 
            these_grades = list()
            for grade in row[1:]:
               these_grades.append(float(grade))
            avg = mean(these_grades)
            average.append(avg)
    f.close()
    average.sort()
    average= average[0:3]
    new_average= []
    for z in average:
       new_average.append(str(z))  
    
    with open(output_file_name, 'w', newline= '') as file:
        writer = csv.writer(file,delimiter=',')
        for row in new_average:
            columns = [c.strip() for c in row.strip(', ').split(',')]
            writer.writerow(columns)
           
    file.close()
def calculate_average_of_averages(input_file_name, output_file_name):
    average= []
    with open(input_file_name, newline= '') as f: 
        reader= csv.reader(f)
        for row in reader: 
            these_grades = list()
            for grade in row[1:]:
               these_grades.append(float(grade))
            avg = mean(these_grades)
            average.append(avg)
            
    f.close()
    realaverage= mean(average)
    realaverage= str(realaverage)   
    with open(output_file_name, 'w', newline= '') as file:
        writer = csv.writer(file,delimiter=',')
        columns = [c.strip() for c in realaverage.strip(', ').split(',')]
        writer.writerow(columns)
           
    file.close()

