+++
title = "Yuk Belajar Cara Membuat API Test Automation Framework Python (Bagian 1)"
date = 2021-01-29T11:00:00+04:00
updated = 2021-12-31T06:55:43+04:00
tags = ["automation-python", "tutorials"]
description = "Panduan membuat automation framework dengan python untuk pengujian Rest API"
cover = "/media/posts/41/pexels-zachary-debottis-1888883.jpg"
cover_caption = "Foto oleh Zachary DeBottis dari Pexels Pexels"
+++

Hi Kawan 👋,

Di kesempatan kali ini saya akan membuat rangkaian post yang berisi tutorial cara membuat API Test Framework dengan Python dari dasar sampai jadi sebuah framework testing yang siap di integrasikan dengan pipeline CI/CD 😎🤘

Oke setiap post akan berisi sebuah topik tahapan pelajaran dari dasar disetiap aspeknya, semoga saja ini bisa bermanfaat bagi teman-teman yang mulai belajar menekuni dunia software quality assurance / Test engineering ya, harapan saya, tutorial ini bisa membantu teman-teman untuk memahami approach API testing, dan bisa mempermudah implementasi API test framework dengan python di tempat kerja kalian

Kurang lebih rangkaian posting akan seperti:

- [Pelajaran 1:  Setup dan pengenalan HTTP requests](/yuk-belajar-cara-membuat-api-test-automation-framework-python-bagian-1/)
- [Pelajaran 2: Pengujian dengan assert dan pytest](/api-test-automation-framework-python-bagian-2/)
- [Pelajaran 3: Struktur awal test framework dan library fluent assertion](/api-test-framework-python-struktur-framework-dan-fluent-assertion-bagian-3/)
- [Pelajaran 4: Refaktoring dan base helper](/refactoring-dan-base-api-api-test-framework-python-bagian-4/)
- [Pelajaran 5: Reporting](/reporting-api-test-framework-python-bagian-5/)
- [Extra: Penambahan schema validation dan running test in parallel](/json-schema-validation-api-test-framework-python-extra-bonus/)

Kamu bisa berkomentar atau bertanya di pada bagian komentar post tersebut, insya alloh nanti akan saya jawab sebisanya ehehe, atau bisa juga DM dan follow @fachrulch untuk kritik dan saran nya dalam pembahasan ini

---

## Apa itu API sih?

Sebenernya saya ga yakin bisa menjelaskannya dengan benar, mungkin bisa kamu googling aja nanti ya klo masih belum jelas dari penjelasan saya ehehe, jadi kurang lebih gini:

<figure class="post__image--left"><img alt="" height="454" loading="lazy" sizes="100vw" src="/media/posts/41/api-1.png" srcset="/media/posts/41/responsive/api-1-xs.png 300w, /media/posts/41/responsive/api-1-sm.png 480w, /media/posts/41/responsive/api-1-md.png 768w, /media/posts/41/responsive/api-1-lg.png 1024w, /media/posts/41/responsive/api-1-xl.png 1360w, /media/posts/41/responsive/api-1-2xl.png 1600w" width="800"/></figure>

API (Application Programming Interface) atau juga seringkali dikenal dengan webservice adalah bentuk komunikasi antar sistem, sederhananya, API menyediakan serangkaian cara/kontrak bagaimana sebuah informasi bisa ditransfer/diakses.

API ada dua kategori, yaitu SOAP dan REST, SOAPmenggunakan format XML yang membungkus informasi data nya, sejauh yg saya tau soap masih umum dipergunakan oleh perbankan sampai saat ini, sedangkan REST sudah umum dipakai oleh khalayak ramai, karena lebih ringan dalam hal ukuran data yang disimpan dalam format JSON, dan umumnya permintaan dan penerimaan data menggunakan protokol HTTP, biasanya menggunakan verbs GET, POST, PUT dan DELETE dalam berinteraksi.

Di kesempatan ini kita akan fokus dalam pembuatan API test framework untuk RESTful API ya, tools yang sering dipergunakan dalam berinteraksi dengan API adalah Postman

<figure class="post__image post__image--full"><img alt="" height="757" loading="lazy" sizes="100vw" src="/media/posts/41/rest-api-contoh-sederhana.png" srcset="/media/posts/41/responsive/rest-api-contoh-sederhana-xs.png 300w, /media/posts/41/responsive/rest-api-contoh-sederhana-sm.png 480w, /media/posts/41/responsive/rest-api-contoh-sederhana-md.png 768w, /media/posts/41/responsive/rest-api-contoh-sederhana-lg.png 1024w, /media/posts/41/responsive/rest-api-contoh-sederhana-xl.png 1360w, /media/posts/41/responsive/rest-api-contoh-sederhana-2xl.png 1600w" width="1280"/><figcaption>RestAPI secara sederhana</figcaption></figure>

## Kenapa Perlu Membuat API test automation?

Test functional dari API sebenarnya lewat postman juga bisa, entah manually atau automation test disana, memiliki functional API automation adalah langkah besar dalam pengujian yang cepat terhadap sistem, apalagi API cenderung lebih stabil daripada UI automation test. Dampak yang bisa kita harapkan dari memiliki automation test pada API/webservice adalah kita bisa menguji user flow, business logic dengan cepat dan stabil.

Nah kita akan membuat API test automation dengan python, walaupun sebenarnya bisa juga dibuat dengan bahasa pemrograman lain seperti java, kotlin, javascript, dll. tetapi menurut saya python lebih sederhana dan mudah dipelajari oleh pemula, juga sangat powerful bagi tingkat mahir sekalipun, so i think it is good investment

