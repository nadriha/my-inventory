# steves-inventory🌻🌼
app link: https://steves-inventory.adaptable.app/main

## Implementasi Model-View-Template (MVT) pada Django
**Steps:**
1.  Membuat proyek Django baru  
    * Membuat  dierktori dengan nama aplikasi yang diinginkan dan membuat file   dependencies seperti file [requirements](/requirements.txt) yang berisi kumpulan modul/library framework yang diperlukan.  
    * Menjalankan virtual environtment dengan menjalankan perintah `env\Scripts\activate.bat`.  
    * Menginstal dependencies tersebut dengan menjalankan perintah `pip install -r requirements.txt`.  
    * Setelah menginstall dependencies tersebut, buat poyek Django dengan perintah `django-admin startproject my_inventory .`
2.  Membuat aplikasi dengan nama main pada proyek tersebut.  
    Menjalankan perintah `python manage.py startapp main`. Django akan membuat direktori [main](/main) yang merupakan sebuah direktori aplikasi untuk mengkonfigurasi fungsionalitas pada aplikasi tersebut. Pada direktori tersebut juga terdapat file-file seperti  `models.py`, `views.py`, `urls.py`, dsb.
3.  Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Agar dapat menjalankan aplikasi main, dalam `settings.py` tedapat variable `INSTALLED_APPS` dan tambahkan `main` ke dalam isi list tersebut. Hal tersebut berfungsi untuk mengakses model, tampilan, fungsi, dll pada aplikasi `main`
4.  Membuat model pada aplikasi main dengan nama Item dan memiliki atribut.  
    *  File `models.py` dalam direktori main membuat model `Item` yang menerapkan `models.Model` yang merupakan kelas dasar untuk mendefinisikan model pada Django.
    * Pada class tersebut, tambahkan atribut-atribut seperti `name`, `amount`, dan `description`
    * Sertakan pula tipe data yang ssesuai seperti `CharField`, `IntegerField`, dan `TextField`.
    * Agar perubahan pada model dapat dideteksi dalam proyek, jalankan `python manage.py makemigrations` untuk mekciptakan perubahan model.
    * Jalankan perintah `python manage.py migrate` untuk mengimplementasikan perubahan model tersebut.
5.  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML
    * Tambahkan kode `from django.shortcuts import render` pada file `views.py` dalam folder `main`. kode tersebut berguna untuk me-render tampilan HTML menggunakan data yang ada
    * Membuat fungsi `show_main` pada `views.py` yang menerima parameter `request`
    * Tambahkan variable berupa directory berisi data yang akan diteruskan ke tampilan HTML
    * Fungsi `show_main` tersebut mereturn fungsi render yang meneruskan 3 argumen, yaitu `request`, `main.html`(nama file html yang menjadi target untuk merender data tersebut), dan `context`.
6.  Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
    * Membuat file `urls.py` dalam folder `main`
    * Mengimport `path` dari library `django.urls` dan fungsi `show_main` dari file views.py yang berada di main.
    * Tambahkan variable `urlpatterns` yang berbentuk list.
    * Tambahkan pola URL menggunakan fungsi `path` 
    * Pada parameter fungsi path,  masukan fungsi `show_main` yang sudah di import pada fungsi tersebut.
7.  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat.
    * Sign in Adaptable menggunakan GitHub, dan sambungkan repository
    * Pilih repository yag akan dibuat menjadi web
    * Pilih `Python App Template` sebagai template deployment dan `PostgreSQL`sebagai tipe basis data yang akan digunakan.
    * Sesuaikan python yang digunakan pada perangkat
    * Tambahkan `Start Command` yang berisi dengan perintah `python manage.py migrate && gunicorn my_inventory.wsgi`
    * Ceklis `HTTP Listener on PORT`
    * Klik `Deploy App`


![alt text](/basic-django.png)

**Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
* Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi dianjurkan untuk menggunakan virtual environment karena dengan menggunakan virtual environment, kita membuat lingkungan yang terisolasi yang tidak saling terkait dan dapat diaktifkan atau dinonaktifkan sesuai kebutuhan. Hal tersebut bisa digunakan untuk mengelola dependencies proyek secara terpisah dan memungkinkan menggunakan versi Django dan Python yang berbeda.

**Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
* 