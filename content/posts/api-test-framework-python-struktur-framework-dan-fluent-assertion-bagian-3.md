+++
title = "Struktur Framework dan Fluent Assertion - API Test Framework Python (Bagian 3)"
date = 2021-01-29T13:00:00+04:00
updated = 2021-08-08T13:36:28+04:00
tags = ["automation-python", "tutorials"]
description = "Hi Kawan 👋, Gimana mudah kan belajar bikin API automation dengan python? tentunya,, di kesempatan ini kita akan belajar lebih lanjut dengan pytest dan menggunakan library tambahan (lagi) agar test kita lebih mudah dibaca dan dipahami dengan bantuan fluent assertion Artikel ini adalah salah satu…"
cover = "/media/website/whois-fachrulch.png"
cover_alt = "penulis"
cover_caption = "Fachrul Choliluddin"
og_image = "/media/website/profile-newletter-3.png"
+++

Hi Kawan 👋,

Gimana mudah kan belajar bikin API automation dengan python? tentunya,, di kesempatan ini kita akan belajar lebih lanjut dengan pytest dan menggunakan library tambahan (lagi) agar test kita lebih mudah dibaca dan dipahami dengan bantuan fluent assertion

Artikel ini adalah salah satu dari rangkaian tutorial cara membuat RestfulAPI Test Framework dengan bahasa pemrograman Python, artikel lainnya bisa kamu cekidot disini ya:

- [Pelajaran 1:  Setup dan pengenalan HTTP requests](/yuk-belajar-cara-membuat-api-test-automation-framework-python-bagian-1/)
- [Pelajaran 2: Pengujian dengan assert dan pytest](/api-test-automation-framework-python-bagian-2/)
- [Pelajaran 3: Struktur awal test framework dan library fluent assertion](/api-test-framework-python-struktur-framework-dan-fluent-assertion-bagian-3/)
- [Pelajaran 4: Refaktoring dan base helper](/refactoring-dan-base-api-api-test-framework-python-bagian-4/)
- [Pelajaran 5: Reporting](/reporting-api-test-framework-python-bagian-5/)
- [Extra: Penambahan schema validation dan running test in parallel](/json-schema-validation-api-test-framework-python-extra-bonus/)

---

## Kenapa kita perlu fluent assertion?

Karena assert terlalu sederhana, dia hanya bisa mengevaluasi value True/False saja,, (eh tapi pada dasarnya semua juga sama sih mau pake library ini pun gitu, hahaha)

