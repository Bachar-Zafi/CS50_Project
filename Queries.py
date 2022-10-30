#from posixpath import split
import sqlite3

# Q2 - find hazard with highest (user chosen) metric in a (user chosen) year
def max_metric_for_year(metric_type, user_year):
    if metric_type not in ["VAR", "Failure_Probability"]:
        print("your metric type is invalid")
        return("invalid_input")
    connection = sqlite3.connect("MyDataBase.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT flood_riverine_{metric_type}, inundation_{metric_type}, heat_{metric_type}, forest_fire_{metric_type}, wind_{metric_type}, soil_movement_{metric_type}, flood_surfacewater_{metric_type} FROM full_table WHERE Year=?", [user_year])

    results = cursor.fetchall()

    results_list = results[0] 
    max_metric = max(results_list)
    max_metric_index =results_list.index(max_metric) 
        
    if max_metric_index==0:
        max_metric_haz = "Riverine Flooding"
    elif max_metric_index==1:
        max_metric_haz = "Coastal Inundation"
    elif max_metric_index==2:
        max_metric_haz = "Extreme Heat"
    elif max_metric_index==3:
        max_metric_haz = "Forest Fire"
    elif max_metric_index==4:
        max_metric_haz = "Extreme Wind"
    elif max_metric_index==5:
        max_metric_haz = "Soil Movement"
    elif max_metric_index==6:
        max_metric_haz = "Surfacewater Flooding"
        
    print(f"The hazard with the highest {metric_type} in your chosen year of {user_year} is: {max_metric_haz}")

    cursor.close()
    connection.close()
    return(max_metric_haz)

# Q1 - find asset's (user chosen) metric for(user chosen) year

def asset_metric_result_for_year(metric_type, user_year):

    if metric_type not in ["VAR", "Failure_Probability", "TIP"]:
        print("your metric type is invalid")
        return("invalid_input")
    
    connection = sqlite3.connect("MyDataBase.db")
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT Asset_{metric_type} FROM full_table WHERE Year=?", [user_year])

    result = cursor.fetchall()
    asset_metric_result = "{}".format(*result[0])
    
    print(f"The asset's {metric_type} in your chosen year of {user_year} is: {asset_metric_result}")
    cursor.close()
    connection.close()
    return(asset_metric_result)

# Q3 - find the year in which a (user chosen) metric reached its max
def year_with_max_metric(metric_type):
    if metric_type not in ["VAR", "Failure_Probability", "TIP"]:
        print("your metric type is invalid")
        return("invalid_input")
    connection = sqlite3.connect("MyDataBase.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT Year FROM full_table WHERE Asset_{metric_type} = (SELECT MAX(Asset_{metric_type})FROM full_table)")

    result = cursor.fetchall()
    max_year = "{}".format(*result[0])
    
    print(f"The asset's maximum {metric_type} was reached in the year {max_year}")
    cursor.close()
    connection.close()
    return(max_year)

# Calling the functions:

if __name__ == "__main__":
    max_metric_for_year("Failure_Probability", "2020")
    asset_metric_result_for_year("VAR", "2080")
    year_with_max_metric("Failure_Probability")


