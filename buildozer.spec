[app]
title = دفتر الزهوب
package.name = debtbook
package.domain = com.mohammed.debtbook

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json

version = 1.0.0

requirements = python3,kivy==2.3.0,pillow,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1