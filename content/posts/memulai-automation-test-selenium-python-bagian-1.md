+++
title = "Memulai Automation Test Selenium + Python (bagian 1)"
date = 2020-05-12T19:03:00+04:00
updated = 2020-05-19T20:59:00+04:00
tags = ["automation-python", "tutorials"]
description = "membuat automation framework selenium dengan python pada browser google chrome"
cover = "/media/website/whois-fachrulch.png"
cover_alt = "penulis"
cover_caption = "Fachrul Choliluddin"
og_image = "/media/website/profile-newletter-3.png"
+++

Hi Kawan,

Sesuai dengan post sebelumnya, pada kesempatan kali ini saya akan berbagi resep tentang membuat automation test framework dengan menggunakan bahasa pemrograman python + selenium, jadi di akhir sesi kamu pasti bisa membuat otomatisasi pengujian pada browser Google Chrome ya (kalau setup nya benar) 😅

### Kenapa membuat tutorial automation test dengan python?

Tujuannya saya buat tutorial kali ini adalah untuk memperkaya khasanah tutorial bahasa Indonesia pada automation test menggunakan bahasa pemrograman python, dimana mayoritas hasil penelusuran yang ada di gugle menggunakan bahasa pemrograman java ataupun javascript.

---

Post ini merupakan rangkaian post mengenai membuat automationt test dengan python

#### Daftar isinya:

1. [Belajar Python dari dasar](/mau-belajar-automation-test-dengan-python-mulai-dari-mana/)
2. [Memahami cara kerja Pytest (bagian 1)](/belajar-pytest-framework-1/)
3. [Mulai membuat automation test dengan Selenium](/memulai-automation-test-selenium-python-bagian-1/)  &lt;== Sekarang disini
4. [Menemukan Element dengan locator strategi yang baik](/selector-locator-strategy-yang-baik/)

---

## Yuk kita mulai!!!

Sebentar.. sebentar.. bentuk tutorial yang akan saya share adalah perpaduan dari video tutorial dan blog post, jadi kedua medium pembelajaran ini akan saling melengkapi, untuk video bisa diakses disini:

<div class="post__iframe"><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" frameborder="0" height="315" loading="lazy" src="https://www.youtube.com/embed/dApgg02293I" width="560"></iframe></div>

Lalu catatan pada video akan merujuk pada postingan disini

## Tools yang digunakan

Hal pertama yang kita perlukan adalah interpreter kode python sudah terinstall di laptop/komputer kamu, terlepas dari sistem operasi apapun (windows/macOS/linux) saya asumsikan command \`python atau python3\` bisa dijalankan di terminal/command line kamu ya, jika belum, silahkan merujuk ke post [pendahuluan python saya sebelumnya disini](/mau-belajar-automation-test-dengan-python-mulai-dari-mana/)

### Kode Editor

Editor python ada banyak, dimulai dari yang ada di terminal seperti vim, kode editor ringan dan lengkap seperti:

1. [sublime](https://www.sublimetext.com)
2. [visual code](https://code.visualstudio.com)
3. [atom](https://atom.io)
4. ataupun IDE yang kumplit seperti [PyCharm Edu](https://www.jetbrains.com/education/download/).

Sebagai pendamping dalam menulis kode python saya biasanya akan menginstal pula [Kite](http://kite.com) sebagai tambahan autocomplete dan documentation di local tapi ini opsional sih, ga di install juga gapapa (ukuran file nya gede sih ahaha)

### Chromedriver

Bisa diunduh di : [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Lalu tambahkan directory binary chromedriver ke sistem path kamu, (windows bisa taruh chromedriver.exe di folder c:\\windows\\System32 klo linux bisa tambahkan di path via ~/.bash\_profile atau ~/.zshrc kamu. Atau klo macOS bisa lebih mudah tinggal jalankan perintah berikut di terminal `brew cask install chromedriver`

### Python Packaging Tools

Salah satu best practice pemrograman python adalah memiliki packaging tools yang menjadi depedency management library python agar tidak saling bertabrakan, jadi diperlukan virtual environment, kita akan menggunakan \`pipenv\` untuk itu, jalankan perintah berikut di terminal

```shell-session
$ pip install pipenv
```

atau klo gagal karena km menggunakan python3 bisa menggunakan command \`pip3 install pipenv\`

Nah yuk kita mulai kodingnya.. Silahkan liat videonya ya

Skenario test yang dijalankan

```gherkin
Scenario: Search Profile in Google
Given I am in google home page
When I search for "Fachrul Choliluddin"
Then I should see search result of "Fachrul Choliluddin"
```

## Apa itu Selector?

*Selector* adalah sebuah format yang digunakan oleh library seperti *Selenium* dan *Capybara* untuk menemukan elemen pada web seperti gambar, tulisan, tombol, dan sebagainya. Untuk bisa menggunakan *Selector* akan lebih baik jika anda mengenal HTML terlebih dahulu. Kamu bisa lihat materinya [disini](https://www.w3schools.com/html/).

## Apa itu CSS Selector?

*CSS* adalah sebuah notasi (*selector*) yang digunakan untuk menemukan elemen tertentu pada halaman web. CSS sendiri digunakan oleh web developer untuk memberikan *style* pada halaman web seperti warna, besar dan lebar gambar, bentuk tombol, dan berbagai fungsi lainnya. Properti-properti pada CSS ini bisa kita manfaatkan untuk mendeteksi sebuah elemen pada web.

## Cara Menggunakan CSS selector

Sebenarnya kita sudah menggunakan syntax CSS pada lesson sebelumnya. Yaitu `#login_link`. Dimana kita memanfaatkan elemen `id` pada tombol login untuk mendeteksi keberadaan tombol login.

