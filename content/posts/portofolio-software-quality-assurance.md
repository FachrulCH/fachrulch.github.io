+++
title = "Portofolio QA: Tampil Memikat Melamar Lowongan Kerja Software Quality Assurance/Engineer"
seo_title = "Portofolio QA: Tampil Memikat Melamar Lowongan Kerja Software Quality Assurance/Engineer"
date = 2022-07-03T06:09:00+04:00
updated = 2022-07-04T18:17:05+04:00
tags = ["tutorials"]
description = "Portofolio seperti apa yang cocok untuk melamar kerja sebagai Software Quality Assurance? apakah harus koding? adakah opsi lain? Saya akan share pengalaman dsini"
cover = "/media/posts/51/maranda-vandergriff-7aakZdIl4vg-unsplash.jpg"
cover_caption = "Photo by Maranda Vandergriff on Unsplash"
+++

Salam, Beberapa waktu lalu, saya mendapatkan sebuah pertanyaan melalui Instagram, mengenai hal apa yang perlu disusun ketika melamar kerja untuk posisi QA (quality assurance) atau SDET / Test engineer.
{: .dropcap }

Tentu saja ini bisa jadi sangat membingungkan terutama bagi pemula dikarenakan minimnya pengalaman, namun tak jarang pula saya termui kandidat senior yang terkesan hanya "bawa diri" saja, tanpa mempersiapkan portofolio pada proses melamar pekerjaan baru juga loh!

Lalu bagaimana cara agar kamu bisa meyakinkan perusahaan bahwa kamu sudah memiliki keahlian yang dibutuhkan dan layak untuk mendapatkan kesempatan bekerja di perusahaan itu?

<figure><figure class="post__image post__image--center"><img alt="DM instagram" height="700" loading="lazy" sizes="100vw" src="/media/posts/51//instagram-dm-3.png" srcset="/media/posts/51//responsive/instagram-dm-3-xs.png 300w, /media/posts/51//responsive/instagram-dm-3-sm.png 480w, /media/posts/51//responsive/instagram-dm-3-md.png 768w, /media/posts/51//responsive/instagram-dm-3-lg.png 1024w, /media/posts/51//responsive/instagram-dm-3-xl.png 1360w, /media/posts/51//responsive/instagram-dm-3-2xl.png 1600w" width="323"/></figure><figcaption>Pertanyaan Melalui DM instagram</figcaption></figure>

Jawabannya adalah dengan melampirkan pengalaman/portofolio yang relevan dengan keahlian QA sehingga membuat kamu menjadi jauh lebih menonjol dibandingkan kandidat lain, berikut ini adalah kiat mempersiapkan portofolio bagi seorang *Software Quality Assurance* menurut pengalaman saya pribadi

---

# 1\. Test Automation Framework

Bisa membuat *test automation* sendiri sudah barang tentu akan membuat kamu lebih berkilau, ini menunjukan kamu memiliki keahlian koding dan cocok menjadi kandidat *test engineer* yang tentu dibutuhkan di perusahaan, karena di beberapa startup (khususnya unicorn) sudah mencantumkan keahlian *automation* sebagai *skill* wajib di beberapa lowongan QA/SDET.

Namun, sulit menilai seberapa baik keahlian koding automation kandidat hanya dari percakapan interview, meluangkan waktu untuk belajar dan membuat *test automation framework* sendiri merupakan persiapan yang layak, tapi jangan berkecil hati jika kamu baru berada pada level sebagai penguna framework yang sudah ada seperti menggunakan Serenity BDD (java), Robot Framework (python) ataupun Codeception (PHP/Javascript) untuk project automation kamu, itu sudah keren loh!

Pada *Test Automation Framework* ini, kamu bisa membuat pengujian *backend* API, web browser automation, mobile automation atau bahkan gabungan semua automation tadi, pasti keren banget!

Berangkat dari pengalaman sebagai penguji kandidat SDET (software development engineer in test), saya akan bocorkan beberapa poin penting yang akan dilihat oleh interviewer yaitu:

