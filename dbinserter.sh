#!/usr/bin/env bash
echo "
insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Alma', 'Colon', '19ene89', 'ciales', '78787878', 'alma@hotmail.com');
insert into supplier(person_id) values (2);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Robert', 'Ruiz', '25dec56', 'dubai', '363636', 'rr@gmail.com');
insert into supplier(person_id) values (3);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Pablo', 'Escobar', '6junio66', 'Colombia', '123123123', 'pabloescobar@plakaplaka.com');
insert into supplier(person_id) values (4);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Tuto', 'Valle', '29ene54', 'Dinamarca', '123123123', 'tuto@peace.com');
insert into supplier(person_id) values (5);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Diego', 'Rivera', '30nov78', 'Ponce', '11223344', 'tuto@peace.com');
insert into consumer(person_id, consumer_severety) values (6, 'high');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Darth', 'Vader', '08ago73', 'hawaii', '1414141', 'thefather@darkside.com');
insert into consumer(person_id, consumer_severety) values (7, 'moderate');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Tom', 'Shelby', '12march12', 'England', '456456', 'ts@pb.com');
insert into consumer(person_id, consumer_severety) values (8, 'high');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Rebeca', 'Diaz', '11jul73', 'NY', '987987', 'becky73@yahoo.com');
insert into consumer(person_id, consumer_severety) values (9, 'low');


insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Luz', 'Verde', '18oct65', 'Hormigueros', '77887788', 'lucy@yahoo.com');
insert into consumer(person_id, consumer_severety) values (10, 'low');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Yvy', 'Queen', '19-04-78', 'dorado', '123456', 'yq@hotmail.com');
insert into admin(person_id) values (11);


insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Kike', 'Li', '29-10-68', 'SJ', '147852369', 'kl@hotmail.com');
insert into admin(person_id) values (12);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Michael', 'Scott', '14-08-60', 'Scranton', '123456', 'ms@dundermifflin.com');
insert into admin(person_id) values (13);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('guanda', 'basket', '02-02-56', 'fortaleza', '123456', 'gb@corrupcion.com');
insert into admin(person_id) values (14);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Robby', 'Cruz', '11-17-60', 'Humacao', '123123', 'robby@admin.com');
insert into admin(person_id) values (15);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Pedro', 'Albizu', '03feb45', 'Ponce', '123456', 'albizu@libertad.com');
insert into supplier(person_id) values (16);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('flor', 'rosario', '03jun45', 'Caguas', '123456', 'albizu@libertad.com');
insert into supplier(person_id) values (17);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Miguel', 'Castro', '16ene33', 'Arroyo', '123456', 'miguel@gmail.com');
insert into supplier(person_id) values (18);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Ana', 'Rivera', '09sept55', 'Cabo Rojo', '123456', 'ana@velvet.com');
insert into supplier(person_id) values (19);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Chuck', 'Bass', '11oct63', 'Ponce', '123456', 'albizu@libertad.com');
insert into supplier(person_id) values (20);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Blair', 'Waldorf', '30nov78', 'Lajas', '147852', 'bw@gg.com');
insert into consumer(person_id, consumer_severety) values (21, 'high');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Eduardo', 'Castro', '14feb36', 'Camuy', '11223344', 'edu@yahoo.com');
insert into consumer(person_id, consumer_severety) values (22, 'low');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Amanda', 'Miguel', '13ago54', 'Barranquitas', '11223344', 'amandamiguel@gmail.com');
insert into consumer(person_id, consumer_severety) values (23, 'moderate');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Micky', 'Woods', '15dec48', 'Ciales', '11223344', 'mickywood@perreo.com');
insert into consumer(person_id, consumer_severety) values (24, 'high');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Nata', 'Niel', '19jul03', 'Moca', '11223344', 'nataniel@gmail.com');
insert into consumer(person_id, consumer_severety) values (25, 'low');

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Ricky', 'Rose', '11-17-60', 'Vieques', '123123', 'ricky@puerco.com');
insert into admin(person_id) values (26);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Mario', 'Party', '13oct51', 'Humacao', '123123', 'robby@admin.com');
insert into admin(person_id) values (27);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Tito', 'Kayak', '28ene89', 'Bayamon', '123123', 'titokayak@gmail.com');
insert into admin(person_id) values (28);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Serena', 'Li', '04may78', 'Barceloneta', '123123', 'serena@ues.com');
insert into admin(person_id) values (29);

