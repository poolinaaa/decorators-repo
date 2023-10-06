from savingReturnsOfDifferentFunc import decoratorTime, decoratorSavingResults, func1, func2, openingDb, creatingTable


cur, con = openingDb('yourDatabase')
creatingTable('functionsResultss', cur)

allData = {}

function1 = decoratorSavingResults(decoratorTime(func2), allData,
                                   con, 'functionsResultss', cur)
function2 = decoratorSavingResults(decoratorTime(func1), allData,
                                   con, 'functionsResultss', cur)

for i in range(5):
    function1(8, 10)
    function1(2, 0)
    function2(3)


print(allData)
con.commit()
con.close()
