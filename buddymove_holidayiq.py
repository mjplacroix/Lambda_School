from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')

print(df.shape)


df.to_sql('buddymove_holidayiq', con=engine)
engine.execute("SELECT * FROM buddymove_holidayiq").fetchall()