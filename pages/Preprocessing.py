# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)


def run():
  
  # print(sklearn.__version__)
  # print("Python version:", sys.version)

  st.header("Preprocessing",divider='rainbow')
  st.write("""
        ## Outlier Preprocessing
           Untuk mengatasi outlier, akan dilakukan Winsorizing yakni mengubah diluar IQR menjadi nilai IQR nya
           bila diatas upper IQR akan dimasukkan ke Upper IQR dan bila dibawah lower IQR akan dimasukkan ke lower IQR
           """)
  st.write("Boxplot sebelum Winsorizing")
  st.image("/workspaces/machine-learning-heart-disease/boxplot_before.png")
  st.write("Boxplot setelah Winsorizing")
  st.image("/workspaces/machine-learning-heart-disease/boxplot_after.png")
  st.header("Karakter Data",divider='rainbow')
  st.image("/workspaces/machine-learning-heart-disease/df_coor.png",caption='Korelasi antar fitur')
  st.image('/workspaces/machine-learning-heart-disease/df_pca.png',caption='Using PCA')
  
  st.header("Normalization",divider='rainbow')
  st.write("""
        ## Min-Max Normalization
        Untuk normalisasi akan menggunakan MinMax dengan alasan masing-masing data cukup independen serta distribusinya yang rendah

        ### Minimum
        Untuk masing-masing kolom mempunyai nilai minimum sebagai :
            
           - Age : 28
           - resting heart : 90
           - cholesterol = 32.625
           - max heart rate : 66
           - oldpeak = -2.25

        ### Maximum
        Untuk masing-masing kolom mempunyai nilai maksimum sebagai :
            
           - Age : 77
           - resting heart : 170
           - cholesterol = 407.625
           - max heart rate : 202
           - oldpeak = 3.75
""")


  maximum_scale = {
      'max_age': 77,
      'max_resting_heart_rate': 170,
      'max_cholesterol': 407.625,
      'max_max_heart_rate': 202,
      'max_oldpeak': 3.75,
      'max_sex': 1,
      'max_chest_pain_type': 1,
      'max_resting_ecg': 1,
      'max_angina': 1,
      'max_st_slope': 1
  }
if __name__ == "__main__":
    run()
