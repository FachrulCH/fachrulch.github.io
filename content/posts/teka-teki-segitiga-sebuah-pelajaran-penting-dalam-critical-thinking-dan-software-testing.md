+++
title = "Teka-Teki Segitiga: Sebuah Pelajaran Penting! Critical Thinking dan Software Testing"
date = 2023-07-02T11:07:00+04:00
updated = 2023-07-02T12:02:21+04:00
tags = ["belajar-qa", "merdeqa"]
description = "Gimana cara gw belajar melatih critical thinking dari sebuah teka-teki untuk softaware quality assurance (tester)"
cover = "/media/posts/62/Teka-Teki-Segitiga-Sebuah-Pelajaran-Penting-Critical-Thinking-dan-Software-Testing.jpg"
+++

Salam 🙌

Beberapa waktu lalu, di timeline gw ada tweet yang lagi rame soal tantangan menghitung jumlah segitiga dalam satu gambar, gw langsung mikir "nah ini contoh bagus buat melatih critical thinking buat software tester"

Kemarin (1 Juli 2023), gw bikin quiz kecil-kecilan di instagram [@ngetest.id](https://www.instagram.com/ngetest.id/), soal pertanyaan teka-teki menghitung segitiga ini "How many triangles?"

<figure><figure class="post__image post__image--center"><img alt="" height="800" loading="lazy" sizes="100vw" src="/media/posts/62/WhatsApp-Image-2023-07-02-at-10.34.17-2.jpeg" srcset="/media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.34.17-2-xs.jpeg 300w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.34.17-2-sm.jpeg 480w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.34.17-2-md.jpeg 768w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.34.17-2-lg.jpeg 1024w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.34.17-2-xl.jpeg 1360w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.34.17-2-2xl.jpeg 1600w" width="360"/></figure><figcaption>quiz di akun @ngetest.id (silakan follow klo belum)</figcaption></figure>

Rate yang jawab ga banyak sih sekitar 27% orang yang menjawab, tapi pas gw cek jawabannya, gw kaget juga banyak yang jawab "salah" alias kejebak pas ngitung jumlah segitiganya! Terus sebenernya, berapa sih jumlah segitiga yang bener?

<figure><figure class="post__image post__image--center"><img alt="" height="451" loading="lazy" sizes="100vw" src="/media/posts/62/WhatsApp-Image-2023-07-02-at-10.35.45-2.jpeg" srcset="/media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.35.45-2-xs.jpeg 300w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.35.45-2-sm.jpeg 480w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.35.45-2-md.jpeg 768w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.35.45-2-lg.jpeg 1024w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.35.45-2-xl.jpeg 1360w, /media/posts/62/responsive/WhatsApp-Image-2023-07-02-at-10.35.45-2-2xl.jpeg 1600w" width="350"/></figure><figcaption>jawabannya 18</figcaption></figure>

Jawaban utamanya 18, tapi plot twist nya, ini bukan jawaban yang gw harapkan loh 😱

Oke kita bahas dulu, dari mana sih angka 18 ini muncul? ini di dapat dari kombinasi garis yang membentuk segitiga, percaya-gak percaya ada rumus matematika juga loh untuk ini, karena katanya menghitung segitiga sama halnya dengan menghitung kombinasi dari tiga garis (three lines chosen out of six)

<figure><figure class="post__image post__image--center"><img alt="" height="355" loading="lazy" sizes="100vw" src="/media/posts/62/jawaban-teka-teki-segitiga.jpeg" srcset="/media/posts/62/responsive/jawaban-teka-teki-segitiga-xs.jpeg 300w, /media/posts/62/responsive/jawaban-teka-teki-segitiga-sm.jpeg 480w, /media/posts/62/responsive/jawaban-teka-teki-segitiga-md.jpeg 768w, /media/posts/62/responsive/jawaban-teka-teki-segitiga-lg.jpeg 1024w, /media/posts/62/responsive/jawaban-teka-teki-segitiga-xl.jpeg 1360w, /media/posts/62/responsive/jawaban-teka-teki-segitiga-2xl.jpeg 1600w" width="350"/></figure><figcaption>jawaban jumlah segitiga</figcaption></figure>

Begitulah kenapa muncul angka 18 sebagai jawaban Quiz di instagram [@ngetest.id](https://www.instagram.com/ngetest.id/), tapi bukan itu jawaban yang gw harapkan dari followers akun ngetest.id yang gw yakin sebagian besar adalah seorang software tester, yaitu "Bertanya"

---

## Eh gimana maksudnya?

Karena di keterangan quiz nya itu banyak informasi yang ambigu bahkan multi tafsir sih, kebiasaan kita tuh banyak yang anggep asumsi umum sebagai kebenaran dari sebuah requirements (user story), padahal belum tentu itu yang diharapkan.

<figure><figure class="post__image post__image--center"><img alt="" height="778" loading="lazy" sizes="100vw" src="/media/posts/62/jawaban-yang-diharapkan.jpeg" srcset="/media/posts/62/responsive/jawaban-yang-diharapkan-xs.jpeg 300w, /media/posts/62/responsive/jawaban-yang-diharapkan-sm.jpeg 480w, /media/posts/62/responsive/jawaban-yang-diharapkan-md.jpeg 768w, /media/posts/62/responsive/jawaban-yang-diharapkan-lg.jpeg 1024w, /media/posts/62/responsive/jawaban-yang-diharapkan-xl.jpeg 1360w, /media/posts/62/responsive/jawaban-yang-diharapkan-2xl.jpeg 1600w" width="350"/></figure><figcaption>harusnya ada yang tanya di story ini</figcaption></figure>

Oke di context quiz segitiga ini, informasi yang perlu diklarifikasi dari pertanyaan (reqirements) "How many ***triangles***?" sebenernya:

- Triangles? eh segitiga yang mana nih? segitiga sama kaki? sama sisi? atau segitiga sembarangan?
- Ini ngitung segitiga yang keliatan doang?
- Luar nya doang? apa termasuk yang di dalem? (segitiga dalam segitiga)
- Atau yang paling epik tuh klo ada yang tanya "Ini garis di lembar kertas diitung membelah segitiga juga ga?"

<figure><figure class="post__image post__image--center"><img alt="" height="100" loading="lazy" sizes="100vw" src="/media/posts/62/detail-segitiga.png" srcset="/media/posts/62/responsive/detail-segitiga-xs.png 300w, /media/posts/62/responsive/detail-segitiga-sm.png 480w, /media/posts/62/responsive/detail-segitiga-md.png 768w, /media/posts/62/responsive/detail-segitiga-lg.png 1024w, /media/posts/62/responsive/detail-segitiga-xl.png 1360w, /media/posts/62/responsive/detail-segitiga-2xl.png 1600w" width="350"/></figure><figcaption>garis kertas juga keiting bikin segitiga baru?</figcaption></figure>

Pertanyaan ini penting banget untuk dipahami sebelum menjawab (ngeTest), karena jumlah jawabanya (jumlah segitiga) akan tergantung dari kesepakatan bersama dalam konteks pertanyaan ini (requirements), karena salah tafsir bisa ngasih jawaban yang salah atau nggak lengkap

Sebagai Software Tester, kita harus paham banget apa sih yang kita tes dan konteks nya gimana. Kita harus pastiin klo tim (QA, Dev, dkk) punya pemahaman yang sama tentang apa yang diharapkan dari softwarenya

## Jadi, apa yang bisa kita pelajari dari teka-teki segitiga ini?

Jangan takut buat nanya. Jangan asumsi kamu udah ngerti semuanya. Pahami konteks, pahami requirement, asah critical thinking kamu. Kita harus bisa melihat lebih dari apa yang nampak di depan mata, kita harus bisa "melihat" apa yang tidak tampak oleh orang lain, menguji batas dan memastikan bahwa tim bisa memberikan yang terbaik melebihi harapan pelanggan (production user)

---

Sumber artikel: [https://www.popularmechanics.com/science/math/a30706968/viral-triangle-brain-teaser-solved/](https://www.popularmechanics.com/science/math/a30706968/viral-triangle-brain-teaser-solved/)
