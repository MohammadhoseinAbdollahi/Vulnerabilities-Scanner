import requests
import json
import _mysql_connector

# Function to get the security assignment
def get_security_assignment():
    # Connect to the database
    conn = _mysql_connector.connect
    