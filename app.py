import os 
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Nôm Translator", layout="wide")

nom_data = pd.read_csv("viet_explanations.csv")
list_nom = nom_data["nom"].tolist()
list_nom = [item for item in list_nom if "𫯲" not in item]

def get_nom_translation(input_text):
    # Find the row in the dataframe that matches the input text
    row = nom_data[nom_data["nom"] == input_text]
    
    if not row.empty:
        return {
            "modern_vn": row["viet"].values[0],
            "explanation": row["explanation"].values[0],
            "en_explanation": row["en_explanation"].values[0]
        }

# --- Sidebar / Header ---
st.title("📜 Nôm Script Translator")
st.markdown("A research tool for translating historical Nôm text to Modern Vietnamese and English.")
st.divider()

# --- Input Section ---
with st.container():
    st.subheader("Input Section")
    # nom_input = st.text_area(
    #     "Enter Nôm characters here:", 
    #     placeholder="e.g., 𡨸喃...",
    #     height=100
    # )
    
    nom_input = st.selectbox(
        "Select a Nôm character string:",
        options=list_nom,
        index=0, # Default selection is the first item
        help="Choose one entry from the list provided."
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        submit_button = st.button("Translate", type="primary", use_container_width=True)

# --- Output Section ---
if submit_button and nom_input:
    data = get_nom_translation(nom_input)
    
    st.success("### Modern Vietnamese")
    st.markdown(f"#### {data['modern_vn']}")
    
    # Explanation section with a distinct background/style
    st.markdown("---")
    with st.expander("📖 View Historical & Interpretive Explanation", expanded=True):
        # st.markdown(f"#### Vietnamese Explanation \n {data['explanation']}")
        st.success("## Vietnamese Explanation")
        st.markdown(f"{data['explanation']}")
        st.markdown("---")
        st.success("## English Explanation")
        st.markdown(f"{data['en_explanation']}")

elif submit_button and not nom_input:
    st.warning("Please enter some text to translate.")

# --- Footer ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: grey;
        font-size: 12px;
    }
    </style>
    <div class="footer">Nôm-HCI Project - Research Purposes Only</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <hr>
    <div style="text-align: center; font-size: 0.8em; color: gray;">
        Input is restricted to pre-defined strings due to current hardware constraints. 
        Future iterations of this project will integrate broader GPU support to handle real-time translation.
    </div>
    """, 
    unsafe_allow_html=True
)