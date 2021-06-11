'''
# File: repair_csv_files.py
# Date: 11.June 2021
# Aim: To set the CSV files into a format fit for PostgreSQL.
        A SQL command is generated , as output, when the CSV file is loaded.
        This command can be copy pasted into SQL terminal
'''
# CSV files to be processed
mar_csv = "march_2021.csv"
apr_csv = "april_2021.csv"
may_csv = "may_2021.csv"
june_csv = "june_2021.csv"

# read the CSV files and get a list of strings
with open(june_csv) as f:
    csv_data = f.readlines()

# format the data accordingly
csv_data = [x.strip() for x in csv_data]    # remove the trailing newline characters
csv_data = [csv_data[i].split(",") for i in range(len(csv_data))]   # split each string into a list of strings sans comma
varchar_format = lambda s: "'{}'".format(s)    # add single quotes around the strings. Needed for the SQL command

# for date formatting
date_split = lambda ds: ds.split("/")
l_d = lambda d_f: "{}-{}-{}".format(d_f[2], d_f[1], d_f[0]) # gives date from dd/mm/yyyy to YYYY-MM-DD

# create the sql command
header = lambda n: "insert into TABLE ({},{},{},{}) values".format(n[0], n[1], n[2], n[3])
value_format = lambda vf: "({})".format(vf)

sql_command = header(csv_data[0])
i = 1

while (i < (len(csv_data) - 1)):
    row_value = ""
    date_value = l_d(date_split(csv_data[i][0]))    # get the date in the appropriate format
    date_value = varchar_format(date_value)
    row_value = date_value+", "

    # get the category value in the appropriate format
    csv_data[i][1] = "NULL" if csv_data[i][1] == "-" else csv_data[i][1]
    csv_data[i][1] = "Others" if csv_data[i][1] in ["Cat1", "Cat2", "Cat3", "Cat4"] \
        else "Essentials" if csv_data[i][1] in ["Cat5", "Cat6", "Cat7"] \
        else csv_data[i][1]
    category_value = varchar_format(csv_data[i][1])
    row_value += category_value+", "

    # get the comments value in the appropriate format
    csv_data[i][2] = "NULL" if csv_data[i][2] == "-" else csv_data[i][2]
    comments_value = varchar_format(csv_data[i][2])
    row_value += comments_value+", "

    # get the cost value in the appropriate format
    csv_data[i][3] = "NULL" if csv_data[i][3] == "-" else csv_data[i][3]
    cost_value = csv_data[i][3]
    row_value += cost_value

    # generate the final sql command
    row_value = value_format((row_value))
    sql_command += row_value
    sym = "," if (i != len(csv_data) - 2) else ";"
    sql_command += sym

    # increment the counter i
    i += 1

print(sql_command)      # this is the final SQL command, which can be directly copy pasted in the SQL terminal

