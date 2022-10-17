
<br>

<div align = center>


<br>
<br>


# Dawn App

*kivy based app* <br>
Kivy==2.1.0
kivymd==0.104.2

<br>


</div>

<br>


## Overview

The goal of the app:


## URI and Versioning

Currently, using version 

## Design

The app is a kivy based phone app using for managing medical data for a user. This use an external API
deployed on Heroku for user DB management.



## Pages

Define the pages in the app

## Users

Define the users

## App Build Method - Buildozer

This project use `buildozer` package for building the app.

https://github.com/kivy/buildozer

###buildozer.spec file special settings

setting | Description
-------|------------
title | `Dawn`
package.name | `dawn`
package.domain | `org.tech19`
source.include_exts | `py,png,jpg,kv,atlas,assets/images/*,libs/uix/kv/*,libs/uix/components/*`
source.include_patterns| `assets/images/*` 
source.exclude_dirs | `tests, bin, venv`
requirements | `python3,kivy==2.1.0,kivymd==0.104.2,pillow`
presplash.filename | `assets/images/presplash.jpg`
icon.filename | `assets/images/app_logo.png`
orientation | `portrait`
fullscreen | `0`
android.presplash_color | `#F5E5D6`
android.permissions | `INTERNET`
android.ndk | `25b` (if there is more up to date version use the new one)




###The steps for building the app in this project

Build step | Description
-----------|------------
Installing Buildozer | Install buildozer on Linux Subsystem. Make sure that the buildozer folder has the latest sdk and ndk folders, if not it will come up at the first build
Clone Repo | Clone this repo to a local directory
Requirements | Install all dependencies using the `requirements.txt` file and check that the app is running on the computer by running the `main.py` file
Build | Open an Ubuntu console and navigate to the local directory where. Run the command `buildozer -v android debug`. This will start the build process. The first time building the app should take long time. The build might crash up to 10 times (see first time build troubleshooting down in this README file)
APK | After the build is finished, an apk should be created in the bin folder at the root directory.

[comment]: <> (this section need to be defined )

##Current APK

https://drive.google.com/drive/folders/1d3okj9NsNIvjIbgfsEx_4dbfGFmINySW?usp=sharing

## Troubleshooting

* ### buildozer.spec file is not in the repo?
create a new buildozer.spec file by using the `buildozer init` command in the Ubuntu console at the diractory. after 
creating the file, open it and change the special setting according to the **buildozer.spec file special settings** section in this README.

* ### buildozer is not running - missing NDK file

To build the app using buildozer, you need to have the latest version of the SDK and NDK folders and locate them in the buildozer folder of the Linux subsystem:

`\home\<user-name>\.buildozer\android\platform`

On the first run, an automatic installation should happen, but sometimes it fails to download the folder. Therefore, the link must be accessed:

https://developer.android.com/ndk/downloads

and the latest version suitable for the operating system must be downloaded.

* ### buildozer is not running - a folder cannot be accessed
On the first run, buildozer getting stuck several times with an error saying it was unable to access a certain folder.
This is because the folder in the particular location that buildozer is trying to access is given a **different name** for some reason.

This is a bug in the buildozer package and the way to fix this error is by going to the folder that buildozer is trying to access and change its name to the name written in the error.
Now the command `buildozer -v android debug` can be run again. **On the first run, expect this error to occur about 10 times for different folders. For each folder, the treatment is the same**.

## GitHub Actions
###Buildozer automation


<br>

<div align = center>


<br>
<br>
This app was built by Tech-19 2022

<br>
<br>




</div>

<br>