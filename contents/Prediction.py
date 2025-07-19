import streamlit as st
from styles import styled_result
from pycaret.regression import load_model, predict_model
import pandas as pd
import numpy as np

boolean_features = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea"]
categorical_features = ["furnishingstatus"]
numeric_discrete_features = ["bedrooms","bathrooms", "stories", "parking"]
numeric_continuous_features = ["area"]
item_per_col = 2
parameters = {}
feature_captions = {
    # Numeric continuous features
    "area": "Total area of the house in square feet",
    
    # Numeric discrete features
    "bedrooms": "Number of bedrooms in the house",
    "bathrooms": "Number of bathrooms in the house",
    "stories": "Number of stories in the house",
    "parking": "Number of parking spaces available",
    
    # Boolean features
    "mainroad": "Is the house connected to a main road?",
    "guestroom": "Does the house have a guest room?",
    "basement": "Does the house have a basement?",
    "hotwaterheating": "Does the house have hot water heating?",
    "airconditioning": "Does the house have air conditioning?",
    "prefarea": "Is the house in a preferred area?",
    
    # Categorical features
    "furnishingstatus": "Current furnishing status of the house"
}
def create_form_item(feature_list, feature_type):
        number_of_columns = len(feature_list) // item_per_col + (len(feature_list) % item_per_col > 0)
        for index, col in enumerate(st.columns(number_of_columns)):
            with col:
                for i in range(min(len(feature_list) - index*2, item_per_col)):
                    caption = feature_captions.get(feature_list[index*2+i], feature_list[index*2+i])
                    if feature_type == "boolean":
                        parameters[feature_list[index*2+i]] = st.selectbox(caption, ["Yes", "No"], key=f"select_{feature_list[index*2+i]}")
                    elif feature_type == "categorical":
                        parameters[feature_list[index*2+i]] = st.radio(caption, ["Furnished", "Semi-Furnished", "Unfurnished"], horizontal=True, key=f"input_{feature_list[index*2+i]}")
                    elif feature_type == "numeric_discrete":
                        parameters[feature_list[index*2+i]] = st.number_input(caption, min_value=0, max_value=10, step=1, key=f"input_{feature_list[index*2+i]}")
                    elif feature_type == "numeric_continuous":
                       parameters[feature_list[index*2+i]] = st.number_input(caption, min_value=50,max_value=20000, step=50, key=f"input_{feature_list[index*2+i]}")

def data_processing(df):
    data = df.copy()
    furnishing_status_encoding = {
        'furnished': 2,
        'semi-furnished': 1,
        'unfurnished': 0
    }
    yes_no_encoding = {
        'yes': 1,
        'no': 0
    }
    for feature in categorical_features:
        data[feature] = data[feature].apply(lambda x: furnishing_status_encoding.get(x.lower(), np.nan))
    for feature in boolean_features:
        data[feature] = data[feature].apply(lambda x: yes_no_encoding.get(x.lower(), np.nan))
    for feature in numeric_continuous_features:
        data[feature]= np.log(data[feature])
    return data

@st.cache_resource
def load_predict_model():
    return load_model('model/house_pipeline')

def make_prediction(parameters):
    df = pd.DataFrame(parameters, index=[0])
    data = data_processing(df)
    loaded_best_pipeline = load_predict_model()
    predictions = predict_model(loaded_best_pipeline, data=data)
    price = predictions['prediction_label'][0]
    price_str = f'${np.exp(price):,.0f}'
    return price_str

def prediction():
    st.header("House Price Prediction", divider='rainbow',anchor=False)
    with st.form("prediction_form"):
        create_form_item(numeric_continuous_features, "numeric_continuous")
        create_form_item(numeric_discrete_features, "numeric_discrete")
        create_form_item(boolean_features, "boolean")
        col_left, col_right = st.columns([4,6])
        with col_left:
            create_form_item(categorical_features, "categorical")
            submitted = st.form_submit_button('Predict Price')
        with col_right:
            if submitted:
                result = make_prediction(parameters)
                st.markdown(styled_result(result), unsafe_allow_html=True)
                with st.popover("Submitted Parameters"):
                    st.write("Parameters:", parameters)
                
        
        
