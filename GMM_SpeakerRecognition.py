import os
from pydub import AudioSegment
import numpy as np
from sklearn.mixture import GaussianMixture
from python_speech_features import mfcc
import scipy.io.wavfile as wav
from joblib import Parallel, delayed, dump, load

def extract_features(audio_path):
    # 如果是 MP3 或 M4A 格式，先转换为 WAV 格式
    if audio_path.endswith('.mp3') or audio_path.endswith('.m4a'):
        audio = AudioSegment.from_file(audio_path)  # 自动识别格式并读取
        audio_path = audio_path.rsplit('.', 1)[0] + '.wav'  # 创建临时 WAV 文件路径
        audio.export(audio_path, format='wav')  # 导出为 WAV 格式

    # 读取 WAV 文件
    rate, signal = wav.read(audio_path)
    mfcc_features = mfcc(signal, rate)
    return mfcc_features

class GMM_SpeakerRecognition:
    def __init__(self, n_components=16):
        self.gmm_models = {}
        self.n_components = n_components

    def train(self, speaker_name, audio_paths):
        features = np.vstack(Parallel(n_jobs=-1)(delayed(extract_features)(path) for path in audio_paths))
        gmm = GaussianMixture(n_components=self.n_components, covariance_type='diag', max_iter=200, random_state=42)
        gmm.fit(features)
        self.gmm_models[speaker_name] = gmm

    def recognize(self, test_audio_path):
        """
        通过 GMM 模型识别说话人（通过与每个训练好的说话人模型匹配）
        :param test_audio_path: 要识别的音频文件路径
        :return: 识别出的说话人
        """
        features = extract_features(test_audio_path)  # 提取音频特征

        # 初始化一个字典来存储每个说话人模型的匹配得分
        scores = {}

        # 遍历每个说话人的 GMM 模型，计算与音频特征的匹配度
        for speaker, gmm in self.gmm_models.items():
            log_likelihood = gmm.score(features)  # 计算与该模型的匹配度
            scores[speaker] = log_likelihood  # 将结果保存到字典中

        # 找到匹配度最高的说话人
        best_speaker = max(scores, key=scores.get)

        # 返回识别出的说话人
        return best_speaker

    def save_model(self, file_path):
        # 使用 joblib 保存模型
        dump(self.gmm_models, file_path)

    def load_model(self, file_path):
        # 使用 joblib 加载模型
        self.gmm_models = load(file_path)

def get_training_data(root_folder):
    training_data = {}
    for speaker_name in os.listdir(root_folder):
        speaker_folder = os.path.join(root_folder, speaker_name)
        if os.path.isdir(speaker_folder):
            # 获取所有 .wav 文件
            audio_files = [os.path.join(speaker_folder, f) for f in os.listdir(speaker_folder) if f.endswith('.wav')]
            if audio_files:
                training_data[speaker_name] = audio_files
    return training_data