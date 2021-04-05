import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn import datasets
from sklearn.linear_model import LogisticRegression #importing the necessary model packages

from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import adjusted_rand_score
from matplotlib import ticker
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def classification(y_test,pred,model_name):
    """
    function to print all the necessary evaluation metrics

    """

    evaluation_table=pd.DataFrame(columns=['Model','Accuracy','Precision','Recall','F-1']) ## defining a table to append all the model evaluation metrics
                                                                                      ## and analyse the table for later use.


    accuracy=round(accuracy_score(y_test,pred)*100,2)
    precision=round(precision_score(y_test,pred)*100,2)
    recall=round(recall_score(y_test,pred)*100,2)
    f_1=round(f1_score(y_test,pred)*100,2)

    evaluation_table = evaluation_table.append({'Model':model_name,
      'Accuracy':accuracy,
      'Precision':precision,
      'Recall':recall,
      'F-1':f_1
    },ignore_index=True,)

    return evaluation_table

def app():

    st.title('Analysis of Model Performances')

    eval_tab=pd.read_csv('eval_tab.csv')
    eval_tab_cfs=pd.read_csv('eval_tab_cfs.csv')
    eval_tab_ffs=pd.read_csv('eval_tab_ffs.csv')
    eval_tab_lfs=pd.read_csv('eval_tab_lfs.csv')


    st.write("Table with measures of different models with all features")
    st.write(eval_tab)


    #visualising the performance
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write("Visualisation of performance of the  models with all features")
    model=eval_tab['Model']
    values=[eval_tab['Accuracy'],eval_tab['Precision'],eval_tab['Recall'],eval_tab['F-1']]
    n=len(values)
    w=.15
    x=np.arange(0, len(model))
    plt.figure(figsize=(25,15))
    plt.title("Comparison of Accuracy,Preccision,Recall,F-1 among Different classifiers")
    for i, value in enumerate(values):
    	position=x + (w*(1-n)/2) + i*w
    	plt.bar(position, value, width=w, label=f'{eval_tab.columns[i+1]}')
    plt.xticks(x, model)
    plt.ylabel('Precise Value')
    plt.ylim(80,100)
    plt.legend()
    st.pyplot()

    st.write("Table with measures of different models with Corelated features")
    st.write(eval_tab_cfs)


    #visualising the performance
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write("Visualisation of performance of the  models with all features")
    model=eval_tab_cfs['Model']
    values=[eval_tab_cfs['Accuracy'],eval_tab_cfs['Precision'],eval_tab_cfs['Recall'],eval_tab_cfs['F-1']]
    n=len(values)
    w=.15
    x=np.arange(0, len(model))
    plt.figure(figsize=(25,15))
    plt.title("Comparison of Accuracy,Preccision,Recall,F-1 among Different classifiers")
    for i, value in enumerate(values):
    	position=x + (w*(1-n)/2) + i*w
    	plt.bar(position, value, width=w, label=f'{eval_tab.columns[i+1]}')
    plt.xticks(x, model)
    plt.ylabel('Precise Value')
    plt.ylim(80,100)
    plt.legend()
    st.pyplot()

    st.write("Table with measures of different models with Forward feature Selection method")
    st.write(eval_tab_ffs)


    #visualising the performance
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write("Visualisation of performance of the  models with all features")
    model=eval_tab_ffs['Model']
    values=[eval_tab_ffs['Accuracy'],eval_tab_ffs['Precision'],eval_tab_ffs['Recall'],eval_tab_ffs['F-1']]
    n=len(values)
    w=.15
    x=np.arange(0, len(model))
    plt.figure(figsize=(25,15))
    plt.title("Comparison of Accuracy,Preccision,Recall,F-1 among Different classifiers")
    for i, value in enumerate(values):
    	position=x + (w*(1-n)/2) + i*w
    	plt.bar(position, value, width=w, label=f'{eval_tab_ffs.columns[i+1]}')
    plt.xticks(x, model)
    plt.ylabel('Precise Value')
    plt.ylim(80,100)
    plt.legend()
    st.pyplot()

    st.write("Table with measures of different models with Lasso feature Selection")
    st.write(eval_tab_lfs)


    #visualising the performance
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write("Visualisation of performance of the  models with Lasso Feature Selection")
    model=eval_tab_lfs['Model']
    values=[eval_tab_lfs['Accuracy'],eval_tab_lfs['Precision'],eval_tab_lfs['Recall'],eval_tab_lfs['F-1']]
    n=len(values)
    w=.15
    x=np.arange(0, len(model))
    plt.figure(figsize=(25,15))
    plt.title("Comparison of Accuracy,Preccision,Recall,F-1 among Different classifiers")
    for i, value in enumerate(values):
    	position=x + (w*(1-n)/2) + i*w
    	plt.bar(position, value, width=w, label=f'{eval_tab_lfs.columns[i+1]}')
    plt.xticks(x, model)
    plt.ylabel('Precise Value')
    plt.ylim(80,100)
    plt.legend()
    st.pyplot()
