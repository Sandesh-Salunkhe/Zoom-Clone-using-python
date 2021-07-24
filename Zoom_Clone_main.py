#from vidstream import AudioReceiver, AudioSender, ScreenShareClient, CameraClient, StreamingServer
# Instead of writing all the function from the module just use * it will automatically import all the functions from the module
from vidstream import *
import tkinter as tk  # These are some Core python modules
import socket     # to get your private Ip Address
import threading  # this will helps us to do multi-threading process like AudioStream that Receive,AudioStream Share/Send,Camera_data Receive ,Camrea_data Share
import requests

local_ip_address = socket.gethostbyname(socket.gethostname())  # To get your local Ip Address
#public_ip_address = requests.get ('https://api.ipify.org').text 
# server = StreamingServer('192.168.0.207',9999)

server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

def start_listening():
    t1 = threading.Thread(target = server.start_server)
    t2 = threading.Thread(target = receiver.start_server)
    t1.start()
    t2.start()

def start_camera_stream ():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'),  7777) 
    t3 = threading.Thread(target = camera_client.start_stream)
    t3.start()   

def start_screen_Sharing ():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'),  7777) 
    t4 = threading.Thread(target = screen_client.start_stream)
    t4.start()   

def start_audio_stream ():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'),  6666) 
    t5 = threading.Thread(target = audio_sender.start_stream)
    t5.start() 

# GUI

window = tk.Tk()
window.title("FaceMeet calls v0.0.1 Alpha")
window.geometry('300x200')

label_target_ip = tk.Label(window, text="Target Ip :")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening) 
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_Sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()

