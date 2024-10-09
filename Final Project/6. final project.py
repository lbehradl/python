import mysql.connector
import requests
from bs4 import BeautifulSoup
from mysql.connector import errorcode

username = input('username: ')
password = input('password: ')
database = input('your database name :')

cnx = mysql.connector.connect(user=username,
                              password=password)

cursor=cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(f'CREATE DATABASE {database}')
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)


try:
    cursor.execute(f'USE {database}')

except mysql.connector.Error as err:
    print(f'database {database} does not exist')
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print(f'database {database} created successfully')
        cnx.database = database
    else:
        print(err)
        exit(1)

try:
    print("Creating table Countries")

    cursor.execute('''CREATE TABLE `Countries` (Name VARCHAR(255), 
                                    Capital VARCHAR(255),
                                    Population INT(15),
                                    Area FLOAT(15,1))''')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("already exists.")
    else:
        print(err.msg)
else:
    print("Table created successfully")


req = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(req.text , 'html.parser')
countries = soup.find_all('div', attrs={'class':'col-md-4 country'})

for country in countries:
    country_name= country.find('h3', attrs={'class':'country-name'})
    country_capital=country.find('span', attrs={'class':'country-capital'})
    country_population = country.find('span', attrs={'class':'country-population'})
    country_area = country.find('span', attrs={'class':'country-area'})

    cursor.execute('INSERT INTO Countries (Name, Capital, Population, Area) VALUES (%s, %s, %s, %s)',(country_name.text.strip(), country_capital.text.strip(), country_population.text.strip(), country_area.text.strip()))

cnx.commit()

import pandas as pd

df = pd.read_sql('SELECT * FROM Countries', cnx)
cursor.close()
cnx.close()

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = df[['Population']]
y = df[['Area']]

x_train, x_test, y_train, y_test = train_test_split(x, y)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

plt.scatter(x_test, y_test, color='blue', label='Actual')
plt.scatter(x_test, y_pred, color='red', label='Predicted')
plt.xlabel('Population')
plt.ylabel('Area')
plt.show()

