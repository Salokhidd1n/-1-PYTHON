import requests
from bs4 import BeautifulSoup
import psycopg2
conn=psycopg2.connect(
    database='erbol',
    user='postgres',
    password='a4',
    host='localhost',
    port='5432'
    )
cur=conn.cursor()
name=[]
years=[]
genre=[]
url="http://kinoteatr.kg/index.php/category/view?id=1"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")



all_class=soup.find_all(class_="text-danger") 

for i in all_class:
    name.append(i.text)
print((name))
R="""create table list_of_films7(
    id serial primary key,
    name_of_films text,
    years_release text,
    genre_type text);"""
cur.execute(R)
# conn.commit()

al_class=soup.find_all(class_="card-text") 
# print(all_class)
l=1
for i in al_class:
    if l==1:
        genre.append(i.text[4:])
        l-=1
    elif l!=1:
        years.append(i.text[3:])
        l+=1
quer='''INSERT INTO list_of_films7(name_of_films,years_release,genre_type)VALUES'''
  
for i in range(0,len(name)):
    quer+=f"""(
        '{name[i]}',
        '{years[i]}',
        '{genre[i]}'),"""
sql_query=quer[:-1]+';'

cur.execute(sql_query)
conn.commit()


cur.close()
conn.close()