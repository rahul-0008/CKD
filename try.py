#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
import pickle
import numpy as np
import joblib

import warnings
warnings.filterwarnings("ignore")


# In[16]:


model = joblib.load('filename.pickle')

st.set_page_config(
    page_title="Prediction App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)



# In[17]:


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


# In[18]:


def main():
	st.title("CKD Prediction")
	html_temp = """
	<div style="background:#025246 ;padding:10px">
	<h2 style="color:white;text-align:center;"> Abalone Age Prediction ML App </h2>
	</div>
	"""
	st.markdown(html_temp, unsafe_allow_html = True)

	age=st.text_input("age","Type Here")
	blood_pressure= st.text_input("blood_pressure","Type Here")
	specific_gravity= st.text_input("specific_gravity","Type Here")
	albumin= st.text_input("albumin","Type Here")
	sugar= st.text_input("sugar","Type Here")
	red_blood_cells= st.text_input("red_blood_cells","Type Here") 
	pus_cell= st.text_input("pus_cell","Type Here") 
	pus_cell_clumps= st.text_input("pus_cell_clumps","Type Here") 
	bacteria= st.text_input("bacteria","Type Here")
	blood_gulcose_random= st.text_input("blood_gulcose_random","Type Here") 
	blood_urea= st.text_input("Length","Type Here") 
	serum_creatinine= st.text_input("serum_creatinine","Type Here") 
	sodium= st.text_input("sodium","Type Here")
	potassium= st.text_input("potassium","Type Here") 
	hemoglobin= st.text_input("hemoglobin","Type Here")
	packed_cell_volume= st.text_input("packed_cell_volume","Type Here")
	white_blood_cell_count= st.text_input("white_blood_cell_count","Type Here") 
	red_blood_cell_count= st.text_input("red_blood_cell_count","Type Here") 
	hypertension= st.text_input("hypertension","Type Here")
	diabetes_melitus= st.text_input("diabetes_melitus","Type Here") 
	coronary_artery_disease= st.text_input("coronary_artery_disease","Type Here") 
	appetite= st.text_input("appetite","Type Here")
	pedal_edema= st.text_input("pedal_edema","Type Here")
	anemia= st.text_input("anemia","Type Here")


	safe_html ="""  
	<div style="background-color:#80ff80; padding:10px >
	<h2 style="color:white;text-align:center;"> The Abalone is young</h2>
	</div>
	"""
	danger_html="""  
	<div style="background-color:#F08080; padding:10px >
	<h2 style="color:black ;text-align:center;"> The Abalone is old</h2>
	</div>
	"""
	if st.button("Predict CKD"):
	   output = predict_ckd(age, blood_pressure, specific_gravity, albumin, sugar,
	   red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
	   blood_gulcose_random, blood_urea, serum_creatinine, sodium,
	   potassium, hemoglobin, packed_cell_volume,
	   white_blood_cell_count, red_blood_cell_count, hypertension,
	   diabetes_melitus, coronary_artery_disease, appetite,
	   pedal_edema, anemia)


	st.success('The age is {}'.format(output))

	if output == 0:
	    st.markdown(danger_html,unsafe_allow_html=True)
	else:
	    st.markdown(safe_html,unsafe_allow_html=True)


# In[19]:


if __name__=='__main__':
    main()


# In[ ]:




