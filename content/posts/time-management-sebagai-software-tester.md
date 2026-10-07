+++
title = "Time Management sebagai Software Tester"
date = 2023-03-26T14:56:00+04:00
updated = 2023-03-26T16:22:30+04:00
tags = ["belajar-qa", "merdeqa"]
description = "Keahlian mengelola waktu merupakan keahlian penting bagi software tester, Ini siasat gw dalam mengelola waktu biar lebih efisien dengan cara mengurangi waktu"
cover = "/media/posts/59/thumbnail-post-fachrul.id-2.jpg"
+++

Sebagai software tester, apakah kamu sering merasakan hal seperti ini?

- Keteteran kerjaan
- Sering dapet tugas dadakan
- Ga tau bisa kelar hari ini apa nggak

Sama, gw juga! ahaha, tapi jangan sedih dulu, gw akan share siasat gw dalam mengelola waktu biar lebih efisien dengan cara **mengurangi** waktu!!

---

<h2><figure class="post__image"><img alt="" height="192" loading="lazy" sizes="100vw" src="/media/posts/59//coin.png" srcset="/media/posts/59//responsive/coin-xs.png 300w, /media/posts/59//responsive/coin-sm.png 480w, /media/posts/59//responsive/coin-md.png 768w, /media/posts/59//responsive/coin-lg.png 1024w, /media/posts/59//responsive/coin-xl.png 1360w, /media/posts/59//responsive/coin-2xl.png 1600w" width="1008"/></figure></h2>

## Mengelola waktu

Sepertinya, time management (manajemen waktu) sudah menjadi sebuah skill wajib bagi software testing, karena pekerja software itu dituntut result oriented, banyak variabel yang bisa bikin waktu tempuh pengujian jadi semakin lama. Misal, klo nemu bugs tapi intermitten atau bahkan klo testnya lancar ga nemu bugs baru (malah was-was ga sih).

Karena waktu adalah **sumber daya yang tidak bisa ditambah atau kurangin**, bahkan ga bisa di transfer juga, jadinya keahlian mengelola waktu sangat kritikal bagi software tester, biar ga burnout saat bekerja, dan kualitas pengujian juga tetap semangat dan produktif.

## Waktunya Ngaret

Sering kali perusahaan itu menempatkan software tester sebagai “Quality gate keeper”, alias si penentu rilis apa nggaknya sebuah fitur/version, akhirnya software tester (QA) menjadi bottleneck, berasa semua pada nungguin kerjaan QA kelar ga sih 😅

Dengan kek gitu, sering kali QA jadi kambing hitam saat tim harus ambil delay rilis/waktu yang ga sesuai jadwal. Karena ujung-ujungnya klo delay itu nambah cost produksi software loh, kebayang ga sih klo ada hard deadline launching produk, tapi H-1 fiturnya masih kayak zombie! klo sampe mesti delay,, beeuuuh berasa duduk di kursi panas!

## Waktu Efisien

Ga selalu loh istilah “Lebih cepat, Lebih baik” berlaku di software testing, karena bisa jadi ternyata cepat dan banyak yang kelewat! ahaha, ujung-ujungnya puter balik 😂

Jadi harus cepat DAN baik, hasilnya adalah efisien, sungguh idaman setiap software tester ya untuk bisa terus efisien, nah karena kita ga bisa menambah waktu lebih dari 24 jam sehari, atau menambah waktu rilis dengan mudah, makanya gw mo share cara gw mengurangi waktu!

<h2><figure class="post__image"><img alt="" height="192" loading="lazy" sizes="100vw" src="/media/posts/59//ilustrasi-jeda-nulis.png" srcset="/media/posts/59//responsive/ilustrasi-jeda-nulis-xs.png 300w, /media/posts/59//responsive/ilustrasi-jeda-nulis-sm.png 480w, /media/posts/59//responsive/ilustrasi-jeda-nulis-md.png 768w, /media/posts/59//responsive/ilustrasi-jeda-nulis-lg.png 1024w, /media/posts/59//responsive/ilustrasi-jeda-nulis-xl.png 1360w, /media/posts/59//responsive/ilustrasi-jeda-nulis-2xl.png 1600w" width="1008"/></figure></h2>

## Mengurangi Waktu Regression Test

Regression test adalah salah satu sumber pengeluaran waktu terbesar bagi seorang software tester, jalanin regression test suite itu bisa berhari-hari (beda-beda sih tiap tim/kantor), gw pun kadang mo muntah ngeliatin testrail runner ga kelar-kelar keknya!

Nah gimana cara ngurangin waktu regression test yang biasa gw lakuin:

#### 1\. Rawatlah test suite si regression test

