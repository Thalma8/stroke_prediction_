
#load the required libraries which are pickle to load the trained model and streamlit to bulid the app.
import pickle
import streamlit as st
 
# loading the trained model and storing it in the variable named classifier
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(gender, age,hypertension,heart_disease,ever_married,Residence_type,smoking_status):   
 
    # Pre-processing user input    
    if gender == "Male":
        gender = 0
    else:
        gender = 1
 
    if ever_married == "Married":
        ever_married = 1
    else:
        ever_married = 0
 
    if Residence_type == "Urban":
        Residence_type = 1
    else:
        Residence_type = 0  
    if hypertension == "yes":
        hypertension = 1
    else:
        hypertension = 0
    if heart_disease == "yes":
        heart_disease = 1
    else:
        heart_disease = 0
    if smoking_status == "formerly smoked":
        smoking_status = 1
    elif smoking_status == "smokes":
          smoking_status = 1
    elif smoking_status == "never smoked":
        smoking_status = 0
    else:
        smoking_status = 0
 
    
 
    # Making predictions 
    prediction = classifier.predict( 
        [[gender, age,hypertension,heart_disease,ever_married,Residence_type,smoking_status]])
     
    if prediction == 0:
        pred = 'No risk'
    else:
        pred = ' a risk'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#A67A5B;padding:13px"> 
    <h1 style ="color:black;text-align:center;text-style="italics">Stroke prediction uisng Machine Learning</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    gender = st.selectbox('Gender',("Male","Female"))
    hypertension = st.selectbox('hypertension',("yes","no"))
    heart_disease = st.selectbox('heart_disease',("yes","no"))
    ever_married= st.selectbox('Marital Status',("Unmarried","Married")) 
    Residence_type = st.selectbox('Residence_type',("Rural","Urban"))
    smoking_status = st.selectbox('Smoking Status',("formerly smoked","smokes","never smoked","Unknown"))
    age = st.number_input("your current age")

    
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(gender, age,hypertension,heart_disease,ever_married,Residence_type,smoking_status) 
        st.success('you are at {}'.format(result))
        print ("of getting a stroke")
       
     
if __name__=='__main__': 
    main()

from pyngrok import ngrok

public_url = ngrok.connect('8501')
public_url
