# 创建一个包含100个产品信息的字典
productInfo = {
    "product1": {"productName": "商品1", "price": 10.0, "inventory": 50},
    "product2": {"productName": "商品2", "price": 15.0, "inventory": 30},
    # 添加更多产品信息...
}

# 创建一个空的购物车集合
shoppingCart = set()

# 浏览商品
def browseProducts():
    print("可用商品:")
    for key, value in productInfo.items():
        print(f"{key}: {value['productName']} - 价格: {value['price']}元 - 库存: {value['inventory']}")

# 添加商品到购物车
def addToCart(productName, quantity):
    if productName in productInfo:
        product = productInfo[productName]
        if product["inventory"] >= quantity:
            for _ in range(quantity):
                shoppingCart.add(productName)
            productInfo[productName]["inventory"] -= quantity
            print(f"{quantity} 个 '{product['productName']}' 已添加到购物车。")
        else:
            print(f"'{product['productName']}' 库存不足。")
    else:
        print("商品不存在。")

# 查看购物车
def viewCart():
    print("购物车内容:")
    for item in shoppingCart:
        product = productInfo[item]
        print(f"{product['productName']} - 数量: {shoppingCart.count(item)}")

# 结账
def checkout():
    total = 0
    for item in shoppingCart:
        total += productInfo[item]["price"] * shoppingCart.count(item)
        productInfo[item]["inventory"] += shoppingCart.count(item)
    print(f"总计: {total}元")
    shoppingCart.clear()
    print("结账成功！购物车已清空。")

# 主程序
while True:
    print("\n在线商店")
    print("1. 浏览商品")
    print("2. 添加商品到购物车")
    print("3. 查看购物车")
    print("4. 结账")
    print("5. 退出")

    choice = input("请选择操作 (1/2/3/4/5): ")

    if choice == '1':
        browseProducts()
    elif choice == '2':
        productName = input("请输入商品名称: ")
        quantity = int(input("请输入数量: "))
        addToCart(productName, quantity)
    elif choice == '3':
        viewCart()
    elif choice == '4':
        checkout()
    elif choice == '5':
        print("退出系统。")
        break
    else:
        print("无效的选项，请重新选择。")