- **Apa yang di-automation?:** Kamu bebas membuat automation web/aplikasi umum/publik, seperti *ecommerce*, *social media*, CMS atau web pribadi, tetapi jangan sampai membuat *test automation* untuk menguji *basic functionality* saja seperti halaman login ya! Harap membuat *test automation* untuk *scenario* yang memiliki dengan beberapa (berbagai) halaman web/mobile.
- **Clean code:** Dengan membagikan kode karya kamu, semua orang bisa menilai keahlian kamu dalam menuliskan kode secara konkrit, bisa dilihat dari bagaimana kamu memilih tipe data yang efisien untuk tujuan tertentu dan bagaimana kamu menggunakan strategi reusable code pada struktur kode kamu (*design pattern)*
- **Selector yang dipilih:** Interviewer bisa melihat pengalaman kamu menggunakan *selenium/appium* dari cara kamu menentukan locator/selector pada element, apakah cukup unik dan kokoh, seberapa ahli dalam menggunakan xpath untuk element yang sulit, jangan pula banyak memakai xpath yang kaku ataupun css selector yang cenderung berubah
- **Page Object Model:** Menandakan kamu paham akan *design pattern* yang umum dipakai, POM yaitu mengelompokan element pada satu halaman menjadi satu object khusus, eh tapi tidak menutup kemungkinan juga kalau kamu mau menggunakan *design pattern* lain semacam *screenplay pattern* loh
- **Commit Message:** kita bisa melihat kedewasaan kode dari cara kamu menuliskan git commit message, seberapa deskriptiv, seberapa sering menulis kode, cara kamu membuat branch baru untuk mengerjakan fitur baru (walaupun repo sendiri sih 😅 )

Opsi tambahan yang bisa meningkatkan *value automation framework* kamu, khususnya untuk kandidat *senior/leader* :

- **Parallel support:** test automation kamu bisa berjalan secara paralel dan cepat
- **Support multi browser/platform:** pengujian mendukung untuk ios/android/chrome/firefox, *portability* *test runner* pada windows/linux/macos
- **Custom Gesture:** ada interaction gesture khusus seperti *swiping* dan *pinching*
- **Visual automation:** topik yang sedang hangat, tentu akan membuat kamu bersinar di mata penguji
- **Data-driven testing:** jika memungkinkan bisa mengimplementasikan penggunaan *spreadsheet files* dalam menjalankan test yang repetitif
- **Database connection:** proses *setup data* sebelum test dimulai, ataupun *query* untuk *assertion process*
- **Performance testing:** memiliki keahlian *non-funcitonal testing* seperti ini umumnya tidaklah wajib, tapi tentu akan membuat kamu menjadi makin cemerlang

---

# 2\. Test Case/Scenario untuk Sebuah Requirement (bisa BDD spec)

Banyak perusahaan mempraktikan test automation dengan menggunakan BDD (*cucumber*), tentu saja kamu bisa membagikan *.features files* dimana kamu menulis kode *gherkin* untuk suatu test scenario.

Mungkin bagi kamu yang baru memulai karir QA, sedikit bingung pada bagian ini, oke saya akan jelaskan sedikit:

*Test case* atau *test scenario* adalah rancangan pengujian yang berisi informasi mengenai hal apa saja yang harus dinilai kelayakannya, lalu langkah pengujian, serta ekspektasi dari hasil yang di harapkan
{: .msg .msg--info }

Misal contoh penulisan gherkin untuk test scenario:

<div><div><code>Given the admin is logged in</code></div><div><code>When the admin deletes a post on the blog</code></div><div><code>Then the post moved to deleted section</code></div><div><code>And a successful deleted message should display</code></div></div>

Apa yang dinilai:

