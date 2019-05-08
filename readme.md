# BarCraft - Cleaner

## Setting up the pi

```bash
# setup a new password
passwd
# setup wifi and add ssh under interfaces
sudo raspi-config
# Enable python 3.5
echo alias python='/usr/bin/python3.5' > ~/.bashrc
. ~/.bashrc
sudo apt-get install rpi.gpio
```
