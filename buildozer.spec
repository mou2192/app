[app]
title = دفتر الزهوب
package.name = debtbook
package.domain = com.mohammed.debtbook

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json

version = 1.0.0
icon.filename = icon.png
presplash.filename = icon.png
requirements = python3,kivy==2.3.1,pillow,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.accept_sdk_license = True

p4a.commit = 957a3e5f8c270f7aa648ba185e5a68c1077a798d

[buildozer]
log_level = 2
warn_on_root = 1
