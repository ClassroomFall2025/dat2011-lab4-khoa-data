class Sanpham: 
    
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.__giam_gia = giam_gia

    #def doc_giam_gia(self):
    #    self.__giam_gia
    #def __phi_giam_gia(self, giam_gia_moi):
    #    self.__giam_gia = giam_gia_moi
    def thue_nhap_khau(self):
        return self.gia * 0.1
    def nhap_thong_tin_sp(self):
        self.ten_san_pham = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("giam gia: "))
        self.thue_nhap_khau = float(input("thue nhap khau: "))
    def xuat_thong_tin_sp(self):
        print(f"Tên sản phẩm: {self.ten_san_pham} có giá {self.gia} và được giảm giá {self.__giam_gia} vaà thuế nhập khẩu là {self.thue_nhap_khau()}")
    def __str__(self):
        return f"Sản phẩm {self.ten_san_pham} có giá {self.gia} và được giảm giá {self.__giam_gia} và thuế nhập khẩu là {self.thue_nhap_khau()}"
sp1 = Sanpham("Bánh mì", 10000, 20000)
sp1.xuat_thong_tin_sp()
print(sp1)
