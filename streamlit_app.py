import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Sampling", ["DeskKat", 'DeskNum','AnakatTB','AnakatB','AnumTB','AnumB'], 
        icons=[], menu_icon=[], default_index=0)
    st.write(f"${'Z_\\alpha='}$1.96")
    st.write(f"${'Z_\\beta='}$0.84")
    st.write(f"${'d='}$Presisi")  

with st.container():
    if selected=="DeskKat":
        st.latex(r'''n=\frac{Z_\alpha.P. Q}{d^2} ''') 
        st.write(f"${'P='}$ variabel yang diteliti")        
        st.write(f"${'Q=1-P'}$")
        Za=st.text_input('$ Z_\\alpha $',value="1.96") 
        P=st.text_input('$ P $',value=".8")    
        Q=st.text_input('$ Q $',value=".2")
        d=st.text_input('$ d $',value=".1")      
        st.write(eval(Za)*eval(P)*eval(Q)/eval(d)**2)
    elif (selected=="DeskNum"):
        st.latex(r'''n=\Bigg(\frac{Z_\alpha.S. Q}{d}\Bigg)^2''') 
    elif (selected=="AnakatTB"):
        st.latex(r'''n=\Bigg(\frac{Z_\alpha \sqrt{2PQ} + Z_\beta \sqrt{P_1Q_1+P_2Q_2} }{P_1-P_2}\Bigg)^2''') 
    elif (selected=="AnakatB"):
        st.latex(r'''n=\frac{Z_\alpha.P. Q}{v^2} ''') 
    elif (selected=="AnumTB"):
        st.latex(r'''n=\frac{Z_\alpha.P. Q}{v^2} ''') 
    elif (selected=="AnumB"):
        st.latex(r'''n=\frac{Z_\alpha.P. Q}{v^2} ''')   
        

    #selected

# horizontal Menu
    #selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    #icons=['house', 'cloud-upload', "list-task", 'gear'], 
   # menu_icon="cast", default_index=0, orientation="horizontal")
   # selected2
