[app]
title = NABZ Market Pulse
package.name = currencyrates
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.2
requirements = python3==3.11.5,hostpython3==3.11.5,kivy==2.3.0

android.permissions = INTERNET
android.ndk = 25b
android.api = 33
android.minapi = 24

[buildozer]
log_level = 2
warn_on_root = 1
