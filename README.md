# Qubes CPU Pinning

[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html) 

## Description

This script is designed for QubesOS. It makes use of Qubes tags (`qvm-tags`) to automatically pin VMs to specified CPUs (e.g. e-cores and p-cores).

## Usage

1. Download `cpu-pinning.service` and `cpu-pinning.py` and copy it over to `dom0`
2. Inside `dom0` copy the service file to `/etc/systemd/system` and the Python script to `/usr/local/bin`
3. Modify the Python script (`P_CORES` and `E_CORES` variables) to match your CPU topology. The `sudo xenpm get-cpu-topology` can help here.
4. Also inside `dom0`, execute `sudo chmod +x /usr/local/bin/cpu-pinning.py; sudo systemctl daemon-reload && sudo systemctl
   enable --now cpu-pinning`.
5. For each VM whose pinnings you want to modify, execute (in `dom0`): `qvm-tags VMNAME add CORES_TAG`. 

`CORES_TAG` can be one of:

- `e_cores` - have VM only execute on your efficient cores.
- `e_cores_soft` - have VM try to execute on efficient cores, using other cores if all e-cores are busy.
- `p_cores` - have VM only execute on your performance cores.
- `p_cores_soft` - have VM try to execute on performance cores, using other cores if all p-cores are busy.

## Credits

The script is expanded from @noskb's and @renehoj's [CPU pinning script](https://forum.qubes-os.org/t/cpu-pinning-alder-lake/17949).

## Other Utilities

See [the qubes-utils repo](https://github.com/Atrate/qubes-utils) for links to other utilities I've written for Qubes.

I recommend also checking out [Qubes Window Boost](https://github.com/Atrate/qubes-window-boost), it works very well in combination with this script.

## License
This project is licensed under the [AGPL-3.0-or-later](https://www.gnu.org/licenses/agpl-3.0.html).

[![License: AGPLv3](https://www.gnu.org/graphics/agplv3-with-text-162x68.png)](https://www.gnu.org/licenses/agpl-3.0.html)
