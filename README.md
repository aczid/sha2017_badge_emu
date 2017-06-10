# SHA2017 badge emulator

An emulator for the SHA2017 badge's micropython bindings.

## This has been superceded by a Unix build of micropython with some of the badge drivers

https://github.com/SHA2017-badge/micropython-esp32/tree/esp32/unix

You'll need `TkInter` for python packages installed:

    sudo apt-get install tk8.5-dev tcl8.5-dev python-imaging-tk python-pil.imagetk python-tk pkg-config

Also you'll need the python `PIL` package:

    pip install -r requirements.txt

After that you should be able to start up the emulator by running:

    python badge.py demo.py

This will execute the script `demo.py` in the emulator.

