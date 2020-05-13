#!/usr/bin/env bash
echo "
insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Fabi', 'Bad', '14may98', 'Quebradillas', '123456', 'fbr@yahoo.com');
insert into supplier(person_id) values (1);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Alma', 'Colon', '19ene89', 'Ciales', '78787878', 'alma@hotmail.com');
insert into supplier(person_id) values (2);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Robert', 'Ruiz', '25dec56', 'Ponce', '363636', 'rr@gmail.com');
insert into supplier(person_id) values (3);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Pablo', 'Escobar', '6junio66', 'San Sebastian', '123123123', 'pabloescobar@plakaplaka.com');
insert into supplier(person_id) values (4);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Tuto', 'Valle', '29ene54', 'Barranquitas', '123123123', 'tuto@peace.com');
insert into supplier(person_id) values (5);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Diego', 'Rivera', '30nov78', 'Ponce', '11223344', 'tuto@peace.com');
insert into consumer(person_id, consumer_severety) values (6, 'high');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Darth', 'Vader', '08ago73', 'Fajardo', '1414141', 'thefather@darkside.com');
insert into consumer(person_id, consumer_severety) values (7, 'moderate');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Tom', 'Shelby', '12march12', 'Lajas', '456456', 'ts@pb.com');
insert into consumer(person_id, consumer_severety) values (8, 'high');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Rebeca', 'Diaz', '11jul73', 'Quebradillas', '987987', 'becky73@yahoo.com');
insert into consumer(person_id, consumer_severety) values (9, 'low');


insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Luz', 'Verde', '18oct65', 'Hormigueros', '77887788', 'lucy@yahoo.com');
insert into consumer(person_id, consumer_severety) values (10, 'low');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Yvy', 'Queen', '19-04-78', 'Coamo', '123456', 'yq@hotmail.com');
insert into admin(person_id) values (11);


insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Kike', 'Li', '29-10-68', 'Morovis', '147852369', 'kl@hotmail.com');
insert into admin(person_id) values (12);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Michael', 'Scott', '14-08-60', 'Camuy', '123456', 'ms@dundermifflin.com');
insert into admin(person_id) values (13);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('guanda', 'basket', '02-02-56', 'San Juan', '123456', 'gb@corrupcion.com');
insert into admin(person_id) values (14);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Robby', 'Cruz', '11-17-60', 'Humacao', '123123', 'robby@admin.com');
insert into admin(person_id) values (15);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Pedro', 'Albizu', '03feb45', 'Ponce', '123456', 'albizu@libertad.com');
insert into supplier(person_id) values (16);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('flor', 'rosario', '03jun45', 'Caguas', '123456', 'albizu@libertad.com');
insert into supplier(person_id) values (17);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Miguel', 'Castro', '16ene33', 'Arroyo', '123456', 'miguel@gmail.com');
insert into supplier(person_id) values (18);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Ana', 'Rivera', '09sept55', 'Cabo Rojo', '123456', 'ana@velvet.com');
insert into supplier(person_id) values (19);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Chuck', 'Bass', '11oct63', 'Ponce', '123456', 'albizu@libertad.com');
insert into supplier(person_id) values (20);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Blair', 'Waldorf', '30nov78', 'Lajas', '147852', 'bw@gg.com');
insert into consumer(person_id, consumer_severety) values (21, 'high');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Eduardo', 'Castro', '14feb36', 'Camuy', '11223344', 'edu@yahoo.com');
insert into consumer(person_id, consumer_severety) values (22, 'low');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Amanda', 'Miguel', '13ago54', 'Barranquitas', '11223344', 'amandamiguel@gmail.com');
insert into consumer(person_id, consumer_severety) values (23, 'moderate');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Micky', 'Woods', '15dec48', 'Ciales', '11223344', 'mickywood@perreo.com');
insert into consumer(person_id, consumer_severety) values (24, 'high');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Nata', 'Niel', '19jul03', 'Moca', '11223344', 'nataniel@gmail.com');
insert into consumer(person_id, consumer_severety) values (25, 'low');

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Ricky', 'Rose', '11-17-60', 'Vieques', '123123', 'ricky@puerco.com');
insert into admin(person_id) values (26);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Mario', 'Party', '13oct51', 'Humacao', '123123', 'robby@admin.com');
insert into admin(person_id) values (27);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Tito', 'Kayak', '28ene89', 'Bayamon', '123123', 'titokayak@gmail.com');
insert into admin(person_id) values (28);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Serena', 'Li', '04may78', 'Barceloneta', '123123', 'serena@ues.com');
insert into admin(person_id) values (29);

insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values ('Jenny', 'Humphrey', '12-06-75', 'San Lorenzo', '123123', 'jh@yahoo.com');
insert into admin(person_id) values (30);

Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('skyhighbannanas',24.99,'Luquillo', 10, '300mg edible', '2019-12-01');
insert into babyFood(resource_id,babyFood_type,babyFood_is_perishable,babyFood_ingrendients,babyFood_unitsize,babyFood_expDate) values ( (SELECT resource_id from resource where resource_id = '1'),'gerber',TRUE,'bannana,ganja',10,'2019-12-12');

Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('skyhighbannanas',0,'Luquillo', 10, '300mg edible', '2019-12-02');
insert into babyFood(resource_id,babyFood_type,babyFood_is_perishable,babyFood_ingrendients,babyFood_unitsize,babyFood_expDate) values ( (SELECT resource_id from resource where resource_id = '2'),'gerber',TRUE,'bannana,ganja',10,'2019-12-12');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('skyhighbannanas',24.99,'Luquillo', 10, '300mg edible', '2019-12-03');
insert into babyFood(resource_id,babyFood_type,babyFood_is_perishable,babyFood_ingrendients,babyFood_unitsize,babyFood_expDate) values ( (SELECT resource_id from resource where resource_id = '3'),'gerber',TRUE,'bannana,ganja',10,'2019-12-12');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Salch',4.99,'Luquillo', 10, 'saben fo', '2019-12-04');
insert into cannedFood(resource_id,cannedFood_type,cannedFood_is_perishable,cannedFood_ingrendients,cannedFood_unitsize,cannedFood_expDate) values ( (SELECT resource_id from resource where resource_id = '4'),'Carmela',TRUE,'no vaca,no pork',10,'2019-12-12');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('beef jerky',7.99,'Caguas', 10, 'saben cool', '2019-12-05');
insert into dryFood(resource_id,dryFood_type,dryFood_is_perishable,dryFood_ingrendients,dryFood_unitsize,dryFood_expDate) values ( (SELECT resource_id from resource where resource_id = '5'),'Wills',FALSE,' vaca, pork',10,'2019-12-12');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('heavy stuff',179.99,'Caguas', 15, 'puff pass', '2019-12-06');
insert into heavyEquipment (resource_id,heavyequipment_type) values( (SELECT resource_id from resource where resource_id = '6'),'veryheavy');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Gelato OG',40.00,'La Perla', 15, 'azota', '2019-12-07');
insert into medication
(resource_id,medication_ingredients,medication_type,medication_expdate) values ((SELECT resource_id from resource where resource_id = 7), 'ganja','natural','NA');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Taladro brr',140.00,'Carolina', 25, 'suena duro', '2019-12-08');
insert into tools
(resource_id,tools_type) values ((SELECT resource_id from resource where resource_id = 8), 'power');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Evian',40.00,'Guaynabo', 35, 'hidrata', '2019-12-09');
insert into water
(resource_id,water_size,water_brand,water_type,water_unitsize)
values ((SELECT resource_id from resource where resource_id = 9),'big','Fiji','liquid','small');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Hot Ice',140.00,'Loiza', 45, 'witchcraft', '2019-12-10');
Insert into ice (resource_id,ice_size) values ((SELECT resource_id from resource where resource_id=10), '12 Oz.' );
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Durakacell ',7.00,'Fajardo', 15, 'azota', '2019-12-11');
insert into batteries (resource_id,batteries_type,batteries_quantityPerUnit) values((SELECT resource_id from resource where resource_id=11),'AA',8);
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Camisa linda',15.00,'Ponce', 45, 'buena tela', '2019-12-12');
insert into clothing (resource_id,clothing_size,clothing_color,clothing_gender,clothing_material) values ((SELECT resource_id from resource where resource_id ='12'), 'M','Blue','M','Cotton');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Gasolina',15.00,'Ponce', 45, 'jode motor', '2019-12-13');
insert into fuel (resource_id, fuel_type) values((SELECT resource_id from resource where resource_id ='13'), 'Liquid');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Marcapaso',285.00,'Maya', 80, 'guillo need', '2019-12-14');
insert into medicalDevices (resource_id, medicalDevices_type) values ((SELECT resource_id from resource where resource_id =14),'Electronic');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('ToallaS',10.00,'Ponce', 45, 'esencial', '2019-12-15');
insert into hygiene (resource_id,hygiene_quantityperunit,hygiene_brand) values((select resource_id from resource where resource_id='15'),13,'Nosotras');
Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values('Paneles',150.00,'Tokyo', 45, 'bueno', '2019-12-16');
insert into powerGenerator (resource_id,powerGenerator_type) values ((SELECT resource_id from resource where resource_id = '16'),'Planta');


insert into request(resource_id , request_date) values (4 ,'2019-11-11');
insert into makesRequest(consumer_id , request_id) values (3 , 1);
insert into supplies(supplier_id , resource_id) values(5,4);
insert into paymentMethod (paymentMethod_type , consumer_id) values ('cash' , 3);
insert into orders(order_amount ,  order_date , order_status , supplier_id , resource_id) values((select resource_price from resource where resource_id = 4) , '2019-12-12', 'complete' , 5 , 4);
insert into paysFor(paymentMethod_id , order_id) values (1,1);

