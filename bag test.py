import machine
from machine import SPI, Pin
import ssd1306
import time
import math

spi = SPI(baudrate=10000000, polarity=1, phase=0, sck=Pin(14,Pin.OUT), mosi=Pin(13,Pin.OUT), miso=Pin(12))
oled = ssd1306.SSD1306_SPI(128, 64, spi, Pin(26),Pin(27), Pin(25))
pump = machine.Pin(16, Pin.OUT)  # 设置 GPIO16 为泵
valve = machine.Pin(17, Pin.OUT)  # 设置 GPIO17 为电磁阀

pumptime = 450 #泵工作时间
valvetime = 1450 #阀开启时间
waittime = 120  #等待时间
#count = 0

def lifetest(pumptime,valvetime,waittime):
  pump.off()    #先关闭泵，阀
  valve.off()
  pump.on()     #设液体先在下液箱，开泵往上抽
  time.sleep(pumptime)     #等待液体抽到上面
  pump.off()    #关泵
  time.sleep(waittime)    #稍等一下，模拟静置时间
  valve.on()    #开阀
  time.sleep(valvetime)     #等待液体流下来
  valve.off()    #关闭阀
  
  
'''
def lifetest(pumptime,valvetime):
  ptime = 0
  vtime = 0
  if ptime < pumptime:
    valve.off()    #关闭阀
    pump.on()    #开泵
    ptime = ptime + 1
    break
  else:
    pump.off()    #关泵
    if vtime < valvetime:
      valve.on()    #开阀
      vtime = vtime + 1
      break
    else:
      valve.off()    #关闭阀
      vtime = 0
      ptime = 0
'''      
      
      
#file = open ("counts.txt", "w")
#file.write(str(count))
#file.close()

file = open ("counts.txt", "r")
count = int(file.read())  #读取上次掉电运行次数
file.close()



for x in range(1010):  假设最多执行1010个循环
  oled.poweron()  #打开OLED
  oled.init_display()  #OLED初始化
  oled.text('Waste Bag',25,6)
  oled.text('life test',25,20)
  oled.text('Count:',10,40)
  oled.text(str(count),70,40)
  oled.show()
#  time.sleep(3)
  oled.fill(0)   #清屏
  
  
  lifetest(pumptime,valvetime,waittime)  #执行一个循环
  count = count + 1   #执行一个循环后累计次数+1
  file = open ("counts.txt", "w")  #打开
  file.write(str(count))
  file.close()






