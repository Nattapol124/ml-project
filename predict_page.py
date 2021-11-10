import streamlit as st
import pickle
import numpy as np
from graph import graph

def load_model():
    with open('save.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("คำนวณเงินเดือน SoftwareDeveloper\n")

    st.write("""กรอกข้อมูลเพื่อทำการคำนวณเงินเดือน""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "ต่ำกว่าปริญญาตรี",
        "ปริญญาตรี",
        "ปริญญาโท",
        "ปริญญาเอก",
        
    )
 
    country = st.selectbox("เลือกประเทศ", countries)
    education = st.selectbox("วุฒิการศึกษา", education)

    expericence = st.slider("ประสบการณ์การทำงาน", 0, 50, 0)
    
    ok = st.button("คำนวนเงินเดือน")
   
    if ok:
        if education == "ต่ำกว่าปริญญาตรี":
            education = "Less than a Bachelors"
        if education == "ปริญญาตรี":
            education = "Bachelor’s degree"
        if education == "ปริญญาโท":
            education = "Master’s degree"
        if education == "ปริญญาเอก":
            education = "Post grad" 
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.title("\n")
        st.subheader(f"รายได้ต่อปีประมาณ ${salary[0]:.2f}   ( { salary[0]*33:.0f} บาท )")
        st.title("\n")
        st.title("\n")
        st.title("\n")
        st.title("\n")
        st.title("\n")
        graph()


