#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

#------------------------------------------------------------
# Database: immobilier_recherche
#------------------------------------------------------------

CREATE DATABASE immobilier_recherche;
USE immobilier_recherche;

#------------------------------------------------------------
# Table: quartier
#------------------------------------------------------------

CREATE TABLE quartier(
        nom Varchar (50) NOT NULL
	,CONSTRAINT quartier_PK PRIMARY KEY (nom)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: ville
#------------------------------------------------------------

CREATE TABLE ville(
        nom Varchar (50) NOT NULL
	,CONSTRAINT ville_PK PRIMARY KEY (nom)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: ville_quartier
#------------------------------------------------------------

CREATE TABLE ville_quartier(
        nom          Varchar (50) NOT NULL ,
        nom_quartier Varchar (50) NOT NULL ,
        prix         Float NOT NULL
	,CONSTRAINT ville_quartier_PK PRIMARY KEY (nom,nom_quartier)

	,CONSTRAINT ville_quartier_ville_FK FOREIGN KEY (nom) REFERENCES ville(nom)
	,CONSTRAINT ville_quartier_quartier0_FK FOREIGN KEY (nom_quartier) REFERENCES quartier(nom)
)ENGINE=InnoDB;