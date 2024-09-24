import streamlit as st
import paho.mqtt.publish as publish
import time
MQTT_SERVER = "broker.hivemq.com"
MQTT_PORT = 1883

def pesan(topic, message):
    try:
        publish.single(topic, message, hostname=MQTT_SERVER, port=MQTT_PORT)
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("""
    <style>
    .title {
        color: #1e59ff;
        font-weight: bold;
        font-size: 50px;  
        margin-bottom: 10px;
    }

    .sub-header {
        color: black;  
        font-size: 20px;  
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .stButton > button {
        background-color: white;
        color: #1e90ff;
        padding: 10px 20px;
        text-align: center;
        height: 50px;
        width: 75%;
        text-decoration: none;
        font-size: px;
        cursor: pointer;
        border-radius: 30px;
        border: 2px solid #1e90ff;
        transition-duration: 0.4s;
    }
    .stButton > button:hover {
        color: white;
        background-color: #1e90ff;
        border: 2px solid #1e57ff; 
    }
    .stButton > button:active {
        color: white;
        background-color: #1e57ff;
        border: 2px solid #1e90ff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h2 style="color : #1e90ff; font-family : Arial;" align="center">EQUITO CONTROL</h2><br>', unsafe_allow_html=True)
st.subheader('KARYA SISWA ELEKTRO SMK NEGERI 2 PEKANBARU')


tab1, tab2, tab3, tab4, tab5 = st.tabs(["TERMINAL 1", "TERMINAL 2","TERMINAL 3","TERMINAL 4","Tentang"])
with tab1:
    st.markdown('<p class="sub-header">Terminal 1</p>', unsafe_allow_html=True)
    if st.button("Always ON"):
        pesan("relay/kontrol", "1")

    if st.button("OFF"):
        pesan("relay/kontrol", "-1")
    
    timer = st.slider(" ", 0, 1000, 15)
    detik = timer * 60
    proses = st.progress(0)
    if st.button("Setel Timer"):
        pesan("relay/kontrol", "1") 
        for tunggu in range(detik, -1, -1):
            proses.progress((detik - tunggu) / detik)
            time.sleep(1)
        st.success("Timer telah selesai.") 
        pesan("relay/kontrol", "-1") 

with tab2:
    if st.button("Always ON  "):
        pesan("relay/kontrol", "2")

    if st.button("OFF  "):
        pesan("relay/kontrol", "-2")
    
    timer = st.slider("  ", 0, 1000, 15)
    detik = timer * 60
    proses = st.progress(0)
    if st.button("Setel Timer  "):
        pesan("relay/kontrol", "2") 
        for tunggu in range(detik, -1, -1):
            proses.progress((detik - tunggu) / detik)
            time.sleep(1)
        st.success("Timer telah selesai.") 
        pesan("relay/kontrol", "-2") 

with tab3:
    if st.button("Always ON    "):
        pesan("relay/kontrol", "3")

    if st.button("OFF    "):
        pesan("relay/kontrol", "-3")
    
    timer = st.slider("   ", 0, 1000, 15)
    detik = timer * 60
    proses = st.progress(0)
    if st.button("Setel Timer    "):
        pesan("relay/kontrol", "3") 
        for tunggu in range(detik, -1, -1):
            proses.progress((detik - tunggu) / detik)
            time.sleep(1)
        st.success("Timer telah selesai.") 
        pesan("relay/kontrol", "-3") 

with tab4:
    if st.button("Always ON     "):
        pesan("relay/kontrol", "4")

    if st.button("OFF     "):
        pesan("relay/kontrol", "-4")
    
    timer = st.slider("    ", 0, 1000, 15)
    detik = timer * 60
    proses = st.progress(0)
    if st.button("Setel Timer     "):
        pesan("relay/kontrol", "4") 
        for tunggu in range(detik, -1, -1):
            proses.progress((detik - tunggu) / detik)
            time.sleep(1)
        st.success("Timer telah selesai.") 
        pesan("relay/kontrol", "-4") 

with tab5:
    st.subheader("EQUITO KONTROL")
    st.write("Tim inovasi kami, terdiri dari Reygan, Ilham, dan Habib, telah berhasil mengembangkan alat pengendali stopkontak cerdas yang terhubung dengan website, memungkinkan pengguna untuk mengatur dan memantau penggunaan listrik secara real-time, memberikan solusi efisien dan ramah lingkungan untuk kebutuhan energi sehari-hari.")

    st.subheader("TIM PENGEMBANG")
    st.write("1. ReyganNS")
    st.write("2. M.ILHAM.A")
    st.write("3. Habib")



