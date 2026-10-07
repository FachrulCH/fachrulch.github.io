+++
title = "Kiat memilih bahasa pemrograman untuk automation test"
date = 2019-05-17T14:00:00+04:00
updated = 2019-05-17T20:37:32+04:00
tags = ["testergadungan", "tutorials"]
description = "Mau belajar automation testing, tapi saya bingung pilih bahasa pemrograman mana yang paling bagus untuk dipelajari? pilih Java, PHP, Ruby, JavaScript, Python"
cover = "/media/posts/15/artificial-intelligence-machine-machine-learning-185725.jpg"
cover_caption = "Photo by Somchai Kongkamsri from Pexels"
+++

## Saya mau belajar automation testing, tapi saya sedikit bingung pilih bahasa pemrograman mana yang paling bagus untuk dipelajari?

Satu hal yang harus dipahami, tidak ada yang namanya bahasa pemrograman paling bagus, lebih baik mencari yang "cocok" berdasarkan situasi dan lingkungan kita dan tim. Pilihan bahasa pemrograman itu tergantung pada **kebutuhan** dan **selera** aja sih kalo kata saya mah.

<figure class="post__image post__image"><img alt="" height="853" loading="lazy" sizes="100vw" src="/media/posts/15/advice-colleagues-communication-1161465.jpg" srcset="/media/posts/15/responsive/advice-colleagues-communication-1161465-xs.jpg 300w, /media/posts/15/responsive/advice-colleagues-communication-1161465-sm.jpg 480w, /media/posts/15/responsive/advice-colleagues-communication-1161465-md.jpg 768w, /media/posts/15/responsive/advice-colleagues-communication-1161465-lg.jpg 1024w, /media/posts/15/responsive/advice-colleagues-communication-1161465-xl.jpg 1360w, /media/posts/15/responsive/advice-colleagues-communication-1161465-2xl.jpg 1600w" width="1280"/><figcaption>Photo by <strong><a href="https://www.pexels.com/@rawpixel?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels">rawpixel.com </a></strong>from <strong><a href="https://www.pexels.com/photo/advice-business-colleagues-communication-1161465/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels">Pexels</a></strong></figcaption></figure>

### Lingkungan