- **Kejelasan penulisan scenario test:** ada yang bilang *.feature files* adalah *living documentation*, dimana kamu harus bisa menuliskan *test scenario* yang mudah dipahami, bahkan oleh orang awam yang baru pertama kali melihat *feature files* ini, apakah cukup konteks yang diberikan pada *step "Given",* apakah suatu action dituliskan pada *step "When"* dst
- **Standar penulisan Gherkin file:** banyak yang salah kaprah dan salah menuliskan step yang harusnya pada step yang Given tapi malah menggunakan When, atau overuse keyword (given-when-then), hindari pula ketidak konsistenan sudut pandang orang pertama atau ketiga,
- **Declaratif vs Imperatif:** Cenderung subjektif, tapi cara penulisan yang saya sukai adalah menuliskan *test scenario* secara *Declarative*, selain lebih singkat dengan begitu pula menjadi mudah dibaca, tinggal bagaimana nanti di implementasikan di step definition untuk menyusun blok kodenya, ada artikel yang menjadi sumber inspirasi saya [disini](https://www.spritecloud.com/the-3-most-common-mistakes-writing-gherkin-features/). tetapi harap diperhatikan risiko masalah yang mungkin timbul, seringkali dengan menggunakan declarative style test step menjadi kurang detail dan informatif terkait apa yang terjadi, seimbangkan saja antara *imperative (too much details)* dengan *declarative* *(not enough details)*

---

# 3\. Laporan Bugs

Saya teringat kisah teman saya si Anggadirja saat interview di Sleekr HR, tempat saya bekerja dulu, di hari dia interview, sang bos besar tiba-tiba melaporkan ada seseorang bernama Angga (tau dari email yang dipakai) yang melakukan spam signup pada environmen Demo di production, karena dia membuat kurang-lebih sekitar 50 perusahaan baru bertubi-tubi, sontak saja kita konfirmasi ke si Angga saat itu sedang *interview* dan dia pun mengakui disertai bukti temuan issue apa saja yang telah dia dapatkan dari aktifitas tersebut! sekilas, saya melihat wajah interviewer yang saat itu geleng-geleng pun tersirat senyum kagum 😂

Memberikan laporan bugs saat interview memang sebuah kesan yang istimewa, sepanjang karir saya meng-interview kandidat QA/SDET hanya dia yang menyetorkan laporan bugs tanpa diminta, menurut saya ini adalah sebuah bukti kalau kandidat bisa bekerja sebagai QA dan memiliki keahlian yang mumpuni (tergantung dari level bugs yang ditemukan).

Disaat saya melamar kerja pun beberapa kali melampirkan hasil temuan bugs saya, dan selalu saya lihat wajah kaget dan takjub dari para interviewer (mungkin setelah ini banyak yang mengikuti jadi lumrah ahaha 🤣)

Tidak mesti kamu harus menemukan bugs baru pada aplikasi yang dibuat oleh perusahaan dimana kamu melamar, bisa juga kamu membagikan temuan bugs dari aplikasi umum, seperti temuan kamu saat menggunakan aplikasi Ojek online, ataupun issue saat kamu menggunakan instagram, yang penting adalah kamu membuat sebuah dokumentasi akan temuan kamu ini

Apa yang dinilai:

- **Penulisan laporan bugs:** Kamu harus memiliki struktur laporan bugs yang baik, setidaknya terdiri dari penjelasan temuan masalah dan langkah reproduce nya
- **Level temuan:** Seberapa *critical bugs* yang kamu temukan, bisa jadi issue UI, functional atau bahkan blocker, semakin parah temuan kamu maka kamu akan terlihat semakin keren (dan mungkin berfikir, ngapain aja QA internal perusahaan itu, sampai kelolosan ahaha #julidModeON )
- **Saran:** Sertakan ide perbaikan yang kamu harapkan, seberapa masuk akal expected result dari bugs tersebut, atau bahkan jika kamu tidak menemukan bugs/issue kamu pun bisa saja menuliskan saran perbaikan dari suatu proses
- **Analisa:** Sangat keren sekali apabila kamu bisa membuat analisa risiko dari temuan kamu tersebut, kamu bisa membahas risiko yang mungkin diderita pengguna dengan adanya bugs tersebut, yang sering kali luput oleh tester adalah menguji accesibility pada aplikasi, seringkali aplikasi menjadi kurang friendly untuk pengguna lanjut usia yang biasanya menggunakan font size besar, dan aplikasi menjadi tidak tersusun baik, bahkan bisa jadi tombol submit menjadi tertimbun element yang overlap

Berikut ini contoh laporan bugs:

<table border="1" style="border-collapse: collapse; width: 100%;"><tbody><tr><td style="width: 25.535%;">Screenshot</td><td style="width: 74.465%;"><figure><figure class="post__image post__image--center"><img alt="temuan bugs pada todo list" height="776" loading="lazy" sizes="100vw" src="/media/posts/51/bug-report-todolist-counter.jpg" srcset="/media/posts/51/responsive/bug-report-todolist-counter-xs.jpg 300w, /media/posts/51/responsive/bug-report-todolist-counter-sm.jpg 480w, /media/posts/51/responsive/bug-report-todolist-counter-md.jpg 768w, /media/posts/51/responsive/bug-report-todolist-counter-lg.jpg 1024w, /media/posts/51/responsive/bug-report-todolist-counter-xl.jpg 1360w, /media/posts/51/responsive/bug-report-todolist-counter-2xl.jpg 1600w" width="1024"/></figure><figcaption>Masalah pada counter todo list</figcaption></figure></td></tr><tr><td style="width: 25.535%;">Judul</td><td style="width: 74.465%;">Invalid counter for Todo list</td></tr><tr><td style="width: 25.535%;">Penjelasan Masalah</td><td style="width: 74.465%;">Todo counter menunjukan angka yang tidak benar, dimana angka yang ditunjukan selalu selisih -1 dari yang seharusnya ditunjukan</td></tr><tr><td style="width: 25.535%;">Langkah Reproduce</td><td style="width: 74.465%;"> Buat satu todo list lalu simpan, perhatikan nilai pada counter menunjukan 0 bukan 1</td></tr><tr><td style="width: 25.535%;">Expected Behaviour</td><td style="width: 74.465%;">Conter menunjukan jumlah todo list yang belum selesai, nilai akan berkurang apabila user menyelesaikan pekerjaan dan nilai akan bertambah apabila ada tambahan pekerjaan</td></tr></tbody></table>

---

# 4\. Kontribusi

Kontribusi seorang QA sering kali tidak terdokumentasikan, baik itu kontribusi teknis ataupun non teknis, mungkin karena kita menganggap itu terlalu  biasa saja atau malas menuliskannya.

Saya akan membagikan contoh kasus non teknis berdasarkan pengalaman saya, jadi pada tahun 2020 dulu di Golife (waktu masih ada), dimana saya melakukan perubahan bagaimana QA status update menjadi lebih menarik dan interaktif.

<figure class="post__image post__image--center"><img alt="story telling pada status update" height="569" loading="lazy" sizes="100vw" src="/media/posts/51/status-update-golife.jpg" srcset="/media/posts/51/responsive/status-update-golife-xs.jpg 300w, /media/posts/51/responsive/status-update-golife-sm.jpg 480w, /media/posts/51/responsive/status-update-golife-md.jpg 768w, /media/posts/51/responsive/status-update-golife-lg.jpg 1024w, /media/posts/51/responsive/status-update-golife-xl.jpg 1360w, /media/posts/51/responsive/status-update-golife-2xl.jpg 1600w" width="521"/></figure>

Pada awalnya QA update pada periode testing berupa informasi grafik test run progress dari testrail, hanya berupa angka persentase dari jumlah total test cases berbanding dengan jumlah test case yang sudah diuji, lalu saya ubah ini menjadi status update yang berupa story telling dan ini berdampak positif, dari engagement tim yang tinggi, dengan begitu kita bisa mengetahui bahwa tim membaca dan memperhatikan progress testing yang ada.

Untuk contoh kontribusi teknis, saya akan membagikan kisah saya membuat semacam "Cheat engine" agar proses testing manual menjadi jauh lebih cepat 95% hingga mendapatkan spotlight untuk showcase di Gojek Townhall November 2021

<figure><figure class="post__image post__image--center"><img alt="" height="675" loading="lazy" sizes="100vw" src="/media/posts/51/fachrul-dan-pertamax.jpg" srcset="/media/posts/51/responsive/fachrul-dan-pertamax-xs.jpg 300w, /media/posts/51/responsive/fachrul-dan-pertamax-sm.jpg 480w, /media/posts/51/responsive/fachrul-dan-pertamax-md.jpg 768w, /media/posts/51/responsive/fachrul-dan-pertamax-lg.jpg 1024w, /media/posts/51/responsive/fachrul-dan-pertamax-xl.jpg 1360w, /media/posts/51/responsive/fachrul-dan-pertamax-2xl.jpg 1600w" width="1080"/></figure><figcaption>Berada pada Townhall bersama CEO</figcaption></figure>

Atau pun bisa kita tuliskan bagaimana test automation yang sudah terimplementasi CI/CD bisa membantu proses relese lebih cepat dengan menjaga kualitas aplikasi tetap tinggi disetiap build barunya, cerita bagaimana kami bisa mengurangi waktu full cycle testing, awalnya 3 hari menjadi 1,5 hari kerja.

---

# 5\. Pitch deck

Saya masih ingat ketika saya membuat *pitch deck* saat apply sebagai QA Leader di GoMart, saat itu head of engineering langsung kepincut dengan apa yang saya lakukan, karena saya sungguh-sungguh membuat slide berisi pengalaman, cara kerja saya, visi saya tentang *Quality Assurance*, serta misi saya dalam membangun tim, tujuan pitch deck ini adalah memudahkan saya "menjual (keahlian) diri" dalam proses interview, saya lebih nyaman menggunakan presentasi daripada hanya bercerita secara verbal, mungkin ini ide saya mengakali interviewer saat itu yang orang India, jadi mengurangi grogi saya karena menggunakan bahasa Inggris, jadi menghindari saya melupakan topik yang harus saya bahas karena sudah direncanakan di slides.

Karena intinya interview adalah seperti mencari jodoh, bisa jadi yang dicari perusahaan sejalan dengan visi &amp; misi pribadi kita.<br><br>

<figure><figure class="post__image post__image--center"><img alt="" height="999" loading="lazy" sizes="100vw" src="/media/posts/51/pitchdeck-fachrulch-2020-small.jpg" srcset="/media/posts/51/responsive/pitchdeck-fachrulch-2020-small-xs.jpg 300w, /media/posts/51/responsive/pitchdeck-fachrulch-2020-small-sm.jpg 480w, /media/posts/51/responsive/pitchdeck-fachrulch-2020-small-md.jpg 768w, /media/posts/51/responsive/pitchdeck-fachrulch-2020-small-lg.jpg 1024w, /media/posts/51/responsive/pitchdeck-fachrulch-2020-small-xl.jpg 1360w, /media/posts/51/responsive/pitchdeck-fachrulch-2020-small-2xl.jpg 1600w" width="1280"/></figure><figcaption>Pitchdeck profil saya pada tahun 2020</figcaption></figure>

---

# Bagaimana cara menyajikan portofolio?

## Google Slides/Documents

Di poin terakhir saya sudah singgung sedikit mengenai slides *(pitch deck)* saya, saya akan membagikan link google slides kepada interviewer sebelum proses interview (bisa sehari sebelum) agar mereka bisa melihat dahulu lalu didiskusikan/ditanyakan saat interview, kenapa menggunakan *google slides*? Karena itu memungkinkan saya untuk bisa memperbarui konten, hal yang tidak bisa terjadi jika saya mengirimkan lampiran file .ppt, tentu jika ada perubahan harus mengirimkan file susulan.

Bisa juga ketika kita ingin menjabarkan informasi lebih banyak untuk membuatnya berupa google documents (word) berformat seperti esai, cocok untuk konten bugs reporting yang kita temukan, ataupun cerita soal analisa bugs seperti pembahasan sebelumnya

<figure><figure class="post__image post__image--center"><img alt="Github FachrulCH" height="687" loading="lazy" sizes="100vw" src="/media/posts/51/github-fachrulch.jpg" srcset="/media/posts/51/responsive/github-fachrulch-xs.jpg 300w, /media/posts/51/responsive/github-fachrulch-sm.jpg 480w, /media/posts/51/responsive/github-fachrulch-md.jpg 768w, /media/posts/51/responsive/github-fachrulch-lg.jpg 1024w, /media/posts/51/responsive/github-fachrulch-xl.jpg 1360w, /media/posts/51/responsive/github-fachrulch-2xl.jpg 1600w" width="1024"/></figure><figcaption>Github FachrulCH</figcaption></figure>

## Github

Kode *automation* yang sudah kita buat alangkah baiknya kita simpan di akun github, walaupun bisa juga gitlab/bitbucket tapi agak kurang populer, oia perlu diingat untuk tidak menyimpan akun kredensial di repositori ya (atau membuat repository menjadi privat)

Github ini merupakan etalase untuk pamer keahlian koding kita, namun perlu diperhatikan juga apa **tujuan** kamu membuat repository baru:

- Untuk membuat *Proof of Concept* dari tools baru
- Membandingkan pilihan *library / concept* secara *head to head*
- Mempraktikan tutorial yang sedang dipelajari

Agar akun profil kamu tidak terlalu ramai repository yang dangkal dan menambah kebingungan bagi pengunjung profil kamu.

## Website

Memiliki *website pribadi* ibarat sebuah KTP, karena *website* adalah *online presence* kita, sebuah tempat dimana kita menunjukan pribadi seperti apakah kita, tempat kita bisa memamerkan pengalaman kita, opini serta keunikan kita.

Tentu saja, ini adalah sebuah keputusan yang sangat baik. Saya berasumsi ini akan terlihat lebih profesional, bahkan saya rasa faktor ini menentukan saya diterima kerja sebagai Software Engineer di Gojek tempo hari, karena aspirasi saya terhadap QA tertuang di website ini [fachrul.id](/)

Saya rasa ini bukanlah hal sulit kan? Web saya ini pun saya hosting di github hanya dengan static html tanpa koneksi database, bermodal sebuah domain saja, justru yang sulit adalah mengisi konten nya, ahaha

---

Demikian kiat singkat (walau ternyata panjang) dari pengalaman saya dan teman-teman saya, semoga bisa bermanfaat dan membantu kamu mendapatkan pekerjaan impianmu, jangan lupa sapa saya di [Instagram](https://www.instagram.com/fachrulch) ataupun [Youtube Ngetest bareng Fachrul](https://www.youtube.com/c/NgeTestBarengFachrul)
