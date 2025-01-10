import streamlit as st
import pickle

with open('vector.pkl','rb') as f:
    my_vector = pickle.load(f)


with open('best_model.pkl','rb') as f:
    my_model_brain = pickle.load(f)



st.title('Fake News Detector')
st.header("Just Paste your News to check It's Fake or Real")

news = st.text_input(' Enter news here: ')
if st.button('Submit'):
    if news is not None:
        vector_result = my_vector.transform([news])
        predict_result = my_model_brain.predict(vector_result)[0]
        if predict_result == 0:
            st.write('FAKE News ❌❌')
        else:
            st.write('REAL News ✅✅')