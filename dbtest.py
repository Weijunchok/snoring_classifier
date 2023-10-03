import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
# Load audio file with librosa
y,sr = librosa.load('1_0.wav')
print(y.shape)
# Plot the spectrogram
D = librosa.stft(y)  # STFT of y
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
print(S_db)
print(S_db.shape)
y, sr = librosa.load('1_0.wav')
librosa.display.waveshow(y)
plt.figure()
plt.plot(S_db, x_axis='time', y_axis='hz')
plt.show()

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
 
# 读取音频，采样率为44100Hz，持续时间为2秒
y, sr = librosa.load('1_0.wav')
 
# 将 stft 之后的 幅度值的绝对值 转换为 分贝值，将返回值传入specshow()方法中
data = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
data2 = np.concatenate([data, data], axis=1)
print(data.shape)
print(data2.shape)
print(np.average(data))
# 绘制图像
fig, ax = plt.subplots(1,1)
# x轴是时间（单位：秒），y轴是由fft窗口和采样率决定的频率值（单位：Hz）
img = librosa.display.specshow(data2, sr=sr, x_axis='time', y_axis='linear')
plt.ylim(0, 8500) # 8000Hz以上没有能量显示，因此y轴上限设为8500
plt.title('Specshow', fontproperties="SimSun")
fig.colorbar(img, ax=ax, format="%+2.f dB")
plt.show()
