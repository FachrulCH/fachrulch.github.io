+++
title = "Kiat Sukses dalam Membuat Automation Test Solution"
date = 2019-02-22T04:35:00+04:00
updated = 2019-02-22T06:57:56+04:00
tags = ["testergadungan"]
description = "apa saja yang perlu diperhatikan dalam  membuat automation test solution"
cover = "/media/posts/8/pexels-photo-1020325.jpeg"
cover_alt = "membuat otomasi test"
cover_caption = "Pexels"
+++

Tidak sulit membayangkan manfaat dari memiliki test yang sudah di-otomatisasi (*automated*) yang dapat membantu proses pengujian aplikasi karena dengan adanya ia akan membuat *feedback* proses development menjadi jauh lebih cepat, meningkatkan efektifitas, efisiensi dan coverage pengujian, dari eksekusi test yang sering dan berulang, itu adalah sedikit-banyak manfaat dari *automated testing*. Seiring waktu, fitur yang ada pada sistem akan terus bertambah, QA akan melakukan pengujian mulai dari sistem/fitur yang sudah ada ditambah dengan sistem baru yang sedang dikembangkan.
{: .dropcap }

Suatu otomatisasi test (*test automation*) mampu melakukan membuat komputer menjalankan rangkaian aktifitas yang telah dirancang untuk membandingkan hasil dari sistem apakah sesuai dengan standar yang diinginkan *(expected behaviour)* sehingga menghasilkan laporan pengujian sistem telah berhasil atau gagal

Dengan adanya otomatisasi test ini diharapkan baban QA menjadi ringan dalam menjalankan *regression test* yang sama berulang kali, tentu ini akan menghemat waktu QA sehingga bisa fokus ke lain hal yang memiliki *impact* yang besar dalam menjaga kualitas *software* yang baik, karena itulah perannya dalam pengembangan perangkat lunak sangat penting dan bisa membantu mencapai kesuksesan dari project

---

Jika pengujian otomatis sudah dibuat dengan benar, seharusnya ia akan sangat menguntungkan bagi tim *development* secara keseluruhan, saya akan coba membagikan kiat dalam membuat otomasi test yang baik dan berguna, kemudian hal-hal apa saja yang harus dihindari saat membuat rangkaian pengujian otomatis ini, karena kita harus realistis, tidak semua bisa di otomatisasi komputer, ada batasan-batasan yang harus tetap di perhatikan

<figure class="post__image post__image--center"><img height="305" loading="lazy" sizes="100vw" src="/media/posts/8/pexels-photo-1020325.jpeg" srcset="/media/posts/8/responsive/pexels-photo-1020325-xs.jpeg 300w, /media/posts/8/responsive/pexels-photo-1020325-sm.jpeg 480w, /media/posts/8/responsive/pexels-photo-1020325-md.jpeg 768w, /media/posts/8/responsive/pexels-photo-1020325-lg.jpeg 1024w, /media/posts/8/responsive/pexels-photo-1020325-xl.jpeg 1360w, /media/posts/8/responsive/pexels-photo-1020325-2xl.jpeg 1600w" width="401"/><figcaption>Membuat Robot</figcaption></figure>

## Manual vs Automated atau Testing vs Checking

Harap dihindari membanding-bandingkan dua hal ini, antara manual dengan *automated testing*, karena keduanya memiliki fungsi yang berbeda dan saling membutuhkan. Ada yang bilang *Testing = Checking + Thinking,* sehingga selayaknya disebut ***automated checking*** bukan disebut ***automated test / test automation***, karena ia adalah pengujian berdasarkan fakta, tapi buat saya sih lebih lumrah orang lain bilang "**testing**" sih ya ahaha.

Selama *manual testing*, sisi perasaan dan nalar dari seorang *tester* akan sangat diperlukan dalam mencari titik lemah dan potensi masalah yang akan ditimbulkan dari sistem, dan seringkali proses ini tidak tidak tertulis di rencana pengujian (e*xploratory testing*) karena *tester* beradaptasi dengan hasil dari proses *testing* sehingga perlu improvisasi dalam "mengusili" aplikasi.

