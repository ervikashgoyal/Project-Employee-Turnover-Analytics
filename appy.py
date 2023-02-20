import pandas as pd
import numpy as np
import pickle
import streamlit as st
import openpyxl

df= pd.read_excel("1673873196_hr_comma_sep.xlsx")

st.title("Project: Employee Turnover Analytics ")
st.write(" by vikash goyal mailID : vikashgoyal1995@gmail.com")


encode_dict= {
     "sales":{ 
             "IT": 0,
             "RandD":  1,
            "accounting": 2,
            "hr": 3,
            "management": 4,
            "marketing": 5,
            "product_mng": 6,
            "sales": 7,
            "support": 8,
            "technical": 9
            },

"salary": {"high":0,"low":1,"medium":2}
}



def model_pred(satisfaction_level,last_evaluation,number_project,
       average_montly_hours,time_spend_company,promotion_last_5years,sales,salary):
    with open("model.pickle","rb") as file:
        clf_model=pickle.load(file)
    
    input_feature = [[satisfaction_level,last_evaluation,number_project,
       average_montly_hours,time_spend_company, Work_accident,
       promotion_last_5years,sales,salary]]
    

    return clf_model.predict(input_feature)

col1,col2 = st.columns(2)
sales= col1.selectbox(" Enter the department",["IT", "RandD", "accounting","hr","management", "marketing", "product_mng",  "sales", "support", "technical"])
salary= col2.selectbox("Enter the salary",["low","medium","high"])
satisfaction_level = col1.slider("set satisfaction_level",0.0,1.0,0.1)
last_evaluation = col1.slider("set last_evaluation",0.0,1.0,0.1)
number_project = col1.slider("set number_project",0.0,20.0,.5)
average_montly_hours = col2.slider("set average_montly_hours",0,400,5)
time_spend_company = col2.slider("set time_spend_company",1,10,1)
Work_accident=  col2.selectbox("setWork_accident ",[0,1])
promotion_last_5years=  col2.selectbox("set promotion_last_5years",[0,1])



if (st.button("predict")):
    sales= encode_dict["sales"][sales]
    salary=encode_dict["salary"][salary]
    output= model_pred(satisfaction_level,last_evaluation,number_project,
       average_montly_hours,time_spend_company, promotion_last_5years,sales,salary)
    if output==1:
        st.text("employee left the company")
    else:
        st.text("employee doest not left the company")
    #st.text("the final pridiction is " +str(output))















