def insert_into_database(
        myDataBase,
        tableName,
        columnNameAndValues
):
    cursor = myDataBase.cursor()
    columnName = str()
    values = str()
    for key, value in columnNameAndValues.items():
        columnName += key + ","
        values += "'" + value + "'" + ","

    cursor.execute("INSERT INTO {0} ({1}) VALUES ({2})".format(
        tableName,
        columnName[:-1],
        values[:-1]
    ))
    myDataBase.commit()
    
    
    
def update_data_base(
        myDataBase,
        tableName,
        columnNameAndValues
):
    cursor = myDataBase.cursor()
    columnNameAndValuesString = str()
    identifyColumnAndValue = str()
    for key, value in columnNameAndValues.items():
        if "id" in key:
            identifyColumnAndValue = key + "=" + value
        else:
            columnNameAndValuesString += key + "=" + "'" + value + "'" + ","
    cursor.execute("UPDATE {0} SET {1} WHERE {2}".format(
        tableName,
        columnNameAndValuesString[:-1],
        identifyColumnAndValue
    ))
    myDataBase.commit()
    
    
    
def update_or_insert(dictOfValues):
    for key in dictOfValues:
        if "id" in key:
            return "to_update"
    return "to_insert"
