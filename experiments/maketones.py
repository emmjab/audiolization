#this makes tones and outputs to .wav file
from scipy.io.wavfile import write
import numpy as np

duration=5
amp=1E4
rate=44100

def note(freq, duration, amp, rate):
    t = np.linspace(0, duration, duration * rate)
    data = np.sin(2*np.pi*freq*t)*amp
    return data.astype(np.int16) # two byte integers

tone0 = note(0, 1, amp, rate) #silence
tone1 = note(261.63, 2, amp, rate) # C4
tone2 = note(329.63, 1, amp, rate) # E4
tone3 = note(392.00, 4, amp, rate) # G4


seq1 = np.concatenate((tone0,tone1,tone2,tone3, tone1),axis=1)
seq2 = np.concatenate((tone0,tone2,tone0,tone0, tone2),axis=1)
seq3 = np.concatenate((tone0,tone0,tone3,tone0, tone3),axis=1)

song = seq1

write('song3.wav', 44100, song)