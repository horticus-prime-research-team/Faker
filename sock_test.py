import socketio
import json
import time
from random import randint
import datetime

time.sleep(1)
sio = socketio.Client()
date = datetime.datetime.now()

@sio.on('my message')
def on_message(data):
  print('I received a message')

@sio.event
def connect():
  print('connection established')

@sio.event
def disconnect():
  print('disconnected from server')

sio.connect('http://localhost:3001')

while True:
  for x in range(20):
    rand1 = randint(1, 1000)
  if rand1 < 300:
    value = 'Dry'
  elif rand1 > 300 and rand1 < 600:
    value = 'Moist'
  else:
    value = 'Wet'
  
  sio.send(json.dumps({'%d' % rand1 : '%s' % value}))
  time.sleep(10)


print('my sid is', sio.sid)
sio.wait()