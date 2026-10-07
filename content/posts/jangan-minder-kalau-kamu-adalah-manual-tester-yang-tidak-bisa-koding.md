+++
title = "Jangan Minder Kalau Kamu adalah Manual Tester yang Tidak Bisa Koding"
date = 2019-02-09T19:30:38+04:00
updated = 2019-02-09T19:30:38+04:00
tags = ["testergadungan"]
description = "Bagaimana mengasah keahlian dalam testing manual (quality assurance) sehingga lebih bernilai bagi tim"
cover = "/media/posts/5/board-broccoli-carrots-952478.jpg"
cover_caption = "Photo by Lukas from Pexels"
+++

Saya pernah dengar istilah **"Asahlah pisau pada sisinya yang tajam"**, artinya kita seharusnya fokus pada apa yang menjadi kelebihan yang dimiliki untuk menjadi **lebih mahir** lagi dalam hal tersebut. Untuk kamu yang pernah menonton *Jiro: Dream of Sushi* mungkin ada sedikit gambaran mengenai apa yang dinamakan spesialis, dunia sebenarnya membutuhkan lebih banyak orang yang sangat mahir pada suatu bidang daripada orang yang bisa banyak hal.

<figure class="post__video"><iframe allowfullscreen="allowfullscreen" data-mce-fragment="1" height="314" loading="lazy" src="https://www.youtube.com/embed/I1UDS2kgqY8" width="560"></iframe></figure>

Spesialis disini bukan berarti menyalahi konsep T shape loh ya, justru selaras dengan itu. kita bahas lebih jauh mengenai analogi film Jiro tadi, untuk menjadi pengusaha restoran Jepang yang sukses, Jiro tidak perlu menjual sushi enak dan ramen nikmat (keahlian horizontal), tetapi cukup menyajikan sushi paling spesial saja, nah konsep T shape disini adalah dalam konteks spesialis sushi, bukan makanan Jepang secara umum, selain Jiro piwai dalam meracik sushi dia menguasai proses pemilihan bahan baku sushi yang paling prima, dari beras, tuna, ataupun sayurannya dia memiliki standard yang tinggi, dia pun menguasai cara penyajian sushi yang baik dan indah, bahkan saya dengar dia menciptakan teknik khusus untuk bisa menjaga kesegaran telur ikan yang musiman, sepanjang tahun!

Pun begitu dengan dunia per-testing-an sedang gandrung dengan *automation engineer* yang mampu meracik kode untuk yang bisa menggerakkan komputer yang bisa melakukan pengecekan aplikasi menjadi otomatis, tanpa perlu dilakukan oleh manusia. Banyak sekali kolega saya yang dulunya manual tester kini berlomba-lomba mempelajari bahasa pemrograman agar bisa  mengendalikan komputer untuk menjadi mesin penguji otomatis, mulai dari lini automation test website, automation mobile app hingga ke pembuatan server CI/CD yang menjadikannya terintegrasi satu sama lain.

Lalu timbul lah stigma kalau manual tester sudah ketinggalan jaman, hari gini ga bisa koding tuh serasa terbelakang sekali saat disandingkan dengan automation engineers (test engineer / TE). padahal faktanya gak gitu juga keles :D . Quality Assurance (manual, yang tidak bisa koding) lalu menjadi Test engineer bukanlah bentuk dari "Evolusi" seorang tester, dua pekerjaan itu memiliki **disiplin ilmu yang berbeda**, ga semua orang suka ngoding, menatap text editor berwarna hitam bisa saja membuat orang mual-mual, seorang QA manual yang tidak bisa koding pun bisa saja memberikan dampak yang luarbiasa bernilai dalam menjaga kualitas aplikasi kita tetap prima.

Jadi jika kamu merasa kurang tertarik belajar koding, jangan dulu gusar, karena ada beberapa hal yang bisa menjadi senjata pamungkas manual tester, percayalah manusia lebih piawai dalam menguji, karena kita telah dianugerahi logika berfikir, perasaan akan estetika dan memiliki ide kreatif yang unlimited dalam menguji aplikasi yang di test, ada beberapa hal berikut ini yang menurut saya bisa menjadi point-point andalan yang bisa kamu latih sebagai software quality assurance / analyst untuk tetap berperan aktif dalam meningkatkan kualitas produk kita, diantaranya:

