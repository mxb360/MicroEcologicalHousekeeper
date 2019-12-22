import os, sys
import configparser

from MicroEcologicalHousekeeper import Config

def _getValue(cf, sec, value):
    try:
        return cf.get(sec, value)
    except configparser.NoSectionError:
        pass


class ConfigData:
    def __init__(self, id_=''):
        self._get_ = False
        self._id_ = id_
        self._file_ = os.path.join(Config.dataFilePath, id_ + 'Config.dat')
        self._method_ = ['isConfigItem', 'isConfigData', 'getConfigData',
                        'setConfigData', 'printConfigData', 'getConfigDataAndCheck']

        print(id_ + '被创建...')

    def isConfigData(self):
        return False, "空配置"

    def _isConfigItem_(self, item):
        return not item.startswith("_") and item not in self._method_

    def isConfigItem(self, item):
        return item in dir(self) and self._isConfigItem_(item)

    def getConfigDataAndCheck(self, reload=False):
        self.getConfigData(reload)
        res, err = self.isConfigData()
        if not res:
            return False, err
        return True, self

    def getConfigData(self, reload=False):
        if self._get_ and not reload:
            for item in dir(self):
                if self._isConfigItem_(item):
                    setattr(self, item, getattr(self, '_' + item, None))
            return self

        configFileParser = configparser.ConfigParser()
        if Config.configFileName:
            configFileParser.read(Config.configFileName) 

        dataFileParser = configparser.ConfigParser()
        dataFileParser.read(self._file_)

        try:
            for item in dir(self):
                if self._isConfigItem_(item):
                    # 先在用户配置文件里读取
                    value = _getValue(configFileParser, self._id_, item)

                    # 然后在数据文件读取
                    if value is None:
                        value = _getValue(dataFileParser, self._id_, item)

                    # 最后在默认配置文件读取
                    if value is None:
                        attr = 'default' + self._id_[0].upper() + self._id_[1:] + item[0].upper() + item[1:]
                        value = getattr(Config, attr, None)

                    if value is not None:
                        value = str(value)
                    
                    setattr(self, item, value)
                    setattr(self, '_' + item, value)
        except Exception as e:
            print("警告：读取配置文件时出现了一个错误：", e)

        self._get = True
        return self

    def setConfigData(self):
        res, err = self.isConfigData()
        if not res:
            print("错误：保存配置时发生了错误：数据格式不正确：", err)
            return False, err

        dataFileParser = configparser.ConfigParser()
        dataFileParser.add_section(self._id_)

        try:
            for item in dir(self):
                if self._isConfigItem_(item):
                    dataFileParser.set(self._id_, item, getattr(self, item, None))

            os.makedirs(Config.dataFilePath, exist_ok=True)
            with open(self._file_, 'w') as f:
                dataFileParser.write(f)
        except Exception as e:
            print("错误：保存配置时发生了错误：", e)
            return False, str(e)
        return True, ""

    def printConfigData(self, file=sys.stdout):
        print('[%s]' % self._id_, file=file)
        for item in dir(self):
            if self._isConfigItem_(item):
                value = getattr(self, item, None)
                if value is not None:
                    print('%s = %s' % (item, value), file=file)
                else:
                    print('%s = (None)' % item, file=file)
        print()


class ServerConfigData(ConfigData):
    def __init__(self, id_="Server"):
        super().__init__(id_)

        self.host = None
        self.port = None

    def isConfigData(self):
        if not self.host.strip():
            return False, "主机为空！"

        try:
            if not 0 <= int(self.port) <= 65535:
                raise ValueError
        except ValueError:
            return False, "端口应该是0-65535之间的整数"

        return True, ""


class DeviceNameConfigData(ConfigData):
    def __init__(self, id_="DeviceName"):
        ConfigData.__init__(self, id_)

        self.name = None

    def isConfigData(self):
        if not self.name.strip():
            return False, "设备名称为空！"
        return True, ""

class HardwareConfigData(ConfigData):
    def __init__(self, id_='', enable_value=Config.EnableValue, use_value=Config.UseValue):
        super().__init__(id_ + 'Hardware')
        self._enable_value_ = enable_value
        self._use_value_ = use_value
    
        self.enable = None
        self.use = None
        self.inputEventFile = None
        self.outputEventFile = None

    def isConfigData(self):
        if self.enable not in self._enable_value_:
            return False, '%s里的enable值应为%s之一' % (self._id_, self._enable_value_)
        
        if self.use not in self._use_value_:
            return False, '%s里的use值应为%s之一' % (self._id_, self._use_value_)

        if not self.inputEventFile:
            return False, '%s里的inputEventFile值为空' % (self._id_)

        if not self.outputEventFile:
            return False, '%s里的outputEventFile值为空' % (self._id_)
        return True, ''

