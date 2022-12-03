import os 
import sys
import pandas as pd 
import sqlalchemy

#solicitando o arquivo para outro 
sys.path.append('..')
# construindo os path do caminho
FILE_DIR = os.path.dirname( os.path.abspath(__file__) )
DATA_DIR = os.path.join( FILE_DIR, 'data' )

# string de conexeção ao banco de dados com renomeação
str_conetion = 'sqlite:///{path}'
str_conetion =  str_conetion.format( path=os.path.join( DATA_DIR,  'cardio.db') )
conetion = sqlalchemy.create_engine( str_conetion )



# 1 opção
filenames = [ f for f in os.listdir(DATA_DIR) if f.endswith('.csv') ]

# 2 opção
for f in filenames:
    df_tmp = pd.read_csv( os.path.join( DATA_DIR, f ) )
    table_name =  'tb_cardio' + f.replace( 'CardioGoodFitness', '' ).strip('.csv')
    df_tmp.to_sql( table_name, conetion )
    
    
