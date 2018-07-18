#验证功能装饰器 2.0
user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'}
]

current_dic={'username':None,'login':False}

def auth_func(func):
    def wrapper(*args,**kwargs):
        if current_dic['username'] and current_dic['login']:
            res = func(*args, **kwargs)
            return res
        username = input('用户名').strip()
        passwd = input('密码').strip()
        for user_dic in user_list:
            if username == user_dic['name'] and passwd == user_dic['passwd']:
                current_dic['username'] = username
                current_dic['login'] = True
                res = func(*args, **kwargs)
                return res
        else:
            print('用户名或者密码错误')
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

print('before-->',current_dic)
index()
home('产品经理')
print('after-->',current_dic)
#shopping_car('产品经理')