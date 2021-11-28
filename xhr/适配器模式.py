# 老的应用
import abc
class Payment(metaclass=abc.ABCMeta):
    def pay(self):
        pass

class AliPay(Payment):
    def pay(self):
        print('阿里支付了！')

class TencePay(Payment):
    def pay(self):
        print('腾讯支付了！')


class YinlianPay:
    def cost(self):
        print('银联支付了!')

#1.继承方式实现适配器(类适配利器)
class YinlianPayApater(YinlianPay,Payment):
    def pay(self):
        self.cost()

#2.组合方式实现适配器(对象适配器)
class YinlianPayApater2(Payment):
    def __init__(self,payment):
        self.payment=payment
    def pay(self):
        self.payment.cost()


#支付系统
class PaymentSystem:
    def __init__(self,payment):
        self.payment=payment
    def autopay(self):
        self.payment.pay()
if __name__ == '__main__':
    PaymentSystem(TencePay()).autopay()
    PaymentSystem(AliPay()).autopay()
    PaymentSystem(YinlianPayApater()).autopay()
    PaymentSystem(YinlianPayApater2(YinlianPay())).autopay()