import streamlit as st
import pandas as pd


def main():
    menu = ["Home", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Decode QR")

        excel_file = st.file_uploader("Upload Image", type=['xlsx', 'xls'])

        if excel_file is not None:
            df = pd.read_excel(excel_file, index_col=0)
            st.dataframe(df)

    else:
        st.subheader("About")


if __name__ == '__main__':
    main()
