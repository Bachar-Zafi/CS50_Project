import json
import csv
from operator import length_hint
import os
import sqlite3
from pathlib import Path
from typing import Dict

connection = sqlite3.connect('MyDataBase.db')
db = connection.cursor()

def table_setup():

    with open('Data/temp.json','r') as f:
        my_data = json.load(f)

    scenario = my_data["scenario"]

    hazards = scenario["hazards"]

    metrics = ["VAR", "Failure_Probability"]

    All_Columns = []

    for metric in metrics:
        for hazard in hazards:
            if hazard=="freeze-thaw": 
                continue
            column_name = hazard+"_"+metric+" float"
            All_Columns.append(column_name)

    query_so_far = ",".join(All_Columns)
    extra_columns = "Asset_TIP float, Asset_VAR float, Asset_Failure_probability float"
    start_columns = "Row_ID integer primary key autoincrement, Asset_ID varchar(50), Year varchar(50)"
    full_query = f"create table full_table({start_columns}, {query_so_far}, {extra_columns});"
    print(full_query)


def table_populate():
    Row_0 = {"Year:1990", }


#user1 = {"id":100, "name": "Rumpelstiltskin", "dob": "12/12/12"}
#c.execute("INSERT INTO users VALUES (:id, :name, :dob)", user1) 
#db.execute("INSERT INTO MyDataBase.db(column_name)VALUES (<data_for_one_row_of your sql table>)")