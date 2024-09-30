import streamlit as st
st.markdown('<p class="big-font">Prediksi Banjir pada Sungai WULAN berbasis Hidden Markov Model</p>', unsafe_allow_html=True)    
def hitung(EU,ED,Q):
    with LR:
       st.write("Menurut Analitis")       
       if (Q<800 ):
           st.write("Normal")
       elif (Q>1100 or EU==ED or ED>EU):
           st.write("Banjir")
       else:
           st.write("Pra Banjir")
    with RL:
       st.write("Menurut HMM")       
       if (Q<800):
           st.write("Normal") 
       elif (Q>1100 or EU==ED or ED>EU):
           st.write("Banjir")
       else:
           st.write("Pra Banjir") 
    with right:
         st.write("Validasi")    
         st.write("Akurasi")  
         st.write(" Normal")
         st.write(" Pra Banjir")  
         st.write(" Banjir")
left,LR,RL,right=st.columns([2,2,2,2])
with left:    
    with st.form("Formulir"):
       EU=float(st.text_input('Elevation Up, cm',"16.30"))
       ED=float(st.text_input('Elevation Down, cm',"16.52"))
       Q=float(st.text_input('Debit Serang,  M3/s',"900"))
       st.form_submit_button("Prediksi Banjir",on_click=hitung(EU,ED,Q))  
st.markdown('<p class="small-font">Joko Sutopo, PhD</p>', unsafe_allow_html=True)          
