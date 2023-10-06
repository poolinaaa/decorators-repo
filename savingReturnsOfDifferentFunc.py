import time
from functools import wraps
import itertools
import sqlite3


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


def decoratorSavingResults(func, dict, con, nameTab, curs):
    idOfCallingFunc = itertools.count()
    keys = dict.keys()

    @wraps(func)
    def wrapper2(*args, **kwargs):
        if func.__name__ in keys:
            timeReturned, returnedByFunc = func(*args, **kwargs)
            d = {}
            d['returned'] = returnedByFunc
            d['nrOfExecution'] = next(idOfCallingFunc)
            d['executionTime'] = timeReturned
            dict[func.__name__].append(d)
            addToTable(func.__name__,  str(d['nrOfExecution']),
                       str(d['executionTime']), str(d['returned']), nameTab, curs, con)
            return dict
        else:
            dict[func.__name__] = []
            timeReturned, returnedByFunc = func(*args, **kwargs)
            d = {}
            d['returned'] = returnedByFunc

            d['nrOfExecution'] = next(idOfCallingFunc)
            d['executionTime'] = timeReturned
            dict[func.__name__].append(d)
            addToTable(func.__name__, str(d['nrOfExecution']),
                       str(d['executionTime']), str(d['returned']), nameTab, curs, con)
            return dict
    return wrapper2


def func1(a):
    return a**a


def func2(a, b):
    return a+b, a


def openingDb(nameDb):
    connectionDb = sqlite3.connect(f'{nameDb}.db')

    connectionDb.row_factory = sqlite3.Row

    cursor = connectionDb.cursor()
    return cursor, connectionDb


def creatingTable(nameTable, cursor):
    cursor.execute(f"""CREATE TABLE if not exists {nameTable}(
            id INTEGER PRIMARY KEY,
            funcName text,
            nrOfExecution text,
            executionTime text,
            returned text)          
            """)


def addToTable(nameFunc, nr, timeOfRun, returned, nameTable, cursor, con):
    cursor.execute(f'INSERT INTO {nameTable}(funcName,nrOfExecution,executionTime,returned) VALUES(?,?,?,?)', (
        nameFunc, nr, timeOfRun, returned))
    con.commit()
