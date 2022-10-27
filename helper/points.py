from enum import Enum

class PointType(str, Enum):
    # enum handle point type
    '''
    1.Shoppoint = Point promo toko
    2.RegisterAccount = Registrasi Akun baru

    '''
    ShopPoint = "shoppoint"
    RegisterAccount = "registeraccount"

class Currency(str, Enum):
    IDR = "IDR"
    JPY = "JPY"
    
