import streamlit as st
def X1(ht): # usia
    if (ht<27.5):
        return 1
    elif(ht>=27.5 and ht!=0):
        return 0
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
        return 130
    elif(ht>=2.36 and ht!=0):
        return -60
    else: 
        return 0 
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
    color:blue;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Prediksi Disfungsi Kardiak <br> pada pasien Graves Disease dalam terapi ATD</p>', unsafe_allow_html=True)    
def X1(ht): # usia
    if (ht<27.5):
        return 1
    elif(ht>=27.5 and ht!=0):
        return 0
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
        return 130
    elif(ht>=2.36 and ht!=0):
        return -60
    else: 
        return 0  
def hitung(x1,x2,x3,x4,x5,x6,x8,x9,x10,x11,x12):
    total=X1(x1)+X2(x2)+X3(x3)+X4(x4)+X5(x5)+X6(x6)+X8(x8)+X9(x9)+X10(x10)+X11(x11)+X12(x12)+18
    if total<20.5:
       return "Kejadian Disfungsi Kardiak : Ya"
    else:
        return "Kejadian Disfungsi Kardiak : Tidak"
left,midle,right=st.columns([2,2,2])
with left:    
    x1=float(st.text_input('Umur(tahun)',"13.3"))
    x2=st.radio('Jenis Kelamin',["L", "P"],horizontal=True,index=1)
    x3=st.radio('Hipertensi',["Ya", "Tidak"],horizontal=True,index=1)
    x4=float(st.text_input('Lama gejala hilang setelah berobat(bulan)',"3.3",help="palpitasi,sesak nafas,nyeri data dan tremor"))
with midle:
    x5=float(st.text_input('Lama terapi ATD(bulan)',"12.2"))
    x6=float(st.text_input('Lama nadi <90 x/menit setelah minum obat(bulan)',"3.4"))
    #x7=st.radio('Pitting Oedema',["Ya", "Tidak","NA"],horizontal=True,index=1)       
    x8=float(st.text_input('Rerata Tekanan Darah Sistolik(mmHg)',"104"))
    x9=float(st.text_input('Rerata Tekanan Darah Diastolik(mmHg)',"88"))
with right:
    x10=float(st.text_input('Rerata Mean Arterial Pressure(mmHg)',"67"))
    x11=float(st.text_input('Rerata Indek Massa Tubuh(Kg/m2)',"22.2"))   
    x12=float(st.text_input('Kadar fT4 awal(ng/dl)',"2.8")) 
    st.write(X1(x1),X2(x2),X3(x3),X4(x4),X5(x5),X6(x6),X8(x8),X9(x9),X10(x10),X11(x11),X12(x12),18)
    st.button("Prediksi")
    st.write(hitung(x1,x2,x3,x4,x5,x6,x8,x9,x10,x11,x12))            