Lo tentu akan masukin fitur baru ke koleksi test suite, tapi apakah lo akan kurangin juga test fitur lama dari koleksi? Udah 10 rilis loh itu ga ada perubahan, aman-aman aja kan? masi tetep perlu di cek berkala? Tentu tergantung ya, klo bukan core features sih lebih baik dikurangin, atau bahkan outsource aja ke test automation

#### 2\. Test planning yang bener

Katakanlah di sprint planning udah ketahuan fitur baru apa aja yang akan di rilis, nah kita bisa rencanain tuh nanti ada dampaknya ga di regression test, klo bisa colong start, coba jalanin regression test dulu di fase feature test biar keliatan ada imbas ke regression test suite ga nya.

Atau bahkan dengan fitur baru, kita perlu persiapan lebih lama buat production testing nantinya, misal kita perlu setup akun dengan kondisi tertentu biar bisa gampang di testnya.

Dan terkait nomer 1 tadi, di planning juga prioritas test cases nya, mana yang masuk test run nanti, mana yang penting di cek duluan sebelum yang lain

#### 3\. Nyuruh Robot

Alias test automation, dengan adanya test automation, pengujian software tentu akan lebih mudah, mereka akan nurut terus disuruh ngetest kapanpun bisa, ga ada capeknya, ga bosen-bosen ngetest hal yang sama 100x sehari. Tentu, robot/automation ini ga akan menggantikan kualitas pengujian yang dijalankan oleh manusia, tapi bayangin deh kita kan klo ngetest ga bisa paralel sekaligus semuanya dikerjain barengan, nah contoh, saat kita lagi test module sign up dengan fitur baru, si test automation ini akan ngetest module login/reset password, nanti pas kita kelar test sign up tinggal liat hasilnya dulu dari yang dikerjain test automation, sebelum kita terjun lebih jauh di pengujian manual, karena kesel juga kan pas ditengah test gataunya ada error dan perbaikannya bisa bikin test kita yang udah kelar harus di-retest lagi.

<figure class="post__image post__image--center"><a href="https://www.tokopedia.com/ngetest-jualan" rel="noopener noreferrer" target="_blank"><img alt="baju keren software tester nih gaes" height="304" loading="lazy" sizes="100vw" src="/media/posts/59/baju-keren-software-tester.jpeg" srcset="/media/posts/59/responsive/baju-keren-software-tester-xs.jpeg 300w, /media/posts/59/responsive/baju-keren-software-tester-sm.jpeg 480w, /media/posts/59/responsive/baju-keren-software-tester-md.jpeg 768w, /media/posts/59/responsive/baju-keren-software-tester-lg.jpeg 1024w, /media/posts/59/responsive/baju-keren-software-tester-xl.jpeg 1360w, /media/posts/59/responsive/baju-keren-software-tester-2xl.jpeg 1600w" width="304"/></a><figcaption>klik gambar ini buar beli di Tokopedia</figcaption></figure>

