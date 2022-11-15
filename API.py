!pip install mysql.connector

import numpy as np
import pandas as pd
import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password="", database="World")

city_data = pd.read_sql_query("SELECT * FROM Student&Student Details", )
