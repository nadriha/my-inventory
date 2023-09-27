# my-inventory🌻🌼
app link: https://steves-inventory.adaptable.app/main

<details>
<summary>Tugas 4</summary>

#### Implementasi Autentikasi, Session, dan Cookies pada Django
**Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**  
Django UserCreationForm adalah tool yang dapat membuat login pengguna dengan cara mengimpor authentication modul pada django. UserCreationForm ini digunakan untuk membuat user baru dalam sebuah aplikasi django dengan sebuah form. UserCreationForm juga merupakan sebuat template untuk membuat user yang memiliki tiga input, yaitu username, password1, dan password2 (yang digunakan untuk konfirmasi kata sandi). Didalamnya juga sudah terdapat authentikasi agar semua input yang diberikan oleh user adalah valid.  
Kelebihan:  
- Mudah digunakan  
- Efisiensi waktu  

Kekurangan:  
- Tampilan default yang kurang sesuai untuk pengguna  
- Terbatas untuk validasi yang kompleks

**Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**  
Autentikasi yaitu proses dimana Django memverifikasi seorang user adalah benar user dari aplikasi tersebut, sementara otorisasi yaitu proses dimana Django memberikan izin/menentukan izin apa yang bisa dilakukan oleh pengguna yang telah terautentikasi.  

Autentikasi dan otorisasi dalam Django sangat penting karena keduanya berperan dalam menjaga keamanan dan perlindungan data dalam aplikasi web. Dengan memadukan autentikasi dan otorisasi yang sesuai, kita dapat menjaga tingkat keamanan, mengendalikan hak akses, melindungi privasi pengguna, dan bahkan dapat mendeteksi pelaku jika terjadi suatu penyalahgunaan aplikasi.

**Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**  
Cookies adalah data yang berukuran kecil yang disimpan pada sisi klien/user. Cookies digunakan oleh aplikasi web untuk menyimpan informasi yang dapat diakses kembali saat pengguna melakukan request pada situs web yang sama.  

Pada Django, cookies biasanya digunakan untuk menyimpan Session ID yang dapat dianggap sebagai suatu token (barisan karakter) untuk mengenali session yang unik pada aplikasi web tertentu. Session ID ini kemudian dipetakan ke suatu database pada sisi web server. Kemudian, saat klien mengirimkan request, browser juga mengirimkan suatu session ID ke server. Server akan mencari data pada database berdasarkan session ID yang didapat, lalu mengembalikan data yang diminta.

**Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**  
Secara default, cookies adalah mekanisme penyimpanan data yang relatif aman karena data cookies hanya dapat diakses oleh server yang mengatur cookie tersebut. Namun, terdapat juga risiko potensial cookies yang harus diwaspadai, yaitu ketika cookie mengandung informasi yang sensitif, seperti password, cookies yang tidak dienkripsi, dan juga pencurian cookies.  

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.**
1.  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
    *   

2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.  
    *   Membuat akun pengguna dengan cara klik `Register Now`
    *   Memasukan username dan password sesuai ketentuan
    *   Klik `Daftar`
    *   Login sesuai username dan password yang di daftarkan
    *   Klik `Add New Item` untuk menambah barang di Inventory

3. Menghubungkan model Item dengan User.  
    *   Mengimport `User` pada `models.py`
    *   Menambahkan variable `User` dengan menggunakan `ForeignKey` agar setiap item dapat diasosiasikan dengan seotang user
        ```ruby
        class Item(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
        ```
    *   Ubah fungsi `create_item` pada `views.py` agar mempunyai attribut `user` dengan cara mengambil variable user pada request
        ```ruby
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        ```
    *   Tambahkan filter pada variable items di fungsi `show_main` pada `main.html` agar item yang diambil pada variable `items` hanya item yang cocok dengan nama user, dan ubah isi `name` dalam `context` dengan mengambil username dari request agar nama yang ditampilkan pada `mail.html` adalah username pengguna.
        ```ruby
        def show_main(request):
        products = Item.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
        }
        ```  
    * Migrate agar perubahan pada model dapat teraplikasi.  
    
