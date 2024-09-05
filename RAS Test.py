# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/173AKrFXLcydLkBw7yWEKrZ4qm3N8sYdM
"""
pip install --upgrade streamlit
import streamlit as st
import pandas as pd

# Load data functions
@st.cache_data  # Caches the data to improve performance when reloading
def loadGejala():
    gejala = pd.read_csv('https://raw.githubusercontent.com/AceLysnd/SPRAS/c383eddb4751e34ef94543b969fb8d2390ec010d/tb_gejalaV2.csv', delimiter=";")
    gejala.drop('id', inplace=True, axis=1)
    return gejala

@st.cache_data
def loadPenyakit():
    penyakit = pd.read_csv('https://raw.githubusercontent.com/AceLysnd/SPRAS/c383eddb4751e34ef94543b969fb8d2390ec010d/tb_penyakitV2.csv', delimiter=";", index_col='id')
    return penyakit

@st.cache_data
def loadRule():
    rule = pd.read_csv('https://raw.githubusercontent.com/AceLysnd/SPRAS/c383eddb4751e34ef94543b969fb8d2390ec010d/tb_ruleV1.csv', delimiter=";", index_col='id')
    return rule

# Main app function
def main():
    # Load the datasets
    gejala = loadGejala()
    penyakit = loadPenyakit()
    rules = loadRule()

    # Initialize rule checking dictionary
    checkRule = {index: row.to_dict() for index, row in rules.iterrows()}

    # Display app title and instructions
    st.title("Do-bot: Sistem Pakar untuk Diagnosa Penyakit Ikan Hias Air Tawar")
    st.write("Halo! Saya adalah Do-bot. Saya akan mendiagnosa penyakit yang Anda alami!")
    st.write("Silakan jawab beberapa pertanyaan mengenai gejala yang Anda alami.")

    # Start the diagnosis process
    st.write("Apakah Anda merasakan beberapa gejala di bawah ini (y/t):")

    # Initialize response dictionary and jawaban string
    resGejala = {}
    jawaban = ""
    hitung = 0

    # Create input fields for each gejala
    for index, row in gejala.iterrows():
        gejala_name = row['gejala'].strip()
        ans = st.selectbox(f"{index + 1}. {gejala_name}?", ['t', 'y'], index=0)

        # Update resGejala dictionary based on the answer
        resGejala[row['kode']] = 1 if ans == 'y' else 0

        # Add to jawaban if the answer is 't'
        if ans == 't':
            hitung += 1
            jawaban += f"{hitung}. {penyakit.loc[index + 1, 'info']};\n"

    # Display diagnosis results
    if st.button("Lihat Hasil Diagnosa"):
        st.write("### Perlu ditambahkan untuk Sistem RAS agar berhasil dalam budidaya ikan hias air tawar:")
        st.write(jawaban)

# Run the app
if __name__ == "__main__":
    main()
