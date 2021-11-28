#创建 一个抽象工厂类，这个抽象工厂能够很好地去创建手机。
import abc

#产品区
class Cpu(metaclass=abc.ABCMeta):
    @staticmethod
    def showCpu():
        pass
class PingMU(metaclass=abc.ABCMeta):
    @staticmethod
    def showPinMU():
        pass
class Phone(metaclass=abc.ABCMeta):
    @staticmethod
    def show():
        pass

#产品区_实现类
class SUMSUNING_PM(PingMU):
    def showPinMU(self):
        print('三星屏幕//')
class LIANXIANG_PM(PingMU):
    def showPinMU(self):
        print('联想屏幕//')
class LIANFAKE_CPU(Cpu):
    def showCpu(self):
        print('联发科cpu...')
class GAOTONG_CPU(Cpu):
    def showCpu(self):
        print('高通cpu...')
class MiniPhone(Phone):
    def __init__(self,cpu,pinmu):
        self.cpu=cpu
        self.pinmu=pinmu
    def show(self):
        print('小米手机运行中...')
        self.cpu.showCpu()
        self.pinmu.showPinMU()
        print('小米手机运行结束...')
class HuaweiPhone(Phone):
    def __init__(self, cpu, pinmu):
        self.cpu = cpu
        self.pinmu = pinmu
    def show(self):
        print('华为手机运行中...')
        self.cpu.showCpu()
        self.pinmu.showPinMU()
        print('华为手机运行结束...')
class IPhonePhone(Phone):
    def __init__(self, cpu, pinmu):
        self.cpu = cpu
        self.pinmu = pinmu
    def show(self):
        print('苹果手机运行中...')
        self.cpu.showCpu()
        self.pinmu.showPinMU()
        print('苹果手机运行结束...')

#工厂类
class PhoneFactory(metaclass=abc.ABCMeta):
    @staticmethod
    def createPhone():
        pass
    @staticmethod
    def createCpu():
        pass
    @staticmethod
    def createPM():
        pass
#工厂类_实现类
class MiniFactory(PhoneFactory):
    def createCpu(self):
        return GAOTONG_CPU()
    def createPM(self):
        return LIANXIANG_PM()
    def createPhone(self):
        return MiniPhone(GAOTONG_CPU(),LIANXIANG_PM())
class HuaweiFactory(PhoneFactory):
    def createCpu(self):
        return GAOTONG_CPU()
    def createPM(self):
        return SUMSUNING_PM()
    def createPhone(self):
        return HuaweiPhone(GAOTONG_CPU(),SUMSUNING_PM())
class IPhoneFactory(PhoneFactory):
    def createCpu(self):
        return LIANFAKE_CPU()
    def createPM(self):
        return SUMSUNING_PM()
    def createPhone(self):
        return IPhonePhone(LIANFAKE_CPU(),SUMSUNING_PM())

def getPhone(factory):
    return factory.createPhone()

# 配置文件
if __name__ == '__main__':
    # IPhoneFactory().createPhone().show()
    # HuaweiFactory().createPhone().show()
    # MiniFactory().createPhone().show()
    p=getPhone(MiniFactory()).show()

