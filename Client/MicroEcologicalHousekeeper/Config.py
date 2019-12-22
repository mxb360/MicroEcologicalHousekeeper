import os, socket

# 当前项目的根路径
rootPath = os.path.abspath(os.path.dirname(__file__))

# 数据保存目录
dataFilePath = os.path.join(rootPath, "Data/data")
inputEventFilePath = os.path.join(rootPath, "Data/input-event")
outputEventFilePath = os.path.join(rootPath, "Data/output-event")

# 用户配置文件
configFileName = None

# 一些配置的取值
EnableValue = ['True', 'False']
UseValue = ['EventFiles', 'PinListen', 'VirtualDevice']
PlatformValue = ['RaspberryPi', 'JZ2440']
StatusValue = ['ON', 'OFF']

SoundUseValue = ['EventFiles', 'LocalSound', 'LocalFile']
CameraUseValue = ['EventFiles', 'LocalCamera', 'LocalFile', 'StreamUrl']


# 服务器默认配置
defaultServerHost = "localhost"
defaultServerPort = 8800

# 设备名字默认配置
defaultDeviceNameName = socket.gethostname()

# Led 默认配置
defaultLedHardwareEnable = EnableValue[0]
defaultLedHardwareUse = UseValue[2]
defaultLedHardwareInputEventFile = os.path.join(inputEventFilePath, 'led')
defaultLedHardwareOutputEventFile = os.path.join(outputEventFilePath, 'led')
defaultLedHardwarePin = 'pin0'
defaultLedHardwarePlatform = PlatformValue[0]
defaultLedHardwareStatus = StatusValue[1]

# 温度传感器默认配置
defaultTemperatureHardwareEnable = EnableValue[0]
defaultTemperatureHardwareUse = UseValue[1]
defaultTemperatureHardwareInputEventFile = os.path.join(inputEventFilePath, 'temperature')
defaultTemperatureHardwareOutputEventFile = os.path.join(outputEventFilePath, 'temperature')
defaultTemperatureHardwareValue = '22.5'

# 水位传感器默认配置
defaultWaterLevelHardwareEnable = EnableValue[0]
defaultWaterLevelHardwareUse = UseValue[1]
defaultWaterLevelHardwareInputEventFile = os.path.join(inputEventFilePath, 'water-level')
defaultWaterLevelHardwareOutputEventFile = os.path.join(outputEventFilePath, 'water-level')
defaultWaterLevelHardwareValue = '75'

# 抽水电机控制器默认设置
defaultDrapWaterHardwareEnable = EnableValue[0]
defaultDrapWaterHardwareUse = UseValue[2]
defaultDrapWaterHardwareInputEventFile = os.path.join(inputEventFilePath, 'drap-water')
defaultDrapWaterHardwareOutputEventFile = os.path.join(outputEventFilePath, 'drap-water')
defaultDrapWaterHardwarePin = 'pin0'
defaultDrapWaterHardwarePlatform = PlatformValue[0]
defaultDrapWaterHardwareStatus = StatusValue[1]

# 喂食设备控制器默认设置
defaultFeedHardwareEnable = EnableValue[0]
defaultFeedHardwareUse = UseValue[2]
defaultFeedHardwareInputEventFile = os.path.join(inputEventFilePath, 'feed')
defaultFeedHardwareOutputEventFile = os.path.join(outputEventFilePath, 'feed')
defaultFeedHardwarePin = 'pin0'
defaultFeedHardwarePlatform = PlatformValue[0]
defaultFeedHardwareStatus = StatusValue[1]

# 麦克风默认配置
defaultSoundHardwareEnable = EnableValue[0]
defaultSoundHardwareUse = SoundUseValue[1]
defaultSoundHardwareInputEventFile = os.path.join(inputEventFilePath, 'sound')
defaultSoundHardwareOutputEventFile = os.path.join(outputEventFilePath, 'sound')
defaultSoundHardwareFile = ''

# 摄像头默认配置
defaultCameraHardwareEnable = EnableValue[0]
defaultCameraHardwareUse = CameraUseValue[1]
defaultCameraHardwareInputEventFile = os.path.join(inputEventFilePath, 'camera')
defaultCameraHardwareOutputEventFile = os.path.join(outputEventFilePath, 'camera')
defaultCameraHardwareFile = ''
defaultCameraHardwareStreamUrl = 'http://localhost:8800'