Materi mengenai CSS sendiri sangat luas, sehingga kamu bisa baca mengenai CSS lebih lanjut [disini](https://www.w3schools.com/css/).

## Apa itu XPath?

*XPath* adalah sebuah notasi (*selector*) yang digunakan untuk menemukan elemen tertentu pada halaman web. *Xpath* memiliki bentuk syntax yang lebih fleksibel jika dibandingkan dengan CSS. Sehingga lebih umum digunakan untuk mencari elemen web yang tidak bisa dicari oleh *selector* CSS.

## Mengapa Memakai XPath?

Misalkan saya punya halaman web dengan format HTML seperti ini ...

<div class="highlight highlight-text-html-basic"><pre>&lt;<span class="pl-ent">div</span> <span class="pl-e">class</span>=<span class="pl-s"><span class="pl-pds">"</span>parent<span class="pl-pds">"</span></span>&gt;
    &lt;<span class="pl-ent">h2</span>&gt;Ayam&lt;/<span class="pl-ent">h2</span>&gt;
    &lt;<span class="pl-ent">p</span>&gt;Ayam adalah salah satu unggas yang bisa dimakan&lt;/<span class="pl-ent">p</span>&gt;
    &lt;<span class="pl-ent">div</span> <span class="pl-e">class</span>=<span class="pl-s"><span class="pl-pds">"</span>child<span class="pl-pds">"</span></span>&gt;
        &lt;<span class="pl-ent">h3</span>&gt;Gambar Ayam&lt;/<span class="pl-ent">h3</span>&gt;
        &lt;<span class="pl-ent">img</span> <span class="pl-e">id</span>=<span class="pl-s"><span class="pl-pds">"</span>ayam_image<span class="pl-pds">"</span></span> <span class="pl-e">src</span>=<span class="pl-s"><span class="pl-pds">"</span>ayam.jpg<span class="pl-pds">"</span></span> <span class="pl-e">alt</span>=<span class="pl-s"><span class="pl-pds">"</span>Smiley face<span class="pl-pds">"</span></span> <span class="pl-e">height</span>=<span class="pl-s"><span class="pl-pds">"</span>42<span class="pl-pds">"</span></span> <span class="pl-e">width</span>=<span class="pl-s"><span class="pl-pds">"</span>42<span class="pl-pds">"</span></span>&gt;
        &lt;<span class="pl-ent">p</span>&gt;Ini adalah gambar ayam&lt;/<span class="pl-ent">p</span>&gt;
    &lt;/<span class="pl-ent">div</span>&gt;
&lt;/<span class="pl-ent">div</span>&gt;</pre></div>

Anda bisa menggunakan *selector* CSS untuk mengambil elemen image dengan cara seperti ini.

<div class="highlight highlight-source-ruby"><pre>driver.find_element_by_css_selector(<span class="pl-s"><span class="pl-pds">'</span>#ayam_image<span class="pl-pds">'</span></span>)</pre></div>

Atau menggunakan XPath dengan cara berikut

<div class="highlight highlight-source-ruby"><pre>driver.find_element_xpath(<span class="pl-pds">'</span>//img<span class="pl-pds">'</span>)</pre></div>

Atau

<div class="highlight highlight-source-ruby"><pre>driver.find_element(by=By.XPATH, value=<span class="pl-pds">'</span>//*[@id="ayam_image"]<span class="pl-pds">'</span>)</pre></div>

<div class="highlight highlight-source-ruby"> </div>

Dan sebagainya ...

Intinya, *XPath* menawarkan banyak metode alternatif untuk mencari suatu elemen pada halaman web.

Materi mengenai *XPath* sendiri sangat luas, sehingga kamu bisa baca mengenai CSS lebih lanjut [disini](https://www.w3schools.com/xml/xpath_intro.asp).

## Perbandingan CSS vs xPath

<table><thead><tr><th>XPath</th><th>Css</th></tr></thead><tbody><tr><td>//div/a</td><td>div &gt; a</td></tr><tr><td>//div//a</td><td>div a</td></tr><tr><td>//div[@id='example']</td><td>#example</td></tr><tr><td>//div[@class='example']</td><td>.example</td></tr><tr><td>//input[@id='username']/following-sibling::input[1]</td><td>#username + input</td></tr><tr><td>//input[@name='username']</td><td>input[name='username']</td></tr><tr><td>//input[@name='login'and @type='submit']</td><td>input[name='login'][type='submit']</td></tr><tr><td>a[contains(text(), 'Log out')]</td><td>a:contains('Log Out')</td></tr><tr><td> </td><td>#recordlist li:nth-of-type(4)</td></tr><tr><td> </td><td> a[id^='id_prefix_']</td></tr><tr><td> </td><td> a[id$='_id_sufix']</td></tr><tr><td> </td><td> a[id*='id_pattern']</td></tr><tr><td> </td><td> </td></tr></tbody></table>

Command yang dijalankan:<br><br>

<table style="width: 681px;"><tbody><tr><td style="width: 280.984px;">➜ pipenv --three</td><td style="width: 399.016px;">Inisiasi directory sebagai virtual environment yang baru dengan python3</td></tr><tr><td style="width: 280.984px;">➜ pipenv shell</td><td style="width: 399.016px;">mengaktivasi virtual environment</td></tr><tr><td style="width: 280.984px;">➜ pip freeze</td><td style="width: 399.016px;">melihat daftar isi library yang sudah di terpasang di virtual environment </td></tr><tr><td style="width: 280.984px;">➜ pipenv install selenium</td><td style="width: 399.016px;">memasang library selenium</td></tr><tr><td style="width: 280.984px;">➜ pipenv install pytest</td><td style="width: 399.016px;">memasang library pytest</td></tr><tr><td style="width: 280.984px;">➜ chromedriver -v</td><td style="width: 399.016px;">cek versi chromedriver</td></tr><tr><td style="width: 280.984px;">➜ python test_googling.py</td><td style="width: 399.016px;">menjalankan kode python</td></tr><tr><td style="width: 280.984px;">➜ pytest</td><td style="width: 399.016px;">menjalankan module pytest di directory aktif</td></tr><tr><td style="width: 280.984px;">➜ pytest -s</td><td style="width: 399.016px;">menjalankan pytest disertai stdout untuk print console</td></tr></tbody></table>

Link terkait:

<table style="width: 681px;"><tbody><tr><td style="width: 339.984px;"><a href="https://selenium-python.readthedocs.io">https://selenium-python.readthedocs.io</a> </td><td style="width: 340.016px;">Dokumentasi library selenium pada python</td></tr><tr><td style="width: 339.984px;"><a href="https://docs.pytest.org/en/latest/">https://docs.pytest.org/en/latest/</a> </td><td style="width: 340.016px;">Dokumentasi pytest </td></tr><tr><td style="width: 339.984px;"> </td><td style="width: 340.016px;"> </td></tr></tbody></table>
