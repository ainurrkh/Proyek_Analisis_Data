import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Mengganti nama data frame sesuai kebutuhan
day = pd.read_csv('day.csv')
hour = pd.read_csv("hour.csv")
bike_sharing = day.merge(hour, on='dteday', how='inner', suffixes=('_daily', '_hourly'))

# Judul Halaman
st.title('Proyek Analisis Data: Bike Sharing Dataset')
st.header('Nama: Ainur Rokhimah')
st.subheader('Email: M008D4KX2937@bangkit.academy')
st.write('\n')
st.write('\n')

# Menampilkan data
st.subheader('Data yang Digunakan')
tab1, tab2, tab3 = st.tabs(["day.csv", "hour.csv", "Data Gabungan"])
 
with tab1:
    st.write(day)
 
with tab2:
    st.write(hour)
 
with tab3:
    st.write(bike_sharing)


# Menghapus kolom 'dteday' yang tidak diperlukan
bike_sharing.drop('dteday', axis=1, inplace=True)

# Menampilkan grafik korelasi
st.subheader('Heatmap Korelasi')
correlation_matrix = bike_sharing.corr()
fig, ax = plt.subplots(figsize=(16, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, annot_kws={"size": 10}, ax=ax)
st.pyplot(fig)


# Pertanyaan 1: Pengaruh Musim Terhadap Jumlah Peminjaman Sepeda Harian
st.subheader('Pertanyaan 1: Pengaruh Musim Terhadap Jumlah Peminjaman Sepeda Harian')
# Menghitung rata-rata jumlah sewa harian untuk setiap musim
seasonal_data = bike_sharing.groupby('season_daily')['cnt_daily'].mean()
# Mengurutkan musim berdasarkan rata-rata jumlah sewa harian secara menurun
seasonal_data_sorted = seasonal_data.sort_values(ascending=False)
# Membuat grafik batang setelah data diurutkan
st.bar_chart(seasonal_data_sorted)
with st.expander("See explanation"):
    st.write(
        """Dari grafik di atas, dapat di lihat bahwa jumlah peminjaman sepeda paling banyak terjadi pada musim gugur (Fall), sedangkan jumlah peminjaman sepeda paling sedikit terjadi pada musim semi (spring).
        """
    )
# Menambahkan nilai rata-rata yang dibulatkan pada tiap batang
for i, value in enumerate(seasonal_data_sorted):
    rounded_value = round(value)
    st.text(f'Musim: {seasonal_data_sorted.index[i]}, Rata-rata Jumlah Sewa Harian: {rounded_value}')

st.subheader('Pertanyaan 2: Perbedaan Jumlah Peminjam Sepeda Harian antara Hari Kerja dan Hari Libur')
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="workingday_daily", y="cnt_daily", data=bike_sharing, ax=ax)
plt.title("Perbedaan Jumlah Peminjam Sepeda Harian antara Hari Kerja dan Hari Libur")
plt.xlabel("Workingday")
plt.ylabel("Jumlah Sewa Sepeda Harian")
st.pyplot(fig)
with st.expander("See explanation"):
    st.write(
        """Dari grafik di atas, dapat dilihat bahwa jumlah peminjaman sepeda pada hari kerja lebih banyak dibandingkan jumlah peminjaman sepeda pada hari libur.
        """
    )

# Kesimpulan
st.subheader('Kesimpulan')
st.write('- Kesimpulan Pertanyaan 1: Jumlah peminjaman sepeda paling banyak terjadi pada musim gugur (Fall), sedangkan jumlah peminjaman sepeda paling sedikit terjadi pada musim semi (spring).')
st.write('- Kesimpulan Pertanyaan 2: Jumlah peminjaman sepeda pada hari kerja lebih banyak dibandingkan jumlah peminjaman sepeda pada hari libur.')
