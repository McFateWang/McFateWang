#账户对象
account = {
    'starting_cash': 0,
    'cash': 0,
    'value': 0,
    'positions': {
        'code': '000000',
        'buy_date': '2000-01-01',
        'buy_price': -1,
        'buy_num': -1,
    },
}

#初始化账户
def initial(starting_cash):
    account['starting_cash'] = starting_cash;
    account['cash'] = starting_cash;
    account['value'] = starting_cash;

#策略函数
def strategy(code, date):



#回测时间函数
def back_test(start, end):


"""量化主函数"""
#初始化账户资金
initial(1000000);
#选择时间回测
