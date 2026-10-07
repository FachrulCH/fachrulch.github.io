+++
title = "Memecahkan masalah yang sebenarnya"
date = 2019-05-16T16:41:03+04:00
updated = 2019-05-16T16:41:03+04:00
tags = ["testergadungan"]
description = "kenapa sisi bisnis memberikan solusi yang salah sih? bagaimana kita sebagai pengrajin kode bisa menyelesaikan masalah yang sesungguhnya dengan software"
cover = "/media/posts/14/accident-action-asphalt-6078-1.jpg"
cover_caption = "masalah mobil mogok Photo by Kaboompics .com from Pexels"
+++

## Mengapa kita mencoba menyelesaikan masalah yang salah?

Pada umumnya, bekerja di dunia software development lebih sering berkecimpung dalam maintenance dari aplikasi tua yang sudah dibuat dari dulu oleh developer sebelumnya dan kita tinggal melanjutkannya saja. Jarang sekali (walaupun ada) kesempatan untuk memulai projek dari awal sekali, lebih sering malah menangani sistem lama yang akan diakhiri (sunset) atau sistem yang sedang terseok-seok, kebakaran dan perlu diselamatkan dengan memberikan peningkatan (scalable) agar bisa memenuhi kebutuhan bisnis pada saat ini.

Tak heran programmer pemula yang kelimpahan kerjaan seperti ini seringkali ngomel-ngomel, memaki dalam hati karena penulis aslinya dulu yang tidak mampu membuat aplikasi dengan pengalaman terbaik (best practice) atau bisa fleksibel disesuaikan dengan kebutuhan bisnis dimasa depan.

Padahal sesungguhnya, semakin lama saya bekerja dilingkungan teknologi, semakin saya menyadari, bahwa seringkali kebutuhan bisnis mengalahkan desain arsitektur paripurna, dengan dalih tenggat waktu yang mendesak, beban sumber daya, dan situasi pasar yang bergejolak.

Kebutuhan bisnis ini hanya mentoleri selama aplikasi bisa menyelesaikan menjawab kebutuhan pasar dengan segera, tidak lebih.

<figure class="post__image post__image"><img alt="Photo by Denniz Futalan from Pexels" height="426" loading="lazy" sizes="100vw" src="/media/posts/14/accident-adult-battle-942560.jpg" srcset="/media/posts/14/responsive/accident-adult-battle-942560-xs.jpg 300w, /media/posts/14/responsive/accident-adult-battle-942560-sm.jpg 480w, /media/posts/14/responsive/accident-adult-battle-942560-md.jpg 768w, /media/posts/14/responsive/accident-adult-battle-942560-lg.jpg 1024w, /media/posts/14/responsive/accident-adult-battle-942560-xl.jpg 1360w, /media/posts/14/responsive/accident-adult-battle-942560-2xl.jpg 1600w" width="639"/><figcaption>Photo by <strong><a href="https://www.pexels.com/@denniz-futalan-339724?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels">Denniz Futalan </a></strong>from <strong><a href="https://www.pexels.com/photo/silhouette-of-fireman-holding-hose-942560/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels">Pexels</a></strong></figcaption></figure>

Saat kita mengais puing-puing kode usang tapi masih bisa berfungsi, seringkali kita dibuat garuk-garung kepala, lalu tersenyum simpul melihat penampakan kode aneh bin ajaib muncul, seolah kita masuk ke lorong waktu dan mengenal betul penulis aslinya, kita bisa tahu kapan masanya si empunya ini sedang gandrung metode MVC, lalu berlanjut dengan gaya functional yang mulai populer, dan perubahan gaya kode kekinian lain sebagainya. Kita harus bisa sekreatif mungkin menjaga kode warisan (legacy codebase) ini agar tetap bekerja sebagaimana bisnis harapkan dengan minim perubahan, toh ini lebih baik daripada menggerutu dan memaksa untuk merubahnya menjadi kode yang lebih keren dengan object orientation yang benar, inheritance dan interface yang mumpuni, karena sangat beresiko jika tidak bisa menjinakannya.<br><br>Sebagian besar yang bikin frustasi adalah ketika perancang kode atau bisnis tidak bisa mengkomunikasikan masalahnya dengan tepat, sehingga lebih sering penyelesaian masalah dengan program perangkat lunak menjadi melenceng, entah bisa menjadi solusi tepat guna atau tidak, sehingga ujung-ujungnya perlu bongkar pasang, malah buang-buang waktu.

## Kenapa sisi bisnis memberikan solusi yang salah sih?

Sebuah hal yang sering terjadi dalam menyelesaikan masalah yang salah adalah ketika bisnis menjelaskan masalahnya dan solusi yang mereka pikirkan sendiri lalu kita menelannya mentah-mentah.

Sebagai sebuah contoh, dengan analogi seseorang yang baru mahir mengendarai sepeda dan mulai memberanikan diri berkendara di jalan umum, lalu ia pergi ke bengkel sepeda dan menyampaikan maksud kedatangannya ke mekanik disana "Mas, saya ingin sepeda ini dipasangi lampu sign seperti sepeda motor, berapa saya harus bayar ya?" dan si mekanik ini dengan pengalaman yang dimiliki tentu perlu tahu kenapa dia inigin hal ini "Hmm jadi yang kamu perlu adalah cara supaya lebih terlihat oleh pengendara lain ketika main sepeda di malam hari? Saya bisa bantu kamu menemukan material yang akan membuatmu terlihat di malam hari dan yang pasti lebih murah daripada sign motor", lalu pemilik sepeda menjawab "Iya bener banget".

<figure class="post__image post__image"><img alt="solution" height="640" loading="lazy" sizes="100vw" src="/media/posts/14/art-artsy-bulb-1938318.jpg" srcset="/media/posts/14/responsive/art-artsy-bulb-1938318-xs.jpg 300w, /media/posts/14/responsive/art-artsy-bulb-1938318-sm.jpg 480w, /media/posts/14/responsive/art-artsy-bulb-1938318-md.jpg 768w, /media/posts/14/responsive/art-artsy-bulb-1938318-lg.jpg 1024w, /media/posts/14/responsive/art-artsy-bulb-1938318-xl.jpg 1360w, /media/posts/14/responsive/art-artsy-bulb-1938318-2xl.jpg 1600w" width="640"/><figcaption>Photo by <strong><a href="https://www.pexels.com/@jhonismartins?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels">Jhonis Martins </a></strong>from <strong><a href="https://www.pexels.com/photo/person-holding-white-light-bulb-beside-black-bulb-socket-1938318/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels">Pexels</a></strong></figcaption></figure>

<h2><br/>Bagaimana kita bisa mengelesaikan masalah yang sesungguhnya?</h2>

Sebagai pengrajin kode yang profesional, kita harus menyadari bahwa klien kita seringkali tidak mengetahui solusi yang terbaik untuk masalah yang mereka hadapi, bantu mereka dengan pengalaman kita mencari solusi yang paling jitu.

Santai dan dengarkan. Bicaralah dengan orang dari sisi bisnis, dan tanyakan hasil seperti apa yang dibutuhkan? Brainstorming dengan ide perbaikan, diskusi debatlah hingga menemukan formula yang tepat guna untuk menjadi solusi dari masalah yang dihadapi
