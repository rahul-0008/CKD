import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle
import numpy as np
import joblib



def app():
    st.title('Check for CKD!')

    st.write('Note : The below result is just an inference and it is not groung truth.')

    model = joblib.load('RF.pickle')


    def predict_ckd(age, blood_pressure, specific_gravity, albumin, sugar,
           red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
           blood_gulcose_random, blood_urea, serum_creatinine, sodium,
           potassium, hemoglobin, packed_cell_volume,
           white_blood_cell_count, red_blood_cell_count, hypertension,
           diabetes_melitus, coronary_artery_disease, appetite,
           pedal_edema, anemia):
        
        
        input=np.array([[age, blood_pressure, specific_gravity, albumin, sugar,
           red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
           blood_gulcose_random, blood_urea, serum_creatinine, sodium,
           potassium, hemoglobin, packed_cell_volume,
           white_blood_cell_count, red_blood_cell_count, hypertension,
           diabetes_melitus, coronary_artery_disease, appetite,
           pedal_edema, anemia]]).astype(np.float64)
        
        
        prediction = model.predict(input)
        
        return int(prediction)

    

    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Chronic Kidney Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    age=st.text_input("Age","in years")
    blood_pressure= st.text_input("blood_pressure","in mm/Hg")
    specific_gravity= st.selectbox("Specific Gravity",[1.005,1.010,1.015,1.020,1.025])
    albumin= st.selectbox("Albumin",[0,1,2,3,4,5])
    sugar= st.selectbox("Sugar",[0,1,2,3,4,5])
    red_blood_cells= st.radio("Red Blood Cells",[0,1]) 
    pus_cell= st.radio("Pus Cell",[0,1]) 
    pus_cell_clumps= st.radio("Pus cell Clamps",[0,1])
    bacteria= st.radio("Bacteria",[0,1])
    blood_gulcose_random= st.text_input("Clood Gulcose Random","in mgs/dl") 
    blood_urea= st.text_input("Blood Urea","in mgs/dl") 
    serum_creatinine= st.text_input("Serum Creatinine","in mgs/dl") 
    sodium= st.text_input("Sodium","in mEq/L")
    potassium= st.text_input("Potassium","in mEq/L") 
    hemoglobin= st.text_input("Hemoglobin","gms")
    packed_cell_volume= st.text_input("Packed Cell Volume"," ")
    white_blood_cell_count= st.text_input("WBC","in cells/cmm") 
    red_blood_cell_count= st.text_input("RBC","in millions/cmm") 
    hypertension= st.radio("Hypertension",[0,1])
    diabetes_melitus= st.radio("Diabetes Melitus",[0,1]) 
    coronary_artery_disease= st.radio("Coronary Artery Disease",[0,1]) 
    appetite= st.radio("Appetite",[0,1])
    pedal_edema= st.radio("Pedal Edma",[0,1])
    anemia= st.radio("Anemia",[0,1])


    safe_html ="""  
    <div style="background-color:#80ff80; padding:10px >
    <h2 style="color:white;text-align:center;"> You're not symtomatic to CKD</h2>
    </div>
    """
    danger_html="""  
    <div style="background-color:#F08080; padding:10px >
    <h2 style="color:black ;text-align:center;"> You're  symtomatic to CKD</h2>
    </div>
    """

    output = ''


    if st.button("Predict CKD"):
       output = predict_ckd(age, blood_pressure, specific_gravity, albumin, sugar,
       red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
       blood_gulcose_random, blood_urea, serum_creatinine, sodium,
       potassium, hemoglobin, packed_cell_volume,
       white_blood_cell_count, red_blood_cell_count, hypertension,
       diabetes_melitus, coronary_artery_disease, appetite,
       pedal_edema, anemia)


    st.success('The output is {}'.format(output))

    if output == 0:
        st.markdown(danger_html,unsafe_allow_html=True)
    elif output==1:
        st.markdown(safe_html,unsafe_allow_html=True)

