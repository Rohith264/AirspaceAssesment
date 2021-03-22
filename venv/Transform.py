import json
import pandas as pd

class Transform:
    # Parsing the json_obj column to obtain the driving distance
    def transdistData(self,ds):
        data = []
        for (i, v) in ds.iterrows():
            dat = json.loads(ds['json_obj'][i])
            if dat['status'] == 'ZERO_RESULTS':
                data.append(0)
            else:
                x = dat['routes'][0]
                f = x['legs'][0]['distance']['text']
                i = f.split()
                if i[1] == 'ft':
                    data.append(float(float(i[0]) * 0.00018))
                elif i[1] == 'km':
                    data.append(float(float(i[0]) * 0.62))
                elif i[1] == 'm':
                    data.append(float(float(i[0]) * 0.00062))
                else:
                    data.append(i[0])

        ds['totalDistance'] = data
        ds['totalDistance'] = pd.to_numeric(ds['totalDistance'], errors='coerce')
        return ds

    # Parsing the json_obj column to obtain the drive time
    def transTimeData(self, ds):
        data = []
        for (i, v) in ds.iterrows():
            dat = json.loads(ds['json_obj'][i])
            if dat['status'] == 'ZERO_RESULTS':
                data.append(0)

            else:
                x = dat['routes'][0]
                f = x['legs'][0]['duration']['text']
                l = f.split()
                if len(l) == 4:
                    data.append(int(l[0]) * 60 + int(l[2]))
                if len(l) == 2:
                    data.append(l[0])
        ds['drivingtime'] = data
        ds['drivingtime'] = pd.to_numeric(ds['drivingtime'])
        return ds

    # Parsing the json_obj column to obtain the flight arrival time
    def transArrivalData(self, d):
        arrivaltime = []

        for (i, v) in d.iterrows():
            if pd.notnull(d['json_obj'][i]):
                dat = json.loads(d['json_obj'][i])
                arrivaltime.append(dat['trip'][0]['legs'][0]['arrival_time'])

            else:
                arrivaltime.append(0)

        d['arrivaltime'] = arrivaltime
        return d

    # Converting all date fields from Object to DateTime type
    def transformdate(self,df6):
        df6.pick_up_time = pd.to_datetime(df6.pick_up_time)
        df6.created_at = pd.to_datetime(df6.created_at)
        df6.arrivaltime = pd.to_datetime(df6.arrivaltime)
        return df6

    def transformAllData(self,ds,d):
        ds=self.transdistData(ds)
        ds=self.transTimeData(ds)
        d=self.transArrivalData(d)
        return ds,d
