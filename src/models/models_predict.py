import os 
import sys
import pandas as pd 
import sqlalchemy



file_dir = os.path.dirname( os.path.dirname( os.path.abspath(__file__)  ) )
data_dir = os.path.join( file_dir , 'data' )
db_one =  os.path.join( data_dir, 'cardio.db' )

# string de conexção
str_conetion = 'sqlite:///{path}'
str_conetion =  str_conetion.format( path=os.path.join( data_dir,  'cardio.db') )
conetion = sqlalchemy.create_engine( str_conetion )

# querys especif. para pandas 
sql_query = pd.read_sql_query(
    """
        SELECT *
        
        FROM tb_cardio
    """,
    conetion
    
)

df =  pd.DataFrame(  sql_query )
print(df.head())