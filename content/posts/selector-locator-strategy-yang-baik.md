+++
title = "Selector (Locator) Strategy adalah koentji dari Test Automation"
date = 2020-05-14T05:25:00+04:00
updated = 2020-05-19T20:58:24+04:00
tags = ["automation-python", "testergadungan", "tutorials"]
description = "Belajar selector/locator strategi yang baik adalah kunci membuat test automation framework yang stabil. Dasar dalam mempelajari automated test selenium appium"
cover = "/media/posts/33/gugel-selector.png"
cover_alt = "selector strategy yang baik"
+++

Hi kawan,

Jika kamu berkecimpung di pemrograman automation test menggunakan selenium / appium tentunya kamu sudah paham banget kalau sampe salah selector (locator) maka kamu telah membuang banyak waktu karena selector yang kamu telah tuliskan tidak ditemukan dan harus re-run lagi 😭

Menemukan element pada tampilan aplikasi seperti buttons, inputs, divs, checkboxes ataupun anchor tag terkadang cukup "menantang", terutama ketika tidak adanya ke-unikan ataupun identitas yang jelas pada element tersebut, bahakan pernah saya menguji aplikasi yang ID nya selalu berubah karena digenerate otomatis oleh library front end nya. Alamakjang 😵

---

Post ini merupakan rangkaian post mengenai membuat automationt test dengan python

#### Daftar isinya:

1. [Belajar Python dari dasar](/mau-belajar-automation-test-dengan-python-mulai-dari-mana/)
2. [Memahami cara kerja Pytest (bagian 1)](/belajar-pytest-framework-1/)
3. [Mulai membuat automation test dengan Selenium](/memulai-automation-test-selenium-python-bagian-1/)
4. [Menemukan Element dengan locator strategi yang baik](/selector-locator-strategy-yang-baik/) &lt;== Sekarang disini

---

## Apa sih web/mobile elements itu?

Terjemahan ala saya sih ia adalah sebuah element adalah entitas pada aplikasi yang di render menjadi halaman web ataupun user interface pada mobile app. Jadi apapun yang dilihat oleh pengguna (termasuk yang ga keliatan sih) adalah element, seperti buttons submit, foto profile, navigasi halaman.

Biasanya bentuknya berupa HTML pada web ataupun XML pada mobile apps, jadi bisa dikatakan memiliki struktur seperti tag name, attributes dan contents, termasuk kedalam hierarki posisinya.

Untuk pembahasan ini saya cenderung membahas element pada web, untuk mobile apps akan dibahas lebih rinci di lain kesempatan karena perbedaan struktur source code tampilan lintas platformnya, tapi masih sangat relevan dengan mobile apps terutama mobile browser ya gaes.

## Nah itu kan baru element, trus selector itu apa?

Jadi selector ataupun locator adalah sebuah bentuk query untuk mengakses element tertentu yang ada di halaman aplikasi, nah untuk website biasanya object hasil query locator ini disebut node yang terletak di Document Object Model (DOM)

Perlunya selector element pada aplikasi adalah sebagai awal mula interaksi automation. Setelah selenium/appium menemukan element sesuai selector maka kamu bisa mengakses method di element itu seperti meng-click button, menginput text, ataupun mengambil text pada element tersebut.

## Kenapa kok perlu banget selector?

