# 创建一个包含100个产品信息的字典
productInfo = {
    "product1": {"productName": "MSI GeForce RTX 4090 GAMING X TRIO 24G", "price": 14999.0, "inventory": 50},
    "product2": {"productName": "MSI GeForce RTX 4080 SUPRIM X 16GB", "price": 9999.0, "inventory": 50},
    "product3": {"productName": "MSI GeForce RTX 4070Ti SUPRIM 12G", "price": 7499.0, "inventory": 50},
    "product4": {"productName": "MSI GeForce RTX 4070 GAMING X TRIO 12G", "price": 5199.0, "inventory": 50},
    "product5": {"productName": "MSI GeForce RTX 4060Ti GAMING X 8G", "price": 3299.0, "inventory": 50},
    "product6": {"productName": "MSI GeForce RTX 4060 GAMING X  NV EDITION 8G", "price": 2699, "inventory": 50},
    "product7": {"productName": "NVIDIA Tesla H100 80G ", "price": 309999.0, "inventory": 50},
    "product8": {"productName": "MSI GeForce RTX 4050 Ti GAMING X 6G", "price": 1899.0, "inventory": 50},
    "product9": {"productName": "MSI GeForce RTX 4050 GAMING X 6G", "price": 1599.0, "inventory": 50},
    "product10": {"productName": "NVIDIA Quadro P5000 16GB", "price": 13999.0, "inventory": 50},
    "product11": {"productName": "NVIDIA Quadro P4000 8GB", "price": 7499.0, "inventory": 50},
    "product12": {"productName": "MSI NVIDIA Quadro P3400", "price": 1899.0, "inventory": 50},
    "product13": {"productName": "AMD Radeon RX 6800 XT", "price": 7999.0, "inventory": 50},
    "product14": {"productName": "AMD Radeon RX 6700 XT", "price": 5999.0, "inventory": 50},
    "product15": {"productName": "AMD Radeon RX 6600 XT", "price": 3999.0, "inventory": 50},
    "product16": {"productName": "AMD Radeon RX 6500 XT", "price": 2399.0, "inventory": 50},
    "product17": {"productName": "AMD Radeon RX 6400", "price": 1799.0, "inventory": 50},
    "product18": {"productName": "ASUS TUF-RTX3080-O8G-GAMING", "price": 7499.0, "inventory": 50},
    "product19": {"productName": "ASUS TUF-RTX3070-O8G-GAMING", "price": 4999.0, "inventory": 50},
    "product20": {"productName": "ASUS TUF-RTX3060-O6G-GAMING", "price": 3299.0, "inventory": 50},
    "product21": {"productName": "ZOTAC RTX3080天启AMP", "price": 6999.0, "inventory": 50},
    "product22": {"productName": "ZOTAC RTX3070天启AMP", "price": 4399.0, "inventory": 50},
    "product23": {"productName": "ZOTAC RTX3060天启AMP", "price": 2699.0, "inventory": 50},
    "product24": {"productName": "NVIDIA GeForce GTX 1660 SUPER", "price": 1899.0, "inventory": 50},
    "product25": {"productName": "NVIDIA GeForce GTX 1650", "price": 1199.0, "inventory": 50},
    "product26": {"productName": "Intel UHD Graphics P63VRV", "price": 324.84, "inventory": 5},
    "product27": {"productName": "Intel UHD Graphics P66", "price": 325.84, "inventory": 5},
    "product28": {"productName": "Intel UHD Graphics P630", "price": 324.84, "inventory": 5},
    "product29": {"productName": "Intel UHD Graphics P63VRV", "price": 324.84, "inventory": 5},
    "product30": {"productName": "Intel UHD Graphics P760", "price": 624.84, "inventory": 5},
    "product31": {"productName": "NVIDIA GeForce GTX 2880Ti", "price": 2199.0, "inventory": 50},
    "product32": {"productName": "NVIDIA GeForce GTX 1850", "price": 1899.0, "inventory": 50},
    "product33": {"productName": "NVIDIA GeForce GTX 1650", "price": 1199.0, "inventory": 50},
    "product34": {"productName": "AMD Radeon RX 6300", "price": 1399.0, "inventory": 50},
    "product35": {"productName": "AMD Radeon RX 6200", "price": 1199.0, "inventory": 50},
    "product36": {"productName": "AMD Radeon RX 6100", "price": 1099.0, "inventory": 50},
    "product37": {"productName": "AMD Radeon RX 5900", "price": 999.0, "inventory": 50},
    "product38": {"productName": "AMD Radeon RX 5800", "price": 899.0, "inventory": 50},
    "product39": {"productName": "AMD Radeon RX 5700", "price": 799.0, "inventory": 50},
    "product40": {"productName": "AMD Radeon RX 5600", "price": 699.0, "inventory": 50},
    "product41": {"productName": "AMD Radeon RX 5500", "price": 599.0, "inventory": 50},
    "product42": {"productName": "AMD Radeon RX 5400", "price": 499.0, "inventory": 50},
    "product43": {"productName": "AMD Radeon RX 5300", "price": 399.0, "inventory": 50},
    "product44": {"productName": "AMD Radeon RX 5200", "price": 299.0, "inventory": 50},
    "product45": {"productName": "AMD Radeon RX 5100", "price": 199.0, "inventory": 50},
    "product46": {"productName": "AMD Radeon RX 5000", "price": 99.0, "inventory": 50},
    "product47": {"productName": "AMD Radeon RX 4900", "price": 89.0, "inventory": 50},
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
