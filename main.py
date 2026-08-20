import time

import pyautogui
import streamlit as st

import pywhatkit as kit


import pandas as pd






st.title("WhatsApp Automation")


url=st.text_input(label="Enter Your Url Here " ,value="https://www.syedmuhammadarsalanshah.com/")
msg=st.text_area(label="Enter Your Url Here " ,value="Follow my sir on github")

meriUploadFile=st.file_uploader("Upload a file ",type=["xlsx"])

if meriUploadFile is not None:
    st.write("Contacts are uploaded ")

    df=pd.read_excel(meriUploadFile)

    st.dataframe(df)

    if st.button("send message "):

        for i , row in df.iterrows():
            phonNumber=f"+92{row["Phone"]}"
            customMessage=f"{msg}\n{url}"


            kit.sendwhatmsg_instantly(phone_no=phonNumber, message=customMessage,wait_time=10)

            time.sleep(10)
            pyautogui.press("enter")

            time.sleep(10)
            pyautogui.press("enter")

st.success("copyright alright reserved by smasb")
