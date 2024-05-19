import subprocess
import time

#initialize
subprocess.run(["config-pin","P9_18", "i2c"])
subprocess.run(["config-pin","P9_19", "i2c"])
time.sleep(1)

subprocess.run(["i2cset", "-y", "1", "0x70", "0x21", "0x00"])
time.sleep(1)
subprocess.run(["i2cset", "-y", "1", "0x70", "0x80","0x00"])
subprocess.run(["i2cset", "-y", "1", "0x70", "0x81","0x00"])

# 0x06 is lowest volume for right channel, 0x08 is mapped to lowest volume for left channel
db = 0
while True:
    while (db < 20):
        if(3 < db < 5):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x00"])
            #time.sleep(1)
        elif(5 < db < 7):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x00"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x00"])
            #time.sleep(1)
        elif(8 < db < 10):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x7E"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x00"])
            #time.sleep(1)
        elif(11 < db < 13):
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x60"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x78"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x7E"])
            subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0xFF"])
            #time.sleep(1)    
        db+=1
    while (db > 0):
        db-=1    
        # subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0xFF"])
        # time.sleep(1)
        # subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0xFF"])
        # time.sleep(1)
        # subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0xFF"])
        # time.sleep(1)
        # subprocess.run(["i2cset", "-y", "1", "0x70", "0x06", "0x00"])
        # time.sleep(1)
        # subprocess.run(["i2cset", "-y", "1", "0x70", "0x04", "0x00"])
        # time.sleep(1)
        # subprocess.run(["i2cset", "-y", "1", "0x70", "0x02", "0x00"])
        # time.sleep(1)
        # subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x00"])
        # time.sleep(1)
