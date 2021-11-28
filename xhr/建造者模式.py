# 建造者模式用于关注建造对象的顺序
# 创建游戏角色
import abc
class arm(metaclass=abc.ABCMeta):
    pass
class body(metaclass=abc.ABCMeta):
    pass
class head(metaclass=abc.ABCMeta):
    pass
class foot(metaclass=abc.ABCMeta):
    pass
class 恶魔_arm(arm):
    pass
class 恶魔_body(body):
    pass
class 恶魔_head(head):
    pass
class 恶魔_foot(foot):
    pass
class player(metaclass=abc.ABCMeta):
    pass
class 恶魔_player(player):
    def __init__(self,arm=None,body=None,head=None,foot=None):
        self.arm=arm
        self.body=body
        self.head=head
        self.foot=foot
class playerFactory(metaclass=abc.ABCMeta):# 用于创建玩家
    @staticmethod
    def createArm(self):
        pass
    @staticmethod
    def createBody(self):
        pass
    @staticmethod
    def createHead(self):
        pass
    @staticmethod
    def createFoot(self):
        pass
    @staticmethod
    def createPlayer(self):
        pass
class 恶魔_factory(playerFactory):
    def createArm(self):
        print('创建恶魔的手臂')
        return 恶魔_arm()
    def createBody(self):
        print('创建恶魔的身体')
        return 恶魔_body()
    def createHead(self):
        print('创建恶魔的头')
        return 恶魔_head()
    def createFoot(self):
        print('创建恶魔的脚')
        return 恶魔_foot()
    def createPlayer(self,arm=None,body=None,head=None,foot=None):
        return 恶魔_player(arm=arm,body=body,head=head,foot=foot)
class builder:#注重建造的顺序
    def __init__(self,factory:playerFactory):
        self.factory=factory
    def buildPlayer(self):
        arm=self.factory.createArm()
        body=self.factory.createBody()
        foot=self.factory.createFoot()
        head=self.factory.createHead()
        return self.factory.createPlayer(arm,body,foot,head)
if __name__ == '__main__':
    p=builder(恶魔_factory()).buildPlayer()
    print(p)