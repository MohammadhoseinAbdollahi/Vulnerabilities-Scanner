import csv

def guess_database_version(cms_version):
    with open('compatiblity_table.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get the header row
        if cms_version not in header:
            return "Unknown CMS version"

        cms_index = header.index(cms_version)  # Get the index of the CMS version in the header
        compatible_databases = []
        for row in reader:
            if row[cms_index] == '1':  # Check if the database is compatible
                compatible_databases.append(row[0])  # Add the database name to the list

    return compatible_databases if compatible_databases else "No compatible databases found"

def find_most_compatible_database(databases_to_consider):
    with open('compatiblity_table.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        most_compatible_database = None
        max_compatibility_count = 0
        for row in reader:
            if row[0] in databases_to_consider:  # Check if the database is in the list
                compatibility_count = row.count('1')  # Count the number of '1's in the row
                if compatibility_count > max_compatibility_count:
                    max_compatibility_count = compatibility_count
                    most_compatible_database = row[0]  # Update the most compatible database

    return most_compatible_database if most_compatible_database else "No compatible databases found"
def get_version_number(database_name):
    # Dictionary to store version numbers for each database
    version_numbers = {
        "MS SQL 2016 SP1": "13.0.4001.0",
        "MS SQL 2014 SP2": "12.0.5000.0",
        "MS SQL 2012": "11.0.7001.0",
        "MS SQL 2008 R2": "10.50.1600.1",
        "MS SQL 2008": "10.0.1600.22",
        "MS SQL 2005": "9.0.5000.0",
        "MongoDB 4.0": "4.0",
        "MongoDB 3.4": "3.4",
        "MongoDB 3.2.1": "3.2.1",
        "MongoDB 3.0": "3.0",
        "MongoDB 2.6": "2.6",
        "Oracle 11g R2": "11.2.0",
        "Oracle 11g": "11.1.0",
        "Oracle 10g": "10.2.0"
    }
    
    # Check if the database name exists in the dictionary
    if database_name in version_numbers:
        return version_numbers[database_name]
    else:
        return "Version number not found for this database"


# Replace 'cms_version' with the actual CMS version you have
def Database_finder(cms_version):
    compatible_databases = guess_database_version(cms_version)
    the_one = find_most_compatible_database(compatible_databases)
    version = 
    return the_one