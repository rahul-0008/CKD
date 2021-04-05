import streamlit as st
import pandas as pd

import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.io as pio




import warnings
warnings.filterwarnings("ignore")
import io


def app():
	st.title('Chronic Kidney Disease - CKD')
	st.write('Chronic kidney Disease (CKD) means your kidneys are damaged and not ﬁltering your blood the way it should. The primary role of kidneys is to ﬁlter extra water and waste from your blood to produce urine and if the person has suffered from CKD, it means that wastes are collected in the body.This disease is chronic because of the damage gradually over a long period. It is ﬂattering a common disease worldwide. Due to CKD may have some health troubles. There are many causes for CKD like diabetes, high blood pressure,heart disease. Along with these critical diseases, CKD also depends on age and gender')
	st.set_option('deprecation.showPyplotGlobalUse', False)


	data=pd.read_csv('kidney_disease.csv')

	columns={
	    'id':'id','age':'age', 'bp':'blood_pressure', 'sg':'specific_gravity', 'al':'albumin', 'su':'sugar', 'rbc':'red_blood_cells',
	    'pc':'pus_cell', 'pcc':'pus_cell_clumps', 'ba':'bacteria', 'bgr':'blood_gulcose_random',
	    'bu':'blood_urea', 'sc':'serum_creatinine', 'sod':'sodium', 'pot':'potassium', 'hemo':'hemoglobin', 'pcv':'packed_cell_volume', 
	    'wc':'white_blood_cell_count', 'rc':'red_blood_cell_count', 'htn':'hypertension', 'dm':'diabetes_melitus', 
	    'cad':'coronary_artery_disease','appet':'appetite', 'pe':'pedal_edema', 'ane':'anemia', 'classification':'class'}


	data.rename(columns=columns,inplace=True)

	data['class']=data['class'].replace({'ckd':'ckd','ckd\t':'ckd','notckd':'notckd'})
	data['packed_cell_volume']=pd.to_numeric(data['packed_cell_volume'],errors='coerce')
	data['white_blood_cell_count']=pd.to_numeric(data['white_blood_cell_count'],errors='coerce')  ## conversion of false object type to numeric type
	data['red_blood_cell_count']=pd.to_numeric(data['red_blood_cell_count'],errors='coerce')

	st.header("Factors influencing CKD")
	st.markdown("The below chart visualises the effect of Red Blood cell count and Packed Cell volume on CKD ")
	plt.figure(figsize=(16,16))
	sns.scatterplot(x='red_blood_cell_count',y='packed_cell_volume',data=data,hue='class')
	plt.xticks(size=20)
	plt.yticks(size=20)
	st.pyplot()
	st.write('RBC count range ~2 to <4.5 and Hemoglobin between 3 to <13 are mostly classified as positive for chronic kidney disease(i.e ckd)')

	st.header("Factors influencing CKD")
	st.markdown("The below chart visualises the effect of Red Blood cell count and Hemoglobin on CKD")
	plt.figure(figsize=(16,16))
	sns.scatterplot(data=data, x=data['red_blood_cell_count'], y=data['hemoglobin'], hue='class')
	plt.xticks(size=20)
	plt.yticks(size=20)
	st.pyplot()
	st.write('RBC count range >4.5 to ~6.1 and Hemoglobin between >13 to 17.8 are classified as negative for chronic kidney disease(i.e not ckd)')

	st.header("Factors influencing CKD")
	st.markdown("The below chart visualises the effect of Hemoglobin and Packed Cell volume on CKD")
	plt.figure(figsize=(16,16))
	sns.scatterplot(x='hemoglobin',y='packed_cell_volume',data=data,hue='class')
	plt.xticks(size=20)
	plt.yticks(size=20)
	st.pyplot()
	st.write('Hemoglobin > 13, mostly classified as not ckd and are visualised as healthy')

	st.header("Factors influencing CKD")
	st.markdown("The below chart visualises the effect of Serum Creatinine and Blood Yrea on CKD")
	plt.figure(figsize=(16,16))
	sns.scatterplot(x='serum_creatinine',y='blood_urea',data=data,hue='class')
	plt.xticks(size=20)
	plt.yticks(size=20)
	st.pyplot()
	st.write('Obviously, if Serum Creatinine > 0 it contributes to Chronic kidney disease')

	st.header("Factors influencing CKD")
	st.markdown("The below chart visualises the effect of Red Blood Cells and Albumin on CKD")
	plt.figure(figsize=(16,16))
	sns.scatterplot(x='red_blood_cell_count',y='albumin',data=data,hue='class')
	plt.xticks(size=20)
	plt.yticks(size=20)
	st.pyplot()
	st.write('Clearly, Albumin levels of above 0 affect the kidney in a larger amount.')


	st.header("Factors influencing CKD")
	st.markdown("The below chart visualises the effect of Packed Cell Volume and Blood Urea on CKD")
	plt.figure(figsize=(16,16))
	sns.scatterplot(x='packed_cell_volume',y='blood_urea',data=data,hue='class')
	plt.xticks(size=20)
	plt.yticks(size=20)
	st.pyplot()
	st.write('Packed cell volume >= 40 more possiblity to avoid the chronic disease.')

	st.header("Factors influencing CKD")
	st.markdown("The below chart visualises the effect of Packed Cell Volume and Specfic gravity on CKD")
	plt.figure(figsize=(16,16))
	sns.barplot(x='specific_gravity',y='packed_cell_volume',hue='class',data=data,dodge=True)
	plt.xticks(size=20)
	plt.yticks(size=20)
	st.pyplot()
	st.write('Clearly, specific gravity >=1.02 does not affects non ckd')






    


