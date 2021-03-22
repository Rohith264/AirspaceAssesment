import numpy as np
import pyodbc
import pandas as pd

class SQL_Load:

    def loadDataToStaging(self,df6):
        # Converting nan to none to load the data to SQL table
        df6.replace([np.inf, -np.inf], np.nan, inplace=True)
        df6 = df6.fillna(0)

        # Establishing connection to MSSQL database
        server = 'eu-az-sql-serv1.database.windows.net'
        database = 'dgyqjjn092cx2k5'
        username = 'u1vucvmhf3q55hq'
        password = 'Gj51GrVO#N66e$b569b980eIL'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()

        # Loading the dataframe to staging table
        for index, row in df6.iterrows():
            cursor.execute(
                "INSERT INTO staging([id_x],[created_at],[pick_up_time],[company_id],[segmenttype],[start_address_id],[end_address_id],[arrivaltime],[startcity],[startlag],[startlng],[endcity],[endlag],[endlng],[totalDistance],[drivingtime],[ordertype]) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                row['id_x'], row['created_at'], row['pick_up_time'], row['company_id'], row['segmenttype'],
                row['start_address_id'], row['end_address_id'], row['arrivaltime'], row['startcity'], row['startlag'],
                row['startlng'], row['endcity'], row['endlag'], row['endlng'], row['totalDistance'], row['drivingtime'],
                row['ordertype'])
        cnxn.commit();
        cursor.close();
        cnxn.close();