Di sisi lain *automated test* adalah hasil karya manusia juga yang berisi instruksi agar komputer bisa melalukan suatu task (dalam hal ini melakukan pengujian dari suatu hasil), nah setiap kali automated test ini dijalankan, maka ia akan melalukan kegiatan yang sama persis seperti instruksi yang dituliskan dalam kode, dan ia hanya menge-cek hal-hal yang diminta untuk di cek.

---

## Mulailah dari *automated regression test*

Tujuan utama kenapa otomasi test itu ada, adalah karena kita bosan menjalankan test yang sama berulang-ulang setiap rilis baru, *Regression test* perlu dijalankan seiringan dengan sistem yang terus berkembang, kita perlu memastikan bahwa setelah menambahkan fitur baru pada sistem tidak akan merusak fitur lainnya yang sudah ada.

Rangkaian test ini sangat memakan waktu dan pekerjaan yang membosankan untuk QA jalankan secara manual setiap kali, ini lah tanda-tanda *automation* diperlukan untuk menjaga konsistensi hasil pengujian, jadi regression test sangan cocok untuk mulai di otomasi

---

## Desainlah testnya dulu sebelum mulai koding

Proses yang baik adalah membuat *user scenario,* *test cases,* apa yang perlu di *expect* sebelum mulai di otomasi, karena ini bisa sangat membantu dalam mencari risiko masalah pada sistem yang ditimbulkan, lalu diskusikan dengan tim juga

Sangat tidak disarankan ketika langsung membuat otomasi kode untuk menguji skenario positif dan *happy flow* saja, dibandingkan dengan memilikirkan dan mengidentifikasi skenario mana saja yang mungkin terjadi dan bisa ditest.

Jangan juga mengotomatisasi hal yang sebenarnya tidak terlalu penting untuk di kerjakan komputer, seperti misalnya kita akan menguji halaman login, definisi orang tersebut terlah berhasil login tidak perlu memastikan URL != "/login" tetapi lebih penting untuk memastikan, misalnya *username* di pojokan sudah sesuai dengan *login credential* tadi , maka dari itu perlu bantuan dari tim member lain untuk mereview desain test kita apakah sudah mencukupi dan sudah baik dalam *test scenario* dan verifikasinya (ekspektasinya)

---

## Hilangkan keraguan

Satu hal yang penjadi point utama dari otomasi adalah bisa menjaga hasil yang konsistens, sehingga kita bisa tahu ketika test fail artinya ada sesuatu yang salah dan muncul anomali sistem

Bayangkan ketika test nya pass kemudian di jalankan lagi jadi fail, tanpa ada perubahan pada aplikasi yang di test (SUT), kita tidak pernah yakin ketika ada fail ini disebabkan oleh kesalahan kode *automation* atau *error* pada sistemnya.

Ketika ada *error*, kita harus periksa penyebab yang mengakibatkan *error* ini, kalau sudah banyak ditemukan inkonsistensi atau false positif akan membuat proses pengecekan error ini lama dan sulit. Jangan takut untuk menghapus test yang ga stabil seperti itu di rangkaian test kita, karena yang kita perlukan adalah hasil yang konsisten dan bisa dipercaya.

Perlu diperhatikan, kualitas otomatisasi test sangat tergantung dari kualitas orang yang menulisnya, bisa jadi test nya berjalan baik, semua check pass, tetapi ada kemungkinan kesalahan bisa saja muncul, tetapi komputer tidak peduli (karena diluar set ekspektasi) sehingga bisa memberikan false quality impression.

<figure class="post__image--center"><img alt="" height="303" loading="lazy" sizes="100vw" src="/media/posts/8/pexels-photo-955450.jpeg" srcset="/media/posts/8/responsive/pexels-photo-955450-xs.jpeg 300w, /media/posts/8/responsive/pexels-photo-955450-sm.jpeg 480w, /media/posts/8/responsive/pexels-photo-955450-md.jpeg 768w, /media/posts/8/responsive/pexels-photo-955450-lg.jpeg 1024w, /media/posts/8/responsive/pexels-photo-955450-xl.jpeg 1360w, /media/posts/8/responsive/pexels-photo-955450-2xl.jpeg 1600w" width="406"/></figure>

