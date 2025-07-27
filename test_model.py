from GMM_SpeakerRecognition import GMM_SpeakerRecognition

if __name__ == "__main__":
    # 加载已经保存的模型
    recognizer = GMM_SpeakerRecognition()
    recognizer.load_model("/Users/your_user_name/~/AutoScore/gmm_models.joblib")  # 修改为你的模型文件路径

    # 识别新的音频文件
    test_audio = "/Users/your_user_name/~/AutoScore/a.mp3"  # 修改为你想测试的音频文件路径
    result = recognizer.recognize(test_audio)
    print(f"识别结果：{result}")