---

<h2><figure class="post__image"><img alt="Photo by Startup Stock Photos from Pexels" height="3648" loading="lazy" sizes="100vw" src="/media/posts/5/action-plan-brainstorming-complex-212286.jpg" srcset="/media/posts/5/responsive/action-plan-brainstorming-complex-212286-xs.jpg 300w, /media/posts/5/responsive/action-plan-brainstorming-complex-212286-sm.jpg 480w, /media/posts/5/responsive/action-plan-brainstorming-complex-212286-md.jpg 768w, /media/posts/5/responsive/action-plan-brainstorming-complex-212286-lg.jpg 1024w, /media/posts/5/responsive/action-plan-brainstorming-complex-212286-xl.jpg 1360w, /media/posts/5/responsive/action-plan-brainstorming-complex-212286-2xl.jpg 1600w" width="5472"/></figure></h2>

## Bug Buster

#### Menemukan lebih banyak bugs

ini adalah tugas pokok dari seorang tester, biasanya manual tester lebih agresif dan usil dalam ngotak-ngatik aplikasinya, tidak seperti automation script yang sudah di buat alur pengujian nya sehingga komputer bisa meniru skenario yang mungkin dilakukan pengguna. Ketika komputer hanya bisa menguji hal sama yang sudah diprogram jangan terlalu berharap banyak kita menamukan bug baru yang berbeda, sesungguhnya manusia jauh lebih baik dalam menemukan bugs daripada mesin yang menguji hal yang sama berulang-ulang.

#### Lebih cepat memberikan timbal balik

Semua orang maunya dapat jawaban lebih cepat, saat ada build baru, programmer mau tau gimana fiturnya udah OK belum. Saat ngetest aplikasi/fitur baru tentu lebih baik diserahkan oleh manusia yang punya daya nalar dan karsa yang luar biasa, sehingga bisa mencari hal-hal apa saja yang diluar batas kewajaran. Sebenarnya komputer akan lebih baik jika melakukan test fitur yang dulu-dulu (regression test). Karena dalam kasus ini, aplikasi/fitur baru biasanya belum begitu stabil dan banyak perubahan tentu manual tester akan lebih cocok, sembari TE sedang menulis code baru untuk implementasi automationnya.

---

## Domain Knowledge

Memahami bisnis proses adalah hal yang sangat berharga, mengetahui jawaban kenapa fitur ini ada? apakah memang ini yang user inginkan? relasi antar fitur, sangat membantu tim menemukan celah masalah yang mungkin timbul di kemudian hari, sehingga bisa menjaga tim untuk tetap men-deliver value berkualitas bagi user

#### Pahami kebutuhan user

Lihatlah cara user menggunakan aplikasi kamu, pelajari apa saja yang menjadi perhatian mereka, berempati terhadap pengguna aplikasi kita, bisa jadi pengguna kita adalah kakek-kakek yang gagap teknologi loh.

#### Gimana kalau...

Sebelum menghadiri design meeting ataupun sprint planing, kita bisa melakukan analisa lebih lanjut tentang requirement yang akan dikerjakan tim dair PO, apakah memang fitur ini dibutuhkan user? bagaimana dengan fitur A yang kemungkinan nyenggol nantinya? gimana kalo HP nya tiba-tiba mati/hilang sinyal/server down? gimana kalau gini,, gitu? jangan takut bertanya terkait fitur tersebut, bombardir tim dengan pertanyaan "gimana kalo", karena semakin banyak kita mendapatkan skenario perilaku user di kondisi tertentu maka akan sangat mengurangi ambuitas fitur tersebut

---

## Technical Knowledge

Pemahaman teknis itu penting sekali dalam konteks menginvestigasi masalah yang timbul, ngusilin aplikasi, troubleshooting, pelajari bagaimana sistem bekerja dalam rangka mencari kelemahan sistem secara lebih efektif, tidak perlu terlalu dalam.

Tetapi jangan sampai terjerat dengan sudut pandang teknis dari developer, karena terkadang seringkali ketika kita memahami kendala teknis yang timbul menjadikan tester malah kompromi dengan masalah yang timbul.

#### Pelajari lebih jauh

