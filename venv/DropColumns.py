class DropColumns:

    def dropDrivingSearch(self,ds):
        drivingSearch = ds.drop(['updated_at', 'json_obj', 'from', 'to', 'created_at'], axis=1)
        return drivingSearch

    def dropDelivery(self, d):
        delivery=d.drop(['json_obj'], axis=1).rename(columns={"type": "segmenttype"})
        return delivery

    def dropOrders(self, os):
        orders = os.drop(['guid', 'quoted_delivery_time', 'should_hold_at_airlines'], axis=1)
        return orders

    def dropStart(self, sa):
        startAddresses = sa.drop(['state', 'zip', 'time_zone'], axis=1).rename(columns={"city": "startcity", "lat": 'startlag', "lng": "startlng"})
        return startAddresses

    def dropEnd(self, ea):
        endAddresses = ea.drop(['state', 'zip', 'time_zone'], axis=1).rename(columns={"city": "endcity", "lat": 'endlag', "lng": "endlng"})
        return endAddresses

    def dropAllColumns(self,ds,d,os,sa,ea):
        drivingSearch=self.dropDrivingSearch(ds)
        delivery=self.dropDelivery(d)
        orders=self.dropOrders(os)
        startAddresses=self.dropStart(sa)
        endAddresses=self.dropEnd(ea)
        return drivingSearch,delivery,orders,startAddresses,endAddresses

