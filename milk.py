import streamlit as st
import pickle

model = pickle.load(open('milk2.pkl', 'rb'))

def run():
    st.title("Milk Prediction using Machine Learning")
    

    ## ph
    ph= st.slider('Enter PH Value',3.0,9.5)

     ## temp
    temp= st.slider('Enter Temperature',34,95)


    ## Taste
    taste= ('0','1')
    taste_options = list(range(len(taste)))
    taste_models = st.selectbox("Taste",taste_options, format_func=lambda x: taste_options[x])

    ## Odour
    odor= ('0','1')
    odor_options = list(range(len(odor)))
    odor_models = st.selectbox("Odor",odor_options, format_func=lambda x: odor_options[x])

    ## Fat
    fat= ('0','1')
    fat_options = list(range(len(fat)))
    fat_models = st.selectbox("Fat",fat_options, format_func=lambda x: fat_options[x])

    ## Turbidity
    tur= ('0','1')
    tur_options = list(range(len(tur)))
    tur_models = st.selectbox("Turbidity",tur_options, format_func=lambda x: tur_options[x])

    ## Color
    color= st.slider('Enter Color',240,255)

    
    if st.button("Submit"):
        features = [[ph, temp,taste_models,odor_models,fat_models,tur_models,color]]
        print(features)
        prediction = model.predict(features)
        weight = [str(i) for i in prediction]
        ans = ', '.join(weight)
        if ans==0:
            st.error("Error in the Inputs: Please Try Again")

        else:
            st.success("The Milk Quality is"+" "+ans)


            

run()