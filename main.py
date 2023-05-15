import speech_recognition as sr
from pydub import AudioSegment
import os

# 加载视频文件
video = AudioSegment.from_file(
    "assets/v0200fg10000cg43lhbc77u3eckjg6pg.mp4", "mp4")
# 将音频设置为单声道、16kHz、16位
audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
# 导出音频为 WAV 文件
audio.export("output/audio.wav", format="wav")

# 初始化 Recognizer 类（用于语音识别）
r = sr.Recognizer()

# 打开音频文件
with sr.AudioFile("output/audio.wav") as source:
    audio_text = r.record(source)

# 识别音频中的语音
text = r.recognize_google(audio_text, language='zh-CN')

# 打印转录结果
file_name = "output/transcription.txt"
with open(file_name, "w") as file:
    # 将转录结果写入文件
    file.write(text)

# 打开文件供用户编辑
os.system(f"start {file_name}")
