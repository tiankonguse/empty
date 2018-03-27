
# https://github.com/FutunnOpen/futuquant
# 依赖富途官方提供的API
import futuquant as ft
import time
import sys
quote_ctx = ft.OpenQuoteContext(host="127.0.0.1", port=1111)
quote_ctx.start()  # 开启异步数据接收

trade_us_ctx = ft.OpenUSTradeContext(host="127.0.0.1", port=1111)
trade_us_ctx.start()
trade_us_ctx.unlock_trade("交易密码的MD5","交易密码的MD5") # 解锁接口


stockNums = ["US.MON", "US.MSFT", "US.JD"]
todayIncrease = 1.2 # 今天涨幅
isGteCostToSell = True #是否大于成本出售
sellPriceIncr = 1.05 #卖出的价格是当前的价格的多少倍




def getMyStocks(ctx):
    ret_code, ret_data = ctx.position_list_query(envtype=0)  # 查询持仓列表
    if ret_code != 0:
        print("刷新个人持有股票信息错误:" + ret_data)
        return False
    return ret_data.set_index("code").to_dict('index')


selfStocks = getMyStocks(trade_us_ctx)
if selfStocks == False:
    print("获取自己持仓股票失败" + ret_data)
    sys.exit()



# 订阅股票信息(只订阅当前挂板价格)
for stockNum in stockNums:
    ret_code, ret_data = quote_ctx.subscribe(stockNum, "QUOTE")
    if ret_code != 0:
        print("订阅股票信息错误:" + ret_data)
        continue

print("Start!")

while(True):
    time.sleep(5)
    ret_code, state_dict = quote_ctx.get_global_state()
    if ret_code != 0:
        print("获取全局状态错误：" + ret_code)
        continue
    
    if state_dict["Market_US"] != "5":
        continue
    print("正在美国盘中时段！开始准备交易！")
    while True:
        ret_code, state_dict = quote_ctx.get_global_state()
        # 获取市场信息错误，或者已经不在盘中阶段，则退出快速循环
        if ret_code != 0 or state_dict["Market_US"] != "5":
            print("不在盘中时段或者获取市场信息错误，退出快速循环")
            break
        
        ret_code, ret_data = quote_ctx.get_stock_quote(stockNums)
        if ret_code != 0:
            print("获取股票详情错误：" + ret_data)
            time.sleep(1)
            continue
        ret_data = ret_data.set_index("code").to_dict('index')
        hasSelledStock = False
        for stockNum in stockNums:
            # 我没有有持有这个股票
            if stockNum not in selfStocks:
                continue

            stockData = ret_data[stockNum]
            selfStockData = selfStocks[stockNum]
			
	    # 当前价格低于成本价 不卖, 卖就亏光了
            if isGteCostToSell and selfStockData["cost_price"] > stockData["last_price"]:
                continue
            # 少于设定增长幅度，不卖，手续费都赚不回来
            if (stockData["last_price"] - stockData["open_price"]) / stockData["open_price"] * 100 < todayIncrease:
                continue
            
            # 判断持有这个股票是否有效
            if selfStockData["cost_price_valid"] != 1 or selfStockData["can_sell_qty"] < 1:
                continue

            # 都满足上面的条件,卖都卖光
            sellPrice = stockData["last_price"] * sellPriceIncr
            ret_code, ret_data = trade_us_ctx.place_order(sellPrice, selfStockData["can_sell_qty"], stockNum, orderside=1, ordertype=2, envtype=0) # 下单接口
            if ret_code != 0:
                print("出售股票：" + stockNum + " 失败，失败原因是：" + ret_data)
                continue
            # 下单成功
            print("出售股票: " + stockNum + " 价格为: " + sellPrice + " 收益为: " + str(sellPrice - selfStockData["cost_price"]))
            hasSelledStock = True

        if hasSelledStock:
            #刷新个人股票信息
            _selfStocks = getMyStocks(trade_us_ctx)
            if _selfStocks == False:
                print("刷新个人持有股票信息错误:" + ret_data)
            else:
                selfStocks = _selfStocks
                print("----------个人持有股票信息----------------")
                print(selfStocks)

        time.sleep(1)
