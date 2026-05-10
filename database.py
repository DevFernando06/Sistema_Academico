""""
AV3

(dependencia postgreSQl) : pip install psycopg2-binary 

"""

import psycopg2

try:
    conn = psycopg2.connect(
        dbname='',
        user='',
        password='',
        host='localhost',
        port='5432'
    )
    print("Conectou")
except Exception as e:
    print(e)