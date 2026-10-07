+++
title = "Pytest: Memahami Cara Kerja Testing Framework (bagian 1)"
date = 2020-05-19T20:59:00+04:00
updated = 2020-05-19T21:06:39+04:00
tags = ["automation-python", "tutorials"]
description = "belajar memahami cara kerja pytest adalah kerangka dalam setiap automation framework pada python, bisa buat unit test, api test, selenium, juga appium"
cover = "/media/posts/34/Screen-Shot-2020-05-20-at-00.05.17.png"
cover_caption = "penggunaan pytest dengan appium"
+++

## Apa itu pytest?

<figure class="post__image post__image--left"><img alt="" height="143" loading="lazy" sizes="100vw" src="/media/posts/34/pytest1.png" srcset="/media/posts/34/responsive/pytest1-xs.png 300w, /media/posts/34/responsive/pytest1-sm.png 480w, /media/posts/34/responsive/pytest1-md.png 768w, /media/posts/34/responsive/pytest1-lg.png 1024w, /media/posts/34/responsive/pytest1-xl.png 1360w, /media/posts/34/responsive/pytest1-2xl.png 1600w" width="150"/><figcaption>icon Pytest</figcaption></figure>

Adalah kerangka kerja dari pengujian pada kode python, bisa dibilang semua test framework (***junit, testng, rspec***, dkk) adalah jantung nya dari segala test automation framework, pytest bisa digunakan pada berbagai tipe dan level dari software testing, sebenarnya ada berbagai alternatif testing tools pada python yang lainya seperti uniitest ataupun nose, tapi banyak open source project yang mulai "hijrah" mengadopsi pytest karena fitur yang ada pada [pytest](https://docs.pytest.org/en/latest/) yang menarik diantara yang lainya yaitu:

- Mudah membuat kode test dari pengujian sederhana hingga pengujian kompeks tetap mudah menuliskan kode pengujiannya dengan pytest
- Mudah dibaca
- Mudah dipelajari
- Kode yang Pythonic banget
- Bahkan pytest bisa menjalankan kode pengujian yang ditulis dengan format unittest ataupun nose
- Komunitas yang sangat aktif dan pengembangan yang terjaga

---

Post ini merupakan rangkaian post mengenai membuat automationt test dengan python

#### Daftar isinya:

1. [Belajar Python dari dasar](/mau-belajar-automation-test-dengan-python-mulai-dari-mana/)
2. [Memahami cara kerja Pytest (bagian 1)](/belajar-pytest-framework-1/) &lt;== Sekarang disini
3. [Mulai membuat automation test dengan Selenium](/memulai-automation-test-selenium-python-bagian-1/)
4. [Menemukan Element dengan locator strategi yang baik](/selector-locator-strategy-yang-baik/)

---

Berikutnya akan kita belajar tentang penggunaan pytest dalam mengembangkan kerangka kerja (framework) pengujian otomatis (automated test) dalam bahasa pemrograman python, dengan menguasai kerangka kerja pengujian di python maka kamu akan dengan mudah mengkombinasikan automated test pada REST API, browser dengan selenium nya ataupun mobile apps dengan appium karena sesungguhnya mereka itu adalah library yang menjadi pelengkap pytest ini 😅

## Persiapan Pytest

Saya asumsikan python sudah terinstal di komputer kamu, dan tak diperlukan untuk tahu banyak tentang python itu sendiri, karena contoh yang akan saya tunjukan cuma kode sederhana bahkan bisa dibilang terlalu sederhana :D

Cara installnya cukup menjalankan command berikut pada terminal ataupun command line kamu

`pip install pytest`

lalu setelah installasi berhasil coba jalankan perintah:

`pytest --help`

jika installasi benar maka akan memunculkan informasi lengkap tentang cara penggunaan pytest pada command line

dokumentasi lebih lanjut bisa dilihat di [https://docs.pytest.org/en/latest/](https://docs.pytest.org/en/latest/)

## Menjalankan Pytest

Secara aturan (convention) di berbagai macam project pengujian, kode test harus ditaruh didalam directory (folder) /tests/, dan secara otomatis pytest akan menemukan dan mengeksekusi test yang ditemukan dalam proses test discovery seperti berikut:

- Nama file mengandung nama "***test\_&lt;sesuatu>.py***" ataupun "***&lt;sesuatu>\_test.py***"
- Test class yang dinamai "***Test&lt;Sesuatu>***"
- Test method/function yang diawali "***test\_&lt;sesuatu>***", dan menariknya, pytest tidak memerlukan sebuah file ***\_\_init\_\_.py*** disemua test directory seperti pada aplikasi python pada umumnya

cara menjalankan kode test:

<table><tbody><tr><td><code>$ ​​pytest​​ tests/</code></td><td>menjalankan seluruh test pada directory /tests/</td></tr><tr><td><code>$ ​​pytest​​ tests/nama_file.py</code></td><td>menjalankan test hanya pada module "nama_file.py"</td></tr><tr><td><code>$ ​​pytest​​ tests/nama_file.py::TestClass</code></td><td>menjalankan test hanya pada class TestClass di module "nama_file.py"</td></tr><tr><td><p><code>$ ​​pytest​​ tests/nama_file::TestClass::test_method</code></p><p>atau jika bentuk test bukan dalam Class</p><p><code>$ ​​pytest​​ tests/nama_file::test_method</code></p></td><td>menjalankan test hanya di method tertentu saja, tidak menjalankan method lainnya</td></tr></tbody></table>

## Marker

Penggunaan decorator ***@pytest.mark.&lt;sesuatu>*** sangat memudahkan kita dalam mengelompokan test, ibarat tagging dari test, satu test bisa memiliki lebih dari satu mark, dan kitapun bisa mengeksekusi test berdasarkan mark tertentu, seperti berikut

`$ ​​pytest​​ -m smoke`

maka pytest akan mencari test mana saja yang memiliki tag @pytest.mark.smoke untuk dijalankan

Informasi lebih lanjut, kamu bisa akses dokumentasinya langsung di terminal dengan perintah

`$ ​​pytest​​ --help`

## Menulis Test

Kurang lebih contoh kerangka kerja test pada pytest sebagai berikut:

<figure class="post__image post__image--center"><img alt="" height="450" loading="lazy" sizes="100vw" src="/media/posts/34/Screen-Shot-2020-05-19-at-22.56.59.png" srcset="/media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.56.59-xs.png 300w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.56.59-sm.png 480w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.56.59-md.png 768w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.56.59-lg.png 1024w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.56.59-xl.png 1360w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.56.59-2xl.png 1600w" width="450"/><figcaption>struktur kode pytest pada umumnya</figcaption></figure>

File test berada dibawah directory tests, dan pytest.ini adalah file optional, biasanya terkait dengan configurasi default cara menjalankan pytest, lalu pytest.py ini juga optional, bisa dianggap file ini berisikan dari "local plugin" karena semua kode yang ada disini bisa diakses oleh seluruh file test yang dijalankan, sehingga sangat cocok untuk menaruh kode yang bisa di reuse antar test

Pada kesempatan kali ini sebagai contoh sederhana dalam mencoba pytest, buatlah sebuah file /tests/test\_math.py yang di dalamnya isinya sebagai berikut:

```python
def test_pertambahan():
    assert 1 + 11 == 12
    
    
class TestHimpunan:
    def test_persamaan(self):
        assert (1,2,3) == (1,2,3)
```

lalu cara menjalankan nya pada terminal dengan perintah sebagai berikut:

`pytest tests/test_math.py`

Output yang dihasilkan kurang lebih seperti berikut:

<figure class="post__image post__image--center"><img alt="" height="538" loading="lazy" sizes="100vw" src="/media/posts/34/Screen-Shot-2020-05-19-at-22.21.54.png" srcset="/media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.21.54-xs.png 300w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.21.54-sm.png 480w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.21.54-md.png 768w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.21.54-lg.png 1024w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.21.54-xl.png 1360w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.21.54-2xl.png 1600w" width="1024"/><figcaption>output test berhasil</figcaption></figure>

Ok kita bahas ya, pada contoh diatas saya menjalankan 2 test pada file ***test\_math.py*** yaitu ***def test\_pertambahan*** dan ***def test\_persamaan***, disini saya menunjukan bahwa pytest support bentuk kode pengujian yang dituliskan sebagai function mandiri atau method pada class, tidak ada perbedaan signifikan, hanya pengelompokan test saja menurut saya.

Dan jika ditilik lagi, jika test berjalan baik dan passed akan ditandai dengan simbol titik warna hijau (di windows gada warnanya) pada output console dan jika failed ditandai dengan huruf F warna merah, disertai dengan informasi pelengkapnya.

agar lebih jelas lagi mari kita coba membuat test gagal dengan mengubah nilai pada assertnya, dan agar tampilan output console lebih informatif, jalankan perintah `pytest -v tests/test_math.py` lalu perhatikan error message yang ditampilkan sebagai berikut

<figure class="post__image post__image--center"><img alt="" height="1352" loading="lazy" sizes="100vw" src="/media/posts/34/Screen-Shot-2020-05-19-at-22.26.15.png" srcset="/media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.26.15-xs.png 300w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.26.15-sm.png 480w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.26.15-md.png 768w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.26.15-lg.png 1024w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.26.15-xl.png 1360w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-22.26.15-2xl.png 1600w" width="1024"/><figcaption>hasil menjalankan kode test yang ternyata failed :P</figcaption></figure>

Ada berbagai macam jenis outcome dari sebuah test yang akan dihasilkan oleh pytest sebagai berikut:

- **PASSED** (.) adalah test yang berjalan sebagaimana mestinya
- **FAILED** (F) adalah test yang tidak berjalan seperti yang diharapkan
- **SKIPPED** (s) adalah test yang tidak dijalankan (dilompati), kita bisa mengkonfigurasi test yang harus di lompati dengan menggunakan decorator ***@pytest.mark.skip()*** atau secara programatically
- **xfail** (x): adalah test yang tidak seharusnya untuk pass, jadi secara eksplisit kita mengharapkan suatu test untuk failed, ditandai dengan decorator ***@pytest.mark.xfail()***
- **XPASS** (X): kurang lebih mirip xfail
- **ERROR** (E) adalah exception yang terjadi diluar test function tersebut, bisa gara-gara fixture, di hook atau dari mis-configurasi

## Ekspektasi

Pytest akan menggak exception yang tidak dihandle sebagai sebuah failure, pada saat statement assert dihadapkan kepada nilai False maka ia akan melempar exception dan langsung memberhentikan eksekusi program, jadi tidak akan dilanjutkan ke statement setelah assert yang failed tersebut

```python
class TestHimpunan:
    def test_persamaan(self):
        assert (1,3,5) == (1,4,5)
        print('Bagian ini tidak akan dijalankan')
```

Tapi jika memang justru exception yang diharpkan maka bisa menggunakan pytest.raises

## Contoh studi kasus JSON api kode post Indonesia

Contoh API test sederhana menggunakan pytest untuk menguji json api dari repo ini [https://github.com/bachors/Kode-Pos-API](https://github.com/bachors/Kode-Pos-API) yang memiliki aplikasi live di firebaseio

Kita buat file di tests/feature\_kodepost/test\_kodepos\_indonesia.py, isinya

```python
iimport requests 

def test_provinsi():
    list_provinsi = requests.get('https://kodepos-2d475.firebaseio.com/list_propinsi.json?print=pretty')
    data_prov = list_provinsi.json()
    assert len(data_prov) == 34
    assert data_prov.get('p9') == 'Jawa Barat'
    
def test_kotakab_jabar():
    list_kotakab = requests.get('https://kodepos-2d475.firebaseio.com/list_kotakab/p9.json?print=pretty')
    data_kotakab = list_kotakab.json()
    assert list_kotakab.status_code == 200
    assert data_kotakab.get('k60') == 'Tasikmalaya_typo'
    assert len(data_kotakab) == 21
    
def test_kodepos_tasik():
    list_keckel = requests.get('https://kodepos-2d475.firebaseio.com/kota_kab/k60.json?print=pretty')
    data_kodepos = list_keckel.json()
    assert list_keckel.status_code == 200
    assert len(data_kodepos) == 420
 
```

lalu cara menjalankannya dengan  command

`➜ pytest -v tests/feature_kodepos`

maka akan muncul output sebagai berikut

<figure class="post__image post__image--center"><img alt="" height="1020" loading="lazy" sizes="100vw" src="/media/posts/34/Screen-Shot-2020-05-19-at-23.21.32.png" srcset="/media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.21.32-xs.png 300w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.21.32-sm.png 480w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.21.32-md.png 768w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.21.32-lg.png 1024w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.21.32-xl.png 1360w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.21.32-2xl.png 1600w" width="1024"/><figcaption>output menjalankan test kdoepos</figcaption></figure>

Test nya sengaja saya buat failed, karena untuk melihat betapa cantiknya error log dari pytest jika terjadi masalah, apa yang menarik disini:

- Informasi kesalahan yang jelas, contoh diatas ada typo pada string yang dibandingkan (assert) maka ditunjukan kelebihan character dengan tanda plus
- test dijalankan sesuai dengan urutan penulisan test pada file, jadi dieksekusi dari atas kebawah
- walaupun test ke-2 failed, tetap melanjutkan ekseskusi test ke-3, (stop ekseskusi karena throw exception hanya pada scope test function, jadi dari failed tersebut tidak akan melanjutkan ekseskusi baris statement berikutnya tapi langsung pindah ke test berikutnya)

Yuk kita bermain dengan kode test diatas, berikutnya kita ubah kode test sebagai berikut

Kita tambahkan decorator xfail di method yg gagal menjadi seperti ini

<div><pre><code class="language-python">@pytest.mark.xfail
def test_kotakab_jabar():<br/>   ...</code></pre><p>Lalu jalankan kembali testnya dan outputnya sekarang berbeda</p><figure class="post__image post__image--center"><img alt="" height="580" loading="lazy" sizes="100vw" src="/media/posts/34/Screen-Shot-2020-05-19-at-23.34.05.png" srcset="/media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.34.05-xs.png 300w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.34.05-sm.png 480w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.34.05-md.png 768w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.34.05-lg.png 1024w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.34.05-xl.png 1360w, /media/posts/34/responsive/Screen-Shot-2020-05-19-at-23.34.05-2xl.png 1600w" width="1024"/><figcaption>semua hasil passed dengan catatan 1 xfail</figcaption></figure><p>Nah terlihat bahwa sekarang semua test hijau (passed) dengan catatan ada 1 test yang memang expected failed (xfailed)</p><h2>Pytest Fixtures</h2><p>Nah bagian ini sebenarnya yang menurut saya paling keren dari pytest, tapi berhubung postingan kali ini sudah cukup panjang, maka informasi lebih lanjut terkait fixture akan disambung di post selanjutnya ya, dengan contoh framework pada web ui testing</p><p>Bersambung ...</p></div>
