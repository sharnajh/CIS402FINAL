import MySQLdb as mc

conn = mc.connect(host='localhost',
                  user='root',
                  password='Frimize33n',
                  db='menagerie')
c = conn.cursor()

c.execute("SHOW DATABASES")

databases = c.fetchall()

for db in databases:
    print(db[0])

menagerie_exists = False

for db in databases:
    if db[0] == 'menagerie':
        menagerie_exists = True
        break

# If 'menagerie' exists, drop the database
if menagerie_exists:
    c.execute("DROP DATABASE menagerie")

c.execute("CREATE DATABASE IF NOT EXISTS menagerie")

c.execute("DESCRIBE pet")

description = c.fetchall()

for column in description:
    print(column)

file_path = 'pet.txt'  # Replace with the path to your SQL file

with open(file_path, 'r') as sql_file:
    sql_queries = sql_file.read().split(';')  # Split statements based on semicolon
    for query in sql_queries:
        if query.strip():  # Skip empty queries
            c.execute(query)

# Commit changes to the database
conn.commit()

c.execute("SELECT * FROM pet")

pets_data = c.fetchall()

for pet in pets_data:
    print(pet)

c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'")
female_dogs = c.fetchall()
for dog in female_dogs:
    print(dog)

c.execute("SELECT name, birth FROM pet")
birth_data = c.fetchall()
for data in birth_data:
    print(f"Name: {data[0]}, Birth: {data[1]}")

c.execute("SELECT owner, COUNT(*) AS num_pets FROM pet GROUP BY owner")
owner_pets_count = c.fetchall()
for owner, count in owner_pets_count:
    print(f"{owner} has {count} pet(s)")

c.execute("SELECT name, birth, MONTH(birth) FROM pet")
databases = c.fetchall()
for database in databases:
    print(database)