4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

</details>

<details>
<summary>Tugas 3</summary>

#### Form dan Data Delivery

**Apa perbedaan antara form POST dan form GET dalam Django?**
Method GET dan POST digunakan untuk mengirim data dari client ke server dalam HTTP, tetapi perbedaan utama antara keduanya adalah bahwa method GET membawa parameter permintaan yang ditambahkan dalam string URLnya, sedangkan POST membawa parameter permintaan dalam body, yang membuatnya lebih aman dalam pengiriman data dari client ke server.  
contoh:  
GET = https://www.google.com/search?q=<b>whats+get+method</b>..  
POST = https://www.dummyweb.com/submit-form

**Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**
* **XML**  
XML adalah markup language yang diguankan untuk menyimpan dan mengirimkan data. XML didefinisikan sebagai aturan untuk mengubah dokumen menjadi sebuah kode yang dapat dibaca oleh mesin dan juga manusia. XML memiliki fleksibilitas yang tinggi karena dapat digunakan untuk mendefinisikan tipe data yang bebas. XML menggunakan sintaks yang berbasis tag dengan elemen yang diapit oleh tanda kurung sudut (<>).  

* **JSON**  
Berbeda dari XML, JSON merupakan format file berbasis teks yang mudah dibaca oleh manusia yang umumnya digunakan dalam proses pertukaran data antara server dan client. JSON menggunakan sintaksis yang berbasis objek dengan pasangan nama-nilai yang diapit oleh kurung kurawal {} seperti dictionary pada python. JSON digunakan secara luas dalam pengembangan web untuk pertukaran data antara server dan klien.  

* **HTML**  
Sama seperti XML, HTML adalah markup language yang digunakan untuk membuat halaman website dan aplikasi web. HTML biasanya digunakan dalam pembuatan tampilan dan struktur halaman web dan memiliki aturan yang lebih terbatas dibandingkan dengan XML dan JSON. HTML menggunakan sintaksis yang mirip dengan XML, tetapi memiliki tujuan yang berbeda dan penamaan tipe data lebih terbatas.  

**Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**  
JSON sering digunakan dalam pertukaran data karena dapat mempermudah proses pertukaran data dan mengolah proses data pada web. JSON memiliki format teks yang ringan dan memiliki format data yang mudah diurai tanpa perlu menulis banyak kode dalam berbagai bahasa pemrograman yang berbeda. Hal ini menjadikan JSON sangat efisien dalam mentransfer dan menggunakan data tidak seperti pada XML.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**  
1.  Membuat input form untuk menambahkan objek model pada app sebelumnya.
    *   Membuat file `forms.py` untuk menyimpan forms code dengan mengimport `ModelForm`
    *   Menambahkan class `ItemForm` yang akan menerima input dari user dan ditambahkan ke model `Item`
    *   Membuat function `create_item` pada `views.py` untuk memproses hasil input yang user berikan. 
    *   Menambahkan path url `create_item` agar bisa menampilkan `create_item.html` dan menjalankan fungsi `create_item`
  
2. Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
    *   Pada `views.py` dalam direktori `main`, import `HttpResponse` dan `Serializer` yang digunakan untuk mentranslate objek model menjadi format yang diinginkan dan ditampilkan pada web.
    *   Membuat function yang menerima input dari user, mengambil data dari model dan mengembalikan HTTP Response dengan data yang sudah diubah ke format yang diinginkan   

    ```ruby
        def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    *   Jika request membutuhkan `id`, masukkan parameter `id` yang dimuat pada variabel ke dalam fungsi, dan data akan difilter sesuai `id` yang dinput yang terdapat pada variable `pk` pada model.   

    ```ruby
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    *   Menampilkan isi form pada file `main.html` dengan menyisipkan code pada tag `{%block content %}`
    ```ruby
        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    ```


