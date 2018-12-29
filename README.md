# RandomSoundSampler
Used to make any collection of mp3's to a random sound sampler button on a Raspberry Pi.
Can also be run on x86, press `enter` on keyboard to play next sound.

## Requirements 

### python3

`sudo apt-get install python3.6`

### mpg123

`sudo apt-get install mpg123`

## Running
Place all mp3s in a folder.
Edit following lines 6 and 8:

```python
#Modify these to correct path to files
path = '/path/to/folder/'
#sound to play inside path on startup
startupSound = 'file'
```

to desired path

If running of Raspberry Pi use a button connected to GPIO pin 10 with a 10k Ohm resistor.

Script will auto-detect OS