Misalkan dilingkungan tim yang mengerjakan program website dengan [rails](#INTERNAL_LINK#/post/null "https://books.goalkicker.com//RubyOnRailsBook/"), tentu akan sangat cocok membuat automation dengan bahasa pemrograman [ruby](#INTERNAL_LINK#/post/null "https://books.goalkicker.com/RubyBook/"), atau ternyata tim menggunakan [Spring](#INTERNAL_LINK#/post/null "https://books.goalkicker.com//SpringFrameworkBook/") untuk membuat aplikasi, tentu pilihan coding [java](#INTERNAL_LINK#/post/null "https://books.goalkicker.com//JavaBook/")/[kotlin](#INTERNAL_LINK#/post/null "https://books.goalkicker.com//KotlinBook/")/atau jvm lain sangat cocok, kenapa begitu?

Karena dengan mengikuti bahasa yang sama dengan program yang menjadi target automation. kita bisa memiliki beberapa kelebihan, diantaranya: automation script bisa hidup berdampingan, satu tempat dengan repository code target aplikasi (application under test) jadi bisa dengan mudah masuk kedalam pipeline build program tersebut, lalu juga dengan bahasa pemrograman yang sama kita akan mendapatkan dukungan teknikal dari developer yang tak sungkan membantu kita ketika menemukan kendala dalam membuat coding automation, misalkan kita bisa bertanya cara menyusun kode menjadi lebih DRY (jangan mengulangi kodemu), konsultasi OOP ataupun library yang bisa membantu

### Selera

Saya adalah termasuk yang senang menggunakan bahasa pemrograman yang dinamis seperti [PHP](#INTERNAL_LINK#/post/null "https://books.goalkicker.com//PHPBook/"), [ruby](#INTERNAL_LINK#/post/null "https://books.goalkicker.com/RubyBook/"), [python](#INTERNAL_LINK#/post/null "https://books.goalkicker.com//PythonBook/") ataupun [javascript](#INTERNAL_LINK#/post/null "https://books.goalkicker.com//JavaScriptBook/") ketimbang menggunakan Java atau C#, karena menurut saya bahasa java/C# terlalu ribet cara koding nya, lebih banyak code ceremony style dalam penulisan sysntax nya, yang mengintimidasi saya bahwa kode yang dituliskan menjadi ribet dan panjang, ditambah lagi waktu compile kode yang bisa sekitar 5 detik cuma untuk menunggu kodenya menjadi executable, dan ini membuat saya merasa diperlambat sih :P

---

<br>Berdasarkan pengalaman saya mempelajari automation ini (dalam konteks selenium) adalah dengan mencoba beberapa bahasa pemrograman langsung, misalkan saya pernah mencoba ruby, java, PHP, dan javaScript untuk membuat kerangka automation suatu website yang sama, banyak loh framework mature dan banyak dukungan dari komunitasnya seperti [capybara](#INTERNAL_LINK#/post/null "https://github.com/teamcapybara/capybara") di ruby, [serenity](#INTERNAL_LINK#/post/null "https://www.thucydides.info/") di java, [codeception](#INTERNAL_LINK#/post/null "https://codeception.com/") di PHP, [robotframework](#INTERNAL_LINK#/post/null "https://robotframework.org/") di python dan makin banyak lagi pilihan di javascript, bahkan yang sering menjadi topik hangat di komunitas [ISQA](#INTERNAL_LINK#/post/null "https://www.meetup.com/Indonesia-Software-Quality-Assurance/") adalah [Katalon Studio](#INTERNAL_LINK#/post/null "https://www.katalon.com/") dengan bahasa groovy nya.

Sehingga kita bisa mempelajari ekosistem darisemua bahasa pemrograman dan framework tadi, pada akhirnya akan membuat kita menjadi lebih paham kekurangan kelebihan masing-masing dan menjadikan generalist yang lebih baik lagi.

<figure class="post__image"><img alt="" height="427" loading="lazy" sizes="100vw" src="/media/posts/15/athletes-black-and-white-black-and-white-34514.jpg" srcset="/media/posts/15/responsive/athletes-black-and-white-black-and-white-34514-xs.jpg 300w, /media/posts/15/responsive/athletes-black-and-white-black-and-white-34514-sm.jpg 480w, /media/posts/15/responsive/athletes-black-and-white-black-and-white-34514-md.jpg 768w, /media/posts/15/responsive/athletes-black-and-white-black-and-white-34514-lg.jpg 1024w, /media/posts/15/responsive/athletes-black-and-white-black-and-white-34514-xl.jpg 1360w, /media/posts/15/responsive/athletes-black-and-white-black-and-white-34514-2xl.jpg 1600w" width="640"/></figure>

Jika ingin langsung terjun mempelajari automation, mungkin saran saya adalah:

- Pilih tools atau library yang mudah dipelajari, bisa dari dokumentasi resminya, komunitas, ataupun banyak bertebaran artikel ketika di gugling
- Lihat apakah tools tersebut ada rutin rilis feature, jangan gunakan tools yang sudah ditinggalkan dan tidak ada rilis lagi kedepannya, contohnya seperti calabash
- Hal-hal teknis yang perlu diperhatikan juga seperti:
    - Library sudah stabil dan aktif dikembangkan, bisa mengikuti rilis selenium misalkan
    - Kemampuan unique test runner nya seperti junit, testNG, rspec
    - Bagaimana scalable test nya nanti, bisa mudah di buat parallel
    - Penulisan kode yang elegan
    - Mudah dan fleksibel saat dijalankan lewat command line
- Pelajari yang paling mudah dan pahami konsep automation nya, bisa mulai dari Katalon Studio (tapi untuk jangka panjang, saran saya jangan gunakan recordernya)
- Jika sudah paham katalon studio dengan kemudahan graphical user interface nya, dan paham bagaimana automation bekerja (selector, interaction, expectation/assertion) coba pelajari automation dengan code langsung
- Jika automation website saya akan memilih ruby dengan capybara nya (bisa pakai cucumber juga)
- Jika automation mobile apps saya akan memilih java-appium karena tutorialnya banyak dan bisa multiplatform (tapi lebih cepat espresso dan xcuitest sih)
- Jika autoamtion API saya akan memilih postman/newman dengan javascript nya
