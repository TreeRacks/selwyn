import subprocess
import time

# initialize
def initMatrix():
    
    subprocess.run(["config-pin","P9_18", "i2c"])
    subprocess.run(["config-pin","P9_19", "i2c"])
    subprocess.run(["i2cset", "-y", "1", "0x70", "0x21", "0x00"])
    subprocess.run(["i2cset", "-y", "1", "0x70", "0x80", "0x00"])
    subprocess.run(["i2cset", "-y", "1", "0x70", "0x81", "0x00"])
def animateFrame(lv, rv):
    

    # 0x06 is lowest volume (ambient) for right channel, 0x08 is mapped to lowest volume for left channel
    
    while True:
        if(lv < 0):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x00"])

        elif(0 < lv < 5):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x00"])
            #time.sleep(1)
        elif(5 < lv < 10):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x00"])
            #time.sleep(1)
        elif(10 < lv < 15):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x7E"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x00"])
            #time.sleep(1)
        elif(lv > 15):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x7E"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0xFF"])
            #time.sleep(1)    
        
        if(rv < 0):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x08", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0A", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0C", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0E", "0x00"])

        elif(0 < rv < 5):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x08", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0A", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0C", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0E", "0x00"])
            #time.sleep(1)
        elif(5 < rv < 10):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x08", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0A", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0C", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0E", "0x00"])
            #time.sleep(1)
        elif(10 < rv < 15):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x08", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0A", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0C", "0x7E"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0E", "0x00"])
            #time.sleep(1)
        elif(rv > 15):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x08", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0A", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0C", "0x7E"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x0E", "0xFF"])
            #time.sleep(1)    
        
