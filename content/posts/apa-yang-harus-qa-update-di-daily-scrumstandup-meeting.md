+++
title = "Apa yang Harus QA Update di Daily Scrum/Standup Meeting?"
date = 2023-03-12T16:27:00+04:00
updated = 2023-03-12T16:31:57+04:00
tags = ["meeting", "agile", "teamwork", "tutorials"]
description = "Ada beberapa tips gimana caranya biar daily scrum standup bisa menarik bagi seorang QA software tester nih"
cover = "/media/posts/54/memikirqan-1.jpg"
cover_caption = "apa yang bisa software tester update di daily scrum"
+++

Apakah kamu suka bingung mau update apa ya buat standup meeting? Masih ngerjain yang sama kayak hari kemarin?

### Apaan tuh daily standup meeting?

Akan semakin panjang kalau saya bahas disini, ada artikel medium yang menggambarkan persis seperti apa itu daily scrum/standup meeting disini:

<div class="graf graf--mixtapeEmbed"><a class="markup--anchor markup--mixtapeEmbed-anchor" data-href="https://medium.com/belajar-scrum/kenalan-dengan-daily-scrum-e7a35dae51ff" href="https://medium.com/belajar-scrum/kenalan-dengan-daily-scrum-e7a35dae51ff" title="https://medium.com/belajar-scrum/kenalan-dengan-daily-scrum-e7a35dae51ff"><strong class="markup--strong markup--mixtapeEmbed-strong">Daily Scrum untuk Komunikasi Efektif dalam Tim</strong><br/><em class="markup--em markup--mixtapeEmbed-em">Apa praktik dalam Scrum yang membuat komunikasi Development Team tetap terjaga dengan baik selama kerja pengembangan…</em>medium.com</a><a class="js-mixtapeImage mixtapeImage u-ignoreBlock" data-media-id="1c917ec926be14867a7afdca90fe84c9" data-thumbnail-img-id="1*QD1Qrje-1PVybwXLs4mRcQ.png" href="https://medium.com/belajar-scrum/kenalan-dengan-daily-scrum-e7a35dae51ff"></a></div>

Umumnya saat daily scrum tim akan menjawab pertanyaan template seperti:

<ul class="postList"><li class="graf graf--li">Apa yang dilakukan dari Daily Scrum sebelumnya sampai saat ini?</li><li class="graf graf--li">Apa yang akan dilakukan hari ini sampai Daily Scrum berikutnya?</li><li class="graf graf--li">Apakah ada kesulitan/hambatan untuk mencapai tujuan Sprint?</li><li class="graf graf--li">(opsional) Siapa seseorang yang bisa diminta bantuannya?</li></ul>

Tapi seringkali saya merasakan daily scrum ini seperti meeting basi dan buang waktu karena ada beberapa kesalahan yang umumnya terjadi pada tim

---

Oia gw juga bikin versio videonya di youtube NgeTest bareng Fachrul ya:

<figure class="post__video"><iframe allowfullscreen="allowfullscreen" data-mce-fragment="1" height="314" loading="lazy" src="https://www.youtube.com/embed/qBw0nfT2Iwc" width="560"></iframe></figure>

### Apa yang harus QA update pada tim saat Daily Scrum

Ada banyak, bisa jadi tergantung dari timeline projectnya, tapi sebelum saya bahas lebih jauh, kita coba dulu bedah kesalahan umum yang sering terjadi pada tim scrum, dan QA bisa berperan untuk meningkatkan kualitas meeting daily scrum/daily standup meeting ini juga loh

### Kesalahan yang sering terjadi pada Daily Scrum

Beberapa hal berikut ini bikin daily scrum menjadi membosankan dan tidak menarik, diantaranya karena masalah:

<ul class="postList"><li class="graf graf--li">jumlah peserta meeting terlalu banyak, jadi tiap orang dapet jatah yang singkat</li><li class="graf graf--li">ga nyimak update dari teman lain, sibuk mikirin “duh gw mau update apa ya”</li><li class="graf graf--li">justifikasi kesibukan, “gw tuh udah ngerjain banyak kemaren, hari ini banyak banget tugas, gada blocker, gw bisa ngerjain sendiri”</li></ul>

Apakah diantara poin di atas tadi, ada yang kejadian juga di tim kamu?

### Gimana Cara Update Daily Scrum yang Baik

Interaktif dan engagment tinggi adalah tanda utama kalau kamu udah menjalankan daily scrum yang baik, plis jangan sampe update cuma 10 detik di update ini, berasa hambar gimana gitu ya kan!

Padahal tujuan adanya rapat singkat ini kan bagus banget, diantaranya kayak:

<ul class="postList"><li class="graf graf--li">Informasi perkembangan terkini fitur yang sedang dikerjakan</li><li class="graf graf--li">Kesempatan untuk gotong royong menyelesaikan masalah</li><li class="graf graf--li">Memperjuangkan sprint goal</li><li class="graf graf--li">Transparansi</li><li class="graf graf--li">Prioritas yang jelas</li></ul>

---