## OK, terus apa yang diperlukan dalam pengembangan API test framework dengan Python?

Udah siap? oke kita list dulu ya apa saja yang diperlukan dalam pengembangan API test framework dengan bahas python

1. Komputer kamu sudah terinstal python (saran saya sudah versi 3.8 keatas ya)
2. Install code editor, saran saya sih menggunakan PyCharm, tapi klo mau yg lebih ringan boleh pake Visual Code ataupun Notepad++ juga bisa harusnya

---

<h2><figure class="post__image--center"><img alt="" height="592" loading="lazy" sizes="100vw" src="/media/posts/41/airportgap.png" srcset="/media/posts/41/responsive/airportgap-xs.png 300w, /media/posts/41/responsive/airportgap-sm.png 480w, /media/posts/41/responsive/airportgap-md.png 768w, /media/posts/41/responsive/airportgap-lg.png 1024w, /media/posts/41/responsive/airportgap-xl.png 1360w, /media/posts/41/responsive/airportgap-2xl.png 1600w" width="500"/></figure></h2>

## Studi Kasus

Oke, sepertinya kita akan bahas dulu aplikasi apa yang akan menjadi target kita dalam pengembangan API test framework, sebagai contoh kita akan mengautomasi pengujian pada [https://airportgap.dev-tester.com](https://airportgap.dev-tester.com) sebuah dummy app yang dikhususkan bagi teman-teman yang berlatih dalam mengasah automation skill pada API

Kenapa saya pilih ini? karena koleksi API disini kurang lebih akan mirip dengan apa yang kamu punya di kantor, ada API yang bisa diakses dengan GET, POST, DELETE dan PUT/PATCH, jadi bisa dikatakan mini project API, apalagi dokumentasinya API juga sudah cukup jelas ya, bisa diakses disini [https://airportgap.dev-tester.com/docs](https://airportgap.dev-tester.com/docs)

<figure class="post__image--left"><img alt="" height="480" loading="lazy" sizes="100vw" src="/media/posts/41/374px-Requests_Python_Logo.png" srcset="/media/posts/41/responsive/374px-Requests_Python_Logo-xs.png 300w, /media/posts/41/responsive/374px-Requests_Python_Logo-sm.png 480w, /media/posts/41/responsive/374px-Requests_Python_Logo-md.png 768w, /media/posts/41/responsive/374px-Requests_Python_Logo-lg.png 1024w, /media/posts/41/responsive/374px-Requests_Python_Logo-xl.png 1360w, /media/posts/41/responsive/374px-Requests_Python_Logo-2xl.png 1600w" width="374"/></figure>

## Pelajaran 1 - pengenalan HTTP requests

Siap kita mulai ya, untuk mengakses API/webservice kita perlu sebuah library yang akan memudahkan kita dalam berinteraksi dengan API, yaitu menggunakan library requests, cara menginstall library ini adalah dengan command

```
pip install requests
```

Dokumentasi requests menurut saya sangat jelas dan keren, coba saja lihat [https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/) , kita bisa pelajari lebih lanjut fitur dan kemampuan requests disana ya, tapi secara natural sangat mudah diingat kok method dan fungsi nya

Lanjut,, kita akan mengakses informasi daftar airports yand bisa diakses dengan melakukan request GET pada endpoint \`/api/airports\` dan melihat apa saja informasi yang terkandung di dalamnya

Untuk itu kita harus membuat file python baru di folder/direktori yang sudah kamu pilih ya

Di baris awal kita perlu melakukan import library request dahulu dengan menambahkan kode \`import requests\` lalu di baris berikutnya kita akan menggunakan library requests dalam mengakses API dengan kode

```python
import requests

response = requests.get('https://airportgap.dev-tester.com/api/airports')
print(response.status_code)
print(response.text) 
    
```

Penjelasan kode:

- import requests => melakukan import library \`requests\` sebelum penggunaan di baris selanjutnya
- response = requests.get(&lt;url>) => kita melakukan permintaan GET pada sebuah url yang kemudian di tampung kedalam variable \`response\`
- print(response.status\_code) dan print(response.text) => kita mengeluarkan text response dan status code kepada python console dengan command print

Bagaimana cara run file ini? yaitu dengan membuka terminal/cmd lalu masuk ke directory/folder dimana file python ini berada, kemudian kita tinggal menjalankan command \`python namafile.py\` maka kita bisa melihat hasil requests di dalam console terminal/cmd

---

## Penutup

Namun,,, ini masih belum ada test nya ya, di pelajaran kali ini kita hanya bisa melihat hasil GET pada console, tanpa ada pengujian secara otomatis (pengujian masih visual oleh kita melalui console ehehe)

Karena materi disini sudah cukup panjang ehehe, PR dari saya di tahap 1 ini adalah untuk mempelajari [dokumentasi requests](https://requests.readthedocs.io/en/master/) ya, kita lihat betapa mudahnya mengkases webservice dengan library ini, baik itu dengan method GET, POST, PUT, PATCH ya

Dimateri berikutnya kita akan menggunakan test dengan assertion jadi sudah mulai masuk ke automation test

Salam!

Selengkapnya ada di Video live coding berikut ini

<div class="post__iframe"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" frameborder="0" height="315" loading="lazy" src="https://www.youtube.com/embed/nsdHPitMSSI" width="560"></iframe></div>
