#!/usr/bin/env bash
echo "aaaaa"
echo -n "Do you wish to reinstall postgresql for better perfmance ? [y/n] " ;
read ans
if [[ "y" == "$ans" ]]; then 

    echo "Unistalling postgresqsl for fresh install "
    echo "y" | sudo apt remove --purge postgresql*  > /dev/null 2>&1
    echo
    echo "waiting for reinstall "
    echo
    echo "y" | sudo apt-get install postgresql postgresql-contrib > /dev/null 2>&1
    echo
    echo "Finished fresh install"
fi


cat postInitialize.txt | sudo -i -u postgres ;
echo 
echo
echo created person:"alma"  db:"almacen" and granted db to usr  ;
cd /;
sudo etc/init.d/postgresql restart ;
echo "create table person(person_id serial primary key , person_firstname varchar(15) , person_lastname varchar(15) , person_dob varchar(10) , person_address varchar(30) , person_phone_number varchar(15) , person_email varchar(30) );
      create table resource(rid serial primary key , rprice float , rlocation varchar(30) , rQuantity integer );
      create table supplier(supplier_id serial primary key , person_id integer references person(person_id)) ;
      create table supplies(supplier_id integer references supplier(supplier_id) , rid integer references resource(rid));
      create table admin(admin_id serial primary key , person_id integer references person(person_id));
      create table consumer(consumer_id serial primary key , person_id integer references person(person_id) ,person_severety varchar(20) );
      create table company(company_id serial primary key , company_name varchar(15) , company_description varchar(20));
      create table worksFor(company_id integer references company(company_id) , supplier_id integer references supplier(supplier_id) , primary key (company_id , supplier_id));
      create table request(request_id serial primary key , request_amount float , request_date varchar(10) , request_status varchar(10));
      create table places_an_request(consumer_id integer references consumer(consumer_id) , request_id integer references request(request_id) , primary key (consumer_id , request_id));
      create table paymentMethod(paymentMethod_id serial primary key , paymentMethod_type varchar(10) , consumer_id integer references consumer(consumer_id));
      create table paysFor(paymentMethod_id integer references paymentMethod(paymentMethod_id) , request_id integer references request(request_id) , primary key (paymentMethod_id , request_id));
      create table contains(request_id integer references request(request_id) , rid integer references resource(rid) , primary key (request_id , rid));
      create table water(water_id serial primary key , rid integer references resource(rid) , water_size varchar(10) , water_brand varchar(10) , water_type varchar(10) , water_unit_size varchar(10));
      create table hygiene(hygiene_id serial primary key , rid integer references resource (rid) , hygiene_description varchar(30) , hygiene_quantity_per_unit integer , hygiene_brand varchar(10));
      create table babyfood(babyfood_id serial primary key , rid integer references resource(rid) , babyfood_type varchar(10) , babyfood_is_perishable boolean  , babyfood_ingrendients varchar(50) , babyfood_unit_size varchar(10) , babyfood_description varchar(20) , babyfood_exp_date varchar(10) );
      create table dryfood(dryfood_id serial primary key , rid integer references resource(rid) , dryfood_type varchar(10) , dryfood_is_perishable boolean  , dryfood_ingrendients varchar(50) , dryfood_unit_size varchar(10) , dryfood_description varchar(20) , dryfood_exp_date varchar(10) );
      create table cannedfood(cannedfood_id serial primary key , rid integer references resource(rid) , cannedfood_type varchar(10) , cannedfood_is_perishable boolean  , cannedfood_ingrendients varchar(50) , cannedfood_unit_size varchar(10) , cannedfood_description varchar(20) , cannedfood_exp_date varchar(10) );
      create table heavyEquipment(heavyEquipment_id serial primary key ,  rid integer references resource(rid) ,heavyEquipment_type varchar(10) , heavyEquipment_description varchar(20) );
      create table medicalDevices(medicalDevices_id serial primary key , rid integer references resource(rid) ,medicalDevices_type varchar(10) , medicalDevices_description varchar(20) );
      create table medication( medication_id serial primary key , rid integer references resource(rid) , medication_name varchar(10) , medication_ingredients varchar(50) , medication_type varchar(10) , medication_exp_date varchar(10));
      create table ice(ice_id serial primary key , rid integer references resource(rid) , ice_size varchar(10));
      create table batteries(batteries_id serial primary key , rid integer references resource(rid) , batteries_type varchar(10) , batteries_quantity_per_unit integer);
      create table fuel(fuel_id serial primary key , rid integer references resource(rid) , fuel_type varchar(10));
      create table powerGenerator(powerGenerator_id serial primary key ,rid integer references resource(rid) , powerGenerator_type varchar(10));
      create table tools(tools_id serial primary key ,rid integer references resource(rid) , tools_type varchar(10));
      create table clothing(clothing_id serial primary key , rid integer references resource(rid) , clothing_size varchar(5) , clothing_color varchar(10) , clothing_gender varchar(3) , clothing_material varchar(10) , clothing_description varchar(20));
      "| psql almacen -U alma -W -h 127.0.0.1 ;
echo "finished db , added table of tables.txt";




