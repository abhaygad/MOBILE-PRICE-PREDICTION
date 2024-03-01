import pandas as pd
import streamlit as st

opt=[]
def option ():

  option1 = st.selectbox(
    'Can you tell the primary purpose ?',
    ('Regular Use', 'Gaming', 'Vlogging', 'Photography'), key="option1")

  option2 = st.selectbox(
    'Can you tell the level of usage ?',
    ('Basic', 'Advanced '), key="option2")

  if st.button('APPLY', key="APPLY"):
    del opt[::]

    opt.append(option1)
    opt.append(option2)
  st.write('You selected:', option1, option2)

def req(new_dataframe):
    a = []
    if opt[0] == 'Regular Use':
        x_new = pd.DataFrame(new_dataframe.iloc[:, [1]].values)
        if opt[1] == 'Basic':
            del a[::]
            a.append(x_new.mean())
        else:
            a.append(x_new.max())
    elif opt[0] == 'Gaming':
        if opt[1] == 'Basic':
            x_new = pd.DataFrame(new_dataframe.iloc[:, [2]].values)
            del a[::]
            a.append(x_new.mean())
        else:
            x_new = pd.DataFrame(new_dataframe.iloc[:, [2, 4, 5]].values)
            del a[::]
            a.append(x_new.max())
    elif opt[0] == 'Vlogging':
        if opt[1] == 'Basic':
            x_new = pd.DataFrame(new_dataframe.iloc[:, [3]].values)
            del a[::]
            a.append(x_new.mean())
        else:
            x_new = pd.DataFrame(new_dataframe.iloc[:, [3, 5]].values)
            del a[::]
            a.append(x_new.max())
    elif opt[0] == 'Photography':
        if opt[1] == 'Basic':
            x_new = pd.DataFrame(new_dataframe.iloc[:, [3]].values)
            del a[::]
            a.append(x_new.mean())
        else:
            x_new = pd.DataFrame(new_dataframe.iloc[:, [4, 5]].values)
            del a[::]
            a.append(x_new.max())

    return x_new, a