class OnePinHardwareConfigData(HardwareConfigData):
    def __init__(self, id_='OnePin',
                       enable_value = Config.EnableValue,
                       use_value = Config.UseValue, 
                       platform_value = Config.PlatformValue, 
                       status_value = Config.StatusValue):
        
        super().__init__(id_, enable_value, use_value)
        self._platform_value_ = platform_value
        self._status_value_ = status_value
    
        self.pin = None
        self.platform = None
        self.status = None

    def isConfigData(self):
        res, err = super().isConfigData()
        if not res:
            return False, err
        
        if not self.pin:
            return False, '%s里的pin值为空！' % (self._id_)

        if  self.platform not in self._platform_value_:
            return False, '%s里的platform值应为%s之一' % (self._id_, self._platform_value_)

        if  self.status not in self._status_value_:
            return False, '%s里的status值应为%s之一' % (self._id_, self._status_value_)

        return True, ''

class ValueHardwareConfigData(HardwareConfigData):
    def __init__(self, id_ = 'Value', 
                       enable_value = Config.EnableValue,
                       use_value = Config.UseValue,
                       min_value = None, 
                       max_value = None):
                    
        super().__init__(id_, enable_value, use_value)
        self._max_value_ = max_value
        self._min_value_ = min_value
    
        self.value = None

    def isConfigData(self):
        res, err = super().isConfigData()
        if not res:
            return False, err
        
        try:
            value = float(self.value)
            if self._max_value_ is None and value > self._max_value_:
                raise ValueError
            if self._min_value_ is None and value < self._min_value_:
                raise ValueError
        except ValueError:
            max_word = ('大于%d' % self._min_value_) if self._min_value_ else ''
            min_word = ('小于%d' % self._max_value_) if self._max_value_ else ''
            if max_word or min_word:
                max_min_word = max_word + min_word + '的'
            else:
                max_min_word = ''
            return '%s里的value值应该是一个' + max_min_word + '小数'

        return True, ''

class LedHardwareConfigData(OnePinHardwareConfigData):
    def __init__(self, id_='Led'):
        super().__init__(id_)


class TemperatureHardwareConfigData(ValueHardwareConfigData):
    def __init__(self, id_='Temperature'):
        super().__init__(id_)
    

class WaterLevelHardwareConfigData(ValueHardwareConfigData):
    def __init__(self, id_='WaterLevel'):
        super().__init__(id_, min_value=0, max_value=100)


class DrapWaterHardwareConfigData(OnePinHardwareConfigData):
    def __init__(self, id_='DrapWater'):
        super().__init__(id_)
    

class FeedHardwareConfigData(OnePinHardwareConfigData):
    def __init__(self, id_='Feed'):
        super().__init__(id_)


class SoundHardwareConfigData(HardwareConfigData):
    def __init__(self, id_ = 'Sound', use_value = Config.UseValue):            
        super().__init__(id_, use_value=use_value)

        self.file = None

    def isConfigData(self):
        res, err = super().isConfigData()
        if not res:
            return False, err

        if not self.file:
            return False, '%s里的file值为空' % (self._id_)
        return True, ''

class CameraHardwareConfigData(HardwareConfigData):
    def __init__(self, id_ = 'Camera', use_value = Config.UseValue):            
        super().__init__(id_, use_value=use_value)
        
        self.file = None
        self.streamUrl = None

    def isConfigData(self):
        res, err = super().isConfigData()
        if not res:
            return False, err

        if not self.file:
            return False, '%s里的file值为空' % (self._id_)

        if not self.streamUrl:
            return False, '%s里的streamUrl值为空' % (self._id_)

        return True, ''


class AllConfigData:
    serverConfigData = ServerConfigData()
    deviceNameConfigData = DeviceNameConfigData()
    ledHardwareConfigData = LedHardwareConfigData()
    temperatureHardwareConfigData = TemperatureHardwareConfigData()
    waterLevelHardwareConfigData = WaterLevelHardwareConfigData()
    drapWaterHardwareConfigData = DrapWaterHardwareConfigData()
    feedHardwareConfigData = FeedHardwareConfigData()
    soundHardwareConfigData = SoundHardwareConfigData()
    cameraHardwareConfigData = CameraHardwareConfigData()

    @staticmethod
    def printConfig(file=sys.stdout):
        AllConfigData.serverConfigData.getConfigData().printConfigData(file)
        AllConfigData.deviceNameConfigData.getConfigData().printConfigData(file)
        AllConfigData.ledHardwareConfigData.getConfigData().printConfigData(file)
        AllConfigData.temperatureHardwareConfigData.getConfigData().printConfigData(file)
        AllConfigData.waterLevelHardwareConfigData.getConfigData().printConfigData(file)
        AllConfigData.drapWaterHardwareConfigData.getConfigData().printConfigData(file)
        AllConfigData.feedHardwareConfigData.getConfigData().printConfigData(file)
        AllConfigData.soundHardwareConfigData.getConfigData().printConfigData(file)
        AllConfigData.cameraHardwareConfigData.getConfigData().printConfigData(file)

if __name__ == '__main__':
    AllConfigData.printConfig()
