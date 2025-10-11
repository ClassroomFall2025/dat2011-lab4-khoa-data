def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10 and so_nuoc >= 0:
        tien_nuoc_trong_thang = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc_trong_thang = (10 * gia_ban_nuoc[0]) + ((so_nuoc - 10) * gia_ban_nuoc[1])
    elif so_nuoc <= 30:
        tien_nuoc_trong_thang = (10 * gia_ban_nuoc [0]) + (10 * gia_ban_nuoc[1]) + ((so_nuoc - 20) * gia_ban_nuoc[2])
    elif so_nuoc > 30:
        tien_nuoc_trong_thang = (10 * gia_ban_nuoc [0]) + (10 * gia_ban_nuoc[1]) + (10 * gia_ban_nuoc[2]) + ((so_nuoc - 30) * gia_ban_nuoc[3])
    return tien_nuoc_trong_thang


def tinh_nguyen_lieu (sl_banh_dau_xanh, sl_banh_thap_cam, sl_banh_deo):
    banh_dau_xanh = {"Duong":0.04, "Dau":0.07}
    banh_thap_cam = {"Duong":0.06, "Dau":0}
    banh_deo = {"Duong":0.05, "Dau":0.02}
    nguyen_lieu_lam_banh = {}
    Duong_hop_banh = sl_banh_dau_xanh * banh_dau_xanh["Duong"] + sl_banh_thap_cam * banh_thap_cam["Duong"] + sl_banh_deo * banh_deo["Duong"]
    Dau_hop_banh = sl_banh_dau_xanh * banh_dau_xanh["Dau"] + sl_banh_thap_cam * banh_thap_cam["Dau"] + sl_banh_deo * banh_deo["Dau"]
    nguyen_lieu_lam_banh["Duong"] = Duong_hop_banh
    nguyen_lieu_lam_banh["Dau"] = Dau_hop_banh
    return nguyen_lieu_lam_banh

