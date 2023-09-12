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



