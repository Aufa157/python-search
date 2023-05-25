def mencari_nomer_telepon(nama,buku_tlepon):
    for nama_kontak , nomer_telepon in buku_tlepon.items():
        if nama_kontak == nama :
            return nomer_telepon
    return None

buku_telepon = {
    "John Doe" : "081234567890",
    "Jane Smith" : "089876543210",
    "Michael Johnson" : "087811223344",
    "Emily Davis" : "082122232425"
}

nama = "Jane Smith"
nomer_telepon = mencari_nomer_telepon(nama,buku_telepon)
if nomer_telepon :
    print("Nomer telepon",nama , "adalah" , nomer_telepon)
else:
    print("Nomer telepon",nama, "tidak ditemukan")
    

