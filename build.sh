rm -fr build
rm -fr dist

pyinstaller -F -n yt2music main.py
