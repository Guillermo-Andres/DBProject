#!/usr/bin/env bash
sudo etc/init.d/postgresql restart ;
echo "Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('skyhighbannanas',24.99,'Luquillo', 10, '300mg edible');
insert into babyFood(resource_id,babyFood_type,babyFood_is_perishable,babyFood_ingrendients,babyFood_unitsize,babyFood_expDate) values ( (SELECT resource_id from resource where resource_id = '1'),'gerber',TRUE,'bannana,ganja',10,'12-12-2024');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Salchichas veganas',4.99,'Luquillo', 10, 'saben fo');
insert into cannedFood(resource_id,cannedFood_type,cannedFood_is_perishable,cannedFood_ingrendients,cannedFood_unitsize,cannedFood_expDate) values ( (SELECT resource_id from resource where resource_id = '2'),'Carmela',TRUE,'no vaca,no pork',10,'12-12-2024');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('beef jerky',7.99,'Caguas', 10, 'saben cool');
insert into dryFood(resource_id,dryFood_type,dryFood_is_perishable,dryFood_ingrendients,dryFood_unitsize,dryFood_expDate) values ( (SELECT resource_id from resource where resource_id = '3'),'Wills',FALSE,' vaca, pork',10,'12-12-2024');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('heavy stuff',179.99,'Caguas', 15, 'puff pass');
insert into heavyEquipment (resource_id,heavyequipment_type) values( (SELECT resource_id from resource where resource_id = '4'),'veryheavy');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Gelato OG',40.00,'La Perla', 15, 'azota');
insert into medication
(resource_id,medication_ingredients,medication_type,medication_expdate) values ((SELECT resource_id from resource where resource_id = ‘5’), 'ganja','natural flower','NA');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Taladro brr',140.00,'Carolina', 25, 'suena duro');
insert into tools
(resource_id,tools_type) values ((SELECT resource_id from resource where resource_id = ‘6’), 'power');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Evian',40.00,'Guaynabo', 35, 'hidrata');
insert into water
(resource_id,water_size,water_brand,water_type,water_unitsize)
values ((SELECT resource_id from resource where resource_id = ‘7’),'big','Fiji','liquid','small');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Hot Ice',140.00,'Loiza', 45, 'witchcraft');
Insert into ice (resource_id,ice_size) values ((SELECT resource_id from resource where resource_id=’8’), '12 Oz.' );
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Durakacell ',7.00,'Fajardo', 15, 'azota');
insert into batteries (resource_id,batteries_type,batteries_quantityPerUnit) values((SELECT resource_id from resource where resource_id=’9’),'AA',8);
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Camisa linda',15.00,'Ponce', 45, 'buena tela');
insert into clothing (resource_id,clothing_size,clothing_color,clothing_gender,clothing_material) values ((SELECT resource_id from resource where resource_id =’10’), 'M','Blue','M','Cotton');
insert into request()
      "|psql almacen -U alma -W -h 127.0.0.1 ;
