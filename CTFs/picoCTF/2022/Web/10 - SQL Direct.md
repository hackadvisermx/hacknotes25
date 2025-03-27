# SQL Direct

Connect to this PostgreSQL server and find the flag! `psql -h saturn.picoctf.net -p 56796 -U postgres pico` Password is `postgres`

## Solucion

```
pico=# \c pico
You are now connected to database "pico" as user "postgres".


pico=# \dt
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)


pico=# \d flags
                        Table "public.flags"
  Column   |          Type          | Collation | Nullable | Default 
-----------+------------------------+-----------+----------+---------
 id        | integer                |           | not null | 
 firstname | character varying(255) |           |          | 
 lastname  | character varying(255) |           |          | 
 address   | character varying(255) |           |          | 
Indexes:
    "flags_pkey" PRIMARY KEY, btree (id)


pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_0414477f}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)


```
