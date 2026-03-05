class Product():
    def __init__(self, name, price, wieght_kg, shipping_cost):
        self.name = name
        self.price = price
        self.wieght_kg = wieght
        self.shipping_cost = shipping_cost
    
    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)
        print(f"New price for {self.name}: £{self.price:.2f}")

    def get_details(self):
        return f"Product: {self.name} Price: £{self.price}"
   
class digital_product(Product):
    def __init__(self, name, price, file_size_mb, download_link):
        super().__init__(name, price)
       
        self.file_size_mb = file_size_mb
        self.download_link = download_link
    
    def download_link(self):
        return f"https://store.com/download/{self.name.}"
   
class in_store_product(Product):
    def __init__(self, name, price, wieght_kg, __sku_code):
        super().__init__(name, price, wieght_kg)
        self.__sku_code = sku_code
        
    def pay_instore(self):
        return f"Product: {self.name} Price: £{self.price} SKU Code: {self.__sku_code}"
   
class delivered_product(Product):
    def __init__(self, name, price, shipping_cost, __delivery_address, estimated_time_min):
        super().__init__(name, price, shipping_cost)
       
        self.__delivery_address = delivery_address
        self.estimated_time_min = estimated_time_min
        
       
   

   
 
   
ebook = digital_product("Python for Beginners", 29.99, 15, "https://downloads.com/py-book")
software_key = digital_product("Visual Studio Code", 199.00, 1200, "https://license-portal.com/get-key")
album = digital_product("Studio Addict", 9.99, 45.2, "https://music.site/download")

keyboard = in_store_product("Keychron Q1 Mechanical Keyboard with RGB", 220.00, 1.5, "SKU-KB-992")
bottle = in_store_product("Air Up Water Bottle (1L)", 25.00, 0.4, "SKU-WB-101")
headphones = in_store_product("Sony XM5 Wireless with Active Noise Cancelling", 350.00, 0.45, "SKU-HP-X500")

pizza = delivered_product("Large Pepperoni Pizza", 18.50, "123 Main St", 30)
flowers = delivered_product("Bouquet of Red Roses", 45.00, "456 Oak Ave", 120)
coffee_sub = delivered_product("Monthly Bean Subscription", 35.00, "789 Pine Rd", 1440)
