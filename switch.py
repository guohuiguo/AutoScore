from pydub import AudioSegment
import os

def audio_to_wav(input_path, output_path):
    """
    将音频文件转换为 WAV 格式

    :param input_path: 输入音频文件的路径，可以是 MP3、M4A、WAV 等格式
    :param output_path: 输出 WAV 文件的路径
    """
    try:
        # 只对非 WAV 文件进行转换
        if not input_path.lower().endswith('.wav'):
            # 加载输入音频文件（支持多种格式：MP3、M4A、WAV 等）
            audio = AudioSegment.from_file(input_path)
            # 将音频导出为 WAV 格式
            audio.export(output_path, format="wav")
            print(f"成功将 {input_path} 转换为 {output_path}")
        else:
            # 如果已经是 WAV 格式，直接复制文件
            os.rename(input_path, output_path)
            print(f"{input_path} 已是 WAV 格式，无需转换。")
    except Exception as e:
        print(f"转换失败: {e}")
