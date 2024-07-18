import streamlit as st
def X1(ht): # usia
    if (ht>=27.5):
        return 13
    elif(ht<27.5 and ht!=0):
        return -3
    else: 
        return 0
def X2(jk): #jenis kelamin
    if (jk=='L'):
        return -48
    elif(jk=='P'):
        return 14
    else:
        return 0

def X3(ht): #HT
    if (ht=='Ya'):
        return 1
    elif(ht=='Tidak'):
        return 0
    else:
        return 0

def X4(ht):  #lama setelah
    if (ht<5.5 and ht!=0.0):
        return -10
    elif(ht>=5.5):
        return 79
    else:
        return 0

def X5(ht):  #lama terapi
    if (ht<22.5 and ht!=0.0):
        return -109
    elif(ht>=22.5):
        return 36
    else:
        return 0
    
def X6(ht): #LHR
    if (ht<4.5):
        return -9
    elif(ht>=4.5 and ht!=0):
        return 25
    else:
        return 0

def X7(ht): #PE
    if (ht=='Ya'):
        return -12
    else:
        return 1
 
def X8(ht): #rtds
    if (ht<126.5):
        return -17
    elif(ht>=126.5 and ht!=0):
        return 28
    else:
        return 0

def X9(ht): #rtdd
    if (ht<79.5):
        return 32
    elif(ht>=79.5 and ht!=0):
        return -95
    else:
        return 0
def X10(ht): #map
    if (ht<90.6):
        return 6
    elif(ht>=90.6 and ht!=0):
        return -8
    else:
        return 0

def X11(ht): #imt
    if (ht<22.7):
        return 16
    elif(ht>=22.7 and ht!=0):
        return -32
    else: 
        return 0

def X12(ht):
    if (ht<2.36):
        return 131
    elif(ht>=2.36 and ht!=0):
        return -60
    else: 
        return 0 
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Prediksi Disfungsi Kardiak <br> pada pasien Graves Disease dalam terapi ATD</p>', unsafe_allow_html=True)    
left,midle,right,right1=st.columns([2 ,2,2,3])
with left:    
    x1=st.text_input('Umur (tahun)',"")   
    x2=st.radio('Jenis Kelamin',["L", "P"],horizontal=True,index=1)
    x3=st.radio('Hipertensi',["Ya", "Tidak","NA"],horizontal=True,index=1)
    x4=st.text_input('Lama gejala hilang setelah berobat (bulan)',"")

with midle:
    x5=st.text_input('Lama terapi ATD (bulan)',"")
    x6=st.text_input('Lama nadi <90 x/menit setelah minum obat (bulan)',"")
    #x7=st.radio('Pitting Oedema',["Ya", "Tidak","NA"],horizontal=True,index=1)       
    x8=st.text_input('Rerata Tekanan Darah Sistolik',"")
    x9=st.text_input('Rerata Tekanan Darah Distolik',"")
with right:
    x10=st.text_input('Rerata Mean Arterial Pressure',"")
    x11=st.text_input('Rerata Indek Massa Tubuh',"")    
    x12=st.text_input('Kadar fT4 awal',"")      

    if (x1==''):
        x1=0
    else:
        x1=float(x1)

    if (x4==''):
            x4=0
    else:
        x4=float(x4)       

    if (x5==''):
        x5=0
    else:
        x5=float(x5)    
 

    if (x6==''):
        x6=0
    else:
        x6=float(x6)  
    if (x8==''):
        x8=0
    else:
        x8=float(x8)              

    if (x9==''):
        x9=0
    else:
        x9=float(x9)    

    if (x10==''):
        x10=0
    else:
        x10=float(x10)    

    if (x11==''):
        x11=0
    else:
        x11=float(x11)  
    if (x12==''):
        x12=0
    else:
        x12=float(x12)  
with right1:
    total=X1(x1)+X2(x2)+X3(x3)+X4(x4)+X5(x5)+X6(x6)+X8(x8)+X9(x9)+X10(x10)+X11(x11)+X12(x12)+18
    st.write(X1(x1),X2(x2),X3(x3),X4(x4),X5(x5),X6(x6),X8(x8),X9(x9),X10(x10),X11(x11),X12(x12),18)
   
    st.write('skor total',total)   
    x12=st.button("Prediksi")

    if x12:
        if total>10.5:
                st.write('Disfungsi Kardiak : Ya')
        else:
                st.write('Disfungsi Kardiak : Tidak')
