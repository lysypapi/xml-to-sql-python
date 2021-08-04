import xml.etree.ElementTree as ET
import mysql.connector
from functionDataBase import *

myDataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kolopop",
    database="sql_honey_8"
)

listOfCustomers = []
tree = ET.parse("document.xml")
root = tree.getroot()
for item in root.findall("customer"):
    customer = {
        child.tag: child.text
        for child in item
    }
    listOfCustomers.append(customer)

for customer in listOfCustomers:
    updateOrInsertResult = update_or_insert(customer)

    if updateOrInsertResult == "to_update":
        update_data_base(myDataBase, root.tag, customer)
    elif updateOrInsertResult == "to_insert":
        insert_into_database(myDataBase, root.tag, customer)
    else:
        print("Error")
