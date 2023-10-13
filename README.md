# my-inventory🌻🌼
app link: https://steves-inventory.adaptable.app/main

<details>
<summary>Tugas 6</summary>

#### JavaScript dan Asynchronous JavaScript  
**Perbedaan antara asynchronous programming dengan synchronous programming**  
Synchronous programming adalah sebuah model pemrograman dimana setiap instruksi dieksekusi satu per satu, dan program menunggu hingga satu instruksi selesai sebelum menjalankan yang berikutnya. Ini berarti bahwa jika ada operasi yang memakan waktu seperti mengambil data dari internet, program akan terhenti dan tidak merespons hingga operasi tersebut selesai. Contohnya adalah saat kita mengambil data dari server dengan AJAX.

Asynchronus programming adalah model pemrograman dimana program dapat melanjutkan menjalankan instruksi lain sambil menunggu operasi tersebut selesai. Contohnya, dengan menggunakan promise atau async/await dalam JavaScript kita dapat mengirim request AJAX ke server selagi menjalankan kode lain saat menunggu responsnya

**Event-driven programming**  
Event-driven programming adalah paradigma pemrograman di mana program merespons peristiwa (events) yang terjadi dalam sistem atau aplikasi dengan sebuah event listener (fungsi atau metode yang akan dijalankan ketika peristiwa terjadi).  

```ruby
document.getElementById("button_add").onclick = addProduct
```
Pada kode tersebut `.onclick` merupakan suatu event dari elemen button yang diambil, dan `addProduct` adalah sebuah event listener (method yang dijalankan) dari event tersebut.

**Jelaskan penerapan asynchronous programming pada AJAX**  
Asynchronous programming pada AJAX memungkinkan pertukaran data dengan server tanpa menghentikan operasi lainnya, hal itu dapat membuat server hanya merender bagian yang diperlukan sebagai respons saat pengguna mengirimkan permintaan. Oleh karena itu, halaman web tetap responsif dan dinamis serta memungkinkan interaksi yang mulus tanpa perlu memuat ulang seluruh halaman.

**Penerapan AJAX menggunakan Fetch API/library jQuery**  
Fetch API dan  jQuery adalah teknologi yang biasa digunakan untuk melakukan permintaan AJAX dalam pengembangan web. Adapun perbedaan antara Fetch API dan jQuery:
*   Fetch API adalah API standar yang telah disertakan dalam semua browser modern. Hal ini berarti Anda tidak perlu lagi mengunduh atau mengimpor library tambahan untuk melakukan permintaan AJAX seperti jQuery.
*   Fetch API menggunakan Promise, yang memungkinkan Anda untuk menulis kode yang lebih bersih dan mudah dibaca saat menangani respons dan kesalahan, sedangkan jQuery memakai callback.  

