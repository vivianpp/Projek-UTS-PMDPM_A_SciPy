import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

def load_model(model_file):
    model_path = os.path.join(r'C:\Users\ASUS\Documents\Projek UTS PMDPM_A_SciPy', 'BestModel_CLF_RF_SciPy.pkl')
    with open(model_path, 'rb') as f:
        return pickle.load(f)

selected = st.sidebar.radio('Pilih Analisis', 
                            ['Analisis Kategori Properti', 'Analisis Harga Properti'])

rf_model = load_model('BestModel_CLF_RF_SciPy.pkl')

def rumah_app():
    st.title("Klasifikasi Jenis Properti")
    st.write("Masukkan fitur properti untuk mengetahui kategori properti.")

    squaremeters = st.number_input("Luas Properti(m2)", min_value=0)
    numberofrooms = st.number_input("Jumlah Kamar Dalam Properti", min_value=0)
    hasyard = st.selectbox("Apakah Properti Memiliki Halaman?", ["yes", "no"])
    haspool = st.selectbox("Apakah Properti Memiliki Kolam Renang?", ["yes", "no"])
    floors = st.number_input("Jumlah Lantai Pada Properti", min_value=0)
    citycode = st.number_input("Kode Kota Properti", min_value=0)
    citypartrange = st.number_input("Rentang Wilayah Properti", min_value=0)
    numprevowners = st.number_input("Jumlah Pemilik Properti Sebelumnya", min_value=0)
    made = st.number_input("Tahun Pembuatan Properti", min_value=1900, max_value=2024)
    isnewbuilt = st.selectbox("Apakah Properti Baru / Lama?", ["yes", "no"])
    hasstormprotector = st.selectbox("Apakah Properti Memiliki Pelindung Badai?", ["yes", "no"])
    basement = st.number_input("Luas Basement Properti(m2)", min_value=0)
    attic = st.number_input("Luas Loteng Properti(m2)", min_value=0)
    garage = st.number_input("Kapasitas Garasi", min_value=0)
    hasstorageroom = st.selectbox("Apakah Properti Memiliki Ruang Penyimpanan?", ["yes", "no"])
    hasguestroom = st.number_input("Berapa Jumlah Kamar Tamu Di Properti?", min_value=0)

    angkaBinary = {"yes": 1, "no": 0}
    input_hasyard = angkaBinary[hasyard]
    input_haspool = angkaBinary[haspool]
    input_isnewbuilt = angkaBinary[isnewbuilt]
    input_hasstormprotector = angkaBinary[hasstormprotector]
    input_hasstorageroom = angkaBinary[hasstorageroom]

    if st.button("Lakukan Prediksi"):
        prediction = rf_model.predict(input_data)[0]
        kategori_map = {0: 'Basic', 1: 'Luxury', 2: 'Middle'}
        kategori_properti = kategori_map.get(prediction, "Tidak Diketahui")
        st.success(f"Kategori properti: **{kategori_properti}**")

if selected == 'Regresi':
    st.title('Regresi')

    st.write('Untuk Inputan File dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader("Masukkan File", type=["csv", "txt"])
    st.write('Untuk usia bisa menggunakan st.slider')
    Age = st.slider("Age", 0, 100)
    st.write('Untuk jenis kelamin bisa menggunakan st.radio')
    Sex = st.radio("Gender", ["Female", "Male"])
    st.write('Untuk beberapa kolom bisa menggunakan st.selectbox')
    nama_kolom = st.selectbox("Nama Kolom", ["Under", "Normal", "Over"])
    
    # Input untuk panjang dan lebar
    st.write('Untuk inputan manual bisa menggunakan st.number_input')
    panjang = st.number_input("Masukan Input", 0)
    lebar = st.number_input("Masukan Nilai Lebar", 0)
    
    alas = st.slider("Masukkan Nilai Alas", 0, 100)
    tinggi = st.slider("Masukkan Nilai Tinggi", 0, 100)
    st.write('Tombol button (Menggunakan st.button)')
    hitung = st.button("Prediksi")

    if hitung:
        luas = 0.5 * alas * tinggi
        st.write("Luas Segitiga Adalah", luas)

# Halaman ketentuan
if selected == 'Catatan':
    st.title('Catatan')
    st.write('''1. Untuk memunculkan sidebar agar tidak error ketika di run, silahkan install library streamlit option menu di terminal dengan perintah "pip install streamlit-option-menu".')
    st.write('2. Menu yang dibuat ada 2 yaitu Klasifikasi dan Regresi.''')
    st.write('3. Inputnya apa saja, sesuaikan dengan arsitektur code anda pada notebook.')
    st.write('4. Referensi desain streamlit dapat di akses pada https://streamlit.io/')
    st.write('5. Link streamlit design ini dapat di akses pada https://apputs-6qzfrvr4ufiyzhj84mrfkt7.streamlit.app/')
    st.write('''6. Library dan file requirements yang dibutuhkan untuk deploy online di github ada 5 yaitu streamlit, scikit-learn, pandas, numpy, streamlit-option-menu.''')
