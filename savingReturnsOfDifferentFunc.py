import time
from functools import wraps
import itertools
import sqlite3

# define a decorator that measures the execution time of a function
def decoratorTime(func3):
    @wraps(func3)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func3(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        runTimeOfFunc = end-start-1
        return runTimeOfFunc, res
    return wrapper

# define a decorator that saves the results of function calls to a dictionary and a database
def decoratorSavingResults(func, dict, con, nameTab, curs):
    # initialize a counter for function calls
    idOfCallingFunc = itertools.count()
    # get the keys from the dictionary
    keys = dict.keys()

    @wraps(func)
    def wrapper2(*args, **kwargs):
        # check if the function name is already in the dictionary
        if func.__name__ in keys:
            # call the original function
            timeReturned, returnedByFunc = func(*args, **kwargs)
            d = {}
            d['returned'] = returnedByFunc
            d['nrOfExecution'] = next(idOfCallingFunc)
            d['executionTime'] = timeReturned
            dict[func.__name__].append(d)
            
            # add the results to the database table
            addToTable(func.__name__,  str(d['nrOfExecution']),
                       str(d['executionTime']), str(d['returned']), nameTab, curs, con)
            return dict
        else:
            dict[func.__name__] = []
            # call the original function
            timeReturned, returnedByFunc = func(*args, **kwargs)
            d = {}
            d['returned'] = returnedByFunc
            d['nrOfExecution'] = next(idOfCallingFunc)
            d['executionTime'] = timeReturned
            dict[func.__name__].append(d)
            
            # add the results to the database table
            addToTable(func.__name__, str(d['nrOfExecution']),
                       str(d['executionTime']), str(d['returned']), nameTab, curs, con)
            return dict
    return wrapper2

# function to open a database connection and return a cursor
def openingDb(nameDb):
    connectionDb = sqlite3.connect(f'{nameDb}.db')
    connectionDb.row_factory = sqlite3.Row
    cursor = connectionDb.cursor()
    return cursor, connectionDb

# function to create a table in the database
def creatingTable(nameTable, cursor, con):
    cursor.execute(f"""CREATE TABLE if not exists {nameTable}(
            id INTEGER PRIMARY KEY,
            funcName text,
            nrOfExecution text,
            executionTime text,
            returned text)          
            """)
    cursor.execute(f'''DELETE FROM {nameTable}''')
    con.commit()

# function to add data to the database table
def addToTable(nameFunc, nr, timeOfRun, returned, nameTable, cursor, con):
    cursor.execute(f'INSERT INTO {nameTable}(funcName,nrOfExecution,executionTime,returned) VALUES(?,?,?,?)', (
        nameFunc, nr, timeOfRun, returned))
    con.commit()
