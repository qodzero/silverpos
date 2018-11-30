#!/bin/sh

echo "[INFO]  Installing Kivy Dependencies..."
sudo apt install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev
echo "[INFO]  Installing Audio Plugins..."
sudo apt install -y \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good
echo "[DONE]  Dependencies installed..."

pip3 install --upgrade virtualenv setuptools
#Uncomment following lines to install in a virtual environment
#virtualenv --no-site-packages -p python3 kivyinstall
#. kivyinstall/bin/activate

echo "[INFO]  Installing Cython(required when building kivy)..."
pip3 install Cython==0.25.2
pip install Cython==0.25.2
echo "[DONE]  Cython Installed..."
echo "[INFO]  Finally installing kivy(latest)..."
pip3 install git+https://github.com/kivy/kivy.git@master
ech "[DONE]  Installed Kivy..."
