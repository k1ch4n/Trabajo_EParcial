#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=vPaBI_IQoJk&ab_channel=FuerzaPopular')
yt.title
yt.thumbnail_url
yt.streams.all()


# In[6]:


from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=vPaBI_IQoJk&ab_channel=FuerzaPopular')
yt.title
yt.thumbnail_url
yt.streams.all()
stream = yt.streams.first()
stream


# 

# In[11]:


from pytube import YouTube        

yt = YouTube('https://www.youtube.com/watch?v=vPaBI_IQoJk&ab_channel=FuerzaPopular')
yt.title
yt.thumbnail_url
yt.streams.all()
stream = yt.streams.first()
stream
stream.download()


# In[24]:


from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=vPaBI_IQoJk&ab_channel=FuerzaPopular')
yt.title
yt.thumbnail_url
yt.streams.all()
stream = yt.streams.filter(file_extension='wav').all()
stream


# In[8]:


yt = YouTube('https://www.youtube.com/watch?v=vPaBI_IQoJk&ab_channel=FuerzaPopular')
stream = yt.streams.get_by_itag('251')
stream
stream.download()


# In[12]:


#####################################################descarga video de youtube
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=vPaBI_IQoJk&ab_channel=FuerzaPopular')
stream = yt.streams.get_by_itag('251')
stream.download()


# In[10]:


import librosa
data, fs = librosa.load('pasos/keiko.wav')
print(data)
print("####################################################")
print(fs)


# In[2]:


##########################################################segmentar audio
from pydub import AudioSegment
t1 = 3 * 1000 #Works in milliseconds
t2 = 6 * 1000
newAudio = AudioSegment.from_wav("pasos/keiko.wav")
newAudio = newAudio[t1:t2]
newAudio.export('pasos/newSong.wav', format="wav") #Exports to a wav file in the current path.


# In[3]:


pip install pydub


# In[2]:


from pytube import YouTube
link = 'https://www.youtube.com/watch?v=1I-3vJSC-Vo&ab_channel=OneminuteSatisfaction'
youtube = YouTube(link)
stream = youtube.streams.filter(only_audio=True).all()
stream.download('descarga')


# In[15]:


#######################################intensidad de sonido

import soundfile as sf
import pyloudnorm as pyln

data, rate = sf.read("newsong.wav")
meter = pyln.Meter(rate) #
loudness = meter.integrated_loudness(data)

print(loudness)


# In[14]:


pip install pyloudnorm

