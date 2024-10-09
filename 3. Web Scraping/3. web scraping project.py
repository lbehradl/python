import mysql.connector
import mysql.connector.errorcode
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

count=0
for country in countries:
    country_name= country.find('h3', attrs={'class':'country-name'})
    country_capital=country.find('span', attrs={'class':'country-capital'})
    country_population = country.find('span', attrs={'class':'country-population'})
    country_area = country.find('span', attrs={'class':'country-area'})

    cursor.execute('INSERT INTO Countries (Name, Capital, Population, Area) VALUES (%s, %s, %s, %s)',(country_name.text.strip(), country_capital.text.strip(), country_population.text.strip(), country_area.text.strip()))

    count+=1
    if count >=20:
        break

cnx.commit()
cursor.close()
cnx.close()
