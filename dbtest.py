# import librosa
# import librosa.display
# import matplotlib.pyplot as plt
# import numpy as np
# # Load audio file with librosa
# y,sr = librosa.load('1_0.wav')
# print(y.shape)
# # Plot the spectrogram
# D = librosa.stft(y)  # STFT of y
# S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
# print(S_db)
# print(S_db.shape)
# y, sr = librosa.load('1_0.wav')
# librosa.display.waveshow(y)
# # plt.figure()
# # plt.plot(S_db, x_axis='time', y_axis='hz')
# plt.show()

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


# import wave
# import numpy as np
# import matplotlib.pyplot as plt
# 
# 
# # 分析音量、分贝的图形
# def analyze_db():
#     # 开发wav音频文件
#     wf = wave.open('./1_0.wav', 'r')
#     
#     # 设置每次读取块的大小
#     chunk = 1024
# 
#     # 用来添加音量的数组
#     value1 = []  # 绝对值的平均值
#     value2 = []  # 对数
# 
#     # 对每1024块的声音进行分析
#     while True:
# 
#         # 每次读取1024
#         stream_data = wf.readframes(chunk)
#         print(stream_data)
# 
#         # 当数据为空的时候，退出
#         if stream_data == b'':
#             break
# 
#         # 每块对应的声音分贝
#         data = np.fromstring(stream_data, dtype=np.int16)
#         # print(data)  # [ 11   8  15 ... -39  -5  12] 是这种数据
# 
#         # 算法1
#         db1 = np.average(np.abs(data)) * 2
# #         # 算法2
# #         db2 = 10 * np.log10(np.sum(data * data))
# 
#         # 只取整数
#         value1.append(int(str(db1).strip().split('.')[0]))
# #         value2.append(int(str(db2).strip().split('.')[0]))
# 
#     # 关闭
#     wf.close()
# 
#     length1 = len(value1)
#     x1 = np.arange(0, length1)
#     y1 = np.array(value1)
#     print(x1, y1)
# 
# #     length2 = len(value2)
# #     x2 = np.arange(0, length2)
# #     y2 = np.array(value2)
#     # print(x, y)
# 
#     # 绘制波形图
#     plt.xlabel('length1')
#     plt.ylabel('value1')
#     plt.plot(x1, y1, c='r')
# 
# #     # 绘制波形图
# #     plt.subplot(2, 1, 2)
# #     plt.xlabel('length2')
# #     plt.ylabel('value2')
# #     plt.plot(x2, y2, c='r')
#     plt.show()
# 
# 
# if __name__ == '__main__':
#     analyze_db()