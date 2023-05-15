## 仅需 15 行 Python 代码，即可将视频文件转录为文本稿件

将视频转录为文本稿件可能是一项耗时的任务，特别是如果您需要处理大量内容。幸运的是，您可以使用 Python 和一些开源库来自动化该过程并达到高准确率。在本教程中，我们将展示如何仅使用 15 行 Python 代码以 97% 的准确率转录视频。

### 先决条件

在开始之前，您需要在计算机上安装 Python 以及我们将要使用的几个库。要安装必要的库，请在终端中运行以下命令：

```python
pip install -r requirements.txt
```

SpeechRecognition 是一个库，可以在音频文件上执行语音识别；而 pydub 是一个库，可以在多种格式的音频文件上进行操作。

### 安装 FFmpeg

FFFmpeg 是用于录制、转换和流式传输音频和视频的完整跨平台解决方案。官网地址是：https://ffmpeg.org/

具体安装步骤参考官网或博客，在此不做详细描述。

### 转录视频

转录视频的第一步是从视频文件中提取音频。在本教程中，我们将使用 MP4 文件，但您也可以使用其他格式。

```python
import speech_recognition as sr
from pydub import AudioSegment
import os

# Load the video file
video = AudioSegment.from_file("assets/v0200fg10000cg43lhbc77u3eckjg6pg.mp4", format="mp4")
audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
audio.export("output/audio.wav", format="wav")
```

在此代码中，我们使用 pydub 的 AudioSegment 类加载视频文件并提取音频。然后，我们将音频设置为单声道、16kHz、16 位，这是 SpeechRecognition 库所要求的格式。最后，我们将音频导出为 WAV 文件。

现在，我们有了音频文件，我们可以使用 SpeechRecognition 库将其转录为文本。以下是实现此操作的代码：

```python
# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Open the audio file
with sr.AudioFile("output/audio.wav") as source:
    audio_text = r.record(source)
# Recognize the speech in the audio
text = r.recognize_google(audio_text, language='en-US')
```

在此代码中，我们初始化 SpeechRecognition 的 Recognizer 类并打开音频文件。然后，我们使用 record 方法读取音频并将其存储在 audio_text 变量中。最后，我们使用 recognize_google 方法将音频转录为文本，并将结果存储在 text 变量中。

> 注：如果视频内容是中文，请将 language 参数更改为 'zh-CN'，还有个需要注意的国内网络问题，你需要解决网络的问题，有可能会提示网络不正常的错误

### 保存文本稿

最后一步是将文本稿保存到文件中。以下是实现此操作的代码：

```python
# Print the transcript
file_name = "output/transcription.txt"

with open(file_name, "w") as file:
    # Write to the file
    file.write(text)
# Open the file for editing by the user
os.system(f"start {file_name}")
```

在此代码中，我们创建了一个名为 transcription.txt 的新文件，并将文本稿写入其中。然后，我们使用 os 库打开该文件供用户编辑。这行代码可能会因您的操作系统而略有不同，因此您可能需要相应地进行调整。

### 欢迎交流

<img src="https://github.com/yinshipeng/langchain-chatbox-pdf/blob/main/visual-guide/me.jpg" width="180px">
