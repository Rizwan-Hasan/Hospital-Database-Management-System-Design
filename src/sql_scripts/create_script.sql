/* Database Creation */
CREATE DATABASE IF NOT EXISTS HospitalDB;

/* Use 'HospitalDB' database for query execution */
USE HospitalDB;

/*
 Creation Starts
 */

/* Creating 'Referral' Table */
CREATE TABLE IF NOT EXISTS Referral
(
    ref_id  INTEGER(5)  NOT NULL,
    doctor  VARCHAR(25) NOT NULL,
    details VARCHAR(100)
);

/* Creating 'Patient' Table */
CREATE TABLE IF NOT EXISTS Patient
(
    patient_id INTEGER(5)  NOT NULL,
    ref_id     INTEGER(5)  NOT NULL,
    name       VARCHAR(25) NOT NULL,
    sex        VARCHAR(6)  NOT NULL,
    address    VARCHAR(50)
);


/* Creating 'Procedure' Table */
CREATE TABLE IF NOT EXISTS `Procedure`
(
    procedure_id INTEGER(5) NOT NULL,
    ref_id       INTEGER(5) NOT NULL,
    patient_id   INTEGER(5) NOT NULL,
    cost         INTEGER(5) NOT NULL,
    result       VARCHAR(50)
);

/* Creating 'Bill' Table */
CREATE TABLE IF NOT EXISTS Bill
(
    bill_id      INTEGER(5) NOT NULL,
    procedure_id INTEGER(5) NOT NULL,
    patient_id   INTEGER(5) NOT NULL,
    ref_id       INTEGER(5) NOT NULL,
    total_cost   INTEGER(5) NOT NULL,
    bill_date    DATE
);

/*
 Primary Key, Foreign Key and Constraints adding
 */

/* Adding Primary Key on 'Referral' Table */
ALTER TABLE Referral
    ADD CONSTRAINT PK_ref_id
        PRIMARY KEY (ref_id);

/* Adding Primary Key 'Patient' Table */
ALTER TABLE Patient
    ADD CONSTRAINT PK_patient_id
        PRIMARY KEY (patient_id, ref_id);

/* Adding Primary Key on 'Procedure' Table */
ALTER TABLE `Procedure`
    ADD CONSTRAINT PK_procedure_id
        PRIMARY KEY (procedure_id);

/* Adding Primary Key on 'Bill' Table */
ALTER TABLE Bill
    ADD CONSTRAINT PK_bill_id
        PRIMARY KEY (bill_id);

/*
 Relation Making Between Tables
 */

/* Adding Primary Key of 'Referral' table as Foreign Key in 'Patient' table */
ALTER TABLE Patient
    ADD CONSTRAINT FK_ref_id_PATIENT
        FOREIGN KEY (ref_id)
            REFERENCES Referral (ref_id)
            ON DELETE CASCADE;

/* Adding Primary Key of 'Referral' table as Foreign Key in 'Procedure' table */
ALTER TABLE `Procedure`
    ADD CONSTRAINT FK_ref_id_PROCEDURE
        FOREIGN KEY (ref_id)
            REFERENCES Referral (ref_id)
            ON DELETE CASCADE;

/* Adding Primary Key of 'Patient' table as Foreign Key in 'Procedure' table */
ALTER TABLE `Procedure`
    ADD CONSTRAINT FK_patient_id_PROCEDURE
        FOREIGN KEY (patient_id, ref_id)
            REFERENCES Patient (patient_id, ref_id)
            ON DELETE CASCADE;

/* Adding Primary Key of 'Procedure' table as Foreign Key in 'Bill' table */
ALTER TABLE Bill
    ADD CONSTRAINT FK_procedure_id_BILL
        FOREIGN KEY (procedure_id)
            REFERENCES `Procedure` (procedure_id)
            ON DELETE CASCADE;

/* Adding Primary Key of 'Patient' table as Foreign Key in 'Bill' table */
ALTER TABLE Bill
    ADD CONSTRAINT FK_patient_id_BILL
        FOREIGN KEY (patient_id, ref_id)
            REFERENCES Patient (patient_id, ref_id)
            ON DELETE CASCADE;
/*
 End of Query
 */
