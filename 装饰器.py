'''
通用装饰器
def rapper(fn): wrapper: 装饰器， fn：目标函数
    def inner（*args, **kwargs):
        #在目标函数执行之前。。。。
        ret = fn(args, **kwargs)   #执行目标函数
        #在目标函数执行之后。。。
        return ret
    return inner     #千万别加括号()

'''
'''
一个函数可以被多个装饰器装饰
如果装饰器层层嵌套，比如
@wrapper1
@wrapper2
def(target)


这时输出的结果是： wrapper1, wrapper2 target wrapper2 wrapper1
'''

def guanjia(game):
    def inner(*args, **kwargs):   ##制作闭包对功能进行封装，以进行装饰器作用
        print("打开外挂")
        ret = game(*args, **kwargs)
        print("关闭外挂")
        return ret
    return inner

@guanjia
def play_dnf(username, password):
    print("我要开始玩dnf了，", username, password)
    print("你好啊，我叫赛利亚，今天又是美好的一天！")
    return "一把屠龙刀"

def play_lol(username, password, hero):
    print("我要开始玩lol了", username, password, hero)
    print('德玛西亚！！！！')

ret = play_dnf("admin", "12345")
print(ret)

'''登陆系统实战（装饰器）'''

login_flag =False

def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag   #对全局变量进行引入
        if login_flag ==False:
            #如果判断登陆状态是False，就要进行验证，如果为True，就继续下面步骤
            print("还没完成登录操作")
            while 1:  #创建while true循环，当用户输入错登录账号和密码的时候，可以再次循环，输入
                username = input(">>>")
                password = input(">>>")
                if username == "admin" and password =="123":
                    print("登陆成功")
                    login_flag =True
                    break
                else:
                    print('登陆失败，用户名或密码错误')
        ret = fn(*args, **kwargs)
        return ret
    return inner
@login_verify
def add():
    print('添加员工信息')
@login_verify
def delete():
    print('删除员工信息')


@login_verify
def upd():
    print('更新员工信息')


@login_verify
def search():
    print('查找员工信息')

add()
delete()
upd()
search()