Baca buku/blog terkait testing, datangi meetup atau confrence, tonton rekaman webminar di youtube, temukanlah inspirasi untuk meningkatkan proses testing kamu, lakukan perubahan, jangan mau terjebak di rutinitas

---

## Communication

Kemampuan berkomunikasi adalah hal kritikal bagi tester, kita harus cakap dalam menyampaikan gagasan, dan mengajukan pertanyaan. Pahami apa yang bisnis mau dengan bertanya pada Product Owner, stakeholder, developer ataupun user sebenarnya, komunikasi disini tidak melulu soal bagaimana cara kita berbicara kepada orang lain, tetapi ahli juga dalam mendengarkan untuk mendapatkan pemahaman, sudut pandang lain secara menyeluruh.

Sampaikanlah hal-hal yang menjadi perhatian kamu untuk dibuatkan test automatis kepada automation engineer, atau bahkan tanyakan hal apa saja yang sulit di otomatisasi komputer sehingga kita bisa tutupi di pengujian manual, lalu Developers sebenarnya sangat senang ketika bertanya, seperti pertanyaan soal bagaimana implementasi fitur itu dibuat, dan titik lemah dari implementasi itu sehingga perlu di test secara detail dan teliti. dan tanyakan bagaimana mereka mengujinya.

#### Lebih informatif

Pahami bagaimana cara melaporkan permasalahan, jangan sampai ketika orang lain baca tiket issue/bug kita mereka mengernyitkan dahi dan bertanya langsung ke kamu, ketika developer bertanya berkali-kali ke kamu soal laporan bug, artinya ada waktu yang terbuang, waktu kamu untuk mejelaskan langsung, dan waktu dev untuk memahami maksud kamu. maka dari itu, sangat penting sekali untuk menuliskan detail permasalah saat menemukan bug. cantumkanlah hal-hal informatif seperti: software version, environment, deskripsi permasalahan dari sisi user, cara reproduce masalah itu, dan tester yang baik akan memberikan informasi dengan jelas bagaimana seharusnya itu tidak terjadi dan harapannya.

idealnya kamu bisa melakukan investigasi ala Sherlock Holmes dari hulu-hilir untuk menemukan tersangka penyebabnya

---

## Organization

Mengatur prioritas, membuat rencana dan keahlian multitasking sangat erat dengan pekerjaan sehari-hari tester, sehingga seringkali dianggap remeh oleh orang lain sampai mengira testing selalu memerlukan waktu lama sampai selesai.

#### Bantu test engineer

Kamu bukanlah orang yang mahir koding, jadi jangan terlalu memaksakan mempelajari automation framework, lebih baik kolaborasi dengan test engineer untuk bisa merancang pola otomatisasi pengecekan yang baik dan efisien, sampaikan skenario mana yang sering dijalankan, dan membosankan untuk di test manual, oh ya, jangan lupa juga berikan pula pemahaman sudut pandang dari segi bisnis ke tim engineer (developer juga termasuk)

---

## Emotions

Sebagai tester sudah tentu kita akan terlibat dengan banyak orang, dari mulai PO, Dev, Stakeholder, bahkan user. kita harus pintar membaca karakter orang lain, sedasng dalam keadaan mood seperti apa, sehingga bisa menggunakan gaya komunikasi yang cocok

---

## Critical Thinking

Berfikir kritis diperlukan untuk mencari celah masalah aplikasi. Memperhatikan detail yang timbul, mungkin tidak tampak dari luar, sehingga perlu dibongkar lebih dalam, menyambungkan titik-titik sambungan antar fitur sehingga melahirkan kombinasi baru yang belum dijaga by sistem.

#### Latihan berfikir kritis

Kita banyak insatal aplikasi di device kita, pernahkan kita berfikir "kok gini sih fiturnya" atau bahkan kita sering menemukan bugs saat penggunaan nya? latih terus daya kreatif kita dalam menggunakan aplikasi orang lain, dan bagaimana seharusnya fitur itu menjadi lebih baik, tester yang bagus biasanya tidak cepat puas

---

Jadi pada intinya tidak ada yang saling menggantikan, robot belum bisa menggantikan manusia dalam test, kuncinya adalah saling bersinergi antara manual dan automation tester, karena saling memiliki sisi tajam nya masing-masing, dan tujuan akhirnya adalah "Don't find bugs, prevent bugs!"