Maksudnya ada banyak fitur tambahan dari library ini, bisa dilihat dokumentasinya di web resminya [https://github.com/assertpy/assertpy](https://github.com/assertpy/assertpy) dan secara kode pun akan mudah dibaca dan dipahami kok

Install library ini dengan command \`pip install assertpy\`

## Mengakses API method POST

Oke kali ini kita ga akan pake GET airports lagi sebagai contoh, tapi kita akan menggunakan contoh API POST untuk menghitung jarak antar airports ya, kurang lebih kode nya akan seperti ini

```python
import requests
from assertpy import assert_that


def test_calculate_distance():
    payload = {
        "from": "LAE",
        "to": "NRT"
    }
    response = requests.post("https://airportgap.dev-tester.com/api/airports/distance", data=payload)
    data = response.json().get("data")
    assert_that(data["type"]).is_equal_to("airport_distance")
    assert_that(data["attributes"]).is_not_empty()
    assert_that(data).has_id("LAE-NRT")
    assert_that(data["attributes"]["kilometers"]).is_equal_to(4753.834755437252)
```

Penjelasan kode, yang beda aja dari artikel sebelumnya ya hehe:

- from assertpy import assert\_that ==> melakukan import function assert\_that yang berada pada module library assertpy
- payload = {} ==> deklarasi variable dengan tipe data dictionary
- response = requests.post(&lt;url>, data) ==> nah seperti pada umumnya method POST adalah untuk mengirim data, maka kita akan mengirim data payload secara programatis dengan menggunakan argument tambahan data=payload
- assert\_that(&lt;condition>).is\_equal\_to(&lt;expected result>) ==> penggunaan assertpy library untuk assertion, lihatlah kodenya jadi mudah dipahami bukan?

---

## Struktur Framework pytest

Pada umumnya kode pengujian pada sebuah project python terletak pada directory \`test\` atau \`tests\` jadi untuk standarisasi kita akan mengikuti kaidah ini, sehingga bentuk project test kita menjadi seperti ini

```
.
└── test
 ├── airport_test.py
 └── favorite_test.py
```

Oia, sebagai convention pun kita perlu menamakan file kita dengan \_test.py agar pytest bisa menemukan file mana saja yang akan dieksekusi sebagai test

Kita membagi dua file utnuk pengujian api yang berkaitan dengan airport dan favorite ke dalam file yang terpisah agar mudah dipahami, jadi semua test yang berkaitan dengan module favorite pasti terletak di favorite\_test.py jadi test kita pun bisa menjadi sebuah dokumentasi yang baik

Kurang lebih contoh akhir dari file airport\_test.py adalah seperti ini

```python
import requests
from assertpy import assert_that

BASE_URL = "https://airportgap.dev-tester.com/api"


def test_get_all_airports():
    response = requests.get(f'{BASE_URL}/airports')
    data = response.json().get('data')

    assert_that(response.status_code).is_equal_to(200)
    assert_that(data).is_greater_than_or_equal_to(5)


def test_get_airports_by_id():
    # arrange/GIVEN
    airport_id = "LAE"
    # action/WHEN
    response = requests.get(f'{BASE_URL}/airports/{airport_id}')
    data = response.json().get('data')
    data_airport = data["attributes"]
    # assertion/THEN
    assert_that(response.status_code).is_equal_to(200)
    assert_that(data_airport["name"]).is_equal_to("Nadzab Airport")


def test_get_not_found_airport():
    airport_id = "NOTFOUND"
    response = requests.get(f'{BASE_URL}/airports/{airport_id}')
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.json()).contains_key("errors")
    assert_that(response.text).contains("The page you requested could not be found")


def test_calculate_distance():
    payload = {
        "from": "LAE",
        "to": "NRT"
    }
    response = requests.post("https://airportgap.dev-tester.com/api/airports/distance", data=payload)
    data = response.json().get("data")
    assert_that(data["type"]).is_equal_to("airport_distance")
    assert_that(data["attributes"]).is_not_empty()
    assert_that(data).has_id("LAE-NRT")
    assert_that(data["attributes"]["kilometers"]).is_equal_to(4753.834755437252)
```

dan favorite\_test.py

```python
from datetime import datetime

import requests
from assertpy import assert_that

BASE_URL = "https://airportgap.dev-tester.com/api"


def get_token(email, password):
    return requests.post(BASE_URL + "/tokens", data={
        "email": email,
        "password": password
    })


def get_my_favorite_airport(token):
    header = {
        "Authorization": f"Token {token}"
    }
    return requests.get(BASE_URL + "/favorites", headers=header)


def test_token():
    token = get_token(email="naruto@mailinator.com", password="shuriken")
    assert_that(token.status_code).is_equal_to(200)
    assert_that(token.json()).contains_key("token")
    assert_that(token.json().get("token")).is_not_empty()


def test_get_favorite():
    give_me_token = get_token(email="naruto@mailinator.com", password="shuriken")
    token = give_me_token.json().get("token")
    header = {
        "Authorization": f"Token {token}"
    }
    response = requests.get(BASE_URL + "/favorites", headers=header)
    data = response.json().get("data")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(data).is_greater_than_or_equal_to(1)


