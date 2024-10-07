import mysql.connector

user= input('user: ')
password= input('password: ')
database = input('database: ')
table= input('which table you want to sort:')

cnx = mysql.connector.connect(user=user,
                              password =password, 
                              database=database)

cursor = cnx.cursor()

query = f'SELECT name, weight, height FROM {table}'

cursor.execute(query)


data = cursor.fetchall()
data_list = []
for record in data:
    data_list.append(record)

cursor.close()
cnx.close()

sorted_data = sorted(data_list, key=lambda x: (x[2],-x[1]), reverse=True)
for name,weight,height in sorted_data:
    print(name,height,weight)

