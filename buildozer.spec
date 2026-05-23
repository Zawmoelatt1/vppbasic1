[app]
p4a.source_dir = /root/vppbasic/python-for-android

# (str) Title of your application
version = 1.0
title = ZM4

# (str) Package name
package.name = zm4app

# (str) Package domain (needed for android packaging)
package.domain = org.zmlatt

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (str) Android loglevel (0 = error, 1 = warning, 2 = info, 3 = debug)
log_level = 2

[buildozer]
# (int) Log level (0 = error, 1 = warning, 2 = info, 3 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
