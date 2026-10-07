+++
title = "Assert dan Pytest - API Test Framework Python (Bagian 2)"
date = 2021-01-29T12:58:00+04:00
updated = 2021-08-08T13:36:48+04:00
tags = ["automation-python", "tutorials"]
description = "Hi Kawan 👋, Di artikel sebelumnya kita telah belajar mengenai instalasi python , library requests dan melakukan HTTP call dengan method GET secara programatis melalui kode python, walaupun belum ada test disana, karena memang artikelnya cukup panjang hehehe, jadi kita lanjut disini saja ya. Oh…"
cover = "/media/website/whois-fachrulch.png"
cover_alt = "penulis"
cover_caption = "Fachrul Choliluddin"
og_image = "/media/website/profile-newletter-3.png"
+++

Hi Kawan 👋,

Di artikel sebelumnya kita telah belajar mengenai instalasi python , library requests dan melakukan HTTP call dengan method GET secara programatis melalui kode python, walaupun belum ada test disana, karena memang artikelnya cukup panjang hehehe, jadi kita lanjut disini saja ya.

Oh iya artikel ini adalah salah satu dari rangkaian tutorial cara membuat RestfulAPI Test Framework dengan bahasa pemrograman Python, artikel lainnya bisa kamu cekidot disini ya:

- [Pelajaran 1:  Setup dan pengenalan HTTP requests](/yuk-belajar-cara-membuat-api-test-automation-framework-python-bagian-1/)
- [Pelajaran 2: Pengujian dengan assert dan pytest](/api-test-automation-framework-python-bagian-2/)
- [Pelajaran 3: Struktur awal test framework dan library fluent assertion](/api-test-framework-python-struktur-framework-dan-fluent-assertion-bagian-3/)
- [Pelajaran 4: Refaktoring dan base helper](/refactoring-dan-base-api-api-test-framework-python-bagian-4/)
- [Pelajaran 5: Reporting](/reporting-api-test-framework-python-bagian-5/)
- [Extra: Penambahan schema validation dan running test in parallel](/json-schema-validation-api-test-framework-python-extra-bonus/)

---

## Bagaimana cara menguji API response secara programatis dengan python?

Pada umumnya di semua bahasa pemrograman memiliki sebuah statement yang digunakan untuk menguji kebenaran sebuah expresion pada program, dan akan mentrigger error pada saat kondisi tersebut bernilai false, pada python kita mengenalnya dengan \`assert\`, namun sebelum kita menggunakan fungsi \`assert\`, alangkah baiknya jika kita mengetahui bagaimana cara menguji aplikasi secara sederhana (atau equivalent dari assert):

```
if not condition:
    raise AssertionError()
```

Apabila menggunakan \`assert\` maka, kode di atas akan menjadi serupa:

```
assert condition
```

Jika kamu perhatikan, assert tidak memiliki kurung seperti function pada umumnya, karena ia adalah sebuah statement bukan sebuah function, oia assert juga bisa memiliki pesan opsional, jadi ketika program kita bisa menyisipkan sebuah kalimat tambahan yang akan mempermudah proses debug, contohnya:

```
assert response_ok, "Oh no! Server /api/airports is not responding OK!"
```

Nah bagaimana implementasinya di kode kita sebelumnya?

```
import requests

response = requests.get('https://airportgap.dev-tester.com/api/airports')
assert response.status_code == 200
```

Penjelasan kode:

- baris 1-3 => kita import library request dan mengakses server dengan method GET lalu disimpan ke dalam variable \`response\`
- baris 4 => kita melakukan pengujian apakah response.status bernilai 200, jika tidak maka program akan error

Oia satu yang perlu disimak, jika assert mengevaluasi nilai False, maka program akan BERHENTI karena error, jadi baris setelah assert failed tidak akan di eksekusi loh! ini bisa memiliki efek samping jika kita perlu melakukan teardown atau proses tertentu setelah test selesai dilakukan (contoh pada pengujian Web, teardown untuk menutup browser setelah sesi test selesai)

---

## Pytest? Benda apakah itu bro?

Pytest adalah test library pada python, mirip junit atau testNG pada java, selengkapnya sudah saya tulis di artikel terpisah di [https://fachrul.id/belajar-pytest-framework-1/](/belajar-pytest-framework-1/)

Oke penggunaan pytest pada project kita sekarang adalah agar kode test yang kita tulis menjadi rapih dan memiliki report pada command line yang lebih rapih manakala ada kejadian error

Untuk menggunakan pytest kita perlu install dahulu library nya dengan cara mengetikan command \`pip install pytest\` pada terminal/cmd kamu

contoh implementasi pytest

```
import requests


def test_get_all_airports():
    response = requests.get('https://airportgap.dev-tester.com/api/airports')
    data = response.json().get('data')

    assert response.status_code == 200
    assert len(data) > 5
```

apa yang beda pada kode kita? berikut penjelasannya

- import requests => kita meninisiasi import library request sebelum digunakan di baris setelahnya
- def test\_get\_all\_airports(): => kita membuat sebuah function yang diawali dengan def lalu nama function nya, dan penamaan function ini wajib memiliki prefix test\_xxxx untuk dikenali sebagai sebuah test case oleh pytest nantinya
- response = requests.get(&lt;url>) => kita melakukan permintaan data pada webserver dan ditampung ke dalam variable response
- data = response.json().get('data') => disini kita akan melakukan chaining proses dari mulai parsing response dalam bentuk json menjadi tipe data dictionary pada python, dan dilanjutkan dengan method .get('data') artinya kita akan mengambil value dari atribut "data" pada dictionary tadi
- assert response.status\_code == 200 => kita melakukan pengujian dengan mengevaluasi status code http response nya harus sama dengan 200
- assert len(data) > 5 => function len digunakan untuk menghitung berapa jumlah data pada suatu list/collection, nah disini artinya kita melakukan pengujian jumlah data airport harus lebih dari 5

## Lalu bagaimana cara menjalankan kodenya?

oia untuk pytest ada sedikit perbedaan pada cara menjalankan kode/file test, jika sebelumnya kita menjalankan kode pada terminal/cmd dengan \`python nama\_file.py\` sekarang menjadi \`pytest nama\_file.py\`

perhatikan output pada console sekarang menjadi berbeda dengan materi sebelumnya di pelajaran 1 kan ya!

oia untuk lebih informatif bisa tambahkan -v (verbose) pada argument pytest menjadi seperti ini \`pytest -v nama\_file.py\`

Jika kode tidak berjalan dengan pytest yang perlu diperhatikan adalah penamaan method (def) harus diawali dengan test\_xxx yaa!

Salam!

Selengkapnya ada pada video live coding ini:

<div class="post__iframe"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" frameborder="0" height="315" loading="lazy" src="https://www.youtube.com/embed/XkrOAdGQ8Zk" width="560"></iframe></div>