---

## Jangan otomasi fitur yang belum stabil

Sebagaimana sebuah fitur baru yang sedang dikembangkan, banyak sekali hal yang tidak mulus, bahkan seringkali saking agile nya ternyata fitur tersebut tidak lagi relevan dan di batalkan karena bisnis telah berubah dari rencana awal, sehingga otomasi menjadi sia-sia

Ketika proses otomasi test sudah dimulai berbarengan dengan fitur tersetbut dimulai, maka test akan sering sekali di ubah untuk bisa menyesuaikan implementasi fitur yang bergerak juga, dan ini sangat menghamburkan waktu, walaupun ada juga kok teman-teman ISQA dari *startup* lain yang sudah berhasil membuat otomasi test berbarengan dengan fitur dibuat.

Bagaimanapun, saya lebih condong berpendapat implementasi *automation* (khususnya UI) itu akan lebih baik dibuat ketika fitur sudah stabil dan tidak banyak berubah

---

## **Jangan harap keajaiban dari otomasi**

Jangan pernah berharap otomasi akan bisa menangkap banyak bugs, faktanya dengan manual testing jumlah bug yang ditemukan lebih banyak loh.

Tujuan dibuatnya *test automation* adalah untuk membantu QA dalam proses testing sehingga waktu luang QA lebih banyak dan bisa digunakan untuk memikirkan improvement proses dan menjalankan test yang sulit dan edge cases segingga bisa memberikan kepercayaan diri bagi bahwa aplikasi masih berjalan mulus dengan adanya *deployement* fitur baru

Rangkaian *regression test scenario* yang dijalankan secara otomatis tentu akan memberikan *feedback* lebih cepat dan bisa memberikan rasa aman bagi tim untuk *deploy* ke *production*

---

## Mengerti konteks nya

Test itu bisa ada di berbagai layer, dari *unit test, API, service,* dan UI, setiap layer memiliki perbedaan tersendiri.

Unit test akan memastikan kode pada level class berjalan sebagaimana mestinya, sesuai dengan logic yang diharapkan, lebih mengutamakan verification ketimbang validation.

API test atau i*ntegration test* akan memastikan satuan function dan class bisa berjalan sesuai harapan ketika digabungkan antar class

UI atau *end to end test* adalah rangkaian dari interaksi perjalanan user, disini bisa dibilang UI level lebih ke validasi daripada verifikasi dalam menguji scenario user, test yang berjalan di layer ini cenderung lambat dan rawan *error*, bisa saja ada perbaikan secara  tampilan, tetapi secara usability masih sama dan tidak berubah sehingga bisa memberikan UI test dibilang error karena ternyata ada element yang berubah (css class ganti bikin element not found).

Dengan mengerti konteks dari setiap layer test kita akan bisa mengatur strategi otomatisasi nya, bisa jadi untuk scenario A, B, C kita akan test melalui API test, lalu hanya scenario B yang dijalankan juga pada UI test agar lebih cepat dan stabil

---

## Jangan repot-repot cover 100% semuanya

*Test coverage* 100% sangatlah sulit dicapai karena kombinasi kemungkinan yang timbul sangat beragam (*possible permutation*), ketika berbicara soal otomatisasi test semakin menambah test tidak selalu berarti manambah keyakinan akan test semakin baik. Semua itu tergantung dari sebagus apa otomatisasi pengujian di rancang.

Untuk membuat *automated scrip*t memerlukan sumber daya dan waktu, ketika kita ingin mengotomasi semuanya, sudah pasti perlu sumber daya dan waktu yang sangat banyak, yang mana pada kasus umumnya tidak bisa dipenuhi, pun semakin banyak test otomasi akan semakin memerlukan pemeliharaan kode yang lebih intens

Maka dari itu lebih baik kita buat berdasaran analisa risiko, agar bisa memilih test mana yang layak untuk di otomasi sehingga bisa sangat memberikan manfaat dalam proses testing dan dari segi skenario proses bisnis.

