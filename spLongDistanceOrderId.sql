create procedure spLongDistanceOrderId
AS
select air.id_x as OrderId
from staging as air 
where dbo.distance(startlag,startlng,endlag,endlng) in (
select max(dbo.distance(startlag,startlng,endlag,endlng))
from staging) 