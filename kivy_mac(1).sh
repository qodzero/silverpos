echo "[INFO] Installing Kivy..."
brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
pip install Cython==0.26.1
pip install https://github.com/kivy/kivy/archive/master.zip
