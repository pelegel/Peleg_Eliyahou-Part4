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
