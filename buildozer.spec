[app]
title = NABZ Market Pulse
package.name = currencyrates
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.2
requirements = python3,kivy==2.3.0,cython==0.29.36

android.permissions = INTERNET
android.ndk = 25b
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
