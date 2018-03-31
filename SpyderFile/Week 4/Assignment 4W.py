import csv
import re

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    data_list = []
    for row in reader:
        data_list.append(row)

#for the names
#first name last name
regex1 = re.compile(r"^([a-zA-Z]+) ([a-zA-Z]+)$")

#last name, first name
regex2 = re.compile(r"^([a-zA-Z]+), ([a-zA-Z]+)$")

#first name MI last name
regex3 = re.compile(r"^([a-zA-Z]+) ([A-Z]\.) ([a-zA-Z]+)$")

#last name, first name MI
regex4 = re.compile(r"^([a-zA-Z]+), ([a-zA-Z]+) ([A-Z]\.)$")

#for the phone numbers
#all numbers
regex5 = re.compile(r"^(\d{3})(\d{3})(\d{4})$")

#(numbers) numbers-numbers
regex6 = re.compile(r"^\((\d{3})\) (\d{3})-(\d{4})$")

#numbers-numbers-numbers
regex7 = re.compile(r"^(\d{3})-(\d{3})-(\d{4})$")

#numbers.numbers.numbers
regex8 = re.compile(r"^(\d{3})\.(\d{3})\.(\d{4})$")

#number-numbers-numbers-numbers
regex9 = re.compile(r"^(\d)-(\d{3})-(\d{3})-(\d{4})$")

with open("data2.csv", 'wb') as k:
    data_writer = csv.writer(k, delimiter = ",")
    namelist = []; phonelist = []
    for row in data_list[1:]:
        print row[1]
        #first create a condition to ignore faulty numbers
        NotFaulty = (regex5.findall(row[1]) or regex6.findall(row[1]) or regex7.findall(row[1]) or regex8.findall(row[1]) or regex9.findall(row[1]))
        
        if NotFaulty:
        #for names
            if regex1.findall(row[0]):
                name_tuple = regex1.findall(row[0])[0]
                namelist.append([name_tuple[0], None, name_tuple[1]])
            elif regex2.findall(row[0]):
                name_tuple = regex2.findall(row[0])[0]
                namelist.append([name_tuple[1], None, name_tuple[0]])
            elif regex3.findall(row[0]):
                name_tuple = regex3.findall(row[0])[0]
                namelist.append([name_tuple[0], name_tuple[1], name_tuple[2]])
            elif regex4.findall(row[0]):
                name_tuple = regex4.findall(row[0])[0]
                namelist.append([name_tuple[1], name_tuple[2], name_tuple[0]])
        
        #for phone numbers
            if regex5.findall(row[1]):
                number_tuple = regex5.findall(row[1])[0]
                phonelist.append("(" + number_tuple[0] + ") " + number_tuple[1] + "-" + number_tuple[2])
            elif regex6.findall(row[1]):
                number_tuple = regex6.findall(row[1])[0]
                phonelist.append("(" + number_tuple[0] + ") " + number_tuple[1] + "-" + number_tuple[2])
            elif regex7.findall(row[1]):
                number_tuple = regex7.findall(row[1])[0]
                phonelist.append("(" + number_tuple[0] + ") " + number_tuple[1] + "-" + number_tuple[2])
            elif regex8.findall(row[1]):
                number_tuple = regex8.findall(row[1])[0]
                phonelist.append("(" + number_tuple[0] + ") " + number_tuple[1] + "-" + number_tuple[2])
            elif regex9.findall(row[1]):
                number_tuple = regex9.findall(row[1])[0]
                phonelist.append("(" + number_tuple[1] + ") " + number_tuple[2] + "-" + number_tuple[3])
    
    data_writer.writerow(["First", "M.I.", "Last", "Number"])
    for name_row, phone_row in zip(namelist, phonelist):
        data_writer.writerow([name_row[0], name_row[1], name_row[2], phone_row])
        

    
