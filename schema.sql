CREATE TABLE user_profiles(
    id serial,
    firstname varchar(20),
    lastname varchar(20),
    age int,
    gender varchar(6),
    bio varchar(200),
    profpic varchar(200),
    username varchar(20),
    date_created date,
    primary key (id)
);
Grant All privileges on table user_profiles to public;
grant usage, select on sequence user_profiles_id_seq to proj1;