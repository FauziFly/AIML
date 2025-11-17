CREATE DATABASE PassportDB
use PassportDB

CREATE TABLE Person (
    PersonId INT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Nationality VARCHAR(50)
)

CREATE TABLE Passport (
    PassportId VARCHAR(20) PRIMARY KEY,
    PersonId INT UNIQUE NOT NULL, 
    PassportNumber VARCHAR(20) UNIQUE NOT NULL,
    IssueDate DATE NOT NULL,
    ExpiryDate DATE NOT NULL,
    -- Defines the Foreign Key relationship
    FOREIGN KEY (PersonId) REFERENCES Person(PersonId)
)

INSERT INTO Person (PersonId, FullName, DateOfBirth, Nationality) VALUES
(101, 'Alex Johnson', '1985-05-15', 'American'),
(102, 'Bala Krishnan', '1992-11-20', 'Malaysian'),
(103, 'Carla Rossi', '1978-01-28', 'Italian'),
(104, 'David Lee', '2000-08-03', 'Canadian'),
(105, 'Emma Dubois', '1965-03-10', 'French'),
(106, 'Fiona Chan', '1998-12-12', 'Singaporean'),
(107, 'George Smith', '1980-04-25', 'British'),
(108, 'Hannah Meyer', '1995-07-07', 'German')

INSERT INTO Passport (PassportId, PersonId, PassportNumber, IssueDate, ExpiryDate) VALUES
('P101', 101, 'A9876543', '2023-01-01', '2028-12-31'),
('P102', 102, 'B1234567', '2020-05-20', '2025-05-19'), -- Expiring soon
('P103', 103, 'C0011223', '2019-10-15', '2029-10-14'),
('P104', 104, 'D5566778', '2024-02-14', '2034-02-13'),
('P105', 105, 'E8765432', '2018-07-01', '2028-06-30'),
('P106', 106, 'F3459871', '2021-03-05', '2026-03-04'),
('P107', 107, 'G2109876', '2022-09-10', '2032-09-09'),
('P108', 108, 'H6543210', '2023-11-01', '2033-10-31')

select * from Person
select * from Passport