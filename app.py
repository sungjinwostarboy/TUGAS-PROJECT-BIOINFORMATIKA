import streamlit as st
from alignments import needleman_wunsch, smith_waterman
from utils import read_fasta
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("🔬 Pencocokan Urutan Biologis")
st.write("Aplikasi ini membandingkan dua urutan DNA atau protein untuk melihat seberapa mirip mereka satu sama lain.")

# Upload File
file1 = st.file_uploader("📄 Upload Urutan Pertama (format .txt atau .fasta)", type=["txt", "fasta"])
file2 = st.file_uploader("📄 Upload Urutan Kedua (format .txt atau .fasta)", type=["txt", "fasta"])

if file1 and file2:
    seq1 = read_fasta(file1)
    seq2 = read_fasta(file2)

    st.write(f"📌 Panjang Urutan 1: **{len(seq1)}** karakter")
    st.write(f"📌 Panjang Urutan 2: **{len(seq2)}** karakter")

    # Pilihan algoritma
    algo = st.radio("🔧 Pilih Cara Perbandingan Urutan:", 
                    ["Global (cocokkan seluruh urutan)", "Local (cocokkan bagian yang paling mirip)"])

    match = st.number_input("✅ Skor Jika Sama", value=1)
    mismatch = st.number_input("❌ Skor Jika Beda", value=-1)
    gap = st.number_input("➖ Penalti Jika Ada Celah", value=-2)

    if st.button("🚀 Jalankan Perbandingan"):
        if algo.startswith("Global"):
            matrix, score = needleman_wunsch(seq1, seq2, match, mismatch, gap)
        else:
            matrix, score = smith_waterman(seq1, seq2, match, mismatch, gap)

        st.success(f"💡 Hasil Skor Kemiripan: **{score}**")

        st.write("📖 **Penjelasan Hasil (Bahasa Sederhana):**")
        st.markdown(f"""
        - Semakin tinggi skor, berarti kedua urutan **semakin mirip**.
        - Skor positif menunjukkan banyak bagian dari urutan yang **sama**.
        - Jika skor rendah atau negatif, maka urutannya **berbeda atau tidak cocok** satu sama lain.
        - Cara pencocokan yang kamu pilih adalah **"{algo}"**.
        """)

        # Visualisasi Heatmap
        st.write("📊 Gambar di bawah menunjukkan seberapa cocok setiap bagian dari kedua urutan.")
        fig, ax = plt.subplots()
        sns.heatmap(np.array(matrix), ax=ax, cmap="YlGnBu", cbar_kws={'label': 'Skor Kecocokan'})
        ax.set_xlabel("Urutan Kedua")
        ax.set_ylabel("Urutan Pertama")
        st.pyplot(fig)
else:
    st.info("Silakan upload dua file urutan untuk memulai.")

