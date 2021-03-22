import pandas as pd
class Merge:

    def mergeAllTables(self,drivingSearch,delivery,orders,startaddresses,endaddresses):
        # Merging the Orders table with Delivery route segment
        df1 = pd.merge(orders, delivery, left_on='id', right_on='order_id').drop(columns=['order_id'])
        # Merging the joined table with start address table
        df2 = pd.merge(df1, startaddresses, left_on='start_address_id', right_on='id', ).drop(columns=['id'])
        # Merging the joined table with end address table
        df3 = pd.merge(df2, endaddresses, left_on='end_address_id', right_on='id').drop(columns=['id', ])
        # Merging the joined table with Driving Search table
        df4 = pd.merge(df3, drivingSearch, how='left', left_on='driving_search_id', right_on='id').drop(
            columns=['id', ])

        # Dropping the unnecessary columns after merge
        df4.drop(columns=['id_y', 'driving_search_id', 'order_id'], inplace=True)

        # Deriving new column to get the order type
        df5 = df4.groupby('id_x', as_index=False).agg({"segmenttype": "count"})
        df5['ordertype'] = df5['segmenttype'].map({3: 'NFO', 2: 'HFPU', 1: 'DRIVE'})
        df5.drop(columns=['segmenttype'], inplace=True)
        df6 = pd.merge(df4, df5, left_on='id_x', right_on='id_x', how='left')
        return df6