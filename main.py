import streamlit as st
import qrcode
import io  # Library penting untuk mengatasi error ini

# --- 1. Fungsi Pembuat QR ---
def buat_qr_custom(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=6,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Membuat gambar
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# --- 2. Tampilan Website ---
st.title("Aplikasi Pembuat QR Code")

# Input Link
url_input = st.text_input("Masukkan URL/Link:", placeholder="https://google.com")

if st.button("Buat QR Code"):
    if url_input:
        # Generate Gambar (Masih berupa objek PilImage)
        gambar_objek = buat_qr_custom(url_input)

        # --- PERBAIKAN ERROR DI SINI ---
        # Kita ubah objek gambar menjadi bytes (data mentah) agar Streamlit bisa membacanya
        buffer = io.BytesIO()
        gambar_objek.save(buffer, format="PNG")
        gambar_bytes = buffer.getvalue()
        # -------------------------------

        # Tampilkan gambar menggunakan data bytes, bukan objek
        st.image(gambar_bytes, caption="Gambar QR Code Anda")

        # Tombol Download
        st.download_button(
            label="⬇️ Download Gambar",
            data=gambar_bytes,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.warning("Mohon isi link terlebih dahulu!")