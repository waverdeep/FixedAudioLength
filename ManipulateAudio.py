import numpy as np


def fix_audio_length(source, sample_rate, duration):
    signal = source
    input_length = duration * sample_rate
    if len(signal) > input_length:
        signal = signal[0:input_length]
    elif input_length > len(signal):
        max_offset = input_length - len(signal)
        signal = np.pad(signal, (0, max_offset), "constant")

    return signal

