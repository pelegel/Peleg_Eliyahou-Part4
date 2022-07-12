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
