# -*- coding: utf-8 -*-
"""Aplicacion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RZuBlm-dCl3AN-apz95riJRQUsSsbjec
"""

import streamlit as st

# Título de la aplicación
st.title("Calculadora Simple- Suma de Dos Números")

#Entrada de los dos números
num1=st.number_input("Ingrese el primer número",value=0.0)
num2=st.number_input("Ingrese el segundo número",value=0.0)

#Botón para calcular
if st.button("Calcular"):
  resultado=num1+num2
  st.success(f"El resultado de la suma es:{resultado}")
