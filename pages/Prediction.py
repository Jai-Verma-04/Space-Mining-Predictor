import pickle 
import streamlit as st 

# loading in the model to predict on the data 
pickle_in = open('model.pkl', 'rb') 
classifier = pickle.load(pickle_in) 
 
def prediction(iron,nickel,water_ice,other,distance,gravity,temp,tilt,rotation,orbit,efficiency): 

	prediction = classifier.predict( 
		[[iron,nickel,water_ice,other,distance,gravity,temp,tilt,rotation,orbit,efficiency]]) 
	print(prediction) 
	return prediction 
	

def main(): 
    st.title("Space Mining Prediction") 
    
    iron = st.number_input("iron", 0, 100)
    nickel = st.number_input("nickel", 0, 100)
    water_ice = st.number_input("water_ice", 0, 100)
    other = st.number_input("other", 0, 100)
    distance = st.number_input("distance", 50, 1000)
    gravity = st.number_input("gravity", 0, 25)
    temp = st.number_input("temp", 50, 700)
    tilt = st.number_input("tilt", 0, 90)
    rotation = st.number_input("rotation", 0, 999)
    orbit = st.number_input("orbit", 0, 9999)
    efficiency = st.number_input("efficiency", 0, 100)
    result ="" 

    if st.button("Predict"): 
        result = prediction(iron,nickel,water_ice,other,distance,gravity,temp,tilt,rotation,orbit,efficiency) 
        st.success('The output is {}'.format(result[0])) 


if __name__=='__main__': 
    main() 