TUGAS 2:
Link menuju PWS: http://reyvano-mario-livingspaces.pbp.cs.ui.ac.id/

Link menuju jawaban pertanyaan: https://docs.google.com/document/d/1VXBnhfY-mlybEKJrxxPkxrCPvkGnb0jJz-qiiD2X_Z4/edit?usp=sharing

TUGAS3:

PERTANYAAN TUGAS 3:
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab: Karena pada sebuah aplikasi diperlukan interaksi antara pengguna dan platform seperti user menginput data melalui form.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawab: Menurut saya, JSON lebih mudah dibaca dibandingkan XML karena yang ditampilkan oleh JSON hanya merupakan atribut-atribut (key dan valuenya) dari model sehingga lebih mudah dibaca, tidak seperti XML yang harus menggunakan tag. Mungkin hal itu merupakan salah satu penyebab JSON menjadi lebih populer.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawab: Memeriksa apakah form sudah diisi dan form yang user isi sesuai dengan ketentuan yang diberikan.


4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawab: csrf_token adalah sebuah token unik yang digenerate pada setiap session setiap kali user yang berbeda masuk ke sebuah form untuk menginput sesuatu. Saat user submit formnya, token tersebut juga disubmit dan web akan memeriksa apakah token tersebut valid atau tidak. Jika valid, web akan mengijinkan form tersebut disubmit sedangkan jika tidak maka submit tersebut tidak akan diijinkan. Jika tidak menambahkan csrf_token, orang lain bisa saja melakukan submit form seakan akan kita yang melakukan submit tersebut karena tidak adanya token unik yang diperiksa pada saat submit form tersebut (orang lain bisa memanfaatkan session kita karena tidak ada csrf token yang digenerate).

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: a. Membuat input form untuk menambahkan objek model pada app sebelumnya: Membuat file forms.py di direktori dan membuat class ProductForm. Setelah itu, mengambil model yang sudah didefinisikan di models.py yaitu Product dan menambahkan fields atribut dari produk produk yang akan diinput. Lalu pada views.py membuat fungsi untuk menampilkan form bernama create_product_entry. Di dalam fungsi tersebut, membuat objek ProductForm baru lalu mengecek apakah isi form valid dan request yang diberikan adalah "POST". Jika kondisi benar, maka form akan disimpan dan user akan langsung diredirect ke tampilan utama aplikasi. Return dari fungsi ini adalah render pada file html untuk menampilkan form.

b. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID: Membuat fungsi bernama show_xml dan show_json untuk menampilkan semua data yang ada dalam bentuk xml dan json. Pada fungsi tersebut, menyimpan hasil query dari seluruh data yang ada pada Product ke dalam suatu variabel dengan fungsi Product.objects.all(). Setelah itu mengembalikan HttpResponse yang merupakan hasil translate objek model yang ditranslate menggunakan serializers ke bentuk XML dan JSON. Lalu 2 fungsi lain yaitu show_xml_by_id dan show_json_by_id isinya hampir sama dengan show_xml dan show_json, hanya saja show_xml_by_id dan show_json_by_id meminta parameter tambahan yaitu id dan data yang ada pada model Product akan difilter sesuai id dengan Product.objects.filter(pk=id) sehingga yang disimpan pada variabel dan akan direturn dalam bentuk XML dan JSON adalah data yang sesuai dengan id tersebut.

c.  Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2: Pada urls.py di direktori main, menambahkan path('xml/', show_xml, name='show_xml') dan path('json/', show_json, name='show_json') yang akan memanggil fungsi show_xml dan show_json. Untuk 2 fungsi lainnya, menambahkan path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id') path('json/<str:id>/', show_json_by_id name='show_json_by_id') yang berarti jika user mengunjungi halaman /xml/<ID PRODUCT> atau /json/<ID PRODUCT> maka akan menampilkan data produk yang sesuai id nya dalam bentuk XML atau JSON.