Jadi gini, sebagai manusia yang menggunakan aplikasi tentu kita tidak perlu selector untuk berinteraksi dengan aplikasi, kita bisa menggunakan indera penglihatan untuk menjalankan aksi seperti submit form, scrolling halaman, click sana sini di halaman web, tapi tidak begitu bagi test automation yang harus menerjemahkan interaksi manusia tadi ke istilah yang komputer bisa mengerti secara programatis. Jadi selenium/appium ga akan melihat aplikasi sebagaimana kita kita melihat tampilannya, tapi ia akan melihatnya secara source code struktural seperti html/xml (catatan: tapi jaman now, sedang gandrung library/tools yang mendukung visual testing juga loh seperti [applitools](https://applitools.com), [mabl](https://www.mabl.com), [test.ai](http://test.ai/) dkk)

## Hmm gitu ya.. Bentuk element itu seperti apa sih?

Sebagai contoh kita akan bedah element di google.co.id ya, coba pada browser chrome kamu (sama juga pada firefox ataupun safari) klik kanan pada kotak pencarian trus pilih opsi menu "Inspect" maka akan muncul jendela Developer tool, pada Tab aktif "Elements", seperti ini gambarannya: (kamu coba juga donk ah)

<figure class="post__image post__image--center"><img alt="" height="901" loading="lazy" sizes="100vw" src="/media/posts/33/gugel.png" srcset="/media/posts/33/responsive/gugel-xs.png 300w, /media/posts/33/responsive/gugel-sm.png 480w, /media/posts/33/responsive/gugel-md.png 768w, /media/posts/33/responsive/gugel-lg.png 1024w, /media/posts/33/responsive/gugel-xl.png 1360w, /media/posts/33/responsive/gugel-2xl.png 1600w" width="1764"/><figcaption>tampilan inspect element pada google chrome</figcaption></figure>

Pada gambar diatas saya memberikan keterangan nomer,  yang akan saya jelaskan sebagai berikut:

1. Pada gambar no.1 diatas, kotak pencarian adalah target element yang kita lihat, nampak ada highlight warna biru di element tersebut
2. Ini adalah kode sumber HTML dari halaman google.co.id yang aktif pada bagian kotak pencarian yaitu tag &lt;input/> beserta atribut yang melekat pada nya
3. Apa yang disarankan oleh browser chrome jika kamu mencari element kotak pencarian ini, ada tag dengan classnya, accessibility yang ada pada element tersebut

Nah jika kita terjemahkan pada kode automation dengan python (yang kurang lebih akan sama juga dengan selenium bindder di bahasa pemrograman lainya) nampak seperti berikut:

<div><pre><code class="language-python line-numbers">search_box = driver.find_element_by_name('q')
# driver.find_element(By.NAME, 'q')  &lt;= atau alternatif bisa juga seperti ini
search_box.send_keys('Belajar automation testing' + Keys.ENTER)</code></pre></div>

di baris pertama saya akan membuat variable search\_box yang isinya adalah element yang mengandung nama "q" seperti pada keterangan element search box yang saya tunjukan sebelumnya si kotak pencarian ini memiliki element &lt;input ... name="q" ... /> nah disini selector yang kita ambil adalah attribut name sama dengan "q", di baris kedua adalah alternatif cara penulisan kode saja

di baris berikutnya, adalah proses automation test code saya untuk berinteraksi dengan element tersebut yaitu mengirimkan perintah send keys alias ketikan kata Belajar automation testing pada kotak pencarian dilanjutkan dengan menekan tombol Enter

<figure class="post__image post__image--center"><img alt="" height="890" loading="lazy" sizes="100vw" src="/media/posts/33/hasil-pencarian-google-belajar-automation.png" srcset="/media/posts/33/responsive/hasil-pencarian-google-belajar-automation-xs.png 300w, /media/posts/33/responsive/hasil-pencarian-google-belajar-automation-sm.png 480w, /media/posts/33/responsive/hasil-pencarian-google-belajar-automation-md.png 768w, /media/posts/33/responsive/hasil-pencarian-google-belajar-automation-lg.png 1024w, /media/posts/33/responsive/hasil-pencarian-google-belajar-automation-xl.png 1360w, /media/posts/33/responsive/hasil-pencarian-google-belajar-automation-2xl.png 1600w" width="1749"/><figcaption>hasil pencarian kata kunci 'belajar automation' pada google search</figcaption></figure>

Selector pun adakalanya bersifat tidak unik, seperti pada halaman pencarian google diatas, search result pada umumnya berupa list yang identik secara rupa dan bentuk, karena memiliki stylesheet (CSS) yang sama, hanya isi yang beda, lantas bagaimana cara kita memilih element yang kita mau agar lebih akurat akan kita diskusikan nanti ya.

Bisa jadi kebutuhan test kita pun perlu mendapatkan element yang lebih dari satu juga, katakan lah contoh diatas mau kita jadikan test code seperti ini jadinya (masih di bahasa python):

<div><pre><code class="language-python line-numbers">results_title = driver.find_elements_by_css_selector('h3')
assert len(results_title) &gt; 0
</code></pre><p> Dimana kebutuhannya memang menghitung jumlah dari hasil pencarian yang didapatkan dengan asusi kata kunci tersebut akan menemukan data pada halaman hasil pencarian, makanya kita memerlukan selector pada element judul pencarian yaitu &lt;h3&gt;</p><p>Pada test framework yang besar umumnya mengadopsi design pattern "<a href="https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html" rel="noopener noreferrer" target="_blank">Page Object Model</a>" untuk mengelola selector / locator dan interaksi di halaman tertentu, ada juga sih yang mengadopsi <a href="https://www.infoq.com/articles/Beyond-Page-Objects-Test-Automation-Serenity-Screenplay" rel="noopener noreferrer" target="_blank">Screenplay Pattern</a> dimana sedikit ada perbedaan lokasi dimana selector disimpan pada kode automation testnya</p><h2>Hmm.. trus gimana cara saya menemukan selector?</h2><p>Sebenernya, cara untuk menentukan selector itu ada banyak, bisa dari element tag, id, class, attributes, isi text, bahkan relatif terhadap element parent/child/sibling juga bisa, bahkan yang saya sebutkan tadi bisa dikombinasikan juga loh. Wadidaw, banyak banget sih selector strategi yang bisa diterapkan. Dalam waktu dekat saya pun akan membuat video tutorial terkait berbagai penggunaan selector strategi, karena medium video lebih enak untuk langsung terjun praktek penggunaan, jadi jangan lupa <a href="https://www.youtube.com/channel/UCZVY3VNPkFs_iINTXEBWWgw" rel="noopener noreferrer" target="_blank">subscibe disini</a> ya gaes ahaha</p><p>Kita harus hati-hati juga, penulisan selector yang salah mengharuskan kita re-run automation test dan ini mubazir waktu loh. Kalau selectornya terlalu luas bisa salah dalam menentukan element yang harusnya kita dapat, kalau terlalu spesifik malah rawan breaking ketika ada yang berubah di struktur DOM nya, kalau terlalu panjang jadi sulit untuk di baca oleh yang lain. Jadi gimana donk?</p><p>Prinsip yang bisa dipegang dalam membuat selector / locator strategy yang saya pegang adalah <strong>Buatlah selector yang paling sederhana dalam menemukan keunikan element yang menjadi target kita</strong></p><p> Nah biasanya urutannya seperti ini:</p><ol><li>Element nya punya ID (yang unik) kah? =&gt; pake ID aja</li><li>CSS class nya spesifik dan cuma ada di element itu (untuk format) =&gt; pake CSS klo selector kalo gitu</li><li>Masih nyampur nih klo pake strategi 1 atau 2 =&gt; yaudah kombinasikan aja kedua nya, jadi "#id .class" atau ".class #id"</li><li>Waduh masih ga bisa nih, saya maunya element yang ke-4 dari filter 1-3 tadi =&gt; Oke tambahin posisi "#id li:nth-of-type(4)"</li><li>Tapi saya maunya element yang mengandung text tertentu =&gt; pake xpath klo gitu //button[text()[contains(.,'Sebut Saja Mawar')]]</li></ol><p>Di urutan 5 itu udah paling rawan banget deh, selector text emang bisa, tapi klo webnya support ganti bahasa bisa jadi ambyar itu loh. Lebih baik diobrolin lagi deh sama developer untuk mulai menuliskan identitas element yang kita mau jadi lebih unik lagi agar lebih testable.</p><p>Sebagai perbandingan, kita coba lihat web tokopedia, mereka memiliki element khusus yang memudahkan QA membuat locator yang stabil</p><figure class="post__image post__image--center"><img alt="" height="893" loading="lazy" sizes="100vw" src="/media/posts/33/contoh-tokopedia-element-data.jpg" srcset="/media/posts/33/responsive/contoh-tokopedia-element-data-xs.jpg 300w, /media/posts/33/responsive/contoh-tokopedia-element-data-sm.jpg 480w, /media/posts/33/responsive/contoh-tokopedia-element-data-md.jpg 768w, /media/posts/33/responsive/contoh-tokopedia-element-data-lg.jpg 1024w, /media/posts/33/responsive/contoh-tokopedia-element-data-xl.jpg 1360w, /media/posts/33/responsive/contoh-tokopedia-element-data-2xl.jpg 1600w" width="1734"/><figcaption>Kode sumber Tokopedia menunjukan penggunaan data-testid sebagai penunjang selector strategy nya</figcaption></figure><p> </p><p>Data-* adalah attribute baru di HTML5 dan termasuk atribut yang valid, enaknya punya atribut khusus macam ini tuh klo ada perubahan desain di UI yang biasanya akan pakai ID atau CLASS, test nya akan tetap sama dan stabil karena tidak terganggu</p><p>Atau di bukalapak juga ada, bedanya disana pakai css class</p><figure class="post__image post__image--center"><img alt="" height="888" loading="lazy" sizes="100vw" src="/media/posts/33/contoh-element-qa-class-bukalapak.jpg" srcset="/media/posts/33/responsive/contoh-element-qa-class-bukalapak-xs.jpg 300w, /media/posts/33/responsive/contoh-element-qa-class-bukalapak-sm.jpg 480w, /media/posts/33/responsive/contoh-element-qa-class-bukalapak-md.jpg 768w, /media/posts/33/responsive/contoh-element-qa-class-bukalapak-lg.jpg 1024w, /media/posts/33/responsive/contoh-element-qa-class-bukalapak-xl.jpg 1360w, /media/posts/33/responsive/contoh-element-qa-class-bukalapak-2xl.jpg 1600w" width="1281"/><figcaption>Kode sumber Bukalapak menunjukan penggunaan qa-* class sebagai penunjang selector strategy nya</figcaption></figure><h2>Jadi gimana sebenarnya selector / locator yang baik?</h2><p>Kalau menurut saya, automation test menjadi stabil, locator yang baik itu harus memenuhi kriteria seperti:</p><h4>Sederhana</h4></div>

<div>Semakin pendek penulisan query selector semakin baik dan stabil, contoh nya "#first_name".  Jangan gunakan attribut atau class yang merujuk ke css formating seperti class="col-sm" atau id="83924csdj" yang tampak seperti di generate otomatis oleh JS lib</div>

<div> </div>

#### Mudah dibaca

<div>Jangan menulis query selector yang panjang ataupun sulit dibaca seperti:</div>

- html/body/div\[1\]/section/div\[1\]/div/div/div/div\[1\]/div/div/div/div/div\[3\]/div\[1\]/div/h4\[1\]/b
- //\*\[@id="wakwaw"\]//child::label//following-sibling::input\[1\]

<div> </div>

#### Semantic

<div>Artinya query yang dipilih harus sesuai kan dengan maksud element tersebut artinya lebih baik menuliskan selector seperti ini "input#kampus" daripada hanya "#kampus" agar lebih jelas lagi saat membaca kode yang di maksud id="kampus" adalah sebuah element input bukan div ataupun button</div>

<div> </div>

## Jadi Kesimpulannya

<div>Selector strategy yang baik berperan besar terhadap stabilitas automation code kamu, jika aplikasi yang akan di test tidak memungkinkan membuat selector yang baik, artinya sudah waktunya mengangkat issue testablility aplikasi dengan developer ataupun stakeholder agar test menjadi lebih stabil maka diperlukan sedikit tunning lagi pada kode sumber aplikasinya<br/><h2> Rujukan lebih lanjut</h2><ul><li><a href="https://blog.mozilla.org/fxtesteng/2013/09/26/writing-reliable-locators-for-selenium-and-webdriver-tests/">https://blog.mozilla.org/fxtesteng/2013/09/26/writing-reliable-locators-for-selenium-and-webdriver-tests/</a> </li><li><a href="https://www.guru99.com/locators-in-selenium-ide.html">https://www.guru99.com/locators-in-selenium-ide.html</a> </li><li><a href="https://www.guru99.com/xpath-selenium.html">https://www.guru99.com/xpath-selenium.html</a></li><li><a href="https://selenium-python.readthedocs.io/locating-elements.html">https://selenium-python.readthedocs.io/locating-elements.html</a></li><li><a href="https://gs.statcounter.com/browser-market-share">https://gs.statcounter.com/browser-market-share</a> Ternyata browser chrome masih paling banyak dipakai oleh orang seluruh dunia</li></ul><p> </p></div>
