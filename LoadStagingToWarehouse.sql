WITH cte AS(
SELECT  air.id_x,
		dateadd(mi,air1.drivingtime,air.arrivaltime) as delivery_time_local
FROM staging as air 
JOIN staging as air1 
ON air.id_x = air1.id_x and air.segmenttype='FlyingSegment' and air.end_address_id + 1=air1.start_address_id
WHERE air.ordertype='NFO')
INSERT INTO airspaceWarehouse
SELECT bq.order_id,
       bq.company_id,
	   upper(air.startcity) as origin_city,
	   upper(air1.endcity) as destination_city,
	   bq.pick_up_time_local,
	   bq.delivery_time_local,
	   bq.minutes_to_pickup,
	   bq.order_type,
	   bq.total_drive_distance
FROM
(
SELECT DISTINCT	air.id_x AS order_id,
	    air.company_id,
		min(air.start_address_id) over(partition by air.id_x) as startcityid,
		max(air.end_address_id) over(partition by air.id_x) as endcityid,
		air.pick_up_time as pick_up_time_local,
		CASE WHEN air.ordertype='NFO' then cte.delivery_time_local
			 WHEN air.ordertype='HFPU' AND air.segmenttype='FlyingSegment' THEN air.arrivaltime
			 WHEN air.ordertype='DRIVE' THEN dateadd(mi,air.drivingtime,air.pick_up_time) 
		END AS delivery_time_local,
		datediff(mi,air.created_at,air.pick_up_time) as minutes_to_pickup,
		ordertype as order_type,
		round(sum(air.totalDistance) over(partition by air.id_x),2) as total_drive_distance
		
FROM staging as air 
LEFT JOIN cte on air.id_x=cte.id_x) as bq
JOIN (select start_address_id,startcity from staging) as air 
ON bq.startcityid=air.start_address_id
JOIN (select end_address_id,endcity from staging) as air1
ON bq.endcityid=air1.end_address_id
