import csv
# Test 1 :
names = []
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    next(csv_data)
    next(csv_data)
    for line in csv_data:
        if line[0] == "No Reward":
            break
        names.append("{} {}".format(line[0], line[1]))

for name in names:
    print(name)

# Test 2

# with open('names.csv', 'r') as csv_file :
#     csv_reader = csv.DictReader(csv_file)

#     with open('new_names.csv', 'w') as new_file:
#         head_list = ["first_name", "last_name", "email"]
#         csv_writer = csv.DictWriter(new_file, fieldnames=head_list, delimiter="\t")
#         csv_writer.writeheader()

#         for line in csv_reader:
#             # del line["email"]
#             csv_writer.writerow(line)