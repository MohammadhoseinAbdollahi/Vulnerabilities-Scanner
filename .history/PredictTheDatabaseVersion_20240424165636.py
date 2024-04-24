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


# Replace 'cms_version' with the actual CMS version you have
def Database_finder(cms_ver)
compatible_databases = guess_database_version(cms_version)
the_one = find_most_compatible_database(compatible_databases)
print(f"The compatible databases for CMS version {cms_version} are {the_one}.")