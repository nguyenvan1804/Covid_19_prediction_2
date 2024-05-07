import json
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
# ➢ st.set_page_config(
    # page_title=None, 
    # page_icon=None, 
    # layout="centered",
    #initial_sidebar_state="auto", 
    # menu_items=None
#)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Sidebar navigation
st.set_page_config(
    page_title = "Home",
    page_icon="🏠",
)


def home():
    animation = load_lottiefile("C:\\Users\\Admin\\Downloads\\Covid_19_prediction-main\\lotties\\Animation.json")
    st_lottie(
        animation,
        speed=1,
        reverse=False,
        loop=True,
        quality="medium",
        # renderer="svg",
        height=500,
        width=500,
        key=None,
    )

    st.title("Covid-19 outbreak prediction model")

    st.write("""
    This project will research and analyze data about coronavirus (COVID-19) in Vietnam and around the world.

    Data is collected from the website: 
    https://data.opendevelopmentmekong.net/dataset/coronavirus-covid-19-cases-in-vietnam/resource/d2967df9-3ef2-4d86-ad21-c14becf043fc         
    """)

    st.subheader("Dataset")

    # Đọc file CSV
    data = pd.read_csv('covid_19/data_vn/covid19-provinces_vn.csv')

    # Hiển thị DataFrame trên Streamlit
    st.dataframe(data)
# st.write(data)s


#   model, scaler = create_model(data)

#   with open('model/model.pkl', 'wb') as f:
#     pickle.dump(model, f)
    
#   with open('model/scaler.pkl', 'wb') as f:
#     pickle.dump(scaler, f)
  

# if __name__ == '__main__':
#   main()