3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
    *   Buat path dalam `urls.py` dalam direktori `main` untuk menampilkan respons dari function yang dibuat.  

    ```ruby
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'), 
    ```
    *   Pada request yang membutuhkan `id`, masukkan variable `id` yang akan dicari ke dalam endpoint tersebut.  

    ```ruby
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ```
**Postman**  
*<b>HTML</b>
![image](https://github.com/nadriha/my-inventory/assets/116888619/9586608a-434e-4582-9e6b-93f7dec75b56)
* <b>JSON</b>
![image](https://github.com/nadriha/my-inventory/assets/116888619/9dd8d41b-2fed-4c66-97db-54cc3fe7a16e)
* <b>XML</b>
![image](https://github.com/nadriha/my-inventory/assets/116888619/b2ebcc9d-524d-44c5-9636-bc6b1b9eb5f6)
* <b>JSON by ID</b>
![image](https://github.com/nadriha/my-inventory/assets/116888619/99bca72b-e2c2-4ede-8b23-867236d99ada)
* <b>XML by ID</b>
![image](https://github.com/nadriha/my-inventory/assets/116888619/f33b1c2d-4a90-4479-96cf-2e6908979cca)


</details>

<details>
<summary>Tugas 2</summary>

#### Implementasi Model-View-Template (MVT) pada Django
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

**Bagan yang berisi request client ke web aplikasi berbasis Django**
![bagan-django](https://github.com/nadriha/my-inventory/assets/116888619/caa929ae-6fe5-4845-a346-6f64004d2dc4)

Pada bagan tersebut dilihat bahwa request datang dari user yang ditangkap oleh `urls.py`. Kemudian oleh `urls.py` diteruskan ke `views.py` yang akan memproses request tersebut. `views.py` meminta `models.py` mengakses database untuk mengambil data dan akan dikembalikan lagi ke `models.py` dan diteruskan lagi ke `views.py`. Data yang sudah didapat dari `views.py` render oleh `template` dan diberikan lagi ke `views.py` untuk menjadi response kepada user.

**Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**  
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi dianjurkan untuk menggunakan virtual environment karena dengan menggunakan virtual environment, kita membuat lingkungan yang terisolasi yang tidak saling terkait dan dapat diaktifkan atau dinonaktifkan sesuai kebutuhan. Hal tersebut bisa digunakan untuk mengelola dependencies proyek secara terpisah dan memungkinkan menggunakan versi Django dan Python yang berbeda.

**Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
* **MVC(Model-View-Controller)**
Membagi kode aplikasi dibagi menjadi 3 komponen, yaitu untuk 
a. Model: Komponen untuk menyimpan data aplikasi, tidak ada kaitannya dengan tampilan aplikasi. Model berfungsi untuk komunikasi dengan database dan jaringan.  
b. View: Komoponen untuk membuat UI yang mengatur tampilan dari data yang diterima dari Model.  
c. Controller: Penghubung antara View dan Model. Mengandung logika dari aplikasi.
* **MVT (Model-View-Template)**
Sama seperti MVC, kode dibagi aplikasi dibagi menjadi 3 komponen, yaitu  
a. Model: Tempat untuk data seperti dalam MVC.  
b. View: Komponen untuk membuat tampilan, sama seperti dalam MVC.    
c. Template: Komponen untuk mengatur bagaimana data ditampilkan di tampilan.
Mirip dengan MVC tetapi perbedaan terdapat komponen `Template` yang berperan sebagai komponen untuk menampilkan page content dan biasanya berisi kode HTML yang merender data.
* **MVVM (Model-View-ViewModel)**  
Sama juga seperti MVC, kode dibagi aplikasi dibagi menjadi 3 komponen, yaitu  
a. Model: Komponen ini berfungsi sebagai tempat untuk data aplikasi  
b. View: Kode yang akan ditampilkan pada layar aplikasi, memberi tahu ViewModel tentang input dari pengguna, dan tidak ada logika aplikasi di dalam komponen ini.  
c. ViewModel: Perantara antara Model Dan View. Komponen ini menyediakan dan menjaga koneksi aliran data dan memastikan jika data berubah pada model, maka tampilan juga diperbaharui.  
Perbedaan terdapat pada ViewModel yang hanya menjadi jembatan antara Model dan View

</details>

