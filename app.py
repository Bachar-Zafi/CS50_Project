from ast import Return
from flask import Flask, request, render_template, current_app
from Queries import max_metric_for_year,asset_metric_result_for_year,year_with_max_metric

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Get_Web_Page():
  
        # if the method is GET, just send me the html page to display in the browser
      return current_app.send_static_file('Project_webpage.html')

@app.route('/asset_metric_result_for_year', methods=['POST'])
def POST_1():

  metric_1 = request.form.get("metric_1")
  year_1 = request.form.get("year_1")

  if metric_1 == "Failure Probability":
      metric_1= "Failure_Probability" 
  #retrieve the user's specified fields from the browser
 
  #feed those two values into the corresponding function imported from Queries

  result_1 = asset_metric_result_for_year(metric_1,year_1)

  Resp_Sentence = f"The asset's {metric_1} in your chosen year of {year_1} is: {result_1}" 
  return render_template("Webpage_w_Results.html",Result_Sentence = Resp_Sentence)

@app.route('/max_metric_for_year', methods=['POST'])
def POST_2():

  metric_2 = request.form.get("metric_2")
  year_2 = request.form.get("year_2")

  if metric_2 == "Failure Probability":
    metric_2 = "Failure_Probability" 

  result_2 = max_metric_for_year(metric_2,year_2)

  Resp_Sentence = f"The hazard with the highest {metric_2} in your chosen year of {year_2} is: {result_2}" 
  return render_template("Webpage_w_Results.html", Result_Sentence = Resp_Sentence)

@app.route('/year_with_max_metric', methods=['POST'])
def POST_3():
  metric_3 = request.form.get("metric_3")

  if metric_3 == "Failure Probability":
    metric_3 = "Failure_Probability" 

  result_3 = year_with_max_metric(metric_3)

  Resp_Sentence = f"The year with the highest {metric_3} is: {result_3}" 
  return render_template("Webpage_w_Results.html", Result_Sentence = Resp_Sentence)


if __name__ == "__main__":
  app.run()      
      
  