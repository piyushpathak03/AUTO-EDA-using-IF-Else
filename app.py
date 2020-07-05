# # import libraries



import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt 


# # Functioning



def main():
    st.title("A simple Auto-EDA-Tool by Piyush Pathak")
    st.write(''' ***Linkedin*** : https://www.linkedin.com/in/piyushpathak03/ ''')
    st.write(''' ***Github*** : https://github.com/piyushpathak03 ''')       
    st.write(" *Drop the data in csv,txt or xls file* ")
    activities = ["EDA" , "PLOT", "ABOUT"]
    choice = st.sidebar.radio("Select Activity :" ,activities)
    

    if choice == "EDA":
        st.subheader("## *A full Exploratory Data Analysis of Data* ##")
        st.write(""" ## *Upload Your dataset* ## """)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])   
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)
            if st.checkbox("SHAPE of the data"):
                st.write(df.shape)
            if st.checkbox("SIZE of the data"):
                st.write(df.size)
            if st.checkbox("Columns"):
                st.write(df.columns)
            if st.checkbox("Select column name"):
                select_columns = st.multiselect("Select Column" , df.columns)
                new_df = df[select_columns]
                st.dataframe(new_df)
            if st.checkbox("Missing values in data"):
                st.write(df.isna().sum())
            if st.checkbox("Value counts of data"):
                column = st.selectbox("Select Columns" , df.columns)
                st.write(df[column].value_counts())
            if st.checkbox("Detailed summary of data"):
                st.write(df.describe())


    elif choice == "PLOT":
        st.subheader("##*Visualization of dataset* ## ")
        st.write(""" ## *Upload Dataset* ## """)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)

            if st.checkbox("Heatmap for Correlation"):
                st.write(sb.heatmap(df.corr() , annot = True))
                st.pyplot()

            if st.checkbox("BAR GRAPHS for analysis"):
                x_axis = st.selectbox("Select x axis:" , df.columns)
                x_axis = df[x_axis]
                y_axis = st.selectbox("Select y axis:" , df.columns)
                y_axis = df[y_axis]
                st.write(sb.barplot(x_axis , y_axis))
                st.pyplot()
                plt.xticks(rotation = 90)
                plt.legend()
                plt.grid()

            
            if st.checkbox("COUNT PLOTS"):
                c = st.selectbox("Select  axis:" , df.columns)
                c_main = df[c]
                st.write(sb.countplot(c_main))
                st.pyplot()
                plt.grid()
                plt.xticks(rotation = 90)
                plt.legend()


            if st.checkbox("PIE CHART for detailed analysis"):
                col = st.selectbox("Select 1 column" , df.columns)
                pie = df[col].value_counts().plot.pie(autopct = "%1.1f%%")
                st.write(pie)
                st.pyplot()

            
       
if __name__ == "__main__":
    main()


# In[ ]:




