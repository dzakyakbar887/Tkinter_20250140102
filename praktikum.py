import tkinter as tk

def prediksi_prodi():
    # Fungsi ini akan menampilkan luaran "Teknologi Informasi" pada label hasil
    label_luaran.config(text="Hasil Prediksi: Teknologi Informasi")

# 1. Membuat jendela utama GUI
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x550")
root.configure(padx=20, pady=20)

# 2. Label Judul
label_judul = tk.Label(
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Helvetica", 14, "bold")
)
label_judul.pack(pady=(0, 15))

# Frame untuk membungkus input mata pelajaran agar tata letak rapi
frame_inputs = tk.Frame(root)
frame_inputs.pack(fill="x", pady=5)

# List untuk menyimpan widget entry nilai mata pelajaran
list_entry = []

# 3. Membuat 10 Input Nilai Mata Pelajaran menggunakan perulangan (loop)
for i in range(1, 11):
    row_frame = tk.Frame(frame_inputs)
    row_frame.pack(fill="x", pady=2)
    
    # Label untuk setiap mata pelajaran
    lbl_mapel = tk.Label(row_frame, text=f"Nilai Mata Pelajaran {i}:", width=22, anchor="w")
    lbl_mapel.pack(side="left")
    
    # Entry untuk input nilai
    entry_nilai = tk.Entry(row_frame)
    entry_nilai.pack(side="right", expand=True, fill="x")
    list_entry.append(entry_nilai)

# 4. Button bertuliskan "Hasil Prediksi"
btn_prediksi = tk.Button(
    root, 
    text="Hasil Prediksi", 
    command=prediksi_prodi,
    bg="#4CAF50", 
    fg="white", 
    font=("Helvetica", 10, "bold"),
    padding=(10, 5) if hasattr(tk, 'ttk') else None # Mengatur tampilan button
)
btn_prediksi.pack(pady=15)

# 5. Label Luaran Hasil Prediksi
label_luaran = tk.Label(
    root, 
    text="Hasil Prediksi: -", 
    font=("Helvetica", 11, "italic"),
    fg="blue"
)
label_luaran.pack(pady=5)

# Menjalankan aplikasi GUI
root.mainloop()