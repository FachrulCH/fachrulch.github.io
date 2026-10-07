+++
title = "Perintah Git yang berguna tapi jarang yang tahu"
date = 2020-04-26T11:44:00+04:00
updated = 2020-05-06T12:44:32+04:00
tags = ["tutorials"]
description = "Aneka perintah GIT yang berguna tapi ga banyak yang tahu"
cover = "/media/posts/29/coding-computer-data-depth-of-field-577585.jpg"
cover_caption = "Perintah GIT Photo by Kevin Ku from Pexels"
+++

GIT? tools andalan dalam kolaborasi pengembangan perangkat lunak yang banyak dari kita sudah familiar dan bahkan menggunakan nya sehari-hari. Tapi buat saya pribadi seringkali cuma pake git commit, git push, git merge doank ahaha, ada beberapa command yg penting dan berguna sebenernya yang bisa sangat memudahkan kita dan ternyata banyak orang yang tahu juga

## Mengurutkan Branch berdasarkan tanggal

```bash
git branch --sort=-committerdate 
```

## Pindah ke Branch sebelumnya

```bash
git checkout -
```

## Menampilkan informasi komit terakhir dari semua branch

```bash
git branch -v
git branch -vv  # kalo mau sama informasi upstream remote branch nya sekalian
```

## Ambil perubahan suatu file di branch lain

```bash
git checkout feature/branch-lain -- fileyangkitamau.txt
```

## Melihat status Git dengan lebih ringkas

kadang kita cuma menjalankan command \`git status\` untuk melihat file apa aja yang mengalami perubahan atau penambahan files. sebagai alternatif untuk informasi perubahan files dengan lebih ringkas kita bisa menjalankan:

```bash
git status -sb
```

## Menelusuri file yang hilang

```bash
git log -- missing_file.txt
```

## Siapa Commiter paling rajin banyak

Buat lucu-lucuan aja di urutin siapa commiter paling banyak

```bash
git shortlog -sn --all --no-merges
```

atau klo mau lebih spesifik lagi bisa ditambahin tempo nya

```bash
git shortlog -sn --since='10 weeks' --until='2 weeks'
```

## Siapa nih yg ubah file dan line tertentu

```bash
git blame -L5,10 .gitlab-ci.yml
```

## Daripada nunjukin line yang berubah mending minta tunjukin kata yang berubah

```bash
git diff --word-diff
```

## Melihat branch mana saja yang akhir-akhir ini kita kerjakan

Kadang terlalu banyak lompat branch jadi suka tersesat sendiri dan bingung mau mulai darimana

```bash
git for-each-ref --count=10 --sort=-committerdate refs/heads/ --format="%(refname:short)"
```

kalo terlalu ribet hapal nya tinggal bikin alias jadi \`git recent\` sih

## Lagi pada ngerjain apaan sih?

buat tim leader biasanya penting untuk ngecek sesekali dari apa yang dikerjain tim kita di repo, sebenernya bisa aja liat di git commit di gitlab/github nya sih, tapi klo lagi di terminal bisa langsung di eksekusi aja command ini

```bash
git log --all --oneline --no-merges
```

atau klo mau ada pembatas waktu bisa ditambahin argument since: days/weeks

```bash
git log --all --since='3 days' --oneline --no-merges
```

Trus klo mau cek orang tertentu bisa pake gini

```bash
git log --all --oneline --no-merges --author=<email address>
```

```bash
git log --since=00:00:00 --all --no-merges --oneline --author=<email address>
```

## Melihat logs yang kompleks dengan grafis

```bash
git log --graph --all --decorate --stat --date=iso
```
