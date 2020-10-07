from FileOI import get_all_file_path, read_audio_file, save_audio_file, get_pure_filename, get_pure_filepath
from ManipulateAudio import fix_audio_length


def playground(input_dir, file_extension='wav', keyword='fix40sec', sample_rate=16000, fixed_length=40):
    file_list = get_all_file_path(input_dir, file_extension)
    for file in file_list:
        signal, sr = read_audio_file(file, '')
        pure_filename = get_pure_filename(file)
        pure_filepath = get_pure_filepath(file)
        man_signal = fix_audio_length(signal, sample_rate, 40)
        save_audio_file('{}/{}-{}'.format(pure_filepath,
                                          pure_filename,
                                          keyword),
                        man_signal,
                        file_extension,
                        sample_rate)


playground('./dataset', file_extension='wav', sample_rate=16000, fixed_length=40)