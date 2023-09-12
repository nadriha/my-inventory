# steves-inventory🌻🌼
app link: https://steves-inventory.adaptable.app/main

## Implementasi Model-View-Template (MVT) pada Django
**Steps:**
1.  Membuat proyek Django baru  
    Membuat  dierktori dengan nama aplikasi yang diinginkan dan membuat file dependencies seperti file [requirements](/requirements.txt) yang berisi kumpulan modul/library/framework yang diperlukan.  
    Menjalankan virtual environtment dengan menjalankan perintah `env\Scripts\activate.bat`. Menginstal dependencies tersebut dengan menjalankan perintah `pip install -r requirements.txt`. Setelah menginstall dependencies tersebut, buat poyek Django dengan perintah `django-admin startproject my_inventory .`
2.  Membuat aplikasi dengan nama main pada proyek tersebut.  
    Menjalankan perintah `python manage.py startapp main`. Django akan membuat direktori [main](/main) yang merupakan sebuah direktori aplikasi untuk mengkonfigurasi fungsionalitas pada aplikasi tersebut. Pada direktori tersebut juga terdapat file-file seperti  `models.py`, `views.py`, `urls.py`, dsb.
3.  Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Agar dapat menjalankan aplikasi main, dalam `settings.py` tedapat variable `INSTALLED_APPS` dan tambahkan main ke dalam isi list tersebut. Hal tersebut berfungsi untuk mengakses model, tampilan, fungsi, dll pada aplikasi `main`
4.  Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut  
    `name` sebagai nama item dengan tipe CharField.  
    `amount` sebagai jumlah item dengan tipe IntegerField.  
    `description` sebagai deskripsi item dengan tipe TextField.
    