Screenshot Postman
![alt text](https://github.com/reyvanomario/living-spaces/blob/main/gambar_jawaban_pertanyaan/Screenshot%202024-09-11%20at%2021.31.00.png?raw=true)
![alt text](https://github.com/reyvanomario/living-spaces/blob/main/gambar_jawaban_pertanyaan/Screenshot%202024-09-11%20at%2021.28.40.png?raw=true)
![alt text](https://github.com/reyvanomario/living-spaces/blob/main/gambar_jawaban_pertanyaan/Screenshot%202024-09-11%20at%2021.28.20.png?raw=true)
![alt text](https://github.com/reyvanomario/living-spaces/blob/main/gambar_jawaban_pertanyaan/Screenshot%202024-09-11%20at%2021.28.06.png?raw=true)


TUGAS 4:

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
Jawab: HttpResponseRedirect() hanya menerima url view , sedangkat redirect() bisa menerima nama view sekaligus url view

2. Jelaskan cara kerja penghubungan model Product dengan User!
Jawab: Membuat field user di model Product. Setelah itu, di fungsi create_product_entry, menambahkan 'commit=False' di form.save agar form tidak langsung disimpan di database dan assign user yang melakukan request sebagai user dari product entry tersebut, lalu save input form nya. Di views show_main, product entries yang akan ditampilkan di filter berdasarkan user yang sedang login.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Jawab: Authentication adalah proses verifikasi identitas pengguna (dalam hal ini username dan password). Django mengimplementasikannya dengan membuat sistem register akun, login, dan logout. Authorization adalah proses untuk mengizinkan seseorang yang sudah terautentikasi untuk mengakses sesuatu. Django mengimplementasikannya dengan decorator seperti "@login_required(login_url='/login')" yang dibuat pada fungsi show_main yang berarti hanya user yang berhasil login yang bisa mengakses fungsi show_main.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Jawab: Django mengingat pengguna yang telah login dengan cookies. Saat user terhubung dengan server, server membuat data cookie yang unik untuk setiap usernya yang akan dicocokan nantinya terhadap informasi apa yang akan ditampilkan ke masing-masing user. Kegunaan lain dari cookies adalah personalisasi konten sesuai aktivitas yang kita lakukan misalnya saat kita browsing di website e-commerce, website tersebut akan menggunakan cookies untuk menampilkan barang-barang yang relevan terhadap histori pencarian kita. Tidak semua cookies aman digunakan terutama third party cookies karena bisa saja pihak ketiga menggunakan cookies untuk mencuri data dan identitas user.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Jawab: 
a. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar:
Membuat html untuk halaman registrasi dan fungsi register di views.py menggunakan import UserCreationForm. Fungsi registrasi ini lalu melakukan render pada file register.html. Setelah itu melakukan routing untuk fungsi register di urls.py subdirektori main. Untuk fungsi login, membuat file html untuk login dan fungsi login_user pada views.py dengan bantuan import AuthenticationForm. Form tersebut akan meminta username dan password user untuk diautentikasi. Jika berhasil login, akan redirect user ke halaman main. Setelah itu melakukan routing untuk fungsi login_user di urls.py. Untuk fungsi logout, membuat fungsi logout_user dengan bantuan import logout dari django.contrib.auth. Setelah itu, menambahkan button untuk memanggil fungsi logout_user di main.html. Saat fungsi logout_user dipanggil, cookie yang sedang ada akan dihapus dan redirect user ke halaman login. Setelah itu melakukan routing di urls.py untuk fungsi logout_user.

b. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal: Menjalankan kode di lokal lalu melakukan register 2 buah akun berbeda. Setelah itu login dengan username dan password lalu menambahkan tiga product untuk masing-masing akun

c. Menghubungkan model Product dengan User:
Membuat field user di model Product. Setelah itu, di fungsi create_product_entry, menambahkan 'commit=False' di form.save agar form tidak langsung disimpan di database dan assign user yang melakukan request sebagai user dari product entry tersebut, lalu save input form nya. Di views show_main, product entries yang akan ditampilkan di filter berdasarkan user yang sedang login.

d. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi:
Di parameter render fungsi show_main di views.py, menambahkan variabel name berupa request.user.username yaitu username user yang melakukan request (user yang sedang login) lalu menampilkan variabel tersebut di main.html. Untuk membuat cookies, di di fungsi login_user setelah user berhasil login, membuat cookie bernama last_login yang berisi datetime saat ini. Pada parameter context di render fungsi show_main, menambahkan variabel last_login yaitu cookies milik user yang melakukan request dan menampilkannya di main.html.


TUGAS 5:

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jawab: Prioritas dimulai dari inline styles, lalu ID selectors, lalu classes selectors, lalu element selectors

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Jawab: Agar pengguna mendapatkan pengalaman yang lebih baik seperti web yang dapat menyesuaikan tampilan dengan ukuran layar device yang pengguna gunakan. Contoh aplikasi yang sudah menerapkan adalah aplikas-aplikas e-commerce seperti Tokopedia dan Shopee, sedangkan contoh aplikasi yang belum menerapkan adalah aren

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Jawab: margin adalah area di luar di sekeliling elemen, border adalah garis yang mengelilingi elemen, dan padding adalah ruang di dalam elemen di sekeliling konten yang terdapat di elemen tersebut.
Cara mengimplementasikannya: border: 4px solid black; margin: 10px; padding: 15px; (diletakkan di dalam css selectors)

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Jawab: flex box adalah sistem layout 1 dimensi (bekerja dalam 1 baris atau 1 kolom), sedangkan grid adalah sistem layout 2 dimensi (bekerja baik dalam baris maupun kolom)

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawab: 
a. Implementasikan fungsi untuk menghapus dan mengedit product: 
    1) Membuat fungsi edit_product di views.py yang menerima parameter request dan id product, lalu buat file edit_product.html (di main/templates) yang akan dirender oleh fungsi edit_product tadi, lalu menambahkan path di urls.py untuk menuju fungsi edit_product
    2) Menambahkan button di setiap baris tabel yang akan memanggil fungsi edit_product
    3) Membuat fungsi delete_product di views.py yang menerima parameter request dan id product, lalu menambahkan path di urls.py untuk menuju fungsi delete_product
    2) Menambahkan button di setiap baris tabel yang akan memanggil fungsi delete_product

b. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS framework (Tailwind):
    1) Menambahkan script CDN di base.html untuk menyambungkan template django dengan taiwind
    2) Membuat direktori static/css dan menambahkan file global.css (lalu menambahkan custom styling) di dalamnya lalu menambahkan link menuju global.css di base.html agar style CSS dapat digunakan
    3) Melakukan styling pada halaman login, register, main, create product entry, edit product
    4) Membuat file navbar.html di direktori templates dan include navbarnya di halaman selain login dan register
    5) Membuat card untuk setiap product dan melakukan styling dengan tailwind


TUGAS 6:
1.  Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Jawab: Membuat aplikasi web yang responsif dan dinamis terhadap interaksi dari user

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Jawab: Pause sementara untuk menunggu promise yang diresolve oleh fungsi getProductEntries(), baru melanjutkan sisa kodenya. Jika tidak menggunakan await, maka fungsi tidak akan menunggu promise dari getProductEntries() sehingga tidak ada produk dari fungsi yang direturn oleh getProductEntries() untuk ditampilkan.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Jawab: Agar tidak perlu melakukan pengecekan CSRF token di bagian add product menggunakan AJAX

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Jawab: Mengurangi beban di frontend, mencegah terjadinya manipulasi data yang langsung ke server


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawab:
1) Ubahlah kode cards data mood agar dapat mendukung AJAX GET: Pada views.py, mengubah variabel data di fungsi show_json dan show_xml menjadi hanya data yang diinput milik user. Setelah itu menghapus block conditional di main.html untuk menampilkan card product ketika kosong atau tidak dan menambahkan tag div dengan id 'product_entry_cards'. Di bawahnya, menambahkan tag script dan fungsi getProductEntries() serta refreshProductEntries() di dalamnya.

2) AJAX POST:
- Membuat button untuk add product by AJAX di main.html yang memanggil fungsi onClick() ketika diklik
- Menambahkan kode untuk mengimplementasikan modal di main.html di bawah div dengan id 'product_entry_cards'
- Menambahkan fungsi addProductEntry() di main.html dan event listener untuk menjalankannya
- Membuat fungsi add_product_entry_ajax di views.py
- Melakukan routing pada fungsi add_product_entry_ajax di urls.py dengan path 'create-product-entry-ajax'
- Memanggil fungsi refreshProductEntries() untuk melakukan refresh pada data product secara asynchronus setiap membuka halaman web

