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