Berdasarkan perbedaan perbedaan tersebut, menurut saya Fetch API lebih cocok pada tugas kali ini karena aplikasi yang dibuat masih relatif sederhana dan cocok untuk pemula

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**
1.  **AJAX GET**
    *   Karena saya menginginkan kode yang terpisah untuk Javascript,  saya menyimpan file javascript di dalam folder static yang sudah saya buat sebelumnya.
    *   Buat `script.js` untuk membuat file Javascript pada elemen HTML
    *   Hubungkan `script.js` dengan file HTML dengan menambahkan kode
        ```ruby
        <script src="{% static 'script.js' %}"></script>
        ```
        pada `body` di `base.html`
    *   Agar dapat mengambil data item menggunakan AJAX GET, buat fungsi `getItem()` pada `views.py`
        ```ruby
        def get_product_json(request):
            product_item = Item.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize('json', product_item))
        ```
        Fungsi tersebut meminta semua data yang dimiliki oleh user tertentu
    *   Buat path pada `urls.py` untuk menjalankan function tersebut
        ```ruby
        path('get-product/', get_product_json, name='get_product_json'),
        ```
    *   Buat fungsi untuk mengambil data dari server dengan menggunakan AJAX GET
        ```ruby
        async function getItems() {
            return fetch("/get-product/").then((res) => res.json())
        }
        ```
    *   Membuat fungsi `showItems()` untuk menampilkan seluruh data yang sudah diambil dari function `getItems()`. 
        ```ruby
        const listItems = document.querySelector(".table-items");
        async function showItems() {
            listItems.innerHTML = '';
            let output = "";
            const items = await getItems()
            items.forEach(item => {
                output += `
                <div class="row list-items justify-content-center">
                    <div class="col-3 mepet">
                            <p class="border-minecraft mepet fs-5">${item.fields.name}</p>
                        </div>
                        <div class="col-1 mepet">
                            <p class="border-minecraft mepet fs-5">${item.fields.amount}</p>
                        </div>
                        <div class="col-4 mepet">
                            <p class="border-minecraft mepet fs-5">${item.fields.description}</p>
                        </div>
                        <div class="col-1 p-0" >
                            <button onclick="deleteItem(${item.pk});" class="button-minecraft lebar-max">Delete</button>
                        </div>
                        <div class="col-1 p-0" >
                            <button onclick="editItem()" class="button-minecraft lebar-max">Edit</button>
                        </div>
                        <div class="col-1 p-0">
                            <button onclick="plusItem(${item.pk});" class="button-minecraft lebar-max">+</button>       
                        </div>
                        <div class="col-1 p-0">
                            <button onclick="minItem(${item.pk});" class="button-minecraft lebar-max">-</button>
                        </div>
                    </div>
                </div>
            `;
            });
            listItems.innerHTML = output;
        }
        ```
    *   Panggil fungsi `showItem()` pada Javascript untuk menjalankan fungsi tersebut.

2.  **AJAX POST**
    *   Buat modal untuk menampilkan form
        ```ruby
        <div class="modal fade border-minecraft" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" style="background-color: rgba(0, 0, 0, 0.1);">
            <div class="modal-dialog">
                <div class="modal-content border-minecraft" style="border-radius: 0;">
                    <div class="modal-header border-minecraft" style="border-radius: 0;">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body border-minecraft" style="border-radius: 0;">
                        <form id="form" onsubmit="return false;">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Name:</label>
                                <input type="text" class="form-control" id="name" name="name" style="border-radius: 0;"></input>
                            </div>
                            <div class="mb-3">
                                <label for="price" class="col-form-label">Amount:</label>
                                <input type="number" class="form-control" id="amount" name="amount" style="border-radius: 0;"></input>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="col-form-label">Description:</label>
                                <textarea class="form-control" id="description" name="description" style="border-radius: 0;"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer border-minecraft" style="border-radius: 0;">
                        <button type="button" class="button-minecraft" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="button-minecraft" id="button_add" data-bs-dismiss="modal">Add Product</button>
                    </div>
                </div>
            </div>
        </div>
        ```
    *   Buat button untuk menampilkan modal yang sudah dibuat dengan menargetkan modal yang ber-id `exampleModal`
        ```ruby
        <button type="button" class="button-minecraft mx-auto d-block mb-2" style="width: 10rem;" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
        ```
    *   Agar dapat mengirim data item menggunakan AJAX POST, buat fungsi `add_item_ajax()` pada `views.py`
        ```ruby
        @csrf_exempt
        def add_item_ajax(request):
            if request.method == 'POST':
                name = request.POST.get("name")
                amount = request.POST.get("amount")
                description = request.POST.get("description")
                user = request.user

                new_product = Item(name=name, amount=amount, description=description, user=user)
                new_product.save()

                response_data = {
                    'success': True,
                    'message': 'Berhasil menambahkan ' + name
                }
            return JsonResponse(response_data)
        ```
        Fungsi tersebut menambahkan Item baru pada model yang dibuat dan mengirimkan response berupa status dan pesan sukses
    *   Buat path pada `urls.py` untuk menjalankan function tersebut
        ```ruby
        path('create-ajax/', add_item_ajax, name='add_item_ajax'),
        ```
    *   Buat fungsi untuk mengambil data dari server dengan menggunakan AJAX POST
        ```ruby
        async function addProduct() {
            fetch("/create-ajax/", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            })
            .then(res => res.json())
            .then(data =>{
                if (data.success){
                    showItems();
                    messageBox.innerHTML = `
                    <p class="text-center">${data.message}<p>
                    `;
                }
            })
            document.getElementById("form").reset()
            return false
        }

        document.getElementById("button_add").onclick = addProduct
        ```
