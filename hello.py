import django
import sqlite3

print("hello");
print(django.get_version());

print(sqlite3.version) # sqlite_version_info)

con = sqlite3.connect("./mysite/db.sqlite3");
cur = con.cursor()

v_sql = "SELECT * FROM sqlite_master WHERE type='table';"
for row in cur.execute( v_sql ):
    print( row );

con.close()
