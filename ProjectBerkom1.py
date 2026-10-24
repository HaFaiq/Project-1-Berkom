#Array untuk hasil perhitungan
g = []

# Menu utama program Perhitungan Stoikiometri
while True:
    print("===PERHITUNGAN STOIKIOMETRI===")
# Menu Pilihan
    print("1. Hitung Mol")
    print("2. Hitung Massa")
    print("3. Hitung jumlah partikel")
    print("4. Hitung gas ideal")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan (1-5): ")


# Perhitungan Mol dan Massa
    # Menghitung mol senyawa
    if pilihan == "1":
        nama_senyawa = input("Masukkan Senyawa: ")
        massa_molar = float(input("Masukkan Masssa Molar (g/mol) : "))
        massa_senyawa = float(input("Masukkan massa senyawa (g): "))
        perhitungan_mol = massa_senyawa / massa_molar
        print(f"Jumlah mol {nama_senyawa} = {perhitungan_mol} mol")
        g.append(f"{nama_senyawa}: {perhitungan_mol} mol")
        
    # Menghitung massa senyawa
    elif pilihan == "2":
        nama_senyawa = input("Masukkan Senyawa: ")
        massa_molar = float(input("Masukkan Masssa Molar (g/mol) : "))
        mol_senyawa = float(input("Masukkan jumlah mol (mol): "))
        perhitungan_massa = mol_senyawa * massa_molar
        print(f"Massa {nama_senyawa} =", perhitungan_massa, "gram")
        g.append(f"{nama_senyawa}: {perhitungan_massa} gram")
        Data_hasil = [perhitungan_massa]
    # Menghitung jumlah partikel senyawa
    elif pilihan == "3":
        nama_senyawa = input("Masukkan Senyawa: ")
        mol_senyawa = float(input("Masukkan mol senyawa: "))
        jumlah_partikel = mol_senyawa * 6.022*10**23
        print(f"jumlah partikel {nama_senyawa} ={jumlah_partikel:e} partikel")
        g.append(f"{nama_senyawa}: {jumlah_partikel:e} partikel")
    # Perhitungan Gas Ideal
    elif pilihan == "4":
        print("=== Perhitungan Gas Ideal ===")
        print("1. Hitung volume gas ideal")
        print("2. Hitung tekanan gas ideal")
        print("3. Hitung suhu gas ideal")
        print("4. Hitung jumlah mol gas ideal")
        print("5. Kembali")
        pilihanGas = input("Masukkan pilihan (1-5) = ")
        # Menghitung volume gas ideal
        if pilihanGas == "1" :
            nama_senyawa = input("Masukkan Senyawa: ")
            P = float(input("Masukkan tekanan gas ideal (atm): "))
            n = float(input("Masukkan jumlah mol gas ideal (mol): "))
            R = 0.0821
            T = float(input("Masukkan suhu gas ideal (K): "))
            V = (n * R * T) / P
            print(f"Volume gas {nama_senyawa} :", V, "liter")
            g.append(f"{nama_senyawa}: volume gas = {V} liter")
        # Menghitung tekanan gas ideal
        elif pilihanGas == "2" :
            nama_senyawa = input("Masukkan Senyawa: ")
            V = float(input("Masukkan volume gas ideal (liter): "))
            n = float(input("Masukkan jumlah mol gas ideal (mol): "))
            R = 0.0821
            T = float(input("Masukkan suhu gas ideal (K): "))
            P = (n * R * T) / V
            print(f"Tekanan gas {nama_senyawa}:", P, "atm")
            g.append(f"{nama_senyawa}: tekanan gas = {P} atm")
        # Menghitung suhu gas ideal
        elif pilihanGas == "3" :
            nama_senyawa = input("Masukkan Senyawa: ")
            P = float(input("Masukkan tekanan gas ideal (atm): "))
            V = float(input("Masukkan volume gas ideal (liter): "))
            n = float(input("Masukkan jumlah mol gas ideal (mol): "))
            R = 0.0821
            T = (P * V) / (n * R)
            print(f"Suhu gas {nama_senyawa}:", T, "kelvin")
            g.append(f"{nama_senyawa}: suhu gas = {T} K")
        # Menghitung jumlah mol gas ideal
        elif pilihanGas == "4" :
            nama_senyawa = input("Masukkan Senyawa: ")
            P = float(input("Masukkan tekanan gas ideal (atm): "))
            V = float(input("Masukkan volume gas ideal (liter): "))
            T = float(input("Masukkan suhu gas ideal (kelvin): "))
            R = 0.0821
            n = (P * V) / (T * R)
            print(f"Mol gas {nama_senyawa}:", n, "mol")
            g.append(f"{nama_senyawa}: {n} mol (gas ideal)")
# Kembali ke menu pilihan
        elif pilihanGas == "5" :
            print("     ")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
# Kembali ke menu utama
    elif pilihan == "5":
        print("=== RIWAYAT PERHITUNGAN ===")
        for i in range(len(g)):
                print(f"{i + 1}. {g[i]}")

        print("Terima kasih telah menggunakan program ini.")
        break 
    else: 
        print("Pilihan tidak valid. Silakan coba lagi.")