Okey kita akan bahas dari sudut pandang “pendengar” dan “pembicara” di standup ini ya

### Sebagai Pembicara

Sebagai QA kita bisa membicarakan banyak hal loh sebenernya, saya bagi lagi ke dalam beberapa bagian Timeline ya:

#### Diawal Sprint

Biasanya diawal sprint belum ada story yang bisa di test, jadi disini kita bisa update seperti:

<ul class="postList"><li>insigt dari rilis sebelumnya<ul class="postList"><li>update persentase rollout sekarang udah di berapa persen</li><li>bugs apa aja yang kejadian (crash)</li><li>adopsi user udah berapa banyak update di versi baru</li><li>apakah perlu direncanakan hotfix/patch dari issue baru</li></ul></li><li class="graf graf--li">review requirement document/design</li><li class="graf graf--li">bikin test scenario, ataupun bikin test plan buat fitur tsb</li><li class="graf graf--li">hasil investigasi production bugs</li><li class="graf graf--li">penambahan test case automation</li><li class="graf graf--li">kolaborasi dengan tim lain </li><li class="graf graf--li">belajar module lain yang ada kena dampak perubahan fitur baru nanti</li><li class="graf graf--li">persiapan test data untuk fitur</li></ul>

dan perlu diingat siasat yang satu ini agar lebih menarik:

<blockquote class="graf graf--blockquote">mention nama teman agar mendapatkan perhatiannya saat kita memberikan update</blockquote>

Contoh:

<ul class="postList"><li class="graf graf--li">Kayaknya gw perlu bantuan mas Ahmad deh buat copy data production biar nanti test fitur A lebih gampang</li><li class="graf graf--li">Klo mas Kamil ga sibuk abis makan siang, gw mau ngajak pairing soal temuan production bugs, gw udah/belum bisa reproduce bugsnya</li><li class="graf graf--li">Mas Bagus, Gw udah siapin test data buat nanti bagian fitur A, jadi klo ada yang perlu buat test implementasi koding, pake aja dulu silakan</li><li class="graf graf--li">Ada yang bisa bantu gw ga nih, ada issue di test automation soal element nya tiba-tiba selectornya ganti sendiri</li></ul>

#### Pertengahan Sprint

Biasanya ada feature testing yang lagi dikerjain, kita bisa update progress pengerjaan tiket di board Jira/Scrum, issue yang ditemukan, edge case apa yang perlu di test, contoh:

- Kemarin ada test tiket JIRA-150 soal (contoh ya) pembayaran QRIS, happy flow nya udah, nah hari ini mau lanjut test negative cases dan edge cases, kayak lagi scan internet mati, saldonya kepotong service laen sebelum confirm, dst
- Kemarin test tiket JIRA-150, tapi ada bugs nya nih Mas Kunto, pas pembayaran QRIS di android 7.0, keknya libaray nya ga kompatible
- Automation test nya failed pagi ini, keknya karena ada changes yang baru di deploy, mo liat dlu ini failed karena valid new bugs, atau test nya perlu di adjust dengan accepatance criteria baru
- Hari ini mau prepare data testing buat tiket JIRA-150, keknya perlu beberapa persona user yang harus di test, ada BE dev yang bisa bantu buat replicate producetion data kah?

#### Diakhir Sprint

Bisa followup issue apa aja yang masih open, dan jadi prioritas sebelum rilis ke real user, trus juga dokumen apa aja yang perlu disiapin dan rencana rilisnya kapan dan persentase rollout

---

### Sebagai Pendengar

Daily scrum tentu akan bahas mengenai deliverable task dalam satu sprint, biasanya diawal sprint sudah dijelaskan sprint goalsnya apa, story dalam sprint, nah pada saat standup ini kesempatan kita untuk mengecek (dalam bentuk pertanyaan) implementasi yang dilakukan oleh Dev, approach apa yang jadinya diambil.

Jadi perlu disimak update dari tim Developer, pastikan mereka memberikan gambaran implementasi story tersebut, dengan asumsi kamu juga udah baca story tersebut, dan acceptance criteria sudah dibuat, tentu kamu akan memiliki gambaran fiturnya akan jadi seperti apa, jika kamu melihat peluang untuk bertanya silakan tanya, agar dev bisa update kepada yang lain juga untuk menghindari surprise diakhir, ataupun beberapa.

Contoh:

- Mas Kunto, mau tanya soal implementasi scan QRIS baru itu jadinya lo mau pake library baru? apakah ada impact ke SDK lama? ada refactor ke modul lama?
- Mba Ani, acceptance criteria di tiket JIRA-150 keknya kurang cover case klo usernya suspend deh, itu di handle di frontend apa backend buat validasinya?

#### Tambahan

Catat poin penting tiap harinya, buat bekal nanti retrospective meeting mau bahas apa, misal bisa dicatet: Si A explore librarynya kelamaan sampe 4 hari, harusnya senior bisa bantuk biar lebih cepet 😅, dkk. biasanya klo dipikirin saat persis sebelum retrospective suka ga ke recall kejadian buruk sehari-hari itu
