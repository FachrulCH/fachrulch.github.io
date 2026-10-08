+++
title = "Apa itu Pengujian Program komputer (software testing)?"
seo_title = "Apa itu Pengujian Program komputer (software testing)?"
date = 2019-06-01T00:33:00+04:00
updated = 2019-06-03T18:51:15+04:00
tags = ["testergadungan"]
description = "Apa itu software testing? Kenapa aplikasi perlu diuji? Siapa yang menguji? Kapan harusnya pengujian dimulai? Bagaimana dikatakan pengujian telah selesai?"
cover = "/media/posts/19/background-blank-craft-301703.jpg"
cover_caption = "Photo by Pixabay from Pexels"
canonical = "https://penguji.id/apa-itu-pengujian-aplikasi-komputer-software-testing/"
listed = false
+++

Pada kesempatan kali ini kita akan bahas secara umum mengenai Software testing (pengujian program komputer). Kita akan kupas lebih dalam terkait dengan Apa, Kenapa, Siapa, Kapan, Bagaimana (4W1H) pengujian program komputer itu.

---

## Apa itu software testing?

Pengujian program komputer (software testing) adalah proses menilai kualitas sebuah sistem komputer, salah satu caranya adalah dengan mencari ketidak sesuaian program (bugs) dengan harapan pengguna dalam dokumen requirement.

Pengujian seperti ini akan bisa mengukur kualitas program secara garis besar dari segi ketepatan (correctness), kelengkapan (completeness), kebergunaan (usability), kinerja (performance) dan juga segi fungsional ataupun non-fungsional lainya

---

## Kenapa program perlu diuji?

Pengujian program akan dilakukan dalam fase pengembangan program komputer, karena:

- Mengetahui kualitas program sebelum digunakan penguna sesungguhnya, apakah sudah memenuhi standar kualitas yang diharapkan
- Menghindari kesalahan program, jangan sampai kesalahan ini menyusahkan pengguna, karena akan berimbas pada reputasi perusahaan
- Menghadirkan rasa aman, dan percaya diri untuk melepaskan fitur/program baru untuk dikonsumsi khalayak
- Menemukan kesalahan di fase awal tentu akan menghemat beban perbaikan daripada ketika ditemukannya kesalahan di fase production
- Tim penguji akan memberikan sudut pandang yang berbeda dalam pengunaan program komputer

---

## Siapa yang melakukan pengujian?

Setiap anggota tim pengembangan memiliki peran dalam meningkatkan dan menjaga mutu program yang baik, pengujian ini beraneka ragam sesuai dengan tingkatannya, kurang lebih:

- Product owner: menguji apakah ide fitur pada program sungguh-sungguh berguna bagi user, dan apakah sudah tepat guna
- Developer: mengerjakan unit testing dalam rangka memastikan setiap kode yang dituliskan bekerja sebagaimana mestinya, dan tahan akan perubahan kode dimasa depan
- Tester: memastikan program bekerja secara fungsional, kebergunaan, kinerja, dan keamanan program.
- Lead/Manager/Architecs: mengawal ataupun merencanakan strategi dan rencana pengujian

---

## Kapan harusnya pengujian dimulai?

Itu sebenarnya disesuaikan dengan proses SDLC (software development life cycle) model yang dijalankan oleh tim pengembangan, bisa jadi ada fase khusus untuk pengujian, ataupun bisa jadi fase pengujian membaur dengan fase impementasi kode oleh tim pengembang, yang menarik ada satu mitos (yang saya yakini) bahwa katanya pengujian hanya bisa dilakukan ketika implementasi oleh pengembang sudah selesai, tetapi ternyata pengujian itu bisa (harusnya) dimulai bahkan ketika kode belum ditulis.

pengujian bisa berjalan beriringan (paralel) dengan fase implementasi fitur oleh tim pengembang, contohnya melalui V model.

<table><tbody><tr><td><strong>Fase</strong></td><td><strong>Aktifitas pengujian</strong></td></tr><tr><td>Perancangan Requirement</td><td>Membuat acceptance criteria</td></tr><tr><td>Spesifikasi fungsional</td><td>Membuat skenario fungsional</td></tr><tr><td>Implementasi</td><td>Membuat otomatisasi pengujian</td></tr><tr><td>Kode selesai</td><td>Menjalankan rencana pengujian</td></tr></tbody></table>

---

## Bagaimana dikatakan pengujian telah selesai?

Pengujian bisa dijalankan secara manual ataupun (dan) secara otomatisasi. pengujian manual seperti verifikasi rancangan requirement, mengatur strategi dan rencana pengujian, persiapan data, regression test, dan eksekusi pengujian, sedangkan pengujian otomatisasi seperti membuat script untuk unit testing, integration test, UI test, performance test, bahkan security test dengan bantuan aplikasi dan program khusus sesuai kebutuhan.

Referensi lanjutan:

- [https://www.guru99.com/software-testing-introduction-importance.html](https://www.guru99.com/software-testing-introduction-importance.html)
- [https://testautomationu.applitools.com/the-whole-team-approach-to-continuous-testing/index.html](https://testautomationu.applitools.com/the-whole-team-approach-to-continuous-testing/index.html)
