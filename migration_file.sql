CREATE TABLE if not exists settelements
(
settelement_id integer NOT NULL,
settelement_name varchar(128) NOT NULL
);

CREATE TABLE if not exists streets
(
street_id integer NOT NULL PRIMARY KEY,
street_name varchar(128) NOT NULL
);

CREATE TABLE if not exists addresses
(
address_id NOT NULL PRIMARY KEY,
region varchar(128),
settlement varchar (128),
streets varchar (128),
house varchar (128)
post code integer(5)
);