import streamlit as st
import math as mt

judul = (
    'Hitung bangun datar dan bangun ruang \n'
    'Berikut Pilihan bangun datar dan bangun ruang : \n'
    ' 1. Persegi Panjang \n'
    ' 2. Segitiga \n'
    ' 3. Lingkaran \n'
    ' 4. Balok \n'
    ' 5. Kubus \n'
    ' 6. Tabung \n'
).upper()

st.title(judul)

bangun = st.text_input("Masukan Kode salah satu bangun yang ingin kamu hitung", placeholder="Contoh : 1")

if bangun == "1":
    panjang = st.number_input("Masukan Panjang", min_value=0, key='panjang')
    lebar = st.number_input("Masukan Lebar", min_value=0, key='lebar')
elif bangun == "2":
    alas = st.number_input("Masukan Alas", min_value=0, key='alas')
    tinggi = st.number_input("Masukan Tinggi", min_value=0, key='tinggi')
elif bangun == "3":
    jari = st.number_input("Masukan jari-jari", min_value=0, key='jari')
elif bangun == "4":
    panjang = st.number_input("Masukan Panjang", min_value=0, key='panjang')
    lebar = st.number_input("Masukan Lebar", min_value=0, key='lebar')
    tinggi = st.number_input("Masukan Tinggi", min_value=0, key='tinggi')
elif bangun == "5":
    sisi = st.number_input("Masukan Sisi", min_value=0, key='sisi')
elif bangun == "6":
    jari = st.number_input("Masukan jari-jari", min_value=0, key='jari')
    tinggi = st.number_input("Masukan Tinggi", min_value=0, key='tinggi')
    

if st.button("Hitung Bangun"):
    if bangun == "1":
        p = st.session_state.panjang
        l = st.session_state.lebar
        luas_persegi_panjang = p*l
        keliling_persegi_panjang = (2*p)+(2*l)
        st.write(f"Luas Persegi Panjang = {luas_persegi_panjang}")
        st.write(f"Keliling Persegi Panjang = {keliling_persegi_panjang}")
    elif bangun == "2":
        a = st.session_state.alas
        t = st.session_state.tinggi
        luas_segitiga = (a*t)/2
        keliling_segitiga= (mt.sqrt(((a/2)*(a/2))+(t*t)))+(mt.sqrt(((a/2)*(a/2))+(t*t)))+a
        sisi_miring = (mt.sqrt(((a/2)*(a/2))+(t*t)))
        st.write(f"Sisi Miring Segitigas = {sisi_miring}")
        st.write("Rumus Luas Segitigas = (Alas x Tinggi)/2")
        st.write(f"Luas Segitiga = {luas_segitiga}")
        st.write(f"Keliling Segitiga = {keliling_segitiga}")
    elif bangun == "3":
        phi = 3.142857142857143
        r = st.session_state.jari
        luas_lingkaran = r*r*phi
        keliling_lingkaran = 2*r*phi
        st.write(f"Luas Lingkaran = {luas_lingkaran}")
        st.write(f"Keliling Lingkaran = {keliling_lingkaran}")
    elif bangun == "4":
        p = st.session_state.panjang
        l = st.session_state.lebar
        t = st.session_state.tinggi
        luas_balok = 2*(p*l + l*t + p*t)
        volume_balok = p*l*t
        st.write(f"Luas Balok = {luas_balok}")
        st.write(f"Volume Balok = {volume_balok}")
    elif bangun == "5":
        s = st.session_state.sisi
        luas_kubus = 6*s*s
        volume_kubus = s*s*s
        st.write(f"Luas Kubus = {luas_kubus}")
        st.write(f"Volume Kubus = {volume_kubus}")
    elif bangun == "6":
        phi = 3.142857142857143
        r = st.session_state.jari
        t = st.session_state.tinggi
        luas_tabung = (2*phi*r*r)+(2*phi*r*t)
        volume_tabung = phi*r*r*t
        st.write(f"Luas Tabung = {luas_tabung}")
        st.write(f"Volume Tabung = {volume_tabung}")
    else:
        st.write("Kode yang Anda masukan tidak ada di dalam pilihan")

