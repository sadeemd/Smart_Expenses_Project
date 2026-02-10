import streamlit as st
import pandas as pd

# عنوان التطبيق
st.title("Project Expenses - Prototype App")

# رفع ملف CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # قراءة الملف
    df = pd.read_csv(uploaded_file)

    # عرض الجدول
    st.subheader("Data Preview")
    st.dataframe(df)
s
    # اختيار عمود رقمي للرسم
    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:
        column_to_plot = st.selectbox(
            "Choose a numeric column to plot",
            numeric_columns
        )

        st.subheader("Simple Plot")
        st.line_chart(df[column_to_plot])
    else:
        st.info("No numeric columns available for plotting.")

    # زر تحميل CSV
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="expenses_data.csv",
        mime="text/csv"
    )
