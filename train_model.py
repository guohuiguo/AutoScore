from GMM_SpeakerRecognition import GMM_SpeakerRecognition, get_training_data

if __name__ == "__main__":
    recognizer = GMM_SpeakerRecognition()
    root_folder = '/Users/guoguohui/PythonProject/AutoScore/训练录音'  # 修改为你的训练音频文件夹路径

    # 获取训练数据
    training_data = get_training_data(root_folder)

    # 对每个说话人训练模型
    for speaker, audio_paths in training_data.items():
        recognizer.train(speaker, audio_paths)

    # 保存训练好的模型
    recognizer.save_model("gmm_models.joblib")
    print("模型训练完成并已保存。")