3.  **Melakukan perintah collectstatic**
    memodifikasi bagian `STATIC_URL` dan `STATIC_ROOT` pada `settings.py`
    ```ruby
    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
        BASE_DIR / "static"
    ]
    ```
    Jalankan pertintah untuk `collectstatic`
    ```ruby
    python manage.py collectstatic
    ```

</details>

<details>
<summary>Tugas 5</summary>

#### Desain Web menggunakan HTML, CSS dan Framework CSS
**Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya**  
*   Element Selector: digunakan untuk mengubah style semua elemen yang memiliki tag HTML yang sama.
    ```ruby
    p {
  
    }
    ```
*   ID Selector: digunakan untuk mengubah style elemen HTML yang memiliki ID unik yang sesuai
    ```ruby
    #header{
    ...
    }
    ```
*   Class Selector: digunakan untuk mengubah style semua elemen yang memiliki class yang sama. Biasanya digunakan untuk elemen HTML yang mempunyai beberapa style yang sama.
    ```ruby
    .card-header{
    ...
    }
    ```

**Jelaskan HTML5 Tag**   
Banyak sekali Tag HTML, dan berikut adalah beberapa Tag HTML yang saya ketahui:
*   `<p>` digunakan untuk membuat paragraf teks.
*   `<br>` digunakan untuk membuat pemisah baris (line break) dalam teks.
*   `<ul>` digunakan untuk membuat list yang  tak terurut (unordered list).
*   `<ol>` digunakan untuk membuat list yang terurut (ordered list). 
*   `<li>` digunakan dalam elemen `<ul>` dan `<ol>` untuk menandakan setiap item dalam daftar. 
*   `<div>` digunakan untuk membuat kontainer yang biasanya digunakan untuk mengelompokkan elemen HTML lainnya.
*   `<header>` digunakan untuk menunjukkan head dari sebuah halaman, biasanya berisi seperti judu, navbar, dll.

