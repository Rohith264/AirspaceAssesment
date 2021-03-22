# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from DropColumns import DropColumns
from Extract import Extract
from Merge import Merge
from SQL_Load import SQL_Load
from Transform import Transform


class Driver:
    if __name__ == '__main__':
        extract = Extract()
        ds,d,os,sa,ea= extract.getAllData()
        transform = Transform()
        ds,d= transform.transformAllData(ds,d)
        dropColumns = DropColumns()
        drivingSearch,delivery,orders,startAddresses,endAddresses= dropColumns.dropAllColumns(ds,d,os,sa,ea)

        merge=Merge()
        finalData = merge.mergeAllTables(drivingSearch,delivery,orders,startAddresses,endAddresses)
        finalData= transform.transformdate(finalData)
        print(finalData)
        ##sqlload=SQL_Load()
        ##sqlload.loadDataToStaging(finalData)

