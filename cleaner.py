# =====================================================================
# PART 1: DEFINISI CLASS (LOGIKA CLEANER)
# =====================================================================

# 1. Class untuk menghapus data duplikat (kembar)
class Deduplicator:
    def __init__(self, data):
        self.data = data

    def clean(self):
        return list(set(self.data))


# 2. Class untuk mengubah tipe data (Teks ke Angka Bulat)
class DataTypeConverter:
    def __init__(self, data):
        self.data = data

    def to_integer(self):
        return [int(x) for x in self.data]


# 3. Class untuk menyaring/memfilter nilai yang diperbolehkan saja
class AllowedValuesFilter:
    def __init__(self, data, allowed_list):
        self.data = data
        self.allowed_list = allowed_list

    def filter_data(self):
        return [x for x in self.data if x in self.allowed_list]


# 4. Class untuk merapikan teks (Hapus spasi gaib & ubah ke huruf kecil)
class StringNormalizer:
    def __init__(self, text_list):
        self.text_list = text_list

    def normalize(self):
        return [text.strip().lower() for text in self.text_list]


# 5. Class untuk menangani data kosong (Missing Value)
class MissingValueHandler:
    def __init__(self, data):
        self.data = data

    def fill_missing(self, default_value="Kosong"):
        return [x if (x is not None and x != "") else default_value for x in self.data]


# =====================================================================
# PART 2: CONTOH EKSEKUSI (MEMBUKTIKAN KODE BERHASIL)
# =====================================================================
if __name__ == "__main__":
    print("--- HASIL PENGUJIAN DATA CLEANER ---\n")

    # Tes 1: Hapus Duplikat
    data_kembar = [1, 2, 2, 3, 4, 4, 4, 5]
    cleaner1 = Deduplicator(data_kembar)
    print("1. Data Asli Duplikat:", data_kembar)
    print("   Hasil Bersih     :", cleaner1.clean(), "\n")

    # Tes 2: Ubah Tipe Data
    data_teks_angka = ["10", "20", "30"]
    cleaner2 = DataTypeConverter(data_teks_angka)
    print("2. Data Asli Teks   :", data_teks_angka)
    print("   Hasil Jadi Angka :", cleaner2.to_integer(), "\n")

    # Tes 3: Filter Data
    data_nilai = ["A", "B", "C", "Z", "X"]
    nilai_boleh = ["A", "B", "C"]  # Hanya nilai ini yg lolos
    cleaner3 = AllowedValuesFilter(data_nilai, nilai_boleh)
    print("3. Data Asli Nilai  :", data_nilai)
    print("   Hasil Filter     :", cleaner3.filter_data(), "\n")

    # Tes 4: Normalisasi Teks
    data_teks_kotor = ["  ANANG  ", " digital skola ", "PyThOn  "]
    cleaner4 = StringNormalizer(data_teks_kotor)
    print("4. Teks Kotor       :", data_teks_kotor)
    print("   Hasil Rapi       :", cleaner4.normalize(), "\n")

    # Tes 5: Mengisi Data Kosong
    data_bolong = ["Budi", None, "Andi", "", "Caca"]
    cleaner5 = MissingValueHandler(data_bolong)
    print("5. Data Bolong      :", data_bolong)
    print("   Hasil Ditambal   :", cleaner5.fill_missing("Nama_Kosong"), "\n")