insert into request(resource_id , request_date) values (2 ,'2019-10-15');
insert into makesRequest(consumer_id , request_id) values (4 , 2);
insert into supplies(supplier_id , resource_id) values(7,2);
insert into paymentMethod (paymentMethod_type , consumer_id) values ('visa' , 4);
insert into orders(order_amount ,  order_date , order_status , supplier_id , resource_id) values((select resource_price from resource where resource_id = 2) , '2019-12-12', 'complete' , 7 , 2);
insert into paysFor(paymentMethod_id , order_id) values (2,2);

insert into request(resource_id , request_date) values (7 ,'2019-12-12');
insert into makesRequest(consumer_id , request_id) values (4 , 3);
insert into supplies(supplier_id , resource_id) values(8,7);
insert into orders(order_amount ,  order_date , order_status , supplier_id, resource_id) values((select resource_price from resource where resource_id = 7) , '2019-12-12', 'complete' , 8 , 7 );
insert into paysFor(paymentMethod_id , order_id) values (2,3);

insert into request(resource_id , request_date) values (1 ,'2019-10-16');
insert into makesRequest(consumer_id , request_id) values (4 , 4);
insert into supplies(supplier_id , resource_id) values(8,1);
insert into orders(order_amount ,  order_date , order_status , supplier_id, resource_id) values((select resource_price from resource where resource_id = 1) , '2019-12-12', 'complete' , 8 , 1);
insert into paysFor(paymentMethod_id , order_id) values (2,4);

create or replace function get_region(person_city varchar(30)) returns varchar(30) as \$$
          begin
              if (person_city = 'San Juan' or person_city = 'Guaynabo' or person_city = 'Aguas Buenas') then
	                return 'San Juan';
              elsif (person_city = 'Bayamon' or person_city = 'Catano' or person_city = 'Toa Baja' or person_city = 'Toa Alta') then
	                return 'Bayamon';
              elsif (person_city = 'Arecibo' or person_city = 'Barceloneta' or person_city = 'Camuy' or person_city = 'Ciales' or person_city = 'Dorado' or person_city = 'Florida' or person_city = 'Hatillo' or person_city = 'Manati' or person_city = 'Morovis' or person_city = 'Quebradillas' or person_city = 'Vega Alta' or person_city = 'Vega Baja') then
	                return 'Arecibo';
              elsif (person_city = 'Aguada' or person_city = 'Aguadilla' or person_city = 'Anasco' or person_city = 'Cabo Rojo' or person_city = 'Hormigueros' or person_city = 'Isabela' or person_city = 'Las Marias' or person_city = 'Mayaguez' or person_city = 'Moca' or person_city = 'Rincon' or person_city = 'San German' or person_city = 'San Sebastian') then
	                return 'Aguadilla';
              elsif (person_city = 'Adjuntas' or person_city = 'Guanica' or person_city = 'Guayanilla' or person_city = 'Jayuya' or person_city = 'Lajas' or person_city = 'Lares' or person_city = 'Maricao' or person_city = 'Penuelas' or person_city = 'Ponce' or person_city = 'Sabana Grande' or person_city = 'Utuado' or person_city = 'Yauco' or person_city = 'Juana Diaz') then
	                return 'Ponce';
              elsif (person_city = 'Arroyo' or person_city = 'Aibonito' or person_city = 'Barranquitas' or person_city = 'Cayey' or person_city = 'Cidra' or person_city = 'Coamo' or person_city = 'Comerio' or person_city = 'Corozal' or person_city = 'Guayama' or person_city = 'Juana Diaz' or person_city = 'Naranjito' or person_city = 'Orocovis' or person_city = 'Salinas' or person_city = 'Santa Isabel' or person_city = 'Villalba') then
	                return 'Guayama';
              elsif (person_city = 'Caguas' or person_city = 'Gurabo' or person_city = 'Humacao' or person_city = 'Juncos' or person_city = 'Las Piedras' or person_city = 'Maunabo' or person_city = 'Naguabo' or person_city = 'Patillas' or person_city = 'San Lorenzo' or person_city = 'Yabucoa') then
	                return 'Humacao';
              elsif (person_city = 'Canovanas' or person_city = 'Carolina' or person_city = 'Ceiba' or person_city = 'Culebra' or person_city = 'Fajardo' or person_city = 'Loiza' or person_city = 'Luquillo' or person_city = 'Rio Grande' or person_city = 'Trujillo Alto' or person_city = 'Vieques' ) then
	                return 'Carolina';
              else
                	return 'Cannot determine region';
              end if;
          end;
          \$$ language plpgsql;


"|psql almacen -U alma -W -h 127.0.0.1 ;

