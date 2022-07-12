create table recommendations
(
    Artist varchar(20) not null
        primary key,
    Type   varchar(20) not null
);

INSERT INTO db.recommendations (Artist, Type) VALUES ('Anna Zak', 'Female Singer');
INSERT INTO db.recommendations (Artist, Type) VALUES ('Justin Bieber', 'Male Singer');
INSERT INTO db.recommendations (Artist, Type) VALUES ('Lady Gaga', 'Female Singer');
INSERT INTO db.recommendations (Artist, Type) VALUES ('Maroon 5', 'Band');
INSERT INTO db.recommendations (Artist, Type) VALUES ('Mergui', 'Male Singer');
INSERT INTO db.recommendations (Artist, Type) VALUES ('Noa Kiler', 'Female Singer');
INSERT INTO db.recommendations (Artist, Type) VALUES ('One Republic', 'Band');
INSERT INTO db.recommendations (Artist, Type) VALUES ('Taylor Swift', 'Female Singer');
