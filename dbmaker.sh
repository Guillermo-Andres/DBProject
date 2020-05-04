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
echo "create table person(person_id serial primary key, person_firstname varchar(15), person_lastname varchar(15), person_dob varchar(10), person_address varchar(30), person_phone_number varchar(15), person_email varchar(30));
      create table resource(resource_id serial primary key, resource_name varchar(15), resource_price float, resource_location varchar(30), resource_quantity integer , available boolean, resource_description varchar(25));
      create table request(request_id serial primary key, resource_id integer references resource(resource_id), request_date varchar(10));
      create table consumer(consumer_id serial primary key, person_id integer references person(person_id), consumer_severety varchar(20));
      create table makesRequest(consumer_id integer references consumer(consumer_id), request_id integer references request(request_id), primary key (request_id,consumer_id));
      create table supplier(supplier_id serial primary key, person_id integer references person(person_id));
      create table supplies(supplier_id integer references supplier(supplier_id), resource_id integer references resource(resource_id), primary key (supplier_id, resource_id));
      create table admin(admin_id serial primary key, person_id integer references person(person_id));
      create table company(company_id serial primary key, company_name varchar(15), company_description varchar(20));
      create table worksFor(company_id integer references company(company_id), supplier_id integer references supplier(supplier_id), primary key (company_id, supplier_id));
      create table orders(order_id serial primary key, order_amount float, order_date varchar(10), order_status varchar(10), supplier_id integer references supplier(supplier_id));
      create table paymentMethod(paymentMethod_id serial primary key, paymentMethod_type varchar(10), consumer_id integer references consumer(consumer_id));
      create table paysFor(paymentMethod_id integer references paymentMethod(paymentMethod_id), order_id integer references orders(order_id), primary key (paymentMethod_id, order_id));
      create table water(water_id serial primary key, resource_id integer references resource(resource_id), water_size varchar(10), water_brand varchar(10), water_type varchar(10), water_unitSize varchar(10));
      create table hygiene(hygiene_id serial primary key, resource_id integer references resource (resource_id), hygiene_quantityPerUnit integer, hygiene_brand varchar(10));
      create table babyFood(babyFood_id serial primary key, resource_id integer references resource(resource_id), babyFood_type varchar(10), babyFood_is_perishable boolean, babyFood_ingrendients varchar(50), babyFood_unitSize varchar(10),  babyFood_expDate varchar(10));
      create table dryFood(dryFood_id serial primary key, resource_id integer references resource(resource_id), dryFood_type varchar(10), dryFood_is_perishable boolean, dryFood_ingrendients varchar(50), dryFood_unitSize varchar(10),  dryFood_expDate varchar(10));
      create table cannedFood(cannedFood_id serial primary key, resource_id integer references resource(resource_id), cannedFood_type varchar(10), cannedFood_is_perishable boolean, cannedFood_ingrendients varchar(50), cannedFood_unitSize varchar(10), cannedFood_expDate varchar(10));
      create table heavyEquipment(heavyEquipment_id serial primary key, resource_id integer references resource(resource_id), heavyEquipment_type varchar(10));
      create table medicalDevices(medicalDevices_id serial primary key, resource_id integer references resource(resource_id), medicalDevices_type varchar(10));
      create table medication(medication_id serial primary key, resource_id integer references resource(resource_id), medication_name varchar(10), medication_ingredients varchar(50), medication_type varchar(10), medication_expDate varchar(10));
      create table ice(ice_id serial primary key, resource_id integer references resource(resource_id), ice_size varchar(10));
      create table batteries(batteries_id serial primary key, resource_id integer references resource(resource_id), batteries_type varchar(10), batteries_quantityPerUnit integer);
      create table fuel(fuel_id serial primary key, resource_id integer references resource(resource_id), fuel_type varchar(10));
      create table powerGenerator(powerGenerator_id serial primary key,resource_id integer references resource(resource_id), powerGenerator_type varchar(10));
      create table tools(tools_id serial primary key,resource_id integer references resource(resource_id), tools_type varchar(10));
      create table clothing(clothing_id serial primary key, resource_id integer references resource(resource_id), clothing_size varchar(5), clothing_color varchar(10), clothing_gender varchar(3), clothing_material varchar(10));
      "| psql almacen -U alma -W -h 127.0.0.1 ;
echo "finished db, added table of tables.txt";
