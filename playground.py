import os
import glob
import librosa
import soundfile as sf
import numpy as np


# find all dataset filepath
def get_all_file_path(input_dir, file_extension):
    temp = glob.glob(os.path.join(input_dir, '**', '*.{}'.format(file_extension)), recursive=True)
    return temp


def read_audio_file(filename, extension, sample_rate=16000):
    if extension is not '':
        y, sr = librosa.load('{}.{}'.format(filename, extension), sr=sample_rate)
        return y, sr
    else:
        y, sr = librosa.load(filename, sr=sample_rate)
        return y, sr


def save_audio_file(filename,  data, extension='', sample_rate=16000, subtype='PCM_16'):
    if extension is not '':
        sf.write('{}.{}'.format(filename, extension), data, samplerate=sample_rate, subtype=subtype)
    else:
        sf.write(filename, data, samplerate=sample_rate, subtype=subtype)


def get_pure_filename(filename):
    temp = filename.split('.')
    del temp[-1]
    temp = ' '.join(temp)
    temp = temp.split('/')
    temp = temp[-1]
    return temp


def fix_audio_length(source, sample_rate, duration, filename, extension):
    signal = source
    input_length = duration * sample_rate
    if len(signal) > input_length:
        signal = signal[0:input_length]
    elif input_length > len(signal):
        max_offset = input_length - len(signal)
        signal = np.pad(signal, (0, max_offset), "constant")

    save_audio_file(filename, signal, extension)


file_list = get_all_file_path('./dataset', 'wav')

for file in file_list:
    signal, sr = read_audio_file(file, '')
    fix_audio_length(signal, sr, 40, './dataset/{}-re.wav'.format(get_pure_filename(file)), '')
