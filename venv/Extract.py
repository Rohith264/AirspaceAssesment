import pandas as pd
class Extract:


    def getDrivingSearchData(self):
        # since we can use multiple CSV data files in future,
        # so will pass csv name as an argument to fetch the desired CSV data.
        ds = pd.read_csv(r"driving_searches.csv")
        return ds

    def getDeliverySegmentData(self):
        # since we can use multiple CSV data files in future,
        # so will pass csv name as an argument to fetch the desired CSV data.
        d = pd.read_csv(r"delivery_route_segments.csv")
        return d

    def getOrdersData(self):
        # since we can use multiple CSV data files in future,
        # so will pass csv name as an argument to fetch the desired CSV data.
        os = pd.read_csv(r"orders.csv")
        return os

    def getStartAddressData(self):
        # since we can use multiple CSV data files in future,
        # so will pass csv name as an argument to fetch the desired CSV data.
        sa = pd.read_csv(r"start_addresses.csv")
        return sa

    def getEndAddressData(self):
        # since we can use multiple CSV data files in future,
        # so will pass csv name as an argument to fetch the desired CSV data.
        ea = pd.read_csv(r"end_addresses.csv")
        return ea

    def getAllData(self):
        ds= self.getDrivingSearchData()
        d= self.getDeliverySegmentData()
        os= self.getOrdersData()
        sa= self.getStartAddressData()
        ea=self.getEndAddressData()
        print("here")
        return ds,d,os,sa,ea

