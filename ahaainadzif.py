import streamlit as st
import time

# ==============================================================================
# 1. VERIFIKASI INSTALASI LIBRARY PENDUKUNG
# ==============================================================================
try:
    from google import genai
    from google.genai import types
    LIBRARY_AMAN = True
except ImportError:
    LIBRARY_AMAN = False

# ==============================================================================
# 2. SETTING HALAMAN & STYLE DESAIN MODERN ELEGAN (HIJAU ISLAMI & EMAS)
# ==============================================================================
st.set_page_config(
    page_title="AHA AI - Maharah Kalam",
    page_icon="🗣️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp { background-color: #f7f9f7; }
    .main-title { color: #0f4c3a; font-family: 'Poppins', sans-serif; font-weight: 700; text-align: center; margin-top: -20px; margin-bottom: 5px; }
    .subtitle { color: #555555; text-align: center; margin-bottom: 35px; font-size: 1.1rem; }
    div.stButton > button:first-child { background-color: #0f4c3a; color: white; border-radius: 8px; border: 1px solid #d4af37; font-weight: bold; }
    div.stButton > button:first-child:hover { background-color: #0a3327; color: #d4af37; }
    .stTextInput>div>div>input { border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

if not LIBRARY_AMAN:
    st.error("❌ Komponen Sistem Belum Lengkap!")
    st.info("Buka Terminal/CMD Anda, lalu jalankan perintah instalasi berikut:\n\n`pip install google-genai streamlit` \n\nSetelah instalasi selesai, jalankan kembali aplikasinya.")
    st.stop()

# ==============================================================================
# 3. MANAJEMEN MEMORI SESI (SESSION STATE)
# ==============================================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_persona" not in st.session_state:
    st.session_state.current_persona = ""
if "current_materi" not in st.session_state:
    st.session_state.current_materi = ""
if "active_model" not in st.session_state:
    st.session_state.active_model = "gemini-2.5-flash"

# ==============================================================================
# 4. GERBANG MASUK (HALAMAN LOGIN & INPUT API KEY)
# ==============================================================================
if not st.session_state.logged_in:
    st.markdown("<h1 class='main-title'>✨ AHA AI ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Asisten Tutor Percakapan Interaktif • Khusus Maharah Kalam Kelas XI Madrasah Aliyah</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.write("### 🔑 Data Mahasiswa & Validasi Akses")
        nama_siswa = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda...")
        nim_siswa = st.text_input("NIM (Nomor Induk Mahasiswa/Siswa)", placeholder="Masukkan NIM atau nomor induk...")
        api_key = st.text_input("Google AI Studio API Key", type="password", placeholder="Masukkan kunci AIzaSy...")
        
        st.markdown("---")
        if st.button("Masuk Ke Ruang Belajar Kalam 🚀", use_container_width=True):
            if nama_siswa.strip() and nim_siswa.strip() and api_key.strip():
                st.session_state.username = nama_siswa
                st.session_state.nim = nim_siswa
                st.session_state.api_key = api_key
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.warning("⚠️ Harap lengkapi Nama, NIM, dan API Key Anda terlebih dahulu!")
    st.stop()

# ==============================================================================
# 5. INTEGRASI API GOOGLE & PANEL SIDEBAR (PILIHAN TOPIK & PERSONA)
# ==============================================================================
client = genai.Client(api_key=st.session_state.api_key)

with st.sidebar:
    st.markdown("<h2 style='color: white; font-weight: bold;'>🗣️ AHA AI</h2>", unsafe_allow_html=True)
    st.write(f"Nama: **{st.session_state.username}**")
    st.write(f"NIM: **{st.session_state.nim}**")
    st.markdown("---")
    
    st.session_state.active_model = st.selectbox(
        "⚙️ Model Engine AI:",
        ["gemini-2.5-flash", "gemini-1.5-flash"],
        index=0
    )
    st.markdown("---")
    
    ustadz_pilihan = st.radio("🎙️ Pilih Partner Hiwar (Dialog):", ["Ustadz Syarif", "Ustadzah Fatimah"])
    materi_pilihan = st.selectbox(
        "📖 Pilih Tema Percakapan (Kelas XI):",
        [
            "التسوق (At-Tasawuq / Berbelanja)",
            "في السوق (Fissuqi / Di Pasar)",
            "الهواية (Al-Hiwayah / Hobi)"
        ]
    )
    
    st.markdown("---")
    if st.button("🚪 Keluar Sesi", use_container_width=True):
        st.session_state.clear()
        st.rerun()

if st.session_state.current_persona != ustadz_pilihan or st.session_state.current_materi != materi_pilihan:
    st.session_state.current_persona = ustadz_pilihan
    st.session_state.current_materi = materi_pilihan
    st.session_state.chat_history = [] 

# Promp sistem difokuskan penuh pada Maharah Kalam (Keterampilan Berbicara)
instruksi_sistem = f"""
Anda adalah {ustadz_pilihan}, seorang tutor penutur asli (native speaker) bahasa Arab yang interaktif untuk siswa kelas XI Madrasah Aliyah.
Fokus utama Anda adalah melatih Keterampilan Berbicara (Maharah Kalam) siswa pada tema: {materi_pilihan}.

Aturan Komunikasi:
1. Mulailah dialog dengan salam Islami yang hangat.
2. Berikan stimulus percakapan pendek berupa pertanyaan pemantik (Hiwar) yang menuntut siswa mempraktikkan ungkapan lisan.
3. Gunakan bahasa Arab yang kasual namun fasih (fusha), berikan transliterasi latin atau arti kata di dalam kurung jika kalimatnya dirasa cukup sulit untuk tingkat MA Kelas XI.
4. Koreksi kesalahan diksi, pengucapan (melalui teks tertulis), struktur kalimat, atau cara merespons dialog secara mendetail.
5. Berikan apresiasi islami seperti ممتاز (Mumtaz), أحسنت (Ahsant), atau بارك الله فيك jika siswa menjawab dengan baik.
6. Ajak siswa untuk terus aktif melakukan percakapan dua arah (tanya-jawab).
"""

# ==============================================================================
# 6. PANEL CHAT UTAMA & RIWAYAT PERCAKAPAN (CONVERSATION HISTORY)
# ==============================================================================
st.markdown(f"## 🏛️ Lab Bahasa Virtual (Kalam): {materi_pilihan}")
st.write(f"Partner Hiwar Anda: **{ustadz_pilihan}**")

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Trigger pesan pembuka otomatis dari AI jika chat masih kosong
if len(st.session_state.chat_history) == 0:
    if ustadz_pilihan == "Ustadz Syarif":
        salam_pembuka = f"Assalamu'alaikum wr. wb. Ahlan wa sahlan Ananda **{st.session_state.username}**! Saya Ustadz Syarif. Hari ini kita akan mempraktikkan percakapan langsung (*Maharah Kalam*) mengenai **{materi_pilihan}**. Silakan balas pesan ini dengan menyapa kembali atau ketik 'Siap Ustadz' untuk memulai tantangan dialog kita!"
    else:
        salam_pembuka = f"Assalamu'alaikum wr. wb. Sabahal khair, anakku yang cerdas **{st.session_state.username}**! Bersama Ustadzah Fatimah di sini, kita akan seru-seruan latihan berbicara bahasa Arab untuk materi **{materi_pilihan}**. Jangan takut salah ya! Sapa Ustadzah sekarang untuk memulai percakapan kita!"
        
    st.session_state.chat_history.append({"role": "assistant", "content": salam_pembuka})
    st.rerun()

if pesan_user := st.chat_input("Ketik respons atau dialog Arab Anda di sini..."):
    with st.chat_message("user"):
        st.markdown(pesan_user)
    st.session_state.chat_history.append({"role": "user", "content": pesan_user})

    if pesan_user.lower() in ['exit', 'quit', 'keluar']:
        st.session_state.clear()
        st.rerun()

    payload_konten = []
    for msg in st.session_state.chat_history:
        peran_api = "user" if msg["role"] == "user" else "model"
        payload_konten.append(
            types.Content(role=peran_api, parts=[types.Part.from_text(text=msg["content"])])
        )

    respons_api = None
    max_retries = 3
    
    with st.spinner(f"{ustadz_pilihan} sedang mendengarkan dan merespons ucapan Anda..."):
        for i in range(max_retries):
            try:
                respons_api = client.models.generate_content(
                    model=st.session_state.active_model,
                    contents=payload_konten,
                    config=types.GenerateContentConfig(
                        system_instruction=instruksi_sistem,
                        temperature=0.7,  # Sedikit lebih tinggi agar respons dialog bervariasi dan natural
                    )
                )
                break 
            except Exception as e:
                if "503" in str(e) and i < max_retries - 1:
                    time.sleep(2)
                    continue
                else:
                    respons_api = e

    if respons_api and not isinstance(respons_api, Exception):
        teks_balasan = respons_api.text
        with st.chat_message("assistant"):
            st.markdown(teks_balasan)
        st.session_state.chat_history.append({"role": "assistant", "content": teks_balasan})
    else:
        st.error("⚠️ Terjadi gangguan koneksi atau server Google Studio sedang padat.")
        st.info("💡 **Solusi Mudah:** Silakan ganti tipe **Model Engine AI** di bilah kiri (Sidebar) menjadi `gemini-1.5-flash`, lalu kirim ulang pesan Anda.")