import streamlit as st


# import pandas as pd

# st.markdown(' <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)
# st.markdown("""
# <div class='container-fluid text-center' style='background-color:red'>
# <div class='row'>
# <div class='col-6'><img src='C:\\Users\\ei12650\\Desktop\\streamlit\\static\\aristacarehealth.PNG'></div>
# <div class='col-6'>col</div>
# </div>
# <div>
# """ ,unsafe_allow_html=True)
# st.image("static/aristacarehealth.PNG")


from streamlit_option_menu import option_menu
st.image('static/New-logo.png',caption='tietoevryy',channels="YELLOW RED GREEN")



# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

# # 2. horizontal menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

import streamlit as st
import pandas as pd


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""

<nav class="navbar fixed-top navbar-expand-lg" style="background-color: #444e5a;margin-top:40px;height:15vh;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank" style='color:white;font-size:40px;'>Tietoevry</a>

  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#" style='color:white'>Home<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank" style='color:white'>YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style='color:white'>Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)


st.markdown("""
<iframe
  src="https://30days.streamlit.app/?embed=true"
  height="450"
  style={{ width: "100%", border: "none" }}
></iframe>
""",unsafe_allow_html=True)


footer = """
    <style>
        .footer {
            position: fixed;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: white;
            padding: 10px;
            text-align: center;
            border-top: 1px solid gray;
            color:black
        }
    </style>
    <div class="footer">
        Copyright © TietoEVRY 2021
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
