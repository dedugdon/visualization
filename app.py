import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("📊 Bar Chart Generator")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)

        st.subheader("Preview of Uploaded Data")
        st.write(df.head())

        # Select numeric columns
        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        if len(numeric_cols) < 1:
            st.warning("No numeric columns found in the file to plot a bar chart.")
        else:
            # Let user choose x and y columns
            x_col = st.selectbox("Select X-axis column", options=df.columns)
            y_col = st.selectbox("Select Y-axis column", options=numeric_cols)

            st.subheader("Bar Chart")

            # Generate bar chart
            fig, ax = plt.subplots()
            ax.bar(df[x_col], df[y_col], color='skyblue')
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f"{y_col} by {x_col}")
            plt.xticks(rotation=45)

            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload a CSV file to proceed.")
