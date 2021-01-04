#!/bin/sh
if [ -f "`command -v apt-get`" ]; then
    echo "Using Ubuntu steps since apt-get was detected:"
    # sudo add-apt-repository ppa:kivy-team/kivy
    # sudo apt-get update")
    sudo apt-get remove python-kivy python3-kivy
    # sudo apt-get install python-setuptools python-pygame \
    #   python-opengl python-gst0.10 python-enchant \
    #   gstreamer0.10-plugins-good python-dev build-essential \
    #   libgl1-mesa-dev-lts-quantal libgles2-mesa-dev-lts-quantal \
    #   python-pip

    # The next commented command is a modified one-line python3
    # version of instruction at
    # <https://kivy.org/docs/installation/installation.html> under
    # "Development Version"
    # sudo apt-get install python3-setuptools python3-pygame \
    #   python3-opengl python3-gst-1.0 python3-enchant \
    #   gstreamer0.10-plugins-good python3-dev build-essential \
    #   libgl1-mesa-dev libgles2-mesa-dev python3-pip
    # # but python3-pygame doesn't exist so follow
    # # <http://askubuntu.com/questions/401342/
    # # how-to-download-pygame-in-python3-3>:
    # sudo apt-get install mercurial
    # hg clone https://bitbucket.org/pygame/pygame
    # cd pygame
    # sudo apt-get install python3-dev python3-setuptools \
    #  python3-numpy libsdl-dev libsdl-image1.2-dev \
    #  libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    #  libportmidi-dev \
    #  libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
    # python3 config.py
    # python3 setup.py build
    # sudo python3 setup.py install

    sudo apt-get install python-setuptools python-pygame python-opengl \
        python-gst0.10 python-enchant gstreamer0.10-plugins-good python-dev \
        build-essential libgl1-mesa-dev-lts-quantal \
        libgles2-mesa-dev-lts-quantal python-pip
    sudo apt-get install python-pip
    # python3-pip
    sudo python -m pip install --upgrade pip
    sudo python -m pip install cython
    sudo python -m pip install --upgrade pip wheel setuptools
    sudo python -m pip install docutils pygments
    sudo python -m pip install kivy --no-cache-dir
elif [ -f "`command -v dnf`" ] then
    # See also (don't seem to exist though google groups page linked
    # below says is solution): gstreamer-python and gstreamer-devel
    cat << END
    Fedora/similar is detected. The following steps are a modified limited
    non-buildozer version of the one-line from
    https://groups.google.com/forum/#!topic/kivy-users/t9248qRFvNM:
END
    sudo dnf install python-devel ffmpeg-libs SDL2-devel SDL2_image-devel \
        SDL2_mixer-devel SDL2_ttf-devel portmidi-devel libavdevice \
        libavc1394-devel zlibrary-devel ccache mesa-libGL mesa-libGL-devel
    # The next line resolves: gcc: error: /usr/lib/rpm/redhat/redhat-hardened-cc1: No such file or directory
    sudo dnf install redhat-rpm-config
    # http://download.opensuse.org/repositories/home:/thopiekar:/kivy/
    # doesn't contain anything for Fedora (even old fedora version folders linked from  )
    # sudo python3 -m pip install --upgrade pip
    # sudo python3 -m pip install cython
    # sudo python3 -m pip install --upgrade pip wheel setuptools
    # sudo python3 -m pip install docutils pygments
    # pypiwin32 kivy.deps.sdl2 kivy.deps.glew

    # cd $HOME/Downloads
    # wget https://kivy.org/downloads/appveyor/kivy/Kivy-1.9.2.dev0-cp35-cp35m-win_amd64.whl
    # sudo python3 -m pip install Kivy-1.9.2.dev0-cp35-cp35m-win_amd64.whl
    # If 'not a supported wheel on this platform, then:
    # wget https://kivy.org/downloads/appveyor/kivy/Kivy-1.9.2.dev0-cp35-cp35m-win32.whl
    # sudo python3 -m pip install Kivy-1.9.2.dev0-cp35-cp35m-win32.whl
    sudo python -m pip install --upgrade pip
    sudo python -m pip install cython
    sudo python -m pip install --upgrade pip wheel setuptools
    sudo python -m pip install docutils pygments
    sudo python -m pip install kivy --no-cache-dir
    # pypiwin32 kivy.deps.sdl2 kivy.deps.glew
else
    echo "ERROR: This script is only implemented for apt-get and dnf."
    exit 1
fi
