from tkinter import Tk, Label, IntVar
from PIL import ImageTk, Image
from pygame import mixer
from os import listdir
from wave import open
from contextlib import closing
from math import ceil

# function to wait for a certain time(seconds)
def waithere(time):
    var = IntVar()
    aoe.after(time*1000, var.set, 1)
    print("waiting...")
    aoe.wait_variable(var)

def run(civ_list):
    
    # playing the last civ in the list
    civ = civ_list[-1]
    
    # Removing the file extintion
    civ = civ[0:-4]

    # Get the duaration of the sound file
    fname = "Audio/{}.wav".format(civ)
    with closing(open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print(duration)

    # Get the images
    img1 = ImageTk.PhotoImage(Image.open(r'Pics_icon/{}.jpg'.format(civ)).resize((150, 150), Image.ANTIALIAS))
    label_img1 = Label(image=img1).grid(row=0, column=0,columnspan=2, padx=0, pady=00)
    
    img2 = ImageTk.PhotoImage(Image.open(r'Pics_uu/{}.jpg'.format(civ)))
    label_img2 = Label(image=img2).grid(row=1, column=0,columnspan=2, padx=70, pady=20)
    print('adding image')

    # Adding Text
    label_text = Label(text='               1               ', font=('Times New Roman', 35, 'bold')).grid(row=2, column=0,columnspan=2, padx=35, pady=20)
    label_text = Label(text='The {}'.format(civ), font=('Times New Roman', 40, 'bold')).grid(row=2, column=0,columnspan=2, padx=35, pady=20)
    print('adding text')

    # playing the sound
    mixer.music.load("Audio/{}.wav".format(civ))
    mixer.music.play(loops=0)
    print('playing sound')
    
    # Removing the civ that was played
    civ_list.pop()

    print(civ_list)
    print(len(civ_list))
    
    # wait for a duaration equal to the sound duration
    waithere(ceil(duration))
        
    # if the list is not empty, continue looping on it :) 
    if len(civ_list) > 0:
        run(civ_list)


# Initalizing Tkinter window
aoe = Tk()
aoe.title('Age of Empires 2 is The Best ... By: MFT')
aoe.iconbitmap(r'helmet.ico')
aoe.geometry("450x470")

# set minimum window size value
aoe.minsize(450, 570)

# set maximum window size value
aoe.maxsize(450, 570)

# Initializing the sound player
mixer.init()

# Get the files
civv_list = listdir('Audio')
civv_list = civv_list[::-1]
print(civv_list)

# run the first loop
run(civv_list)

# Close the window when it is finished
aoe.destroy()

# start the program
aoe.mainloop()

# Thanks for Microsoft, Voobly, Fandom for the pics and the audio 