#验证功能装饰器1.0

user_dic={'username':None,'login':None}

def auth_func(func):
    def wrapper(*args,**kwargs):
        if user_dic['username'] and user_dic['login']:
            res = func(*args, **kwargs)
            return res
        username = input('用户名').strip()
        passwd = input('密码').strip()
        if username == 'sb' and passwd == '123':
            user_dic['username']=username
            user_dic['login'] = True
            res = func(*args,**kwargs)
            return res
        else:
            print('用户名或密码错误')
    return wrapper

@auth_func
def index():
    print('欢迎来到京东主页')

@auth_func
def home(name):
    print('欢迎回家%s' %name)

@auth_func
def shopping_car(name):
    print('%s的购物车里有[%s,%s,%s]'%(name,'奶茶','可乐','薯片'))


index()
home('产品经理')
shopping_car('产品经理')

