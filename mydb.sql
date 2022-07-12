create table users
(
    user_id  int auto_increment
        primary key,
    email    varchar(50) not null,
    username varchar(20) not null,
    password varchar(20) not null,
    constraint users_email_uindex
        unique (email),
    constraint users_user_id_uindex
        unique (user_id)
);

INSERT INTO db.users (user_id, email, username, password) VALUES (2, 'Shir@gmail.com', 'Shir', 'Shir12345');
INSERT INTO db.users (user_id, email, username, password) VALUES (3, 'Yossi@gmail.com', 'Yossi', 'Yossi12345');
INSERT INTO db.users (user_id, email, username, password) VALUES (5, 'Ben@gmail.com', 'Ben', 'Ben12345');
INSERT INTO db.users (user_id, email, username, password) VALUES (6, 'Noam@gmail.com', 'Noam', 'Noam12345');
INSERT INTO db.users (user_id, email, username, password) VALUES (7, 'Adi@gmail.com', 'Adi', 'Adi12345');



create table contact
(
    id        int auto_increment
        primary key,
    name      varchar(20)  not null,
    email     varchar(50)  not null,
    phone_num varchar(20)  null,
    rate      int          null,
    content   varchar(300) not null,
    constraint contact_id_uindex
        unique (id)
);

INSERT INTO db.contact (id, name, email, phone_num, rate, content) VALUES (1, 'Pelegel', 'peleg2805@walla.com', '', 5, 'afsv');
INSERT INTO db.contact (id, name, email, phone_num, rate, content) VALUES (2, 'Pelegel', 'pelegel@post.bgu.ac.il', '052-5839021', 5, 'gfdd');
INSERT INTO db.contact (id, name, email, phone_num, rate, content) VALUES (3, 'vazsha', 'peleg2805@walla.com', '', 5, 'jjjijpo');
INSERT INTO db.contact (id, name, email, phone_num, rate, content) VALUES (4, 'Pelegel', 'pelegel@post.bgu.ac.il', '052-5839021', 5, 'great website!');




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
