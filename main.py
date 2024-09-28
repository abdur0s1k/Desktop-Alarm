import datetime     
import pyglet
from datetime import * 

#проверка правильного ввода даных
def validate_time(val_time):
    if len(val_time) != 8:    #проверка строк в переменной val_time 
        return'Invalid format, try again.'
    else:
        if int(val_time[0:2]) > 23:
            return 'Invalid clock format, try again.' 
        elif int(val_time[3:5]) > 59: 
            return 'Incorrect minutes format, try again.'
        elif int(val_time[6:8]) > 59: 
            return 'Incorrect seconds format, try again.'
        else:
            return 'Great!'

#показывает время на компьютере 
time_now = datetime.now()
time_ = ['hour','minute','second']
print (time_)
print ('Time now:',time_now.hour,':',time_now.minute,':',time_now.second)
example = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
explanations = ('hour',10,'minute',13,'second',15)

#ввод времени и отаброжения времени на которое поставлен будильник  
while True:
    print ('example input:',example[1],explanations)
    val_time = input('Enter the time in the following format HH:MM:SS \nAlarm time:')
    validate = validate_time(val_time)
    if validate != 'Great!':
        print(validate)
    else:
        print(f"Alarm clock set to time {val_time}...")
        break

#главный механизм будильника 
hour = int(val_time[0:2])
minutes = int(val_time[3:5])
sec = int(val_time[6:8])
music = pyglet.resource.media('16.mp3')

while True:
    now = datetime.now()
    current_hour = now.hour
    current_minutes = now.minute
    current_sec = now.second
    if hour == current_hour:
        if minutes == current_minutes:
            if sec == current_sec:
                print ("Get up!!!")
                music.play()
                break
                
pyglet.app.run()
