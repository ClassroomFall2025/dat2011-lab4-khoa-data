class Sinh_vien:
    # các thuộc tính
    ten_sinh_vien = ""
    nam_sinh =""
    diem=""



    # các phuong thức
    def them_sinh_vien(self,ten,namsinhvien,diem):
        self.ten_sinh_vien = ten
        self.nam_sinh = namsinhvien
        self.diem = diem

    def xuat_thong_thong_tin (self):
        print(f"sinh viên{self.ten_sinh_vien},sinh năm {self.nam_sinh},điểm môn {self.diem}")

sv1 = Sinh_vien()
sv1.them_sinh_vien("Tuấn Chó điên",2005,0.5)
sv1.xuat_thong_thong_tin()