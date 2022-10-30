from bdb import Breakpoint
import json
import csv
from operator import length_hint
import os
from pathlib import Path
from typing import Dict
import sqlite3

def Asset_IDs(features):
    
    Asset_ID = features[0]["_id"]

    return Asset_ID

def Asset_VAR_FUN(features):

# designate the "total risk" list (containing all the asset VAR figures) as one (list) object

    Asset_VARs = features[0]["properties"]["totalRisk"] 

    Asset_VAR_by_Year = {}

    year = 1990
    n=0
    for i in Asset_VARs:
    
        Asset_VAR_by_Year[year] = Asset_VARs[n] 
        n = n+1
        year = year+1

    return Asset_VAR_by_Year

def Asset_FP_FUN(features):
    Asset_FPs = features[0]["properties"]["totalFailure"]

    Asset_FP_by_Year = {}

    year = 1990
    n=0
    for j in Asset_FPs:
    
        Asset_FP_by_Year[year] = Asset_FPs[n] 
        n = n+1
        year = year+1

    return Asset_FP_by_Year

def Hazard_FP_FUN(features,scenario):

    Hazard_FPs = features[0]["properties"]["failureHazards"]

    #Creating a dictionary of dictionaries to grab all the hazard FP figures against each year

    hazards = scenario["hazards"]

    Haz_FP_by_Year = {}

    year = 1990
    n=0

    for n in range (len(Hazard_FPs)):
        my_dict = {}
        for m,haz in enumerate(hazards):
            my_dict[haz] = Hazard_FPs[n][m]
        Haz_FP_by_Year[year] = my_dict 
        year+=1
        
    return Haz_FP_by_Year

def Hazard_VAR_FUN(features,scenario):

    Hazard_VARs = features[0]["properties"]["riskHazards"]
    hazards = scenario["hazards"]

    Hazard_VAR_by_Year = {}

    year = 1990
    n=0

    for n in range (len(Hazard_VARs)):
        my_dict = {}
        for m,haz in enumerate(hazards):
            my_dict[haz] = Hazard_VARs[n][m]
        Hazard_VAR_by_Year[year] = my_dict 
        year+=1

    return Hazard_VAR_by_Year

    # Hazard_VAR_By_Year retains the original hazard names as shown in the Geojson

def TIP_FUN(features):
    Asset_TIP = features[0]["properties"]["totalRiskCost"] 

    TIP_by_Year = {}

    year = 1990
    n=0
    for i in Asset_TIP:
    
        TIP_by_Year[year] = Asset_TIP[n] 
        n = n+1
        year = year+1

    return TIP_by_Year

with open('Data/temp.json','r') as f:
    my_data = json.load(f)

features = my_data["features"]
scenario = my_data["scenario"]

Asset_VARs = Asset_VAR_FUN(features)
Hazard_VARs = Hazard_VAR_FUN(features,scenario)
Asset_FPs = Asset_FP_FUN(features)
Hazard_FPs = Hazard_FP_FUN(features,scenario)
TIPs = TIP_FUN(features)
AssetID = Asset_IDs(features)

connection = sqlite3.connect('MyDataBase.db')
db = connection.cursor()

for i,year in enumerate(range(1990,2101)):
    if i == 0:
        continue
    row = {}

    row["Year"] = year
    row["Asset_ID"] = AssetID

    row["flood_riverine_Failure_Probability"] = Hazard_FPs[year]["flood_riverine"]
    row["flood_surfacewater_Failure_Probability"] = Hazard_FPs[year]["flood_surfacewater"]
    row["soil_movement_Failure_Probability"] = Hazard_FPs[year]["soil_movement"]
    row["wind_Failure_Probability"] = Hazard_FPs[year]["wind"]
    row["heat_Failure_Probabillity"] = Hazard_FPs[year]["heat"]
    row["forest_fire_Failure_Probability"] = Hazard_FPs[year]["forest_fire"]
    row["inundation_Failure_Probability"] = Hazard_FPs[year]["inundation"]

    row["Asset_Failure_probability"] = Asset_FPs[year]

    row["flood_riverine_VAR"] = Hazard_VARs[year]["flood_riverine"]
    row["flood_surfacewater_VAR"] = Hazard_VARs[year]["flood_surfacewater"]
    row["soil_movement_VAR"] = Hazard_VARs[year]["soil_movement"]
    row["wind_VAR"] = Hazard_VARs[year]["wind"]
    row["heat_VAR"] = Hazard_VARs[year]["heat"]
    row["forest_fire_VAR"] = Hazard_VARs[year]["forest_fire"]
    row["inundation_VAR"] = Hazard_VARs[year]["inundation"]

    row["Asset_VAR"] = Asset_VARs[year]

    row["Asset_TIP"] = TIPs[year]

    row["Row_ID"] = i
    res = db.execute("""INSERT INTO full_table VALUES (:Row_ID, :Asset_ID, :Year, :flood_riverine_Failure_Probability, 
    :flood_surfacewater_Failure_Probability, 
    :soil_movement_Failure_Probability,:wind_Failure_Probability,:heat_Failure_Probabillity, 
    :forest_fire_Failure_Probability,:inundation_Failure_Probability, :Asset_Failure_Probability,
    :flood_riverine_VAR, :flood_surfacewater_VAR, :soil_movement_VAR, :wind_VAR,
    :heat_VAR, :forest_fire_VAR, :inundation_VAR, :Asset_VAR, :Asset_TIP)""", row) 
    
    connection.commit()

connection.close()

