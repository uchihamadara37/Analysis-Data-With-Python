# Dicoding Collection Dashboard ✨
Ini adalah tugas akhir belajar analisis data dengan python di Dicoding.Academy
## Installasi
### Kita perlu membangun environment terlebih dahulu, di sini saya menggunakan venv bawaan dari python
```bash
python -m venv myenv
```
### Untuk pengguna OS Windows bisa melakukan activasi seperti ini
```bash
myenv/Scripts/activate 
```
### Kemudian mulai cek package pip apakah sudah tersedia, kemudian lakukan installasi package atau dependencies yang akan kita perlukan dari file requirements.txt
```bash
pip --version 
pip install -r requirements.txt
```
### Apabila terkendala dengan jupyter-notebook yang tetap memakai python dari environment yang bukan dari myenv, silakan melakukan pengecekan dengan cara berikut
### lakukan pengecekan di baris pertama code file.ipynb
```bash
import sys
print(sys.executable)
```
### kemudian cek apakah itu ada di dalam direktori myenv kita atau bukan, jika iya maka jupyter-notebook telah berhasil mengenali environment kita.
### Namun jika ternyata direktory berbeda, lakukan hal ini
```bash
pip install ipykernel
python -m ipykernel install --user --name=myenv --display-name "Python dengan Nama(myenv)"
```
### kemudian ganti kernel jupyter-notebook ke kernel 'Python dengan Nama(myenv)', lalu cek kembali dengan module sys di atas.
### Kemudian untuk menjalankan web service nya silakan pakai perintah berikut
```bash
streamlit run dashboard.py
```

