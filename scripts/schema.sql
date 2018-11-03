create table "users" (
    "id"                serial          not null,
    "username"          varchar(50)     not null,
    "password"          varchar(50)     not null
);

alter table "users"
    add constraint "pk_users"
    primary key ("id");
