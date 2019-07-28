/*
 Creation Starts
 */

/*
 Creating 'Referral' Table
 */
CREATE TABLE Referral
(
    ref_id  NUMBER(5)    NOT NULL,
    doctor  VARCHAR2(25) NOT NULL,
    details VARCHAR2(100)
);

/*
 Adding Primary Key on 'Referral' Table
 */
ALTER TABLE Referral
    ADD CONSTRAINT PK_ref_id
        PRIMARY KEY (ref_id);

/*
 Creating 'Patient' Table
 */
CREATE TABLE Patient
(
    patient_id NUMBER(5)    NOT NULL,
    ref_id     NUMBER(5)    NOT NULL,
    name       VARCHAR2(25) NOT NULL,
    sex        VARCHAR2(6)  NOT NULL,
    phone      VARCHAR2(11) NOT NULL
);

/*
 Adding Primary Key 'Patient' Table
 */
ALTER TABLE Patient
    ADD CONSTRAINT PK_patient_id
        PRIMARY KEY (patient_id);

/*
 Creating 'Procedure' Table
 */
CREATE TABLE Procedure
(
    procedure_id NUMBER(5) NOT NULL,
    ref_id       NUMBER(5) NOT NULL,
    cost         NUMBER(5) NOT NULL,
    result       VARCHAR2(50)
);

/*
 Adding Primary Key on 'Procedure' Table
 */
ALTER TABLE Procedure
    ADD CONSTRAINT PK_procedure_id
        PRIMARY KEY (procedure_id);

/*
 Creating 'Bill' Table
 */
CREATE TABLE Bill
(
    bill_id      NUMBER(5) NOT NULL,
    procedure_id NUMBER(5) NOT NULL,
    patient_id   NUMBER(5) NOT NULL,
    amount       NUMBER(5) NOT NULL,
    bill_date    DATE
);

/*
 Adding Primary Key on 'Bill' Table
 */
ALTER TABLE Bill
    ADD CONSTRAINT PK_bill_id
        PRIMARY KEY (bill_id);

/*
 Relation Making Between Tables
 */

/*
 Adding Primary Key of 'Referral' table as Foreign Key in 'Patient' table
 */
ALTER TABLE Patient
    ADD CONSTRAINT FK_ref_id_PATIENT
        FOREIGN KEY (ref_id)
            REFERENCES Referral (ref_id)
                ON DELETE CASCADE;

/*
 Adding Primary Key of 'Referral' table as Foreign Key in 'Procedure' table
 */
ALTER TABLE Procedure
    ADD CONSTRAINT FK_ref_id_PROCEDURE
        FOREIGN KEY (ref_id)
            REFERENCES Referral (ref_id)
                ON DELETE CASCADE;

/*
 Adding Primary Key of 'Procedure' table as Foreign Key in 'Bill' table
 */
ALTER TABLE Bill
    ADD CONSTRAINT FK_procedure_id_BILL
        FOREIGN KEY (procedure_id)
            REFERENCES Procedure (procedure_id)
                ON DELETE CASCADE;

/*
 Adding Primary Key of 'Patient' table as Foreign Key in 'Bill' table
 */
ALTER TABLE Bill
    ADD CONSTRAINT FK_patient_id_BILL
        FOREIGN KEY (patient_id)
            REFERENCES Patient (patient_id)
                ON DELETE CASCADE;
/*
 End of Query
 */