Oh ya, harap diperhatikan ga semua test bisa di otomasi, sering ada kasus test tersebut aslinya sangat kompleks sering kali hasilnya tidak konsisten, sehingga kasus ini lebih baik kita uji secara manual oleh QA, karena lebih baik kita fokus ke fitur/funcionality yang paling penting dan krusial bagi bisnis untuk di otomatisasi ketimbang mengejar full coverage.

---

## Jangan berniat menggantikan manual tester

Ada saja orang yang berfikir memiliki automated test sudah cukup dan tidak perlu QA manual lagi, padahal sudah jelas untuk membuat otomatisasi, kita harus pahami dlu hasil seperti apa yang diinginkan, apa yang perlu dicek sehingga dikatakan v*alid outcome*. Proses testing itu perlu kemampuan multi disiplin seperti investigasi, detektif, psikologis sehingga kita bisa merencanakan ujicoba sekaligus meneksekusi langsung, seorang manual tester yang baik akan selalu memiliki kemampuan untuk berfikir kritis mencegah error terjadi lagi bagi pengguna

---

## Jangan sampai hilang kepercayaan

Ini yang paling penting, kita harus mengantisipasi efek samping dari *test automation*, ketika kita sudah mencurahkan waktu dan tenaga untuk membuat rangkaian pengujian otomatis yang sempurna dan keren, tetapi ternyata menjadi sia-sia karena tidak berguna dan membantu bagi tim.

Bisa jadi tim tidak merasakan manfaatnya, atau bahkan tidak tahu, jadi perlu juga visibility dari rangkaian test automation solution yang kita buat, bagaimana cara mereka memakainya, lalu test apa saja yang ada di dalamnya agar tidak melakukan regression yang duplikat.

Jika automated test ini sering kali flaky (intermittent error), lambat dan tidak transparan, bagaimana bisa  memberikan indikasi kualitas sistem sedangkan automated test nya saja tidak berkualitas baik dan stabil.

---

<figure class="post__image post__image--center"><img height="326" loading="lazy" sizes="100vw" src="/media/posts/8/pexels-photo-1068523-1.jpeg" srcset="/media/posts/8/responsive/pexels-photo-1068523-1-xs.jpeg 300w, /media/posts/8/responsive/pexels-photo-1068523-1-sm.jpeg 480w, /media/posts/8/responsive/pexels-photo-1068523-1-md.jpeg 768w, /media/posts/8/responsive/pexels-photo-1068523-1-lg.jpeg 1024w, /media/posts/8/responsive/pexels-photo-1068523-1-xl.jpeg 1360w, /media/posts/8/responsive/pexels-photo-1068523-1-2xl.jpeg 1600w" width="498"/><figcaption>we are a team</figcaption></figure>

Rangkaian pengujian otomatis ini perlu dirawat layaknya mahluk hidup, ia terus berkembang dari waktu ke waktu, ada kalanya test tertentu sudah tidak relevan, jangan takut untuk mencopot test yang seringkali fail atau tidak memberikan hasil yang konsisten demi menjaga kredibilitas dari test automation solution kita sebagai indikator dari kualitas aplikasi/sistem.

Dengan mengerti batasan diatas, menurut saya peran manusia tetap berperan penting dalam proses pengujian belum bisa digantikan sepenuhnya oleh otomasi komputer, lalu kenapa kita perlu membuat otomatisasi pengujian aplikasi? alasan singkatnya adalah "**repeatability**",  lebih ke kolaborasi dengan adanya bantuan komputer untuk menjalankan pengujian otomatis akan membantu QA untuk bisa lebih luang dan bisa lebih fokus untuk melakukan exploratory testing untuk lebih banyak mengali risiko, dan defects.

Jadi, lain kali ketika kamu berencana membuat otomatisasi test, coba berfikir sejenak dan berfikir, seberapa sering test ini akan di jalankan? apakah cukup layak untuk dikerjakan manual? bagaimana sampai dikatakan test nya sukses?

**Hmm sepertinya itu saja, ada tambahan kah dari teman-teman?**
{: .msg .msg--info }
