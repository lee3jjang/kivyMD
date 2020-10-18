-- create table todo
create table todo (
    id integer primary key autoincrement,
    contents text not null,
    category text not null,
    is_complete integer not null,
    complete_date text
)

-- todo sample
insert into todo (contents, category, is_complete, complete_date)
values ('공과금내기', '일상', 0, null);
insert into todo (contents, category, is_complete, complete_date)
values ('팔굽혀펴기', '운동', 1, date('2020-10-19'));

