+++
title = "Today I learn: April 2019"
date = 2019-04-26T14:15:00+04:00
updated = 2019-04-26T14:20:04+04:00
tags = ["today-i-learned"]
description = "22/04/2019: Bagaimana cara debug HTTP request? gimana cara kita tau ada yang salah di HTTP request kita sampe return error 400 Bad request. kalo bikin API request pake postman sih gampang, buat liat request yang dibuat udah bener apa ngak, tinggal buka developer console di…"
cover = "/media/website/whois-fachrulch.png"
cover_alt = "penulis"
cover_caption = "Fachrul Choliluddin"
og_image = "/media/website/profile-newletter-3.png"
+++

## 22/04/2019: Bagaimana cara debug HTTP request?

gimana cara kita tau ada yang salah di HTTP request kita sampe return error 400 Bad request. kalo bikin API request pake postman sih gampang, buat liat request yang dibuat udah bener apa ngak, tinggal buka developer console di postman nya, kita bisa inspect request-response nya, tapi akan sangat sulit kalo kita bikin request ini programatically pake bahasa pemrograman, karena request nya sekejap aja langsung?

Solusinya:

`ruby -rsocket -e "trap('SIGINT') { exit }; Socket.tcp_server_loop(8080) { |s,_| puts s.readpartial(1024); puts; s.puts 'HTTP/1.1 200'; s.close }`

kode diatas akan buat program kecil via ruby yang akan listen port 8080, kita bisa hit http://localhost:8080 buat lihat apakah request kita sudah benar

<figure class="post__image"><img alt="" height="580" loading="lazy" sizes="100vw" src="/media/posts/12/Screen-Shot-2019-04-26-at-17.14.00.png" srcset="/media/posts/12/responsive/Screen-Shot-2019-04-26-at-17.14.00-xs.png 300w, /media/posts/12/responsive/Screen-Shot-2019-04-26-at-17.14.00-sm.png 480w, /media/posts/12/responsive/Screen-Shot-2019-04-26-at-17.14.00-md.png 768w, /media/posts/12/responsive/Screen-Shot-2019-04-26-at-17.14.00-lg.png 1024w, /media/posts/12/responsive/Screen-Shot-2019-04-26-at-17.14.00-xl.png 1360w, /media/posts/12/responsive/Screen-Shot-2019-04-26-at-17.14.00-2xl.png 1600w" width="2010"/></figure>

sumber: [https://www.rubyguides.com/2018/08/ruby-http-request/](https://www.rubyguides.com/2018/08/ruby-http-request/)

---

## 26/05/2018: Cara biar Cucumber Ruby ga langsung fail ketika assert / expect

klo pake expect biasanya tiap ga terpenuhi langsung error, nah padahal kan bisa jadi di halaman itu kita perlu banyak cek sekaligus, biar sekalian dibenerin gitu. gimana caranya?

`aggregate_failures "testing response" do  expect(response.status).to eq(200)  expect(response.headers["Content-Type"]).to eq("application/json")  expect(response.body).to eq('{"message":"Success"}')end`

sumber: [https://www.rubydoc.info/github/rspec/rspec-expectations/RSpec%2FMatchers:aggregate\_failures](https://www.rubydoc.info/github/rspec/rspec-expectations/RSpec%2FMatchers:aggregate_failures)
