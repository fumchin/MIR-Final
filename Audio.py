import librosa
class Audio:
    def __init__(self, file_path, sr=222050):
        self.file_path = file_path
        self.y, self.sr = librosa.load(self.file_path, sr=sr)
        self.start_index = 0
        self.end_index = 0
        self.current_index = 0

    # 方法(Method)

