import os 
import sys
import pandas as pd 
import dataframe_image 
import sqlalchemy
import matplotlib.pyplot as plt 


from pandas.plotting import table




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

# Mostrando o data set Geral
def dataset_all():
    dataframeone = df
    ax = plt.subplot(111, frame_on=True)
    ax.xaxis.set_visible(False)  
    ax.yaxis.set_visible(False) 

    table(ax, df)
    
    plt.savefig('dataframe.png')
    

dataset_all()



# Descrição completa com média e desvio padrão
def describe_dataset():
    analyzer = df.describe().T
    df_std = pd.DataFrame(analyzer)
    
    print(df_std)

    
    
# describe_dataset()