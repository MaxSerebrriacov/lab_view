create unique index idx_coord on fn_all using btree (x);
refresh materialized view concurrently fn_all;