def test_add_new_favorite():
    """
    Since the data is hardcoded, then it was not idempotent/repeatable
    This test will failed, if NRT already in my favorite list
    Need to remove after test teardown
    """
    give_me_token = get_token(email="naruto@mailinator.com", password="shuriken")
    token = give_me_token.json().get("token")

    before_add = get_my_favorite_airport(token)
    data_before = before_add.json().get("data")
    assert_that(before_add.text).does_not_contain("NRT")

    new_airport = {
        "airport_id": "NRT",
        "note": "I like Narita"
    }

    header = {
        "Authorization": f"Token {token}"
    }

    response = requests.post(BASE_URL + "/favorites", headers=header, data=new_airport)
    assert_that(response.status_code).is_equal_to(201)
    response_data = response.json().get("data")
    assert_that(response_data["attributes"]["airport"]["iata"]).is_equal_to(new_airport["airport_id"])
    assert_that(response_data["attributes"]["note"]).is_equal_to(new_airport["note"])

    after_add = get_my_favorite_airport(token)
    data_after = after_add.json().get("data")
    assert_that(len(data_after)).is_greater_than(len(data_before))
    assert_that(after_add.text).contains(new_airport["note"])


def test_update_favorite_note():
    give_me_token = get_token(email="naruto@mailinator.com", password="shuriken")
    token = give_me_token.json().get("token")

    before_add = get_my_favorite_airport(token)
    data_before = before_add.json().get("data")

    assert_that(len(data_before)).is_greater_than(0)
    id_airport_to_modify = data_before[0]["id"]

    header = {
        "Authorization": f"Token {token}"
    }

    # Add dynamic unique string with a timestamp
    new_note = {
        "note": f"The note for ID:{id_airport_to_modify} is changed at time: {datetime.now()} "
    }

    response = requests.patch(f"{BASE_URL}/favorites/{id_airport_to_modify}", headers=header, data=new_note)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.text).contains(new_note["note"])

    after_add = get_my_favorite_airport(token)
    data_after = after_add.json().get("data")
    for airport_data in data_after:
        if airport_data["id"] == id_airport_to_modify:
            print(f"Found the modified airport {id_airport_to_modify}")
            print("\nHere is the check for specific airport in an array data")
            assert_that(airport_data["attributes"]["note"]).is_equal_to(new_note["note"])


def test_delete_favorite():
    give_me_token = get_token(email="naruto@mailinator.com", password="shuriken")
    token = give_me_token.json().get("token")

    before_add = get_my_favorite_airport(token)
    data_before = before_add.json().get("data")

    assert_that(len(data_before)).is_greater_than(0)
    id_airport_to_delete = data_before[0]["id"]

    header = {
        "Authorization": f"Token {token}"
    }

    response = requests.delete(f"{BASE_URL}/favorites/{id_airport_to_delete}", headers=header)
    assert_that(response.status_code).is_equal_to(204)
    after_delete = get_my_favorite_airport(token)
    data_after = after_delete.json().get("data")
    assert_that(len(data_after)).is_less_than(len(data_before))
```

Penjelasan kode? hmm sepertinya akan sangat panjang, nanti akan saya jelaskan pada video sepertinya agar lebih runut ehehe, klo nulis keknya panjang ehehe

## Bagaimana cara menjalankan kode dengan pytest?

Klo mau menjalankan satu satu sih bisa seperti cara sebelumnya \` pytest test/airport\_test.py\`

Tapi klo mau menjalankan seluruh test, karena sudah sesuai convention (dalam folder test, file sudah bearakhiran xxx\_test.py dan method berawalan test\_xxx) sebenarnya cukup menggunakan \`pytest\` saja tanpa embel embel loh

---

Cukup sekian tutorial kali ini, silakan teman-teman pelajari approach saya dalam menulis kode di atas, apakah sudah test nya seperti itu? atau kamu mungkin punya assertion yang bisa jadi ditambahkan juga, silakan tulis di kolom komentar di bawah ya!

Berikutnya kita akan bahas, bagaimana kode ini bisa kita refactor dengan menggunakan class Base API ya

Salam!

Selengkapnya ada pula di video live coding berikut ini:

<div class="post__iframe"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" frameborder="0" height="315" loading="lazy" src="https://www.youtube.com/embed/8XcDzl5vVBU" width="560"></iframe></div>