**Jelaskan perbedaan antara margin dan padding.**    
![image](https://github.com/nadriha/my-inventory/assets/116888619/34814590-073f-4b43-96d6-9e2e434da693)  
Bisa dilihat dari gambar diatas, padding adalah ruang di dalam elemen, yaitu jarak antara isi di dalam elemen dengan batas elemen itu sendiri. Padding memengaruhi elemen dengan cara memberikan ruang tambahan di dalam elemen tersebut. Sedangkan margin adalah ruang di luar elemen, yang berarti itu adalah jarak antara elemen  dengan elemen-elemen lain di sekitarnya. Margin memengaruhi elemen dengan cara membuat jarak antara elemen dan elemen-elemen lain yang ada di sekitarnya.  

**Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**    
Tailwind CSS adalah kerangka kerja CSS membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya. Ini memungkinkan tingkat kustomisasi yang tinggi dan ukuran file CSS yang lebih kecil karena hanya memuat kelas-kelas utilitas yang telah didefinisikan sebelumnya. Selain itu, Tailwind CSS memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek. Sedangkan Bootstrap, adalah kerangka kerja CSS "component based" yang menyediakan sejumlah besar komponen UI siap pakai, tetapi mungkin memerlukan lebih banyak penyesuaian. Oleh karena itu, Bootstrap memiliki file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena termasuk banyak komponen yang telah didefinisikan. Bootstrap sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan.

Bootstrap cocok ketika kita membutuhkan website dengan solusi yang simple dengan komponen yang telah dibuatkan sebelumnya dan konsistensi tampilan yang kuat. Di sisi lain, Tailwind cocok ketika kita menginginkan kustomisasi yang tinggi, mengutamakan ukuran file yang kecil, dan ingin memahami secara mendalam bagaimana tampilan dibangun.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**
*   Karena saya menginginkan kode yang terpisah untuk HTML dan CSS, saya membuat directory baru bernama static yang akan menyimpan file CSS dan elemen yang dibutuhkan.
*   Buat `styles.css` untuk mengatur style pada elemen HTML
*   Hubungkan `styles.css` dengan file HTML dengan menambahkan kode
    ```ruby
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    ```
    pada `head` di `base.html`
*   Hubungkan `styles.css` dengan projek Django utuk menggunakan static files yang merupakan file-file pendukung HTML pada suatu situs web dengan menambahkan kode
    ```ruby
    STATICFILES_DIRS = [
    BASE_DIR / "static"
    ]
    ```
*   Mengubah tampilan login pada `login.html` dengan membuat border dan mengubah margin-marginnya
    ```ruby
    {% block content %}
    <div class="login container background d-flex justify-content-center align-items-center min-vh-100">
        
        <div class=" border-minecraft p-3" style="width: 50%;">
            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <div>
                    <div class="mb-2">
                        <label for="username" class="form-label mb-0">Username</label>
                        <input type="text" class="form-control border-minecraft mt-0" style="background-color: #c6c6c6;border-radius: 0;" id="username" name="username" placeholder="Username">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label mb-0">Password</label>
                        <input type="password" class="form-control border-minecraft mt-0" style="background-color: #c6c6c6;border-radius: 0;" id="password" name="password" placeholder="Password">
                    </div>
                    <button type="submit" class="button-minecraft mb-2 ">Login</button>
                </div>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}

            <div class="mt-auto">
                Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
            </div>
        </div>
    </div>
    {% endblock content %}
    ```
*   Mengubah tampilan `register.html` agar sama dengan `login.html` dengan menambahkan border dan background
    ```ruby
    {% block content %}  

    <div class="container register background d-flex justify-content-center align-items-center min-vh-100">
        <div class="row border-minecraft p-3" style="width: 70%;">
                <h1>Register</h1>
                
                <form method="POST">
                    {% csrf_token %}
                    {{ form.as_p }}
                    <button type="submit" class="button-minecraft" style="height: 2rem;">Register</button>
                </form>
                
                {% if messages %}
                    <div class="alert alert-info mt-3">
                        <ul>
                            {% for message in messages %}
                                <li>{{ message }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                {% endif %}
            
        </div>
    </div>

    {% endblock content %}
    ```
*   Mengubah tampilan `create_item.html` dan `edit_product.html` menggunakan template yang sama dengan menambahkan border dan juga mengubah padding pada container
*   Pada setiap langkah langkah diatas, saya menambahkan style pada css eksternal (`styles.css`) dengan kode berikut
    ```ruby
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    body{
        font-family: 'VT323';
        background-color: #c6c6c6;
        
    }

    .border-minecraft {
        background-color: #8b8b8b ; 
        box-shadow: inset 1.5px 1.5px 0px rgba(55, 55, 55, 0.8), 
                    inset -2px -2px 0px #ffffff;
        height: 100%;

    }

    .button-minecraft {
        background-color: #c6c6c6 ; 
        box-shadow: inset 1.5px 1.5px 0px rgba(55, 55, 55, 0.8), 
                    inset -2px -2px 0px #ffffff;
        height: 100%;
    }

    .tidak-bold {
        font-weight: normal; /* This makes the font not bold */
    }

    .mepet {
        padding: 0;
        margin: 0;
    }

    .lebar-max{
        width: 100%;
    }

    .login{
        background-image: url('/static/images/minecraft-wallpaper-hd.jpg'); /* Update the path to your background image */
        background-size: cover;
        background-repeat: no-repeat;
        max-width: 100%;
    }

    .register{
        background-image: url('/static/images/minecraft-wallpaper-hd.jpg'); /* Update the path to your background image */
        background-size: cover;
        background-repeat: no-repeat;
        max-width: 100%;
    }

    ```
*   Tambahkan navbar pada `main.html` dengan menggunakan template yang tersedia dari Bootsrap. 
*   Tambahkan Header yang berisi nama, kelas, dan kapan terakhir user login.
*   Gunakan grid pada Bootsrap untuk menampilkan list of item, yang seiap column dipakaikan border masing masing.
*   Ubah tampilan button-button dengan memakaikan class yang sama
    ```ruby
    {% extends 'base.html' %}

    {% block content %}

        <!--Navigation Bar-->
        <nav id="navigation" class="navbar navbar-expand-lg navbar-dark border-minecraft">
            <div class="container">
                <p class="navbar-brand fs-2 p-0 mb-0" href="#" >MY INVENTORY</p>
                <a class="fs-5" href = "{% url 'main:logout' %}">
                    <button class="border-minecraft" style="background-color: #c6c6c6; ">Logout</button >
                </a>
            
            </div>
        </nav>
        <!--End Navigation Bar-->
        <!--Header-->
        <section style="background-color: #c6c6c6;">
            <h2 class="text-center m-0 pt-2">Hello, {{name}} from {{class}}!</h2>
            <p class="text-center mb-0">Last login: {{ last_login }}</p>
        </section>
        <!--End of Header-->
        <!--Tabel-->
        <section style="background-color: #c6c6c6;">
            <div class="container items text-center mb-3" style="max-width: 60%;">
                <div class="row">
                <div class="col">
                    <h5 class="mt-4 mb-2">{{name}}'s Inventory</h2>
                </div>
                </div>
                <div class="row">
                    <div class="col-3">
                    Name
                    </div>
                    <div class="col-1">
                        Amount
                    </div>
                    <div class="col-4">
                        Description
                    </div>
                </div>
                {% for item in items %}
                <div class="row justify-content-center">
                    <div class="col-3 mepet">
                        <p class="border-minecraft mepet fs-5">{{item.name}}</p>
                    </div>
                    <div class="col-1 mepet">
                        <p class="border-minecraft mepet fs-5">{{item.amount}}</p>
                    </div>
                    <div class="col-4 mepet">
                        <p class="border-minecraft mepet fs-5">{{item.description}}</p>
                    </div>
                    <div class="col-1 p-0" >
                        <a href="{% url 'main:delete_item' item.id %}">
                            <input type="hidden"  value="{{ item.id }}">
                            <button class="button-minecraft lebar-max">Delete</button>
                        </a>
                    </div>
                    <div class="col-1 p-0" >
                        <a href="{% url 'main:edit_product' item.pk %}">
                            <button class="button-minecraft lebar-max">
                                Edit
                            </button>
                        </a>
                    </div>
                    <div class="col-1 p-0">
                        <a href="{% url 'main:tambah_item' item.id %}">
                            <input type="hidden" value="{{ item.id }}">
                            <button class="button-minecraft lebar-max">+</button>
                        </a>
                    </div>
                    <div class="col-1 p-0">
                        <a href="{% url 'main:kurang_item' item.id %}">
                            <input type="hidden" value="{{ item.id }}">
                            <button class="button-minecraft lebar-max">-</button>
                        </a>
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>
        <!--End of Tabel-->
        <!--Messages-->
        </section style="background-color: #c6c6c6; min-height: 2rem;">
            {% if messages %}
                <ul class="text-center">
                    {% for message in messages %}
                        <p class="mt-2">{{ message }}</p>
                    {% endfor %}
                </ul>
            {% endif %} 
        </section> 
        <!--End of messages-->
        <!--Add Item-->
        <section class="text-center" style="background-color: #c6c6c6">
            <a href="{% url 'main:create_item' %}">
                <button class="button-minecraft" style="width: 10rem;">
                    Add New Item
                </button>
            </a>
            
            <a href="{% url 'main:logout' %}">
                <button class="button-minecraft" style="width: 10rem">
                    Logout
                </button>
            </a>
        </section>
        <!--End of Add Item-->
    {% endblock content %}
    ```
*   Tambahkan kode dibawah, untuk menandakan elemen `p` terakhir pada `row` berubah menjadi warna merah
    ```ruby
    .row:last-child p{
    background-color: red;
    }
    ```
</details>

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
    **Registrasi**
    *   Mengimport library `redirect`, `UserCreationForm`, dan `messages` pada `views.py`
    *   Membuat function `register` dengan form dari `UserCreationForm`
        ```ruby
        def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
        ```
    *   Membuat tampilan html (`register.html`) pada direktori `templates` untuk menampilkan form untuk registrasi
    *   Pada `register.html` taruh form yang didapat dari `UserCreationForm`
        ` {{ form.as_table }}` dan menaruh button `Daftar` untuk mensubmit form.
    *   Menambahkan path url ke dalam `urls.py` dan memasukan function `register` yang telah diimport dari `views.py`  

    **Login**
    *   Mengimport function `authenticate` dan `login` dari `django.contrib.auth`
    *   Membuat function untuk login user 
        ```ruby
        def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
        ```
    *   Membuat tampilan html (`register.html`) pada direktori `templates` untuk menampilkan halaman login
    *   Menambahkan path url ke dalam `urls.py` dan memasukan function `login_user` yang telah diimport dari `views.py`  

    **Logout**
    *   Mengimport function `logout` dari `django.contrib.auth`
    *   Membuat function untuk logout
        ```ruby
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        ```
    *   Tambahkan button untuk logout pada `main.html` yang di-link menucu path `logout`
    *   Menambahkan path url ke dalam `urls.py` dan memasukan function `logout_user` yang telah diimport dari `views.py`  

    *   Agar pengguna yang masuk hanya pengguna yang sudah login, maka masukkan kode
        ```ruby
        @login_required(login_url='/login')
        ```
        pada barus sebelum fungsi `show_main` dibuat.

2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.  
    *   Membuat akun pengguna dengan cara klik `Register Now`
    *   Memasukan username dan password sesuai ketentuan
    *   Klik `Daftar`
    *   Login sesuai username dan password yang di daftarkan
    *   Klik `Add New Item` untuk menambah barang di Inventory
   ![messageImage_1695777866470](https://github.com/nadriha/my-inventory/assets/116888619/103e1d96-d66f-4699-a8f3-d583e0d5491f)
   ![messageImage_1695778156459](https://github.com/nadriha/my-inventory/assets/116888619/207eafaa-eb09-480a-ae43-2939de18a2ff)

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
    *   Tambahkan filter pada variable items di fungsi `show_main` pada `main.html` agar item yang diambil pada variable `items` hanya item yang cocok dengan nama user.
        ```ruby
        def show_main(request):
        products = Item.objects.filter(user=request.user)
        ```  
    * Migrate agar perubahan pada model dapat teraplikasi.  

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.  
    **Menampilkan detail informasi pengguna yang sedang logged in**
    *   Pada fungsi `show_main` bagian `context`, ambil username dari properti dari objek `request.user` dan masukan ke dalam variable `name`.
        ```ruby
        def show_main(request):
        products = Product.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
        }
        ```
    **Cookies seperti last login pada halaman utama aplikasi**
    *   Pada fungsi `login_user` ketika user berhasil login, masukan waktu kapan user tersebut login dengan cara:
        ```ruby
        response.set_cookie('last_login', str(datetime.datetime.now()))
        ```
    *   Pada fungsi `show_main`, tambahkan variable `last_login` di dalam `context` yang mempunyai value
        ```ruby
        request.COOKIES['last_login']
        ```
        Kode tersebut mereturn variable `last_login` yang dibuat saat user login dan memasukkannya ke dalam variable `last_login`. 
    *   Agar variable `last_login` dapat muncul pada halaman utama aplikasi web, tambahkan kode 
        ```ruby
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        ```` 
        pada `main.html`.

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