[Coba cek ini, deh kaos keren di toko gw "NgeTest Jualan" Tokopedia](https://www.tokopedia.com/ngetest-jualan)
{: .align-center }

#### 4\. Menggunakan jurus pengujian yang tepat

Pernah denger jurus “Kunyuk Melempar buah”? ahaha generasi 90an doang keknya yang inget!

Oke maksudnya adalah menggunakan teknik pengujian yang tepat bisa meningkatkan kualitas pengujian lebih efektif dan confidence, contohnya gini, pada suatu fitur baru untuk tambah validasi pada suatu form input, kita punya 30 macem validasi, nah kita harus tau ini validasi dari Backend apa frontend, klo tau ini validasi datengnya dari BE, jadi si 30 macem validasi kita test di level API aja, 1x di FE, buat liat tampilan errornya aja, karena konten error message nya dateng dari BE toh, jadi ga perlu deh tuh kita habisin waktu lama-lama buat ngetest semua 30 validasi tadi (atau bahkan influence dev buat cover 30 test tadi di level unit testing)

<h2><figure class="post__image"><img alt="" height="192" loading="lazy" sizes="100vw" src="/media/posts/59/ilustrasi-jeda-nulis-2.png" srcset="/media/posts/59/responsive/ilustrasi-jeda-nulis-2-xs.png 300w, /media/posts/59/responsive/ilustrasi-jeda-nulis-2-sm.png 480w, /media/posts/59/responsive/ilustrasi-jeda-nulis-2-md.png 768w, /media/posts/59/responsive/ilustrasi-jeda-nulis-2-lg.png 1024w, /media/posts/59/responsive/ilustrasi-jeda-nulis-2-xl.png 1360w, /media/posts/59/responsive/ilustrasi-jeda-nulis-2-2xl.png 1600w" width="1008"/></figure></h2>

## Mengurangi Waktu Debug

Gw sangat senang sama debugging, ibarat detektif yang lagi ngumpulin bukti kriminal, dan cari tau siapa dalangnya, dalam hati “ini tuh beneran error loh gaes, nih liat aja lognya, screenshot nya, video reproducenya”

Tapi semua itu perlu waktu yang ga singkat, reproduce issue deh minimal lebih dari satu kali, kadang buat mastiin ini kejadiannya cuma di kondisi A aja apa juga di kondisi B, belom lagi klo kita mau mastiin ini kejadain nya sejak di versi baru aja atau kejadian juga di production! gimana ga lama tuh waktu debuging nya ahahaa

Yang bisa kita kurangin di waktu debug adalah:

#### 1\. Error Logging sistem yang terintegrasi

Pastikan aplikasi kamu udah terkoneksi dengan logging system yang baik, minta developer manager buat pasang di aplikasi development (integration/alpha/beta) juga, ga cuma di production aja gitu, karena kan fitur baru pasti di testnya ga langsung di production donk!

Jadi mana kala muncul bugs/crash/faliures, langkah pertama kita adalah ngecek log ini, yang barusan kejadian tuh stacktrace nya kek mana, seringkali informasi ini udah cukup jelas buat dev

#### 2\. Laporan bugs yang jelas

Red flag deh klo devnya selalu nanya QA di standup/DM buat jelasin temuan bugsnya, karena itu berarti laporan bugsnya ga jelas dimengerti oleh dev (atau Devnya masih baru, atau emang pengen ngobrol sama lo aja/PDKT 🤣 )

Coba refleksi, apa yang ditanyakan dev itu, apakah step reproduce nya ga jelas? tambahin foto, klo kurang jelas juga tambahin video! apakah mungkin bugs report lo itu description nya ga jelas, ekspektasi yang ga make sense.

Intinya, ini adalah feedback dari dev agar komunikasi lo jadi lebih baik, kalaupun ga ada komentar dari Dev, coba tanyain kira-kira ada yang bisa di improve ga dari bugs report nya yang biasa dia terima? kadang ada dev yang mau juga di tambahin info device/browser detail.

Jadi devnya bisa sat-set langsun ngerjain bugsnya.

<h2><figure class="post__image"><img alt="" height="192" loading="lazy" sizes="100vw" src="/media/posts/59/ilustrasi-jeda-nulis-1.png" srcset="/media/posts/59/responsive/ilustrasi-jeda-nulis-1-xs.png 300w, /media/posts/59/responsive/ilustrasi-jeda-nulis-1-sm.png 480w, /media/posts/59/responsive/ilustrasi-jeda-nulis-1-md.png 768w, /media/posts/59/responsive/ilustrasi-jeda-nulis-1-lg.png 1024w, /media/posts/59/responsive/ilustrasi-jeda-nulis-1-xl.png 1360w, /media/posts/59/responsive/ilustrasi-jeda-nulis-1-2xl.png 1600w" width="1008"/></figure></h2>

## Mengurangi Waktu Nunggu

Menunggu itu pemborosan waktu, apalagi klo sambil bengong gada kuota internet, beuh mati gaya dah tuh nunggu! ehehe tapi ini bukan soal nunggu bus transjakarta gaes, kita harus identifikasi titik mana aja yang biasanya kita habiskan buat menunggu

#### Menunggu feature yang Ready for Testing

Di awal sprint biasanya belum ada fitur baru yang ready for testing langsung kan, coba liat apa yang bisa QA kerjain di waktu kosong ini, misalkan cek crashlytic di production, di release sebelumnya banyak error ganya, bikin test automation, entah buat automate fitur lama atau fitur yang berjalan (API sih ada kontrak response yang bisa dipake buat automate), atau ngerjain apa kek biar nanti test nya langsung sat-set-sat-set, macam prepare test data gitu

#### Menunggu bugs yang Ready for Testing

Nah ini sering jadi bumerang, kita udah rise issue tapi ternyata ga kunjung dikerjain developer! Mana itu bugs severity critical, bisa masalah klo dilolosin sebelum rilis! nah makanya tetep pantau terus itu bugs report kita, tiap hari di standup kita harus sundul developernya:

- bugs yang gw report udah di baca belom?
- ada yang perlu gw jelasin ga soal bugs itu?
- ke reproduce ga di tempat lo?
- apa perlu gw yang kerjain itu bugs? (ini klo bisa ya ahaha)
- gw bilangin bapak lo ya! (eskalasi)
