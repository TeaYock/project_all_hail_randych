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