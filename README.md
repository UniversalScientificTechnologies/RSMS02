### Radio Storm Monitoring Station

Mobile VLF lightning mapping station based on a multi-directional loop antenna array.
The array could be mounted stationary or mobile on the car roof.

![Mobile VLF array mounted on the CRREAT measurement car](./DOC/SRC/img/mobile_array.jpg)

The instrument is capable of processing the lightning signal and generating a trigger to another instrument (high-speed camera, for example). 

##### Features and parameters

  * Time precision of samples recording:  100 ns
	* Network connection: 1000M metallic Ethernet
	* FPGA type: Zynq XC7Z01
	* Central processing unit: ARM® Cortex®-A9
	* Computing coprocessor: Epiphany III  E16G301
	* Operating system: Linux Ubuntu
	* RAM size: 1 GB
	* Recording media: uSD card
	* Recording media size: 16GB
	* Maximal recording length: 1.46 s
	* Ability to record signal before trigger: yes
	* Pre-trigger recording length: 0.7 s
	* Sampling rate: 2.5 MHz
	* Sample bit depth: 12-bit.
	* Antenna array: 3-loop orthogonal VLF antenna
	* Trigger output to other instruments: Yes, TTL
	* Delay to rendering signal preview: 2s
	* Input power voltage: 9 - 14.8 V (Car compatible)

#### Block Schematics

![Station block schamatics](./DOC/SRC/img/RSMS02_receiver.png "Overview of interconnectio of station components")


#### Visualization

![Waterfall frequency display for antenna array](./DOC/SRC/img/frequency_display.png)

![Time display for antenna array](./DOC/SRC/img/time_display.png)

#### Relevant scientific publications

  * [In situ ground-based mobile measurement of lightning events above central Europe](https://amt.copernicus.org/articles/16/547/2023/)

