import sys
import pymysql.cursors


class ControlDatabaseAccess :

    ############################################

    # Return a dictionary consisting of key and value taken from columns having names in these two tuples
    # keysTuple and valuesTuple
    @staticmethod
    def getDictionaryFromDatabase(tableName, keysTuple, valuesTuple):
        # Create a connection to the database
        connection = pymysql.connect(host='localhost',
                                     user='root', # user of database
                                     password='helloworld', # password of database
                                     db='enrollment_database', # name of database
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Execute the query to database
                cursor.execute("SELECT * FROM %s" % (tableName))
                records = cursor.fetchall() # Getting all of data from cursor
                # Create new dictionary to contain the returned results
                result = {}
                for recordIndex in range(len(records)) :
                    keys = []
                    values = []
                    # Create the set of key and value
                    for keyIndex in range(len(keysTuple)):
                        keys.append(records[recordIndex].__getitem__(keysTuple[keyIndex])) # or using : get() method

                    for valueIndex in range(len(valuesTuple)):
                        values.append(records[recordIndex].__getitem__(valuesTuple[valueIndex])) # or using : get() method
                    # Insert the set of key and value into the dictionary.
                    result.__setitem__(tuple(keys), values)
        finally:
            connection.close()
        return result

    ############################################

    # Return a list consisting of values taken from columns having names inside the tuple tupleOfColumnNames
    def getListFromDatabase(tableName, tupleOfColumnNames):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='helloworld',
                                     db='enrollment_database',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Execute the query to database
                cursor.execute("SELECT * FROM %s" % (tableName))
                records = cursor.fetchall()

                # Create new list to contain the returned results
                result = []
                if(len(tupleOfColumnNames) > 1) : # when tupple have multiple names of columns
                    for recordIndex in range(len(records)):
                        valuesList = []
                        for tupleIndex in range(len(tupleOfColumnNames)) :
                            valuesList.append(records[recordIndex].__getitem__(tupleOfColumnNames[tupleIndex]))
                        result.append(valuesList)
                else:       # if tuple has only one column name
                    for recordIndex in range(len(records)) :
                        result.append(records[recordIndex].__getitem__(tupleOfColumnNames[0]))
        finally:
            connection.close()
        return result