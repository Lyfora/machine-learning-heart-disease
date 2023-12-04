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

  st.header("About - Isian Kolom !",divider='rainbow')
  st.warning("""
    ## Spesifikasi Data
    Data akan dibagi atas:
             
    1. Gender = Jenis Kelamin
    2. Umur = Umur Pasien
    3. Resting Heart-Rate = Detak Jantung saat aktifitas normal
    4. Maximum Heart Rate = Detak Jantung maksimal seseorang
    5. Cholesterol = Jumlah kolesterol yang dimiliki seseorang
    6. Oldpeak (ECG) = perubahan segmen ST yang terjadi setelah aktifitas berat
    7. Tipe Sakit Dada
        - ASY : Angina Tidak Stabil
        - NAP : Non-Anginal Pain / bukan disebabkan karena aliran darah
        - ATA : Unstable-Angina , sakit di dada yang berkemungkinan serangan jantung
        - TA  : Aktivitas listrik tidak normal di atrium jantung
    8. Tipe Resting ECG:
        - LVH (Left Venticular Hypetrophy) : Otot jantung ventrikel sebelah kiri menebal
        - ST : Segmen ST Tidak Teratur
        - Normal : Normal
    9. Angina : Sakit dada karena aktifitas dengan detak jantung yang tinggi
    10. ST-Slope : 
        - Flat : Normal
        - Up
        - Down
    """)

    


if __name__ == "__main__":
    run()
