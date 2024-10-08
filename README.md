# click-and-cart: All your needs in one click

# Contents
- [Data Diri](#data-diri)<br>
- [Link Produk](#link-produk)<br>
- [Tugas 2](#tugas-2)<br>
- [Tugas 3](#tugas-3)<br>
- [Tugas 4](#tugas-4)<br>
- [Tugas 5](#tugas-5)
- [Tugas 6](#tugas-6)

## Data Diri
**Nama : Muhammad Faizi Ismady Supardjo**<br>
**NPM : 2306244955**<br>
**Kelas : PBP C**<br>

## Link Produk
**Tautan menuju PWS yang sudah di deploy :** "http://muhammad-faizi-clickandcart.pbp.cs.ui.ac.id"

# Tugas 2
- [Contents](#contents)<br>

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1.1. Membuat direktori dan mengaktifkan virtual environment<br>
- Buat direktori (folder) baru bernama sama dengan nama produk (dalam kasus ini `click-and-cart`)

- Gunakan IDE seperti vscode atau terminal. Buka direktori yang sudah dibuat dan jalankan perintah `python -m venv env` untuk membuat virtual environment

- Jalankan virtual environment dengan perintah `env\Scripts\activate`. Jika venv berhasil aktif, akan ada (env) di depan baris terminal

1.2. Membuat projek Django (checklist 1)<br>
- Di dalam direktori `click-and-cart` buat file `requirements.txt` dan isi dengan
```bash
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
```

- Install dependencies dengan perintah `pip install -r requirements.txt`

- Buat projek django bernama click_and_cart dengan perintah `django-admin startproject click_and_cart .` yang berfungsi membuat folder bernama proyek tersebut dengan isi file bawaan dari django

- Tambahkan string pada ALLOWED_HOSTS di `settings.py` direktori `click_and_cart`
```bash
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

-  Membuat berkas `.gitignore` untuk menentukan file yang tidak ingin dimasukkan ke dalam versi kontrol Git

1.3. Membuat aplikasi bernama main pada proyek (checklist 2)<br>
- Buat aplikasi bernama `main` dengan perintah berikut `python manage.py startapp main` di dalam direktori
- Tambahkan `main` kedalam INSTALLED_APPS pada file `settings.py`. Main merefer ke file html yakni `main.html`

1.4. Melakukan routing pada proyek agar dapat menjalankan aplikasi main (checklist 3)<br>
- Melakukan routing dengan menambahkan kode ini dalam `urls.py`
```bash
    from django.contrib import admin
    from django.urls import path
    from django.urls import path, include

    urlpatterns = [
        path('', include('main.urls')),
        path('admin/', admin.site.urls), path('', include('main.urls'))
    ]
```

1.5. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, dan description (checklist4)<br>
- Isi `models.py` dengan kode berikut
```bash
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        quantity = models.IntegerField()
```

Note: atribut quantity opsional

1.6. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas. (checklist 5)<br>
- Isi file `views.py` dengan kode berikut untuk dapat dikembalikan ke `main.html`
```bash
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
```

- Isi file `main.html` dengan kode berikut
```bash
    <h1>Click and Cart</h1>
    <h3>oleh Muhammad Faizi Ismady Supardjo, kelas PBP C, NPM 2306244955</h3>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Price: </h5>
    <p>{{ price }}<p>
    <h5>Quantity: </h5>
    <p>{{ quantity }}<p>
    <h5>Description: </h5>
    <p>{{ description }}<p>
```

1.7. Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`. (checklist 6) <br>
- Isi file `urls.py` pada direktori main dengan kode berikut agar dapat menghubungkan `views.py` di dalam direktori main dengan `urls.py`
```bash
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
```

1.8. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh orang lain melalui Internet. <br>
- Buka laman PWS, jika belum memiliki akun register jika sudah login

- Buat proyek baru pada website PWS dengan menekan tombol Create New Project. Lalu, isi Project Name dengan clickandcart. setelah itu, tekan Create New Project.

- Akan muncul string credentials yang perlu kita simpan sendiri karena tidak dapat dilihat lagi.

- Pada `settings.py` di proyek Django, tambahkan URL deployment PWS pada ALLOWED_HOSTS. Isi ALLOWED_HOSTS menjadi
```bash
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "muhammad-faizi-clickandcart.pbp.cs.ui.ac.id"]
```

- Buat repositori github bernama `click-and-cart`. Lalu add commit dan push perubahan kedalam repositori tersebut. Jalankan perintah project command yang terlihat di website PWS. Terakhir lakukan command berikut `git push pws main` yang berfungsi push dari github ke pws. Jika PWS tidak error, seharusnya projek sudah berhasil di launch.

1.9. Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut. (checklist 7)<br>
- Buat file `README.md` pada direktori `click-and-cart` terluar dan isi sesuai dengan Tugas 2 PBP.

**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

![Screenshot 2024-09-11 071719](https://github.com/user-attachments/assets/2033f79d-990b-4ecb-9559-4e9fd6eed75d)

Pada Django, apabila klien/user mengirim HTTP request melalui web platform, request tersebut (address HTTP yang dikirim klien)akan di cek sesuai atau tidak pada file `urls.py`. Jika request sesuai, akan dilanjutkan ke file `views.py` yang kemudian memperoleh data dari `models.py` berisi atribut-atribut. Setelah itu, data dan atribut akan di proses di template yang berisi main.html. Lalu, setelah data sudah ada di dalam template, template akan menghasilkan respon ke web platform, menampilkan tampilan web pada `views.py`

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

# Tugas 3
- [Contents](#contents)<br>
- [Screenshot Postman](#screenshot-postman)<br>

**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**<br>
Data delivery adalah proses terjadinya proses pengiriman atau distribusi data dari suatu sistem, server, atau aplikasi ke sistem lain (antarsistem) atau ke pengguna. Data delivery mencakup transfer data antar server, komunikasi antar aplikasi, sinkronisasi informasi, serta pengiriman data real-time ke perangkat atau sistem yang memerlukan akses informasi secara tepat waktu. Tentu kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data delivery memastikan platform dapat beroperasi dengan efisien dan responsif. Contohnya ada user yang mengirim data melalui form, tentu server harus dengan cepat memberi umpan balik ke pengguna apakah data tersebut berhasil masuk.

**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**<br>
Menurut saya, JSON (JavaScript Object Notation) lebih baik dibanding XML (eXtensible Markup Language). Beberapa alasan JSON lebih populer dibanding XML:<br>

- Lebih sederhana: JSON memiliki sintaks yang dapat dibilang cukup sederhana (mirip dictionary pada Python) dibanding XML yang memerlukan tag pembuka dan penutup.

- Struktur data: JSON memiliki struktur data yang fleksibel dan ukuran data yang lebih kecil dikarenakan format yang ringkas.

- Terintegrasi: Penggunaan JSON sangat umum dalam pemrograman web.

**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**<br>
Fungsi method is_valid() pada form Django adalah untuk memeriksa apakah data yang dimasukkan oleh pengguna valid atau tidak berdasarkan aturan validasi yang telah ditentukan di form. Metode ini mengecek apakah semua field yang diperlukan diisi, apakah format data sesuai (field, parameter, dll), dan apakah ada kesalahan dalam input.

Setelah memanggil is_valid(), Django akan:<br>
- Melakukan Validasi: Memastikan bahwa data yang dimasukkan sesuai dengan persyaratan (misalnya, panjang string, tipe data, atau aturan khusus lain yang diterapkan pada form).

- Mengisi Atribut cleaned_data: Jika data valid, is_valid() akan mengembalikan True, dan data yang telah dibersihkan akan tersedia di atribut cleaned_data. Ini memudahkan developer untuk mengakses data yang telah diproses dan valid.

- Menyimpan Error Jika Tidak Valid: Jika data tidak valid, is_valid() akan mengembalikan False, dan pesan error akan disimpan di atribut errors, yang dapat ditampilkan kembali kepada pengguna untuk perbaikan.

Alasan method is_valid() dibutuhkan:<br>
- Mencegah Input Tidak Valid: Tanpa proses validasi, pengguna dapat mengirimkan data dalam berbagai bentuk yang tidak sesuai atau tidak aman (misalnya, SQL injection, XSS). Dengan validasi, hanya data yang memenuhi aturan yang bisa diproses lebih lanjut.

- Keamanan Data: Validasi membantu mencegah potensi serangan dan menjaga integritas serta keamanan aplikasi, memastikan bahwa data yang diterima sesuai dan tidak berbahaya.

- Pengalaman Pengguna: is_valid() membantu mengidentifikasi kesalahan input pengguna, memberikan umpan balik yang bermanfaat, dan memastikan data yang dikirim benar sebelum diproses lebih lanjut.<br>

Kesimpulannya, is_valid() memastikan hanya data yang benar dan sesuai yang masuk ke dalam sistem.

referensi: https://www.javatpoint.com/django-form-validation

**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?** <br>
csrf_token (Cross Site Request Forgery Token) dibutuhkan saat membuat form di Django untuk melindungi aplikasi dari Cross Site Request Forgery. Cross Site Request Forgery adalah bentuk penyerangan dimana penyerang mencoba memaksa pengguna untuk menjalankan aksi tidak sah tanpa sepengetahuan mereka, contohnya transaksi.

Apabila tidak menambahkan csrf_token pada form Django maka aplikasi menjadi rentan terhadap serangan csrf. Hal ini dimanfaatkan penyerang yang dapat dengan mudah memodifikasi situs sehingga pengguna tanpa sadar membuka situs tersebut. Adanya csrf_token pada form memastikan ada token unik pada setiap form yang dikirim ke server. Jika csrf_token tidak ada, aplikasi tidak bisa menentukan mana form yang sah atau tidak.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**<br>
5.1. Membuat direktori baru `templates` pada root folder dan isi dengan file `base.html`. File `base.html` berisi:
```bash
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
5.2. Menambahkan line berikut pada `settings.py`
```bash
'DIRS': [BASE_DIR / 'templates'],
```

5.3. Mengubah `main.html` yang ada pada main/templates/ untuk mengextend `base.html`. Dilakukan dengan menambah line berikut dipaling atas.
```bash
{% extends 'base.html' %}
```

5.4. Memodifikasi `models.py` untuk menjaga keamanan website dengan menambahkan atribut id.
```bash
import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
```

5.4.1 Lakukan migrasi model

5.5. Membuat form input data (checklist 1) dengan membuat file `forms.py` pada direktori main. Isi file sebagai berikut:
```bash
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "quantity", "description"]
```

5.6. Memodifikasi `views.py` dengan membuat method agar dapat menambah produk dari form yang disubmit dan memodifikasi show_main agar menerima parameter input dari form. Isi file sebagai berikut:
```bash
from django.shortcuts import render, redirect  
from main.forms import ProductEntryForm
from main.models import Product
from django.shortcuts import render

# Create your views here.
def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'name': 'Sepeda',
        'price' : '2000000',
        'quantity' : '10',
        'description': 'sepeda roda dua, cocok untuk pemula',
        'product_entries' : product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

5.6.1. Buka file `urls.py`, import method yang sudah dibuat, dan tambahkan path URL dengan menambahkan line berikut:
```bash
from main.views import show_main, create_product_entry

urlpatterns = [
    ...
    path('create-product-entry', create_product_entry, name='create_product_entry'),
]
```

5.7. Pada direktori main/templates/ buat file baru bernama `create_product_entry.html` dan isi sebagai berikut:
```bash
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>
{% endblock %}
```

5.8. Modifikasi `main.html` pada main/templates/ agar dapat melihatkan data produk. Isi file sebagai berikut:
```bash
{% extends 'base.html' %}
{% block content %}
<h1>Click and Cart</h1>
<h3>oleh Muhammad Faizi Ismady Supardjo, kelas PBP C, NPM 2306244955</h3>

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Price: </h5>
<p>{{ price }}<p>
<h5>Quantity: </h5>
<p>{{ quantity }}<p>
<h5>Description: </h5>
<p>{{ description }}<p>

{% if not product_entries %}
<p>Belum ada data product pada Click and Cart.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Quantity</th>
    <th>Description</th>
  </tr>

  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.quantity}}</td>
    <td>{{product_entry.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
{% endblock content %}
```

5.8.1. Memodifikasi `views.py` agar dapat return data dalam bentuk XML dan JSON secara keseluruhan serta return data XML dan JSON sesuai id. Isi file dimodifikasi sebagai berikut:
```bash
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect  
from main.forms import ProductEntryForm
from main.models import Product
from django.shortcuts import render

# Create your views here.
def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'name': 'Sepeda',
        'price' : '2000000',
        'quantity' : '10',
        'description': 'sepeda roda dua, cocok untuk pemula',
        'product_entries' : product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

5.8.2. Memodifikasi `urls.py` untuk mengimport method yang sudah dibuat dan menambahkan url patterns yang sesuai. Isi file sebagai berikut:
```bash
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Screenshot Postman
- [Tugas 3](#tugas-3)<br>

**JSON**
![Screenshot 2024-09-17 175417](https://github.com/user-attachments/assets/8d10be97-e4d3-43cd-adbd-d60d6e652395)

**XML**
![Screenshot 2024-09-17 175049](https://github.com/user-attachments/assets/20489b1b-0679-4eca-bdf3-d3f91635e232)

**JSON by ID**
![Screenshot 2024-09-17 175438](https://github.com/user-attachments/assets/23cf54ad-c8db-486b-bffd-433f4bc864b1)

**XML by ID**
![Screenshot 2024-09-17 175230](https://github.com/user-attachments/assets/ba4a7aba-5712-49f6-a077-4a95b09d5ddc)

# Tugas 4
- [Contents](#contents)<br>
- [Foto akun pengguna](#foto-akun-pengguna)

**1. Apa perbedaan antara HttpResponseRedirect() dan redirect()**<br>
i. `HttpResponseRedirect()`
- Definisi: adalah kelas bawaan Django yang digunakan untuk membuat respons HTTP dengan kode status `302` (Redirect Found) untuk mengarahkan pengguna ke URL yang ditentukan.
- Sintaks:
```bash
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some-url/')
```
- Parameter: url tujuan
- Kekurangan: Tidak bisa melakukan reverse lookup secara otomatis. Karena itu dalam tugas ini kita harus menggunakan fungsi reverse untuk mendapat url dari urls.py.

ii. `redirect()`<br>
- Definisi: adalah fungsi bantu (helper function) di Django yang lebih fleksibel dan mudah digunakan daripada HttpResponseRedirect(). Fungsi ini dapat otomatis mmengarahkan pengguna ke URL, view, nama URL, dll sehingga lebih praktis.
- Sintaks:
```bash
from django.shortcuts import redirect

def my_view(request):
    return redirect('/some-url/')
```
- Parameter: String URL, Nama view dari `urls.py`, dll.
- Keuntungan: Lebih fleksibel

**2. Jelaskan cara kerja penghubungan model MoodEntry dengan User!**<br>
Untuk menghubungkan model `MoodEntry` dengan model User dalam Django, Anda dapat menggunakan field `ForeignKey` pada model `MoodEntry` yang mengacu pada model User

- Contoh implementasi
```bash
from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.mood} at {self.time}"
```
- Penjelasan:<br>
Setiap ada user membuat input suasana hati, maka input tersebut dikaitkan dengan user yang login.<br>
Field user: Menggunakan ForeignKey untuk membuat hubungan many-to-one dengan model User. Parameter on_delete=models.CASCADE memastikan bahwa jika seorang pengguna dihapus, semua entri suasana hati yang terkait juga akan dihapus.

referensi = Django documentation

**3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**<br>
i. Perbedaan:
- Authentication:<br>
Proses verifikasi identitas pengguna. Biasa melibatkan password dan username dimana input pengguna akan dibandingkan dengan data yang ada di database, jika cocok pengguna ter autentikasi.

- Authorization:<br>
Proses menentukan apa yang dapat dilakukan (authorized) oleh pengguna setelah terautentikasi. Setelah terautentikasi, sistem mengecek apa yang bisa dilakukan oleh pengguna (contohnya role berbeda-beda pada sistem seperti admin, user biasa, dll).

ii. Yang dilakukan saat pengguna login:<br>
- Pengguna memasukkan kredensial (username dan password)
- Sistem melakukan verifikasi, Django membandingkan input pengguna dengan data yang ada di database.
- Jika cocok pengguna berhasil login, jika tidak akan terdapat pesan error.

iii. Implementasi authentication dan uthorization di Django<br>
Implementasi pada Django<br>
Authentication:
- User model: Django memiliki model user bawaan yang menyimpan informasi pengguna.
- Middleware: Mengecek apakah pengguna sudah
terautentikasi untuk setiap request. Jika belum akan diarahkan ke page login.

Authorization:
- Permission: Django memiliki sistem permission sehingga dapat menentukan memberi izin ke pengguna.
- Group: Django dapat mengelompokkan pengguna kedalam grup. Dimana kita dapat menentukan izin grup tersebut.

**4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**<br>
i. Cara Django mengingat pengguna:<br>
Django mengingat pengguna dengan session. Saat pengguna berhasil login, Django akan membuat session unik dan menyimpannya dalam bentuk cookie di browser pengguna. Cookie ini merujuk ke data session yang disimpan pada server.

ii. Kegunaan lain cookies:<br>
Selain mengingat session pengguna cookies berfungsi untuk
- Personalisasi: Menyimpan preferensi user seperti bahasa, tema web, dll.
- Autentikasi: Cookies dapat digunakan untuk autentikasi pihak ketiga.
- "Remember me": Fitur remember menggunakan cookies untuk memungkinkan pengguna tetap login dalam waktu lama.<br>

iii. Apakah semua cookies aman?<br>
Tidak, tidak semua cookies aman. Dibalik kegunaannya, cookies membawa berbagai tantangan, diantaranya:
- Cross-Site Scripting (XSS): Jika keamanan kurang, cookies dapat dimasukkan dengan kode jahat,
- Cross-Site Request Forgery (CSRF): Serangan CSRF dapat mengeksploitasi cookie session untuk melakukan tindakan yang tidak diinginkan atas nama pengguna.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**<br>
5.1 Membuat Fungsi dan Form Registrasi (Checklist 1)
- Aktifkan virtual environment

5.1.2 Buka `views.py` yang ada pada direktori `main`. Tambahkan import berikut di paling atas.
```bash
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

- Buat fungsi `register` didalam `views.py`. Sebagai berikut.
```bash
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

5.1.3 Buat file bernama `register.html` pada direktori `main/templates`. Isi sebagai berikut.
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

- Buka file `urls.py`, impor fungsi yang sudah dibuat dan masukkan pathnya.
```bash
from main.views import register

 urlpatterns = [
    ...
    path('register/', register, name='register'),
 ]
```

5.2 Membuat Fungsi Login<br> (Checklist 1)
5.2.1 Buka `views.py` yang ada pada direktori `main`. Tambahkan import berikut di paling atas.
```bash
from django.contrib.auth.forms import UserCreationForm AuthenticationForm
from django.contrib.auth import authenticate, login
```

5.2.2 Buat fungsi login_user di dalam `views.py`
```bash
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

5.2.3 Buat file `login.html` di dalam `main/templates`. Isi file sebagai berikut.
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

- Buka file `urls.py`, import fungsi yang sudah dibuat dan masukkan pathnya.

```bash
from main.views import login_user

urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```

5.3 Membuat fungsi logout<br> (Checklist 1)
5.3.1 Buka `views.py` yang ada pada direktori `main`. Tambahkan import berikut di paling atas.
```bash
from django.contrib.auth import logout
```

5.3.2 Buat fungsi logout didalam `views.py`
```bash
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

5.3.3 Buat tombol logout pada `main.html`. Kode sebagai berikut
```bash
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```
- Buka file `urls.py`, impor fungsi yang sudah dibuat dan masukkan pathnya.
```bash
from main.views import logout_user

urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```

5.4 Restriksi akses<br>
5.4.1 Buka `views.py`, tambahkan import login required
```bash
from django.contrib.auth.decorators import login_required
```

- Taruh login_required diatas show_main
```bash
...
@login_required(login_url='/login')
def show_main(request):
...
```

5.5 Menggunakan data dari cookies (Checklist 4) <br>
5.5.1  Buka `views.py`, tambahkan import berikut di paling atas
```bash
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

- Ubah fungsi login user untuk dapat melihat kapan pengguna terakhir login. Kodenya sebagai berikut (ganti pada if block)
```bash
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

- Pada fungsi show_main, tambahkan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context`

- Modif fungsi `logout_user`. Menjadi sebagai berikut:
```bash
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

- Tambahkan tombol logout pada `main.html` sebagai berikut
```bash
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

5.6 Menghubungkan entri produk dengan user (Checklist 3)
- Import  model user pada `models.py`. Tambahkan variabel user pada model `productentry`. Kode sebagai berikut
```bash
import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
```

- Buka `views.py`, ubah kode pada fungsi `create_product_entry`. Kode sebagai berikut:
```bash
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

- Ubah value product entries pada `show_main()` sebagai berikut:
```bash
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'price' : '2000000',
        'quantity' : '10',
        'description': 'sepeda roda dua, cocok untuk pemula',
        'product_entries' : product_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```

- Lakukan migration dengan perintah `python manage.py makemigrations`

5.7 Mempersiapkan aplikasi web untuk environtment production.
- Tambahkan import baru pada `setttings.py` dan ganti variabel `DEBUG` menjadi seperti.
```bash
import os

PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

5.8 Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal. (Checklist 2)<br>

## Foto akun pengguna
- [Tugas 4](#tugas-4)

**username: kingsapi**
![alt text](image.png)
**username:sapihitam**
![alt text](image-1.png)

# Tugas 5

- [Contents](#contents)<br>
- [Foto Navbar](#foto-navbar)

**1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Urutan prioritas pengambilan CSS selector yakni:<br>
1.1 `!important` (Important Rule), Deklarasi yang menggunakan `!important` akan selalu memiliki prioritas tertinggi mengesampingkan yang lainnya. Contoh penggunaan:
```bash
p {
  color: red !important;
}
``` 
1.2 Inline Styles, penulisan menggunakan inline styles akan selalu memiliki prioritas tertinggi. Contoh penggunaan:
```bash
<p style="color: blue;">This text is blue</p>
``` 

1.3 ID Selector, `#id` memiliki prioritas lebih tinggi dibandingkan elemen atau class.

1.4 Class Selector, `.class`, attribute selector `[type="text"]` memiliki prioritas menengah (lebih tinggi daripada tag).

1.5 Tag Selector, memiliki prioritas terendah.

**2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!** <br>
Alasan responsive design menjadi konsep penting dalam pengembangan web adalah, karena membantu memastikan bahwa tampilan dan fungsionalitas website atau aplikasi web beradaptasi dengan berbagai ukuran layar dan perangkat yang digunakan oleh pengguna, seperti smartphone, tablet, dan desktop. Hal tersebut menghasilkan:<br> 
- Pengalaman pengguna yang lebih baik 
- Penggunaan yang efisien di berbagai perangkat
- Integrasi sistem yang lebih baik

Contoh:<br>
Aplikasi yang sudah menerapkan:<br>
- Amazon
- X/Twitter
- Instagram

Aplikasi yang belum menerapkan:<br>
- SiakNG

**3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!** <br>
3.1 Margin, adalah border (ruang luar batas) elemen yang berfungsi membuat jarak antara elemen satu dan elemen lainnya.<br>
Contoh penggunaan:
```bash
.element {
  margin: 20px; /* Semua sisi diberi margin 20px */
}
```

3.2 Border, adalah garis yang mengelilingi elemen. Berada di antara margin dan padding.Kita bisa mengatur ketebalannya, warnanya, dan jenis garisnya.<br>
Contoh penggunaan:
```bash
.element {
  border: 2px solid black; /* Border hitam, solid, dengan ketebalan 2px */
}
```

3.3 Padding, adalah border (ruang dalam batas) elemen yang berfungsi memisahkan konten elemen dari batasnya.  Padding menambah ruang antara konten (misalnya teks) dengan bagian dalam dari border.<br>
Contoh penggunaan:
```bash
.element {
  padding: 10px; /* Semua sisi diberi padding 10px */
}
```

**4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
Secara garis besar, flex box dan grid layout adalah dua teknik layout yang sangat populer dalam CSS untuk mengatur tata letak elemen-elemen di halaman web secara fleksibel dan responsi. <br>

4.1 Flex box<br>
4.1.1 Konsep: <br>
Flexbox adalah model layout satu dimensi yang digunakan untuk mengatur elemen di sepanjang sumbu utama (horizontal atau vertikal). Dengan Flexbox, kita bisa dengan mudah menyusun ruang antar elemen dalam suatu kontainer.

4.1.2 Kegunaan:<br>
- Mengatur tata letak elemen secara horizontal atau vertikal dalam satu dimensi.
- Mengatur elemen agar responsif dan mudah diposisikan tanpa memikirkan ukuran pasti.
- Mengatur tata letak elemen yang memiliki lebar atau tinggi dinamis.

4.2 Grid Layout<br>
4.2.1 Konsep:<br>
CSS Grid Layout adalah model layout dua dimensi yang dapat mengatur elemen berdasarkan baris dan kolom. Grid Layout memberikan kontrol lebih rinci dibandingkan Flexbox karena kita dapat mengatur elemen secara horizontal dan vertikal (dua dimensi) dalam grid.

4.2.2 Kegunaan<br>
- Mengatur elemen dalam bentuk baris dan kolom.
- Sangat berguna untuk layout yang lebih kompleks dan presisi, seperti layout halaman web dengan beberapa kolom dan baris.
- Membuat tata letak responsif yang lebih terstruktur.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**<br>

5.1 Mengimplementasi fungsi edit dan delete product (Checklist 1)<br>
5.1.1 Membuat kedua fungsi pada `views.py`
```bash
def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```

5.1.2 Import dan route kedua fungsi ke `urls.py`
```bash
from main.views import edit_product
from main.views import delete_product

urlpatterns = [
    ...
    path('edit-mood/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    ...
]
```

5.2 Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya<br>
- Menambahkan kode pada file `base.html` agar bisa dihubungkan dengan tailwind. Isi file sebagai berikut
```bash
<meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
```

- Membuat folder `static` yang didalamnya berisi `css` dan `image`. Buat file `global.css` didalamnya sebagai berikut
```bash
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #674ea7;
    box-shadow: 0 0 0 3px #674ea7;
}
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}
```

5.2.1 Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
- Ubah file `login.html` sebagai berikut
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex flex-col items-center justify-center bg-gray-900 py-12 px-4 sm:px-6 lg:px-8 relative">
  <!-- Text Above the Form -->
  <div class="absolute top-24 text-center">
    <p class="text-4xl font-bold text-gray-300">
      Click and Cart by Faizi Ismady
    </p>
  </div>

  <!-- Login Form -->
  <div class="max-w-md w-full space-y-8 bg-gray-800 p-6 rounded-lg shadow-lg mt-12">
    <div>
      <h2 class="text-center text-3xl font-extrabold text-gray-100 mb-4">
        Welcome Back!
      </h2>
      <p class="text-center text-gray-400 mb-6">
        Please login to your account
      </p>
    </div>
    <form method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm space-y-4">
        <div>
          <label for="username" class="block text-gray-400">Username</label>
          <input id="username" name="username" type="text" required 
                 class="appearance-none block w-full px-3 py-2 border border-gray-600 
                        placeholder-gray-500 text-gray-300 bg-gray-700 rounded-md 
                        focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" 
                 placeholder="Enter your username">
        </div>
        <div>
          <label for="password" class="block text-gray-400">Password</label>
          <input id="password" name="password" type="password" required 
                 class="appearance-none block w-full px-3 py-2 border border-gray-600 
                        placeholder-gray-500 text-gray-300 bg-gray-700 rounded-md 
                        focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" 
                 placeholder="Enter your password">
        </div>
      </div>

      <div class="mt-6">
        <button type="submit" 
                class="group w-full py-2 px-4 border border-transparent text-sm font-medium 
                       rounded-md text-white bg-indigo-600 hover:bg-indigo-500 
                       focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 
                       transition-transform transform hover:scale-105 duration-300">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-gray-100">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-indigo-400 hover:text-indigo-300 transition">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```

- Ubah file `register.html` sebagai berikut
```bash
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style bg-gray-800 p-6 rounded-lg shadow-lg">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-100">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-100">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-700 hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-gray-100">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-indigo-400 hover:text-indigo-300">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```

- Ubah file `create_product_entry.html` sebagai berikut
```bash
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Create Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="flex flex-col min-h-screen bg-gray-900">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-gray-100">Create Product Entry</h1>
  
    <div class="bg-gray-800 shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-100">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-400">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-gray-700 text-white font-semibold px-6 py-3 rounded-lg hover:bg-gray-600 transition duration-300 ease-in-out w-full">
            Create Product Entry
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

{% endblock %}
```

5.2.2 Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Jikabelum ada product, halaman daftar product akan menampilkan gambar dan pesan.Jika sudah ada, halaman daftar product akan menampilkan detail product menggunakan card. Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!

- Buat file `card_product.html` dengan isi sebagai berikut
```bash
<div class="relative break-inside-avoid">
  <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
    <div class="w-[3rem] h-8 bg-gray-700 rounded-md opacity-80 -rotate-90"></div>
    <div class="w-[3rem] h-8 bg-gray-700 rounded-md opacity-80 -rotate-90"></div>
  </div>
  <div class="relative top-5 bg-gray-800 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-gray-700 transform rotate-1 hover:rotate-0 transition-transform duration-300">
    <div class="bg-gray-700 text-white p-4 rounded-t-lg border-b-2 border-gray-600">
      <h3 class="font-bold text-xl mb-2">{{ product_entry.name }}</h3>
    </div>
    <div class="p-4">
      <p class="font-semibold text-white mb-2">Product Description</p> 
      <p class="text-gray-300 mb-2">
        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{ product_entry.description }}</span>
      </p>
      <div class="mt-4">
        <p class="text-gray-300 font-semibold mb-2">Stock Quantity</p>
        <div class="relative pt-1">
          <div class="flex mb-2 items-center justify-between">
            <div>
              <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-indigo-400 bg-gray-600">
                {% if product_entry.quantity > 100 %}100+{% else %}{{ product_entry.quantity }}{% endif %}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="absolute top-0 -right-4 flex space-x-1">
    <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
    </a>
    <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
</div>
```
- Ubah file `main.html` sebagai berikut
```bash
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Click and Cart</title>
{% endblock meta %}
{% block content %}
{% include 'navbar.html' %}
<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-900 flex flex-col">
  <div class="p-2 mb-6 relative">
    <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
      {% include "card_info.html" with title='User Name' value=name show_member_since=True %}
      {% include "card_info.html" with title='Entered Products' value=total_products show_member_since=False %}
    </div>
  </div>
  <div class="px-3 mb-4">
    <div class="flex rounded-md items-center bg-gray-700 py-2 px-4 w-fit">
      <h1 class="text-gray-100 text-center">Last Login: {{last_login}}</h1>
    </div>
  </div>
  <!--
  <div class="flex justify-end mb-6">
    <a href="{% url 'main:create_product_entry' %}" class="bg-gray-700 hover:bg-gray-600 text-gray-100 font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
      Add New Product Entry
    </a>
  </div>
  -->
    
  {% if not product_entries %}
  <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
    <img src="{% static 'image/images.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
    <p class="text-center text-gray-400 mt-4">Belum ada data product pada Click and Cart.</p>
  </div>
  {% else %}
  <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
    {% for product_entry in product_entries %}
      {% include 'card_product.html' with product_entry=product_entry %}
    {% endfor %}
  </div>
  {% endif %}
</div>
{% endblock content %}
```

5.3 Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
- Buat file `navbar.html` pada direktori `templates` isi sebagai berikut
```bash
<nav class="bg-gray-800 shadow-lg fixed top-0 left-0 z-40 w-screen">
  <div class="max-w-full px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <h1 class="text-2xl font-bold text-left text-gray-400">Click and Cart by Faizi Ismady</h1>
      </div>
      <div class="hidden md:flex items-center">
        {% if user.is_authenticated %}
          <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:create_product_entry' %}" class="text-center bg-gray-700 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-4">
            Add New Product
          </a>
          <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
  <!-- Mobile menu -->
  <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
    <div class="pt-2 pb-3 space-y-1 mx-auto">
      {% if user.is_authenticated %}
        <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
        <a href="{% url 'main:create_product_entry' %}" class="block text-center bg-gray-700 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Add New Product
        </a>
        <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Logout
        </a>
      {% else %}
        <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
          Login
        </a>
        <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Register
        </a>
      {% endif %}
    </div>
  </div>
  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");

    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>
```

## Foto Navbar
- [Tugas 5](#tugas-5)

**Kondisi navbar mobile**
![S__43261979](https://github.com/user-attachments/assets/de6f6807-0c85-4899-961d-3c339a3d647e)


**Kondisi navbar desktop**
![Screenshot 2024-10-02 093123](https://github.com/user-attachments/assets/76da57c0-6eb0-48e7-af1e-e7f166480d42)

# Tugas 6
- [Contents](#contents)<br>

**1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**
- Interaktivitas dan responsivitas<br>
JavaScript membuat  web menjadi lebih interaktif dan responsif. seperti
elemen dropdown, transisi, dll.

- Pengolahan data sisi klien<br>
JavaScript membuat data dapat diproses di sisi klien (browser pengguna), mengurangi 
beban server dan mempercepat aplikasi.

- Pembaharuan dinamis<br>
Dengan JavaScript, konten page dapat diperbarui secara dinamis, tidak perlu merefresh halaman
contohnya menggunakan teknik seperti AJAX.

- Crossplatform compatibility<br>
JavaScript dapat dijalankan pada banyak browser tanpa perlu konfigurasi lanjutan.

- Integrasi dengan teknologi lain<br>
JavaScript dapat diintegrasikan dengan berbagai macam teknologi seperti HTML dan CSS. Selain itu, JS
mendukung berbagai framework dan library.

**2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()!` Apa yang akan terjadi jika kita tidak menggunakan `await`?**<br>
Fungsi `await` ketika digunakan dengan `fetch()` adalah untuk memastikan bahwa JavaScript menunggu 
hingga operasi `fetch()` selesai sebelum melanjutkan eksekusi kode berikutnya. `fetch()` sendiri adalah 
fungsi asinkron yang mengembalikan sebuah Promise. Dengan menggunakan `await`, kita menunggu 
respons dari Promise tersebut sebelum melanjutkan ke langkah berikutnya dalam kode.

Apabila kita tidak menggunakan `await` atau fungsi lain yang sejenis (seperti `.then()`), maka JavaScript akan 
melanjutkan eksekusi kode tanpa menunggu hasil dari operasi asinkron tersebut. Dalam kasus ini, kode bisa
terjalankan, walaupun data yang diperlukan belum selesai di proses.

**3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?**<br>
Kita perlu menggunakan decorator `@csrf_exempt` pada view yang digunakan untuk AJAX POST dalam Django 
ketika kita tidak ingin memeriksa token CSRF (Cross-Site Request Forgery) untuk permintaan tertentu. Beberapa alasan 
digunakannya antara lain:
- Mencegah Kesalahan CSRF<br>
Django secara default menerapkan perlindungan CSRF pada semua permintaan POST untuk mencegah 
serangan CSRF, di mana pengguna yang tidak sah mencoba untuk mengirimkan permintaan tanpa izin. 
Jika kita tidak menonaktifkan pemeriksaan CSRF pada view AJAX, dan tidak mengirimkan token CSRF 
dengan benar dari sisi klien, kita akan mendapatkan kesalahan "403 Forbidden".

- Kemudahan Implementasi<br>
Dalam beberapa kasus, terutama pada aplikasi yang tidak menangani data sensitif atau ketika keamanan 
CSRF sudah diatur dengan cara lain, kita dapat memilih untuk menggunakan `@csrf_exempt` untuk 
menghindari penanganan manual token CSRF pada permintaan AJAX.

- AJAX dari Domain yang Sama (Same-Origin Requests)<br>
Ketika kita menggunakan AJAX pada domain yang sama, kita mungkin merasa aman untuk 
menonaktifkan pemeriksaan CSRF karena risikonya lebih rendah dibandingkan dengan permintaan lintas 
domain. Namun, ini hanya aman jika aplikasi kita tidak terpapar terhadap risiko serangan CSRF.

Meski demikian, menonaktifkan CSRF dengan menggunakan `@csrf_exempt` juga membuka potensi risiko 
keamanan. Oleh karena itu, penggunaan decorator ini harus dipertimbangkan dengan hati-hati.

**4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**<br>
Validasi data di backend wajib dilakukan untuk keamanan, karena pengguna bisa memanipulasi data di sisi 
frontend. Backend memastikan data konsisten dan sesuai standar, serta tidak bergantung pada fitur browser. 
Validasi kompleks juga lebih efektif dilakukan di backend. Frontend validation tetap penting untuk pengalaman 
pengguna yang lebih responsif, tapi tidak cukup untuk menjamin keamanan data.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**<br>

5.1 AJAX `GET`<br>
5.1.2 Ubahlah kode `cards` data mood agar dapat mendukung AJAX `GET`
- Tambahkan import dan membuat fungsi `product_entry_by_ajax` pada `views.py`. Sebagai berikut.
```bash
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    user = request.user

    new_product = Product(
        name=product_name, 
        description=description,
        price=price,
        quantity=quantity,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```

- Melakukan routing fungsi `product_entry_by_ajax` ke `urls.py`, sebagai berikut
```bash
...
from main.views import add_product_entry_ajax

urlpatterns = [
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
]
```

5.1.2 Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
- Fungsi JavaScript untuk GET Data: Berikut ini adalah fungsi JavaScript yang digunakan untuk mengambil data dari server menggunakan AJAX `GET` dan mengupdate card di halaman utama.
```bash
async function getProductEntries() {
    return fetch("{% url 'main:show_json' %}").then((res) => res.json());
}

async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";
    const productEntries = await getProductEntries();
    
    let htmlString = "";
    let classNameString = "";

    if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/images.png' %}" alt="No product data" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">No product data available.</p>
            </div>
        `;
    } else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
        productEntries.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);  
            const description = DOMPurify.sanitize(item.fields.description);  

            htmlString += `
            <div class="relative break-inside-avoid">
                <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
                    <h3 class="font-bold text-xl mb-2">${name}</h3>
                    <p class="text-gray-600">${description}</p>
                </div>
                <div class="p-4">
                    <p class="font-semibold text-lg mb-2">Stock Quantity</p>
                    <p class="text-gray-700 mb-2">${item.fields.quantity}</p>
                    <p class="text-gray-700 font-semibold mb-2">Price</p>
                    <p class="text-xs inline-block py-1 px-2 bg-gray-300 rounded">${item.fields.price}</p>
                </div>
            </div>`;
        });
    }
    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
}

refreshProductEntries();
```

5.2 AJAX Post
5.2.1 Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
- Modal Form: Tambahkan form dalam modal untuk menambahkan data baru. Pastikan form tersebut terhubung dengan tombol yang membuka modal. Berikut kodenya pada `main.html`
```bash
...
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
    <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
      <!-- Modal header -->
      <div class="flex items-center justify-between p-4 border-b rounded-t">
        <h3 class="text-xl font-semibold text-gray-900">
          Add New Product Entry
        </h3>
        <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
          <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
          </svg>
          <span class="sr-only">Close modal</span>
        </button>
      </div>
...
```

5.2.2  Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data
- Fungsi `add_product_entry_ajax` pada `views.py`: Berikut ini adalah fungsi untuk menyimpan data baru ke dalam database. Modifikasi fungsi agar membersihkan input data menggunakan `strip_tags` untuk mencegah serangan XSS. (Sisanya sama seperti kode pada 5.1.2)
```bash
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
```

5.2.3 Buatlah path `/create-ajax/` yang mengarah ke fungsi view yang baru kamu buat.
- Menambahkan routing pada `urls.py` dengan import dan menambah urlpatters. (Sama seperti step 5.1.2)

5.2.4 Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/create-ajax/`.
- JavaScript untuk AJAX POST: Kode di bawah ini digunakan untuk mengirim data dari form modal ke server melalui AJAX POST, kemudian memperbarui data di halaman tanpa reload. Kode pada `main.html`
```bash
  function addProductEntry() {
    fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => refreshProductEntries())

    document.getElementById("productEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }

  document.getElementById("productEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProductEntry();
  })
```
