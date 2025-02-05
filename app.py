
import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open('final_model.pkl', 'rb') as file:
    model = pickle.load(file)


def prediction(input_list):

    input_list = np.array(input_list, dtype = object)

    pred = model.predict_proba([input_list])[:,1][0]

    if pred > 0.5:
        return f'''You are more prone to depression
Your Chances of being depressed are {round(pred,2)} 
So Stop Overthinking, Have Some Water and TAKE CARE :('''
    else:
        return f'''You are less prone to depression
Your Chances of being depressed are {round(pred,2)} 
So TAKE CARE :)'''



def main():
    st.title('ARE YOU DEPRESSED!!!')
    ag = st.slider('Enter Your Age Please ', min_value = 10, max_value = 100, step = 1)
    
    gen =(lambda x: 0 if x == 'Female' else 1)(st.selectbox('Please tell Your Gender', ['Male', 'Female']))

    wp =(lambda x: 0 if x == 'Student' else 1)( st.selectbox('Are You a Working Professional or Student', ['Working Professional', 'Student']))

    apwp = st.slider('Rate Your Work/Academic Pressure ? (1 for low pressue and 5 for high pressure)', min_value = 1, max_value = 5, step = 1)

    js = st.slider('Rate Your Study/Job Satisfaction ? (1 for low satisfaction and 5 for high pressure)', min_value = 1, max_value = 5, step = 1)

    cgpa = st.number_input('Enter Your CGPA ? (Put 0 if you are a Working Professional) ', min_value = 0, max_value = 10, step = 0.01)

    mp = (lambda x : 0 if x == 'Less than 5 hours' else 1 if x == '5-6 hours' else 2 if x == '7-8 hours'  else 3 if x == 'More than 8 hours')
    sd = mp(st.selectbox('What About Your Sleeping Schedule ?', ['Less than 5 hours', '5-6 hours', '7-8 hours','More than 8 hours' ]))

    dt = (lambda x: 0 if x == 'Unhealthy' else 1 if x == 'Moderate' else 2)(st.selectbox("How's Your Dietery Habit ? ", ['Healthy', 'Moderate', 'Unhealthy']))

    suc = (lambda x: 0 if x == 'No' else 1)(st.selectbox('Have You Ever Have Sucidal Thoughts ', ['Yes', 'No']))

    fhmi = (lambda x: 0 if x == 'No' else 1)(st.selectbox('Do You Have Any family History of Mental Illness ', ['Yes', 'No']))

    finstress = (lambda x: 5 if x == 'Severe' else 4 if x == 'High' else 3 if x == 'Moderate' else 2 if x == 'Slightly' else 1)\
        (st.selectbox('What about Your Financial Stress ?', ['Severe','High', 'Moderate', 'Slightly', 'Least']))

    workstudyhr = st.slider('What is the number of your Work hours or Study hours ?', max_value = 24, min_value = 0, step = 1)


    deg = (lambda x: 0 if x == 'Schooling' else 1 if x == 'Undergraduate' else 2 if x == 'Postgraduate' else 3 if x == 'PhD')\
        (st.selectbox(' What About Your Education Level ?', ['Schooling', 'Undergraduate', 'Postgraduate', 'PhD']))


    input_list = [ag, gen, wp, apwp, js, cgpa, sd, dt, suc, fhmi, finstress, workstudyhr, deg]


    if st.button('Show Prediction'):
        response = prediction(input_list)
        st.success(response)


if __name__ == '__main__':
    main()



