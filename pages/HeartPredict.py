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
import sys
import numpy as np
import pandas as pd
import keras
import joblib
import sklearn
import tensorflow as tf

LOGGER = get_logger(__name__)


def run():
  
  # print(sklearn.__version__)
  # print("Python version:", sys.version)

  st.title("🏥Did He Have A Heart Disease 💖")
  st.write("For code and model documentation you can visit : https://www.kaggle.com/code/lyfora/heartfailure-splitmapped ")
  model_random_forest = joblib.load(
      '/workspaces/machine-learning-heart-disease/rf_model.joblib')
  gender = st.selectbox('Gender', ['Laki-Laki', 'Perempuan'])
  age = st.number_input('Umur Pasien')
  resting_heart_rate = st.number_input("Masukkan Resting heart-rate ")
  max_heart_rate = st.number_input("Maximum Heart-Rate")
  cholesterol = st.number_input("Masukkan Cholesterol")
  oldpeak = st.number_input("Masukkan Oldpeak/Depresi ST")
  chest_pain_type = st.selectbox('Tipe Sakit Dada', ['ASY', 'ATA', 'NAP', 'TA'])
  resting_ecg = st.selectbox('Tipe Resting ECG', ["Normal", "LVH", "ST"])
  angina = st.selectbox('Adakah Sakit di Dada saat Beraktifitas dengan BPM yang tinggi/Angina', [
      "Tidak", "Ya"])
  st.write(" ST segment adalah bagian dari kurva EKG yang mencerminkan periode antara depolarisasi ventrikel dan repolarisasi ventrikel.")
  st_slope = st.selectbox('Analisa ST-Slope', [
      "Flat", "Down", "Up"])


  # ---------------------------- 0 -------------------------------
  # Preprocessing data
  # Urutannya adalah
  # [Age,RestingBP,Cholesterol,MaxHR,OldPeak,Sex_F,Sex_M,ChestPainType_ASY,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,]
  minimum_scale = {
      'min_age': 28,
      'min_resting_heart_rate': 90,
      'min_cholesterol': 32.625,
      'min_max_heart_rate': 66,
      'min_oldpeak': -2.25,
      'min_sex': 0,
      'min_chest_pain_type': 0,
      'min_resting_ecg': 0,
      'min_angina': 0,
      'min_st_slope': 0
  }
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


  # ------------------ ----- 1 --Renumerisasi bila diatas dan dibawah outlier
  # Age

  if (age < minimum_scale['min_age']):
      age = minimum_scale['min_age']
  elif (age > maximum_scale['max_age']):
      age = maximum_scale['max_age']

  # Resting_Heart_Rate
  if (resting_heart_rate > minimum_scale['min_resting_heart_rate']):
      resting_heart_rate = minimum_scale['min_resting_heart_rate']
  elif (resting_heart_rate < maximum_scale['max_resting_heart_rate']):
      resting_heart_rate = maximum_scale['max_max_heart_rate']

  # Cholesterol
  if (cholesterol < minimum_scale['min_cholesterol']):
      cholesterol = minimum_scale['min_cholesterol']
  elif (cholesterol > maximum_scale['max_cholesterol']):
      cholesterol = maximum_scale['max_cholesterol']

  # Heart Rate
  if (max_heart_rate < minimum_scale['min_max_heart_rate']):
      max_heart_rate = minimum_scale['min_max_heart_rate']
  elif (max_heart_rate > maximum_scale['max_max_heart_rate']):
      max_heart_rate = maximum_scale['max_max_heart_rate']

  # Oldpeak
  if (oldpeak < minimum_scale['min_oldpeak']):
      oldpeak = minimum_scale['min_oldpeak']
  elif (oldpeak > maximum_scale['max_oldpeak']):
      oldpeak = maximum_scale['max_oldpeak']

  # ----------------- 2 ------- Categorical data to Numerical
  # Inisialisasi Categorical to Numerical
  sex_male = 0
  sex_female = 0
  chest_pain_type_ASY = 0
  chest_pain_type_ATA = 0
  chest_pain_type_NAP = 0
  chest_pain_type_TA = 0
  resting_ecg_LVH = 0
  resting_ecg_Normal = 0
  resting_ecg_ST = 0
  angina_N = 0
  angina_Y = 0
  st_slope_down = 0
  st_slope_flat = 0
  st_slope_up = 0


  # Gender
  if (gender == 'Laki-Laki'):
      sex_male = 1
  else:
      sex_female = 1

  # chest_pain_type
  if (chest_pain_type == 'ASY'):
      chest_pain_type_ASY = 1
  elif (chest_pain_type == 'ATA'):
      chest_pain_type_ATA = 1
  elif (chest_pain_type == 'NAP'):
      chest_pain_type_NAP = 1
  else:
      chest_pain_type_TA = 1

  # RestingECG
  if (resting_ecg == 'LVH'):
      resting_ecg_LVH = 1
  elif (resting_ecg == 'Normal'):
      resting_ecg_Normal = 1
  else:
      resting_ecg_ST = 1

  # Angina
  if (angina == 'Tidak'):
      angina_N = 1
  else:
      angina_Y = 1
  if (st_slope == 'Flat'):
      st_slope_flat = 1
  elif (st_slope == 'Down'):
      st_slope_down = 1
  else:
      st_slope_up = 1

  # ----- Forming a dataframe ----- #


  def predict_random_forest():
      data = np.array([age, resting_heart_rate, cholesterol, max_heart_rate, oldpeak, sex_female, sex_male, chest_pain_type_ASY, chest_pain_type_ATA,
                       chest_pain_type_NAP, chest_pain_type_TA, resting_ecg_LVH, resting_ecg_Normal, resting_ecg_ST, angina_N, angina_Y, st_slope_down, st_slope_flat, st_slope_up])
      columns = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak',
                 'Sex_F', 'Sex_M', 'ChestPainType_ASY', 'ChestPainType_ATA',
                 'ChestPainType_NAP', 'ChestPainType_TA', 'RestingECG_LVH',
                 'RestingECG_Normal', 'RestingECG_ST', 'ExerciseAngina_N',
                 'ExerciseAngina_Y', 'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up']
      X = pd.DataFrame([data], columns=columns)
      prediction = model_random_forest.predict(X)[0]

      X['Random_Forest_Prediction'] = prediction
      

      # Model Neural Network
      neural_network_model = tf.keras.models.load_model(
          '/workspaces/machine-learning-heart-disease/RandomForest_NeuralNetwork')
      valid_predict = neural_network_model.predict(X)
      if valid_predict == 1:
          st.error('🏥 Anjrot Punya Penyakit Jantung Bos 🏥 ')
      else:
          st.success(' 💖 Selamat Cuy Aman Sentosa 💖 ')
      st.write('Dengan data')
      st.dataframe(X)


  st.button('Predict', on_click=predict_random_forest)
  # ------------Testing --------------------


# Original Minimum values: [28.    90.    32.625 66.    -2.25   0.     0.     0.     0.     0.
#   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
# Original Maximum values: [ 77.    170.    407.625 202.      3.75    1.      1.      1.      1.
#    1.      1.      1.      1.      1.      1.      1.      1.      1.
#    1.      1.   ]

    


if __name__ == "__main__":
    run()
