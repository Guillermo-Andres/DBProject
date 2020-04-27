#!/usr/bin/env bash

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
echo created user:"alma"  db:"almacen" and granted db to usr  ;
cd /;
sudo etc/init.d/postgresql restart ;
echo "create table consumer(cid serial primary key);
      create table places_an_order(placesID serial primary key , cid integer references consumer (cid))" | psql almacen -U alma -W -h 127.0.0.1 ;
echo" finished db , added table of tables.txt"




