# 观察者模式：推送者，订阅者，
from abc import abstractmethod, ABCMeta


# 用于发布所有信息
class Pusher(metaclass=ABCMeta):
    @abstractmethod
    def push_all(self):
        pass

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass


class Receiver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, msg):
        pass


class Staff(Receiver):
    def __init__(self):
        self.company_msg = None

    def update(self, msg):
        self.company_msg = msg


class Message:
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return self.msg


class CompanyPusher(Pusher):
    def __init__(self, receivers=[]):
        self.receivers = receivers
        self.__msg = None

    def attach(self, receiver):
        self.receivers.append(receiver)

    def detach(self, receiver):
        self.receivers.remove(receiver)

    def push_all(self):
        for receiver in self.receivers:
            receiver.update(self.__msg)

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value
        self.push_all()


if __name__ == '__main__':
    R1 = Staff()
    R2 = Staff()
    print(R1.company_msg)
    print(R1.company_msg)
    c = CompanyPusher(receivers=[R1, R2])
    c.msg = Message('这是初始化的信息！！')
    print(R1.company_msg)
    print(R2.company_msg)
    c.msg = Message('推广会！！')
    print(R1.company_msg)
    print(R2.company_msg)
