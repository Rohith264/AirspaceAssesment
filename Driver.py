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
        # Extracting data from 5 excel files
        extract = Extract()
        ds,d,os,sa,ea= extract.getAllData()
        # Transforming data to obtain additional columns
        transform = Transform()
        ds,d= transform.transformAllData(ds,d)
        # Dropping unnecessary columns
        dropColumns = DropColumns()
        drivingSearch,delivery,orders,startAddresses,endAddresses= dropColumns.dropAllColumns(ds,d,os,sa,ea)
        # joining the 5 tables
        merge=Merge()
        finalData = merge.mergeAllTables(drivingSearch,delivery,orders,startAddresses,endAddresses)
        # Converting the date columns from Object type to DateTime
        finalData= transform.transformdate(finalData)
        sqlload=SQL_Load()
        sqlload.loadDataToStaging(finalData)

