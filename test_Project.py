import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')


st.title('Prédiction de prix de maison')

taille = st.number_input("Taille maison")
nb_rooms = st.number_input("Nombre de chambre")
garden = st.number_input("Y a un jardin")


model = load_model()

if taille <= 0:
    st.write('mettre taille correcte')
if nb_rooms <= 0:
    st.write("mettre nombre de chambre correct")


if taille > 0 and nb_rooms > 0:
    
    X = [[taille, nb_rooms, garden]]
    prediction = model.predict(X)
    ## afficher la prediction
    st.write("<p id='prediction'>le prix de la maison est : {}</p>". format(prediction[0]), unsafe_allow_html=True)

def main():
    import pandas as pd 
    from sklearn.linear_model import LinearRegression
    import joblib
    df = pd.read_csv('houses.csv')
    X = df[["size", "nb_rooms", "garden"]]
    y = df["price"]
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "regression.joblib")
    
       
if __name__ == "__main__":
  main()