# AlmacenesPR

## Introduction
A database application consists of many different areas within the realm of software. Applications are interconnected by various frameworks that allow for quick database management systems to easily provide information to a client. A client is usually a barebones application that can make requests to a server that hosts the database to query the required information. To begin our journey in the realm of database systems we were tasked to employ a mock warehouse management system web application with the help of the python FLASK web framework and a POSTGRESQL database to house the required information.  To begin the preliminary design of the application we were given a list of resources and required operations our system needed to support. From there we needed to develop an E-R diagram of the logical model of our database and develop mock operation handlers to begin the preliminary design of our application. 

## ER-Diagram


![](https://github.com/Guillermo-Andres/DBProject/blob/master/ER.png)

## Entities
### Person
Generalization for all the different users our app will support. It contains contact information such as: name, date-of-birth, address, phone number and email address

### Administrator
Specification user that manages the application. 

### Consumer
Specification of user that uses the application to browse, request or purchase essential resources needed in an emergency.

### Supplier
Specification of user that uses the application to supply one or more types of resources as needed by the consumers.

### Company
Represents the companies that employ the suppliers and provide the resources to be supplied by them.

### Order
Represents the order made by the supplier which supplies the resource being requested by the consumer. It contains the total amount of the order, if the amount is zero the resource is donated (free), else, the resource must be purchased. It also contains the date in which the order was placed and its status. The order status determines if the order is pending confirmation, in process or delivered.

### Request
Represents the request made by a consumer for a specific resource. It contains the date when the request was issued. 

### Payment Method
Represents the payment method used by the consumer to acquire the desired resource. The consumer can pay for the order in cash, debit, credit, via remote payments or if the resource is donated, the payment method is none. 

### Resources
Generalization of the resources to be supplied to the consumers. It contains the resource name, price, the location from where is provided, the quantity, a brief description of the product and a date that states when it became available. If the resource is to be donated, instead of purchased, the price is zero. 

### Water
Specification of resources that represents drinking water. It contains the size (galloned, bottled, etc.), the brand, the type (regular, alkaline, carbonated, etc) and the unit size (number of bottles/gallons per package). 

### Ice
Specification of resources that represents the ice. It contains the size (oz, lbs) of the ice package.

### Canned, Dry, and Baby Food
Specification of resource that represents 3 big ranges of food necessary in disaster sites, canned, dry and baby food. It contains the type (beans, rice, snack bars, etc), if it is perishable, the ingredient list, the unit size (oz, lbs, etc), and the expiration date. 

### Medications
Specification of resource that represents the medications. It contains the name of the medication, the ingredient list, the type of the medication (liquid, tablets, gel capsules, etc), and the expiration date.

### Hygiene
Specification of resource that represents hygiene products. It contains the number of items per package and the brand.

### Clothing
Specification of resource that represents clothing. It contains the size (kids small, adult large, etc), color, gender (women, men, girls, boys), and the material (cotton, polyester, lycra,etc).

### Heavy Equipment
Specification of a resource that represents heavy equipment. It contains the type of equipment. 

### Batteries
Specification of a resource that represents batteries. It contains the type of battery (AA, AAA, DD, etc), and the number of batteries per package. 

### Fuel
Specification of a resource that represents fuel. It contains the type of fuel (regular, premium, diesel, propane gas, etc)

### Tools
Specification of a resource that represents the hand and power tools.  It includes the type of tool (drill, circular saw, etc)

## Relationships 

### Supplier works for company
This relationship associates a supplier with a specific company. The cardinality of this relationship is one-to-many. The company employs multiple suppliers, a supplier works for one company.

### Supplier supplies resources
This relationship associates a supplier with a resource. The cardinality is many to many given that suppliers can supply any number of things and the same resources can be accepted from different suppliers.

### Consumer uses payment method
This relationship associates a consumer with payments methods to be used for paying the order. The cardinality of the relationship is one to many , any consumer can have multiple payments methods.

### Consumer makes a request
This relationship associates a consumer with a request for a desired resource. The cardinality of the relationship is one to many, one consumer can place multiple requests, but a request belongs only to one consumer.

### Supplier submits an order
This relationship associates a supplier and an order. The supplier that supplies the resource requested by the consumer submits an order to be processed. The cardinality of this relationship is one to many, one supplier may submit multiple orders but an order can be submited by one supplier. 

### Payment method pays for order
This relationship associates payment methods with orders. The cardinality is many to many , the same payment method can be used in multiple orders and an order can be fulfilled with multiple payment methods or even none if the order is free.

### Request contains resources
This relationship associates resources with requests. The cardinality is one to one, a resource can be associated to many requests (if the quantity is greater than 1) and a request can have multiple resources.


## Structure of the Code
As stated previously the application is built with the FLASK web framework on top of our machine’s standard IP (127.0.0.1.). It consists of the main application module which houses all of our application’s routes along with the CRUD operations that are required to be operated by each route. We built a database following the ER diagram. For this development phase, we are using dummy data to implement all the GET operations. Handlers were developed for each table on our E-R along with its data access object which is in charge of performing the queries on our database. A set of operations is to be supported, so a distinct route for each operation is necessary. For example, we design a route to view all requested items which is located at @app.route('/almacenespr/requested', methods = ['GET']), in this route we employ the request handler in order to identify requested resources. As for the request table, each table has its specific handler to respond to the operations. 





Universidad de Puerto Rico
Recinto Universitario de Mayagüez
Departamento de Ciencia e Ingeniería de Computación
CIIC 4060 Sistemas de Bases de Datos

Project Phase II - Warehouse Management System: A Case Study
By: Fabiola Badillo, Guillermo Betancourt and Pablo Santiago


## Requirements
You need the following software installed to run this application:
1. PostgreSQL - database engine
2. Pyscopg2 - library to connect to PostgreSQL form Python
3. PgAdmin3 - app to manage the databases
4. Flask - web bases framework to implement the REST API.

Completed 11/30/17
