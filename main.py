from savingReturnsOfDifferentFunc import decoratorTime, decoratorSavingResults, openingDb, creatingTable
from functionsExamples import func1, func2, lottery

if __name__=='__main__':
    
    cur, con = openingDb('yourDatabase')
    creatingTable('functionsResults', cur, con)

    allData = {}

    # decorate the functions with decorators and save the decorated functions
    function1 = decoratorSavingResults(decoratorTime(func2), allData,
                                    con, 'functionsResults', cur)
    function2 = decoratorSavingResults(decoratorTime(func1), allData,
                                    con, 'functionsResults', cur)
    function3 = decoratorSavingResults(decoratorTime(lottery), allData, con , 'functionsResults', cur)

    # call the decorated functions multiple times
    for i in range(3):
        function1(8, 10)
        function1(2, 0)
        function3(5, 100)

    # print results to check them quickly
    print(allData)
    con.commit()
    con.close()
