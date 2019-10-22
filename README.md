# AppBusiness


In Raspbberry Pi the communication of the `RC522 RFID` reader is made through the `Serial Peripheral Interface (SPI)` interface. The `SPI` uses full duplex synchronous communication using the master-slave communication model.

In the image below you can see which pins correspond to the SPI on the Raspberry Pi 3 GPIO, they are highlighted in purple.

![](/images/raspberry_pi3_gpio-288x300.png)


### RFID Module Connection with Raspberry Pi
The table below describes the `RFID module` pin and its associated pin / GPIO. Follow the wiring diagram shown in the table to use RFID with Raspberry Pi 3.
> Attention, the module voltage is 3.3 volts.

![](/images/Tabela_Ligacao_RC522_RPi.png)


### Preparing the environment
This walkthrough is for Raspbian `Jessie version 2016-03-18` (download), versions after this release have problems with the SPI interface, and versions of Wheezy do not support Device Tree, used in the example below. Read more about Device Tree in the Raspberry documentation. If you want to configure another version of Raspbian follow the SPI documentation tutorial.

Raspbian comes with SPI disabled by default, to check whether or not it is enabled we will execute the following command:

```bash
ls /dev/spi*
```

If the result is as follows:
```bash
ls: cannot access /dev/spi*: No such file or directory
```


In this case we must enable the SPI.
To enable SPI on Raspbian go to `Menu> Preferences> Raspberry Pi Configuration` and on the Interface tab enable` SPI`. Click on OK.


![](images/Habilitar_SPI.png)

Then in your favorite text editor open the file /boot/config.txt (as root) and add the following line:

```bash
dtoverlay=spi-bcm2708
```

Restart Raspbian and check again, the result should be:

```bash
/dev/spidev0.0 /dev/spidev0.1
```

Verify that the SPI module was loaded correctly by the command:

```bash
dmesg | grep spi
```

The result should look something like the one below, indicating RFID communication with Raspberry Pi:

```bash
[ 6.240564] bcm2708_spi 3f204000.spi: master is unqueued, this is deprecated
[ 6.241262] bcm2708_spi 3f204000.spi: SPI Controller at 0x3f204000 (irq 80)
```

To use the RC522 module in Python we need to install some components before we can start programming. First we will install the python-dev package through the command:

```bash
sudo apt-get install python-dev
```

Once installed we will install the Python package for SPI communication, for this run the following commands:

```bash
git clone https://github.com/Robot-Hockey/AppBusiness.git
cd AppBusiness
sudo python setup.py install
```
### Running

```bash
python main.py
```

When approaching a `RFID` tag from the module.

```bash
Show your card RFID
Card detected!
UID do cartão: 4F:FD:2F:0:9D
```
