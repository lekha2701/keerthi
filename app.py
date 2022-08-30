import streamlit as st
import joblib

#load the joblib model
model_nb = joblib.load('spam-ham')

st.title('spam ham classifier')
ip = st.text_input('enter your text :')
 
  op = model_nb.predict([ip])
  if st.button('PREDICT'):
    st.title(op[0])

    
    
    
    
    
    
