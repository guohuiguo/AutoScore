# 在 main.py 中导入模块 这个脚本能够完成所有的功能，但是无法和界面结合在一起
import asr_customization_demo
import gpt
import excel
import switch
import GMM_SpeakerRecognition  # 使用 GMM_SpeakerRecognition 模块
import train_model  # 导入模型训练部分
import subprocess

# 音频文件路径
path1 = 'qu.mp3'
path2 = 'a.mp3'

# 录制音频
input("Press Enter to start recording question audio...")
asr_customization_demo.record_audio(path1, duration=5)
input("Press Enter to start recording answer audio...")
asr_customization_demo.record_audio(path2, duration=5)

# 语音转写
q = asr_customization_demo.asrc_short_example(path1)  # 转写第一个问题音频
a = asr_customization_demo.asrc_short_example(path2)  # 转写第二个答案音频

# 使用 GPT-3 获取问题和答案的评分
score = gpt.chat(str(q), str(a))
score = score.split('：')[1]  # 假设评分是“评分：数字”，提取数字部分

# 将 MP3 转换为 WAV 格式
switch.audio_to_wav(path2, 'a.wav')  # 转换第二个音频文件为 WAV 格式

# 使用 GMM_SpeakerRecognition 模块中的 GMM_SpeakerRecognition 类进行说话人识别
new_recognizer = GMM_SpeakerRecognition.GMM_SpeakerRecognition()
new_recognizer.load_model("gmm_models.joblib")  # 加载训练好的模型
print("模型加载成功！")  # 调试信息 模型加载成功

test_audio = "a.wav"
result = new_recognizer.recognize(test_audio)  # 对音频进行识别
print(f"识别结果：{result}")  # 输出识别的说话人

# 将问题、答案和评分保存到 Excel 文件
excel.save_to_excel(q, a, score, result)