import streamlit as st
#from styles import welcome_msg
def welcome():
    st.header(":wave: Welcome - House Price Prediction", divider='rainbow',anchor=False)
    st.image("images/welcome.jpg", caption="House Price Prediction")
    #st.markdown(welcome_msg, unsafe_allow_html=True)
    
    st.markdown("<h3>Site Overview</h3>", unsafe_allow_html=True)
    st.write("This site serves as a means for users to obtain an estimated price on their house given the features of the house")
    
    st.markdown('<h5>Currently, our model is able to estimate a price based on the following features:</h5>'
    '<li>Area: The total area of the house in square feet</li></ul>'
    '<li>Bedrooms: The number of bedrooms in the house </li></ul>'
    '<li>Bathrooms: The number of bathrooms in the house </li></ul>'
    '<li>Stories: The number of stories in the house</li></ul>'
    '<li>Mainroad: Whether the house is connected to the main road</li></ul>'
    '<li>Guestroom: Whether the house has a guest room </li></ul>'
    '<li>Basement: Whether the house has a basement</li></ul>'
    '<li>Hot Water Heating: Whether the house has a hot water heating system</li></ul>'
    '<li>Air Conditioning: Whether the house has an air conditioning system</li></ul>'
    '<li>Parking: The number of parking spaces available within the house</li></ul>'
    '<li>Prefarea: Whether the house is located in a preferred area</li></ul>'
    '<li>Furnishing status: The furnishing status of the house </li></ul>', unsafe_allow_html=True)

    st.markdown("<h4>An interface where you can enter your house's features can be found on the 'Prediction' page. Feel free to give it a try!</h4>", unsafe_allow_html=True)
    st.markdown("<h4>You can also explore the data obtain on our AI model can be viewed on the 'Exploration' page</h4>", unsafe_allow_html=True)
    st.markdown("<h4>Finally, if you wish to know more about who made this model, head on over to the 'About' page!</h4>", unsafe_allow_html=True)
