import soundfile as sf
import pyloudnorm as pyln
from pydub import AudioSegment
import librosa

#Etiqueta de politicos:
#JULIOG
#MARTINV
#FRANCISCOS
#ALANG
#FERNANDOO
#CESARA
#MARIOV
#KEIKOF
#VERONICAM
#LOCUTORA1
#LOCUTORA2

nombre_politico = "_JULIOG"
step = 1 #Intervalo en segundos del audio
file_name = 'audio0010' #nombre del archivo
file_name_full = "pasos/"+file_name+".wav" #Crear una carpeta "pasos" en la carpeta donde esta el proyecto
len_audio = int(librosa.get_duration(filename=file_name_full)) #Longitud del audio en segundos.
print("El audio tiene una duracion de ",len_audio, " segundos")
espaciado = "_______________________________"
audio_vacio = []

#abrir el archivo wav y convertirlo a monaural.
sound = AudioSegment.from_wav(file_name_full)
sound = sound.set_channels(1)
file_name_full_mono = "pasos/"+file_name+"_mono.wav"
sound.export(file_name_full_mono, format="wav")

data1, rate1 = sf.read(file_name_full_mono)  # Carga el audio
meter1 = pyln.Meter(rate1)
loudness1 = meter1.integrated_loudness(data1)
print(loudness1)


#crear objeto a partir del audio wav monaural:
newAudio = AudioSegment.from_wav(file_name_full_mono)



#proceso de segmentacion:
for i in range(int(len_audio/step)):
    t1 = step*1000*i #Works in milliseconds
    t2 = step*1000*(i+1)
    segment_name = '_'
    if(i<1000):
        if(i<100):
            if(i<10):
                segment_name = segment_name+'000'
            else:
                segment_name = segment_name + '00'
        else:
            segment_name = segment_name + '0'

    segment_name = segment_name+str(i+1)
    segment = newAudio[t1:t2]
    segment_name_full = "pasos/"+file_name + segment_name + nombre_politico+ ".wav"
    segment.export(segment_name_full, format="wav") #Exporta el archivo wav en el directorio indicado.
    print(segment_name_full)

    #Muestra la intensidad del audio:
    data, rate = sf.read(segment_name_full)  # Carga el audio
    meter = pyln.Meter(rate)
    loudness = meter.integrated_loudness(data)  # Mide el volumen del audio
    if(abs(loudness1-loudness)>10): #Si el volumen del audio está por
        audio_vacio.append(i+1)
    print("Intensity: ",loudness+1, "\n", espaciado)


print(audio_vacio)
