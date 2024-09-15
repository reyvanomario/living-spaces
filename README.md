Link menuju PWS: http://reyvano-mario-livingspaces.pbp.cs.ui.ac.id/

Link menuju jawaban pertanyaan: https://docs.google.com/document/d/1VXBnhfY-mlybEKJrxxPkxrCPvkGnb0jJz-qiiD2X_Z4/edit?usp=sharing


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


![alt text](https://github.com/reyvanomario/living-spaces/blob/main/gambar_jawaban_pertanyaan/Screenshot%202024-09-11%20at%2021.31.00.png?raw=true)
![alt text](https://github.com/reyvanomario/living-spaces/blob/main/gambar_jawaban_pertanyaan/Screenshot%202024-09-11%20at%2021.28.40.png?raw=true)
![alt text](https://github.com/reyvanomario/living-spaces/blob/main/gambar_jawaban_pertanyaan/Screenshot%202024-09-11%20at%2021.28.20.png?raw=true)
![alt text](https://github.com/reyvanomario/living-spaces/blob/main/gambar_jawaban_pertanyaan/Screenshot%202024-09-11%20at%2021.28.06.png?raw=true)
