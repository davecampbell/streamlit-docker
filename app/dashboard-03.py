import streamlit as st

import pandas as pd
import numpy as np
# make sure you get the same data each time
np.random.seed(1)


def build_dataframe():
    # create two columns with random data
    data = {
        'impressions': np.random.randint(low=111, high=10000, size=100),
        'clicks': np.random.randint(low=0, high=1000, size=100)
    }

    df = pd.DataFrame(data)
    # add a date column and calculate the weekday of each row
    df['date'] = pd.date_range(start='1/1/2018', periods=100)
    df['weekday'] = df['date'].dt.dayofweek

    return df


st.title('Streamlit dashboard')

selected_kpi = st.selectbox(
        'Select a KPI: ',
        ['clicks', 'impressions']
    )

df = build_dataframe()

st.dataframe(df.describe())