insert into person (person_firstname, person_lastname, person_dob, person_address, person_phone_number, person_email) values ('Jenny', 'Humphrey', '12-06-75', 'San Lorenzo', '123123', 'jh@yahoo.com');
insert into admin(person_id) values (30);

Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('skyhighbannanas',24.99,'Luquillo', 10, '300mg edible');
insert into babyFood(resource_id,babyFood_type,babyFood_is_perishable,babyFood_ingrendients,babyFood_unitsize,babyFood_expDate) values ( (SELECT resource_id from resource where resource_id = '1'),'gerber',TRUE,'bannana,ganja',10,'12-12-2024');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('skyhighbannanas',24.99,'Luquillo', 10, '300mg edible');
insert into babyFood(resource_id,babyFood_type,babyFood_is_perishable,babyFood_ingrendients,babyFood_unitsize,babyFood_expDate) values ( (SELECT resource_id from resource where resource_id = '2'),'gerber',TRUE,'bannana,ganja',10,'12-12-2024');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('skyhighbannanas',24.99,'Luquillo', 10, '300mg edible');
insert into babyFood(resource_id,babyFood_type,babyFood_is_perishable,babyFood_ingrendients,babyFood_unitsize,babyFood_expDate) values ( (SELECT resource_id from resource where resource_id = '3'),'gerber',TRUE,'bannana,ganja',10,'12-12-2024');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Salch',4.99,'Luquillo', 10, 'saben fo');
insert into cannedFood(resource_id,cannedFood_type,cannedFood_is_perishable,cannedFood_ingrendients,cannedFood_unitsize,cannedFood_expDate) values ( (SELECT resource_id from resource where resource_id = '2'),'Carmela',TRUE,'no vaca,no pork',10,'12-12-2024');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('beef jerky',7.99,'Caguas', 10, 'saben cool');
insert into dryFood(resource_id,dryFood_type,dryFood_is_perishable,dryFood_ingrendients,dryFood_unitsize,dryFood_expDate) values ( (SELECT resource_id from resource where resource_id = '3'),'Wills',FALSE,' vaca, pork',10,'12-12-2024');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('heavy stuff',179.99,'Caguas', 15, 'puff pass');
insert into heavyEquipment (resource_id,heavyequipment_type) values( (SELECT resource_id from resource where resource_id = '4'),'veryheavy');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Gelato OG',40.00,'La Perla', 15, 'azota');
insert into medication
(resource_id,medication_ingredients,medication_type,medication_expdate) values ((SELECT resource_id from resource where resource_id = 5), 'ganja','natural','NA');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Taladro brr',140.00,'Carolina', 25, 'suena duro');
insert into tools
(resource_id,tools_type) values ((SELECT resource_id from resource where resource_id = 6), 'power');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Evian',40.00,'Guaynabo', 35, 'hidrata');
insert into water
(resource_id,water_size,water_brand,water_type,water_unitsize)
values ((SELECT resource_id from resource where resource_id = 7),'big','Fiji','liquid','small');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Hot Ice',140.00,'Loiza', 45, 'witchcraft');
Insert into ice (resource_id,ice_size) values ((SELECT resource_id from resource where resource_id=8), '12 Oz.' );
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Durakacell ',7.00,'Fajardo', 15, 'azota');
insert into batteries (resource_id,batteries_type,batteries_quantityPerUnit) values((SELECT resource_id from resource where resource_id=9),'AA',8);
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Camisa linda',15.00,'Ponce', 45, 'buena tela');
insert into clothing (resource_id,clothing_size,clothing_color,clothing_gender,clothing_material) values ((SELECT resource_id from resource where resource_id ='10'), 'M','Blue','M','Cotton');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Gasolina',15.00,'Ponce', 45, 'jode motor');
insert into fuel (resource_id, fuel_type) values((SELECT resource_id from resource where resource_id ='11'), 'Liquid');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Marcapaso',285.00,'Maya', 80, 'guillo need');
insert into medicalDevices (resource_id,medicaldevices_type) values ((SELECT resource_id
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values(‘ToallaS’,10.00,'Ponce', 45, ‘esencial’);
insert into hygiene (resource_id,hygiene_quantityperunit,hygiene_brand)
((select resource_id from resource where resource_id=''),13,'Nosotras');
Insert into resource (resource_name,resource_price,resource_location,resource_quantity,resource_description) values('Paneles',150.00,'JTokyo', 45, 'bueno');
insert into powergenerator (resource_id,powergenerator_type) values ((SELECT resource _id from resource where resource_id='14'),'Planta');

      "|psql almacen -U alma -W -h 127.0.0.1 ;
