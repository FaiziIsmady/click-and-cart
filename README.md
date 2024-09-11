# click-and-cart 
**Nama : Muhammad Faizi Ismady Supardjo**
**NPM : 2306244955**
**Kelas : PBP C**

**Tautan menuju PWS yang sudah di deploy :** "http://muhammad-faizi-clickandcart.pbp.cs.ui.ac.id"

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1.1. Membuat direktori dan mengaktifkan virtual environment<br>
- Buat direktori (folder) baru bernama sama dengan nama produk (dalam kasus ini click-and-cart)

- Gunakan IDE seperti vscode atau terminal. Buka direktori yang sudah dibuat dan jalankan perintah "python -m venv env" untuk membuat virtual environment

- Jalankan virtual environment dengan perintah "env\Scripts\activate". Jika venv berhasil aktif, akan ada (env) di depan baris terminal

1.2. Membuat projek Django (checklist 1)<br>
- Di dalam direktori click-and-cart buat file requirements.txt dan isi dengan
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3

- Install dependencies dengan perintah "pip install -r requirements.txt"

- Buat projek django bernama click_and_cart dengan perintah "django-admin startproject click_and_cart ." yang berfungsi membuat folder bernama proyek tersebut dengan isi file bawaan dari django

- Tambahkan string pada ALLOWED_HOSTS di settings.py direktori click_and_cart 
        ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

-  Membuat berkas .gitignore untuk menentukan file yang tidak ingin dimasukkan ke dalam versi kontrol Git

1.3. Membuat aplikasi bernama main pada proyek (checklist 2)<br>
- Buat aplikasi bernama main dengan perintah berikut "python manage.py startapp main" di dalam direktori
- Tambahkan 'main' kedalam INSTALLED_APPS pada file settings.py. Main merefer ke file html yakni main.html

1.4. Melakukan routing pada proyek agar dapat menjalankan aplikasi main (checklist 3)<br>
- Melakukan routing dengan menambahkan kode ini dalam urls.py
        from django.contrib import admin
        from django.urls import path
        from django.urls import path, include

        urlpatterns = [
            path('', include('main.urls')),
            path('admin/', admin.site.urls), path('', include('main.urls'))
        ]

1.5. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, dan description (checklist4)<br>
- Isi models.py dengan kode berikut
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=255)
            price = models.IntegerField()
            description = models.TextField()
            quantity = models.IntegerField()

Note: atribut quantity opsional

1.6. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas. (checklist 5)<br>
- Isi file views.py dengan kode berikut untuk dapat dikembalikan ke main.html
        from django.shortcuts import render

        # Create your views here
        def show_main(request):
            context = {
                'name': 'Sepeda',
                'price' : '2000000',
                'quantity' : '10',
                'description': 'sepeda roda dua, cocok untuk pemula'
            }

            return render(request, "main.html", context)

- Isi file main.html dengan kode berikut
        <!-- <h1>Click and Cart</h1> -->
        <!-- <h3>oleh Muhammad Faizi Ismady Supardjo, kelas PBP C, NPM 2306244955</h3> -->

        <h5>Name: </h5>
        <p>{{ name }}<p>
        <h5>Price: </h5>
        <p>{{ price }}<p>
        <h5>Quantity: </h5>
        <p>{{ quantity }}<p>
        <h5>Description: </h5>
        <p>{{ description }}<p>
Note: <!-- --> adalah komen pada HTML

1.7. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. (checklist 6) <br>
- Isi file urls.py pada direktori main dengan kode berikut agar dapat menghubungkan views.py di dalam direktori main dengan urls.py
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]

1.8. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. <br>
- Buka laman PWS, jika belum memiliki akun register jika sudah login

- Buat proyek baru pada website PWS dengan menekan tombol Create New Project. Lalu, isi Project Name dengan clickandcart. setelah itu, tekan Create New Project.

- Akan muncul string credentials yang perlu kita simpan sendiri karena tidak dapat dilihat lagi.

