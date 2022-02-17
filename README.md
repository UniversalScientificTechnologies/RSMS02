### Radio Storm Monitorig Station

Mobile VLF lightning mapping station based on multi-directional loop antenna array.
The array could be mounted stationary or mobile on the car roof.

![Stationary antenna array](./DOC/SRC/img/Stationary_array.jpg "Stationary antenna array on an observatory roof")

![Mobile antenna array](./DOC/SRC/img/mobile_array.jpg "Mobile antenna array on a car roof")


#### Block Schematics

![Station block schamatics](./DOC/SRC/img/RSMS_receiver.png "Overview of interconnectio of station components")


#### Visualization

The device uses [fosphor](https://osmocom.org/projects/sdr/wiki/fosphor) for real-time spectral vizualization.

    sudo apt-get install nvidia-opencl-dev opencl-headers


![Fosphor waterfall for antenna array](./DOC/SRC/img/fosphor_waterfall.png)
