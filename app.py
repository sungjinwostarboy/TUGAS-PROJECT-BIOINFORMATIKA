import streamlit as st
from alignments import needleman_wunsch, smith_waterman
from utils import read_fasta
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("🔬 Aplikasi Pencocokan Urutan Biologis")

uploaded_file1 = st.file_uploader("Upload File FASTA Urutan 1", type=["fasta", "txt"])
uploaded_file2 = st.file_uploader("Upload File FASTA Urutan 2", type=["fasta", "txt"])

if uploaded_file1 and uploaded_file2:
    seq1 = read_fasta(uploaded_file1)
    seq2 = read_fasta(uploaded_file2)

    st.write(f"Urutan 1 ({len(seq1)} nt): {seq1[:50]}...")
    st.write(f"Urutan 2 ({len(seq2)} nt): {seq2[:50]}...")

    algo = st.radio("Pilih Algoritma:", ["Global Alignment (Needleman-Wunsch)", "Local Alignment (Smith-Waterman)"])
    match = st.number_input("Skor Match", 1)
    mismatch = st.number_input("Penalti Mismatch", -3)
    gap = st.number_input("Penalti Gap", -2)

    if st.button("Jalankan Alignment"):
        if algo.startswith("Global"):
            score_matrix, final_score = needleman_wunsch(seq1, seq2, match, mismatch, gap)
        else:
            score_matrix, final_score = smith_waterman(seq1, seq2, match, mismatch, gap)
        
        st.success(f"Skor Alignment: {final_score}")
        
        fig, ax = plt.subplots()
        sns.heatmap(np.array(score_matrix), ax=ax, cmap="YlGnBu")
        st.pyplot(fig)
