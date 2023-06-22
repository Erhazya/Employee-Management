from faker import Faker
import random
import mysql.connector




fake = Faker("fr_FR")

id_em = random.randint(100000,999999)
name = fake.last_name()
firstname = fake.first_name()
phone = fake.phone_number()
address = fake.address()
diplome = random.choice([True,False])
salary = random.randint(2000,5000)


print(id_em)
print(name)
print(firstname)
print(phone)
print(address)
print(diplome)
print(salary)



config = {
        'user': 'admin',
        'password': 'Azertyuiop$1',
        'host': '109.89.241.235',
        'port': '3306',
        'database': 'Employes_Informations',
        'raise_on_warnings': True
    }

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

query = "INSERT INTO employes (id,name,firstname,phone,address,diplome,salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"

values = (id_em, name, firstname, phone, address, diplome, salary)



cursor.execute(query, values)


conn.commit()

cursor.close()
conn.close()


