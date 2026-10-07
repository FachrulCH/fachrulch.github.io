+++
title = "Senangnya ketika bug report di Github Project telah di resolved"
date = 2020-09-03T20:29:00+04:00
updated = 2021-01-23T22:29:39+04:00
tags = []
description = "Senangnya dalam hati Ketika issue yang kita raise di github project akhirnya di aknowledge dan di resolve oleh maintener 😅 Whooaa.. eeh apaan tuh? Jadi gini, di kantor gw tuh pake library python Toolium untuk ngerjain automation test mobile app, library nya kece banyak banget…"
cover = "/media/website/whois-fachrulch.png"
cover_alt = "penulis"
cover_caption = "Fachrul Choliluddin"
og_image = "/media/website/profile-newletter-3.png"
listed = false
+++

Senangnya dalam hati

Ketika issue yang kita raise di github project akhirnya di aknowledge dan di resolve oleh maintener 😅

<figure class="post__image post__image--center"><img alt="" height="180" loading="lazy" sizes="100vw" src="/media/posts/36/ada-notif-github.png" srcset="/media/posts/36/responsive/ada-notif-github-xs.png 300w, /media/posts/36/responsive/ada-notif-github-sm.png 480w, /media/posts/36/responsive/ada-notif-github-md.png 768w, /media/posts/36/responsive/ada-notif-github-lg.png 1024w, /media/posts/36/responsive/ada-notif-github-xl.png 1360w, /media/posts/36/responsive/ada-notif-github-2xl.png 1600w" width="564"/><figcaption>ada yang menarik di notifikasi kali ini</figcaption></figure>

**Whooaa.. eeh apaan tuh?**

Jadi gini, di kantor gw tuh pake library python [Toolium](https://github.com/Telefonica/toolium) untuk ngerjain automation test mobile app, library nya kece banyak banget ngebantu generate test appium dengan lebih cepat, nah suatu ketika ternyata library ini ada problem dimana test android kalo failed jadi ada freeze di teardown process karena ada proses streaming android bugreport yang ukurannya gede bisa 3 MB di ekstrak dari device, nah akhirnya gw coba debug kenapa kok proses teardown ini selalu lama.

Akhirnya ketahuan dari library Toolium ini ada tindakan secara "paksa" untuk ambil 3 macem log, yaitu appium log, android logcat, dan bugreport, yang jadi masalah prose load log ini ga bisa configured, jadi di paksa ambil data gede terus makanya test jadi freeze saat teardown karena generate dan ekstrak 3 megabyte bugreport itu bisa makan waktu 1 menit, kan kesel nungguinnya 😅

**Ok,, trus trus**

Sebenernya bisa aja saya monkey patch library ini, dengna overide method tersebut, tapi buat permanen solution harusnya dari library nya ini yang di ubah, akhirnya saya coba create bug tiket serius yang pertama [disini](https://github.com/Telefonica/toolium/issues/178#event-3713583701) dan berharap di solved sama maintener nya, klo dilihat sih lumayan aktif development dari perusahaan Telefonica ini, walau toolium web yang sering dapet updatenya.

<figure class="post__image--center"><img alt="" height="2026" loading="lazy" sizes="100vw" src="/media/posts/36/issue-di-resolved.png" srcset="/media/posts/36/responsive/issue-di-resolved-xs.png 300w, /media/posts/36/responsive/issue-di-resolved-sm.png 480w, /media/posts/36/responsive/issue-di-resolved-md.png 768w, /media/posts/36/responsive/issue-di-resolved-lg.png 1024w, /media/posts/36/responsive/issue-di-resolved-xl.png 1360w, /media/posts/36/responsive/issue-di-resolved-2xl.png 1600w" width="2028"/></figure>

Selang waktu beberapa lama, ternyata 3 hari lalu solved dan sudah ada di versi release Toolium terbaru donk 😍

**Sounds cool, apa lagi tuh?**

Nah sebenernya pun saya sudah tau cara resolvednya, tapi mau raise PR sendiri kok belum percaya diri, jadi memilih raise bug tiket saja, dan ternyata memang betul, jika saya perhatikan diff changes codenya, banyak hal yang kemungkinan saya lewatkan dalam perbaikan sendiri seperti cara verifikasi test serta dokumentasinya

Ternyata sangat menyenangkan membandingkan approach problem solving yang berbeda dari kita, bisa dilihat style dan karakter dia dalam bentuk kode

<figure class="post__image post__image--center"><img alt="" height="804" loading="lazy" sizes="100vw" src="/media/posts/36/perubahan-pertama.png" srcset="/media/posts/36/responsive/perubahan-pertama-xs.png 300w, /media/posts/36/responsive/perubahan-pertama-sm.png 480w, /media/posts/36/responsive/perubahan-pertama-md.png 768w, /media/posts/36/responsive/perubahan-pertama-lg.png 1024w, /media/posts/36/responsive/perubahan-pertama-xl.png 1360w, /media/posts/36/responsive/perubahan-pertama-2xl.png 1600w" width="3224"/><figcaption>perubahan kode</figcaption></figure>

Dengan sedikit perubahan saja, ternyata bisa beranak banyak test baru seperti:

```python
def test_save_webdriver_logs_one_log_type(driver_wrapper, utils):
def test_save_webdriver_logs_multiple_log_types(driver_wrapper, utils):
def test_save_webdriver_logs_multiple_log_types_with_spaces(driver_wrapper, utils):
def test_save_webdriver_logs_none_log_type(driver_wrapper, utils):
def test_save_webdriver_logs_all_log_type(driver_wrapper, utils):
def test_save_webdriver_logs_without_log_types(driver_wrapper, utils):
```

Mantap, bisa kita pelajari juga cara dia menguji kode yang dia tulis sebelumnya

jadi semangat ikut kontribusi ke projek ini/lain selanjutnya