- Pada settings.py di proyek Django, tambahkan URL deployment PWS pada ALLOWED_HOSTS. Isi ALLOWED_HOSTS menjadi
        ALLOWED_HOSTS = ["localhost", "127.0.0.1", "muhammad-faizi-clickandcart.pbp.cs.ui.ac.id"]

- Buat repositori github bernama click-and-cart. Lalu add commit dan push perubahan kedalam repositori tersebut. Jalankan perintah project command yang terlihat di website PWS. Terakhir lakukan command berikut "git push pws main" yang berfungsi push dari github ke pws. Jika PWS tidak error, seharusnya projek sudah berhasil di launch.

1.9. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut. (checklist 7)<br>
- Buat file README.md pada direktori click-and-cart terluar dan isi sesuai dengan Tugas 2 PBP.

**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

![Screenshot 2024-09-11 071719](https://github.com/user-attachments/assets/2033f79d-990b-4ecb-9559-4e9fd6eed75d)

Apabila klien/user mengirim HTTP request melalui web platform, address HTTP yang dikirim klien akan di cek sesuai atau tidak pada file urls.py. Jika tidak sesuai akan return page not found, jika sesuai, dilanjutkan ke file views.py yang memperoleh data dari models.py berisi atribut-atribut. Setelah itu, data dan atribut akan di proses di template yang berisi main.html. Lalu, setelah data sudah ada di dalam template, template akan menghasilkan respon ke web platform, menampilkan tampilan web pada views.py

**3. Jelaskan fungsi git dalam pengembangan perangkat lunak!**<br>

3.1. Melacak perubahan kode
    Git dapat melacak perubahan kode yang dilakukan selama proses development. Setiap kali ingin melakukan perubahan dan disimpan di Git (add commit push), Git memiliki log versi sebelum update dan sesudah update sehingga memudahkan melihat perubahan kode.

3.2. Memudahkan kolaborasi
    Git membuat developer dapat bekerja pada proyek yang sama tanpa mengganggu bagian (fitur) satu sama lain. Untuk menggabung perubahan git mengatur proses "merging".

3.3. Branching
    Git membuat developer dapat membuat branch (cabang), yang merupakan copy dari kode utama. Hal ini memungkinkan developer untuk mengetes fitur seperti update, debug, dll yabg kemudian dapat digabungkan kembali ke cabang utama.

3.4. Backup File
    Karena Git melacak perubahan kode (file) maka dapat menjadi tempat backup file apabila terjadi error.

**4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
<br>Alasan Django menjadi permulaan pembelajaran PBP adalah Django cocok untuk pemula, beberapa alasan diantaranya yakni:

<br>4.1. Menyediakan Struktur yang Terorganisir
    MTV (Model-Template-View) memberikan struktur yang jelas dan terorganisir untuk pengembangan aplikasi web. Pemula dapat memahami bagaimana bagian-bagian aplikasi bekerja sama, seperti:
    - Model untuk interaksi dengan database (ORM),
    - View untuk mengelola logika aplikasi,
    - Template untuk menyusun tampilan front-end.

4.2. Memiliki banyak built in features

4.3. Menggunakan Python
    Selain python yang bahasanya relatif mudah dipelajari, kita sudah belajar python pada semester 1 sehingga memudahkan pembelajaran PBP.

4.4. Skalabel dan Fleksibel
    Django dapat digunakan baik untuk proyek kecil maupun besar.

4.5. Keamanan
    Django relatif aman terhadap ancaman siber umum.

**5. Mengapa model pada Django disebut sebagai ORM?**
<br>Alasan model pada Django disebut ORM (Object-Relational Mapping) adalah karena Django memungkinkan developer untuk berhubungan dengan data base pada kode python. Django berfungsi sebagai penghubung antara objek-objek dalam kode dan data dalam data base. Dengan ORM kita dapat membuat data base menggunakan Python (dictionary dalam kasus proyek ini) dan otomatis menghasilkan pernyataan SQL untuk dapat berhubungan dengan data base model.



