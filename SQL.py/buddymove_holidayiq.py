import pandas
import sqlite3

df = pd.read_csv('buddymove_holidayiq.py')
conn = sqlite3.connect('df')
df.to_sql(name= 'buddymove_holidayiq', index= 'User Id')
curs = conn.cursor()

buddymove_rows = 'SELECT COUNT(*) FROM User Id'
buddy_views_nat_shop = 'SELECT Nature > 100 INNER JOIN SHOPPING > 100 ON User Id'
