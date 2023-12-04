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

  st.header("About - Model!",divider='rainbow')
  st.write("""
    ## RandomForest
    Pada awalnya akan digunakan RandomForest untuk pengklasifikasian awal.
    Hasil dari klasifikasi akan digunakan sebagai features tambahan ke Final Model Neural Network dengan tujuan untuk menambah accuracy
    
    ### Confussion Matrix beserta ROA-Curve menggunakan RandomForest

""")
  st.image("/workspaces/machine-learning-heart-disease/Random_forest.png")
  st.write("""
    ## Neural Network
    Setelahnya, Data dari form digabung dengan hasil prediksi RandomForest akan dimasukkan ke Neural Network Sederhana
    dengan settingan 1 Dense (20 Neuron) + 1 Dense (1 Neuron Sigmoid)
           
    Didapatkan peningkatan hasil sebagai berikut :
    ### Confussion Matrix beserta ROA-Curve menggunakan Stacked RandomForest-NeuralNetwork
""")
  st.image("/workspaces/machine-learning-heart-disease/Rf_nn.png")


if __name__ == "__main__":
    run()
