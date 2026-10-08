+++
title = "Catat ini! berbagai command ADB yang berguna untuk automation tester"
date = 2020-04-27T12:24:00+04:00
updated = 2020-06-12T11:51:23+04:00
tags = ["testergadungan", "tutorials"]
description = "command ADB, android debug bride yang berguna untuk QA automation tester"
cover = "/media/posts/30/ADB.png"
+++

Hallo Para Penguji Aplikasi Digital!

Pada saat saya mengembangkan kode automation untuk android, seringkali saya menemukan command penting dan berguna dalam membantu automation code saya dan saya simpan di snippet microsoft oneNote, dan setelah dipikir-pikir sangat mubazir kalo catatan itu saya simpan sendiri, jadi pada kesempatan kali ini akan saya tuliskan disini command Android Debug Bridge (ADB) apa saja yang bisa membantu pengujian kita

## Buka kunci Ponsel

```bash
adb shell input keyevent  # idupin HP
adb shell input text yourpasscode  # Masukin PIN 
adb shell input keyevent KEYCODE_ENTER   # tekan enter
```

## Toggle status bar

```bash
#pull status bar
adb shell service call statusbar 1
#collapse status bar
adb shell service call statusbar 2
```

## Buka/tutup app

```bash
#open app : 
adb shell monkey -p id.fachrul.packagename 1

# Open gmail 
adb shell monkey -p com.google.android.gm 1
#close app :
adb shell am force-stop packagename
# Close gmail 
adb shell am force-stop com.google.android.gm
```

## Tap di aplikasi

```shell
adb shell input tap x y
```

nah \`x y\` itu koordinat sumbu X dan Y, gimana cara dapetinnya?

```shell
# dump the current screen ui
adb shell uiautomator dump
# copy the xml file to computer 
adb pull sdcard/window_dump.xml ~/Desktop/
# atau gini juga bisa
adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') /sdcard/window_dump.xml
```

trus cek attribut "bounds" di element yang kita mau buat dapetin koordinatnya, hint: bisa juga sih dapetin koordinat dari uiautomatorviewer :D

## Install aplikasi langsung

```shell
adb install -r namafile.apk
```

bisa ditambahin argument

```shell
adb -d = untuk device, 
adb -e = utk emulator, 
adb -s = untuk ke serial number tertentu
```

atau klo mau sekaligus install apk di banyak devices

```shell
alias apkinstall="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X install -r $1"

# Penggunaannya Install an apk on all devices
apkinstall ~/Downloads/MyAppRelease.apk  

# atau klo cuma mau copy files apk nya doank
adb push <lokasi file path> /sdcard/
```

## Hapus aplikasi

```shell-session
adb shell pm uninstall com.example.MyApp     
adb shell pm clear id.fachrul.package // Deletes all data associated with a package.
```

## Buka aktivity langsung

```shell-session
adb shell am start -W -n com.gojek.life/com.gojek.golife.presentation.feature.LifeSplashActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000
```

Apa nama activity sekarang ini (lagi dibuka/focus)

```shell-session
adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp' 
```

## Monkey test

```shell
adb shell monkey -p <nama package> -v --pct-syskeys 0 3000

adb shell monkey -p com.myAppPackage -v 10000 -s 100 // monkey tool is generating 10.000 random events on the real device
```

## Filter adb log dengan lebih indah

```shell
pidcat <nama package>
```

nah pidcat ini adalah aplikasi tambahan based on python script, bisa di install mengikuti petunjuk [disini](https://github.com/JakeWharton/pidcat/blob/master/README.md)

## Hapus log device

```shell
adb logcat -c
```

## Ambil bug report berupa informasi dari device, dumpstate, dumpsys dan logcat output

```css
adb bugreport > path_file_nya
adb logcat -b crash 
```

## Ambil screenshoot

```
adb exec-out screencap -p > <nama_sshot>.png
```

## Open deeplink

`adb shell am start -a android.intent.action.VIEW -d "schema://link"`

## Reset permissions

```shell
adb shell pm reset-permissions -p your.app.package
```

## Kasih permission

```shell-session
adb shell pm grant your.app.package
```

## Key event

```shell-session
adb shell input keyevent 3 // Home btn
adb shell input keyevent 4 // Back btn

adb shell input keyevent 5 // Call

adb shell input keyevent 6 // End call

adb shell input keyevent 26  // Turn Android device ON and OFF. It will toggle device to on/off status.

adb shell input keyevent 27 // Camera

adb shell input keyevent 64 // Open browser

adb shell input keyevent 66 // Enter

adb shell input keyevent 67 // Delete (backspace)

adb shell input keyevent 207 // Contacts

adb shell input keyevent 220 / 221 // Brightness down/up

adb shell input keyevent 277 / 278 /279 // Cut/Copy/Paste

// https://developer.android.com/reference/android/view/KeyEvent.html
```

Ambil serial dari connected device

```shell-session
adb devices | tail -n +2 
```

## Emulator

```
emulator -avd <nama emulatornya> -netdelay none -netspeed full 
```

## Cara menampilkan screen android di Windows/mac/linux (cocok buat presentasi)

Bisa menggunakan aplikasi [Scrcpy](https://github.com/Genymobile/scrcpy) aplikasi ini open source jadi bisa menjadi alternatif kamu yang biasa menggunakan Vysor, klo pake mac bisa langsung instal via \`brew install scrcpy\` trus jalanin nya tinggal jalanin command \`scrcpy\` atau klo mau lihat dia bisa ngapain aja bisa cekidot \`scrcpy --help\`

```
scrcpy --help
# mulai mirroring android, tapi tampilin juga lokasi sentuhan
scrcpy -t
# mirroring android sambil direkam
scrcpy -r coba_health.mp4
# klo ada lebih dari satu, bisa konek sesuai dengan serial device nya
scrcpy -s serial_1234
```
