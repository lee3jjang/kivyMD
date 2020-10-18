create table todo (
    id integer primary key autoincrement,
    contents text not null,
    category text not null,
    is_complete integer not null
)