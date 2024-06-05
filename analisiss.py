import pandas as pd
import matplotlib.pyplot as plt

# Membaca file data persediaan
data_persediaan = pd.read_csv('data_persediaan.csv')

# Menampilkan lima baris pertama data
print("Lima baris pertama data:")
print(data_persediaan.head())

# Menampilkan informasi umum tentang data
print("\nInformasi umum tentang data:")
print(data_persediaan.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(data_persediaan.describe())

# Menampilkan jumlah data yang hilang (missing values) dalam setiap kolom
print("\nJumlah data yang hilang dalam setiap kolom:")
print(data_persediaan.isnull().sum())

# Menampilkan jumlah unik dari setiap nilai dalam suatu kolom
print("\nJumlah nilai unik dalam setiap kolom:")
print(data_persediaan.nunique())

# Menampilkan tipe data dari setiap kolom
print("\nTipe data dari setiap kolom:")
print(data_persediaan.dtypes)

# Visualisasi data
# Histogram jumlah persediaan per produk
plt.figure(figsize=(10, 6))
plt.hist(data_persediaan['jumlah_persediaan'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram Jumlah Persediaan per Produk')
plt.xlabel('Jumlah Persediaan')
plt.ylabel('Frequency')
plt.show()

# Boxplot jumlah persediaan per lokasi
plt.figure(figsize=(8, 6))
plt.boxplot(data_persediaan['jumlah_persediaan'], vert=False)
plt.title('Boxplot Jumlah Persediaan per Lokasi')
plt.xlabel('Jumlah Persediaan')
plt.yticks([])
plt.show()

# Scatter plot hubungan antara jumlah persediaan dan harga
plt.figure(figsize=(8, 6))
plt.scatter(data_persediaan['jumlah_persediaan'], data_persediaan['harga'], color='green', alpha=0.5)
plt.title('Scatter Plot Jumlah Persediaan vs. Harga')
plt.xlabel('Jumlah Persediaan')
plt.ylabel('Harga')
plt.show()