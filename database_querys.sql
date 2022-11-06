create database myBank;

CREATE TABLE clients(Name CHAR(20), CardNumber int(15), Pin int(10), BankAccount VARCHAR (20), Balance int(20));

INSERT INTO clients VALUES('Jhon', 012345, 1234, 'ES-22334455', 10000);
INSERT INTO clients VALUES('Mary', 98765, 981, 'ES-9864675', 10000);

ALTER table clients ADD PRIMARY KEY(CardNumber);
