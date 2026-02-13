import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Формулы по физике",
    page_icon="⚛️",
    layout="wide"
)

# ТОЛЬКО СТИЛИ ДЛЯ КНОПКИ МЕНЮ (больше ничего не меняем)
st.markdown("""
<style>
    /* Делаем кнопку меню больше и ярче */
    button[data-testid="baseButton-header"] {
        background-color: #ff4b4b !important;
        border: 2px solid white !important;
        border-radius: 8px !important;
        width: 50px !important;
        height: 50px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3) !important;
    }
    
    /* Иконка внутри кнопки */
    button[data-testid="baseButton-header"] svg {
        width: 25px !important;
        height: 25px !important;
        fill: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Заголовок
st.title("⚛️ Главные формулы по физике")
st.markdown("Справочник основных формул для школьников и студентов")

# --- Сайдбар с навигацией ---
st.sidebar.title("Разделы")
section = st.sidebar.radio(
    "Выберите раздел:",
    ["Механика", "Молекулярная физика и термодинамика", "Электричество и магнетизм", "Оптика", "Квантовая физика"]
)

# --- ОСНОВНОЙ КОНТЕНТ ---

# 1. МЕХАНИКА
if section == "Механика":
    st.header("📐 Механика")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Кинематика")
        st.latex(r"v = v_0 + at")
        st.latex(r"S = v_0t + \frac{at^2}{2}")
        st.latex(r"v^2 - v_0^2 = 2aS")
        st.latex(r"\text{Скорость при РПД: } \omega = \omega_0 + \varepsilon t")
        
        st.subheader("Динамика")
        st.latex(r"F = ma")
        st.latex(r"F_{тр} = \mu N")
        st.latex(r"F_{упр} = -kx")
        st.latex(r"F = G\frac{m_1 m_2}{R^2}")
    
    with col2:
        st.subheader("Законы сохранения")
        st.latex(r"p = mv")
        st.latex(r"E_k = \frac{mv^2}{2}")
        st.latex(r"E_p = mgh")
        st.latex(r"E_p = \frac{kx^2}{2}")
        st.latex(r"A = FS\cos\alpha")
        
        st.subheader("Статика и колебания")
        st.latex(r"M = F \cdot l")
        st.latex(r"T = 2\pi\sqrt{\frac{l}{g}}")
        st.latex(r"T = 2\pi\sqrt{\frac{m}{k}}")

# 2. МОЛЕКУЛЯРНАЯ ФИЗИКА
elif section == "Молекулярная физика и термодинамика":
    st.header("🔥 Молекулярная физика и термодинамика")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("МКТ")
        st.latex(r"p = \frac{1}{3} m_0 n v^2")
        st.latex(r"p = nkT")
        st.latex(r"U = \frac{3}{2}RT")
        
        st.subheader("Газовые законы")
        st.latex(r"pV = \nu RT")
        st.latex(r"\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}")
    
    with col2:
        st.subheader("Термодинамика")
        st.latex(r"\Delta U = Q - A")
        st.latex(r"A = p \Delta V")
        st.latex(r"\eta = \frac{Q_1 - Q_2}{Q_1}")
        st.latex(r"\eta = 1 - \frac{T_2}{T_1}")

# 3. ЭЛЕКТРИЧЕСТВО
elif section == "Электричество и магнетизм":
    st.header("⚡ Электричество и магнетизм")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Электростатика")
        st.latex(r"F = k\frac{|q_1||q_2|}{r^2}")
        st.latex(r"E = \frac{F}{q}")
        st.latex(r"E = \frac{kq}{r^2}")
        st.latex(r"\varphi = \frac{W}{q}")
        st.latex(r"C = \frac{q}{U}")
        st.latex(r"C = \frac{\varepsilon\varepsilon_0 S}{d}")
    
    with col2:
        st.subheader("Цепи постоянного тока")
        st.latex(r"I = \frac{U}{R}")
        st.latex(r"R = \rho \frac{l}{S}")
        st.latex(r"A = IUt")
        st.latex(r"P = IU")
        st.latex(r"I = \frac{\varepsilon}{R + r}")
        
        st.subheader("Магнетизм")
        st.latex(r"F_A = IBl\sin\alpha")
        st.latex(r"F_L = qvB\sin\alpha")
        st.latex(r"\Phi = BS\cos\alpha")

# 4. ОПТИКА
elif section == "Оптика":
    st.header("🔦 Оптика")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Геометрическая оптика")
        st.latex(r"\frac{1}{F} = \frac{1}{d} + \frac{1}{f}")
        st.latex(r"D = \frac{1}{F}")
        st.latex(r"\Gamma = \frac{f}{d}")
        st.latex(r"n = \frac{c}{v}")
        st.latex(r"\frac{\sin\alpha}{\sin\beta} = \frac{n_2}{n_1}")
    
    with col2:
        st.subheader("Волновая оптика")
        st.latex(r"\lambda = \frac{c}{\nu}")
        st.latex(r"\Delta d = k\lambda")
        st.latex(r"d\sin\varphi = k\lambda")

# 5. КВАНТОВАЯ
elif section == "Квантовая физика":
    st.header("✨ Квантовая физика")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Фотоэффект")
        st.latex(r"E = h\nu")
        st.latex(r"h\nu = A_{вых} + \frac{mv^2}{2}")
        st.latex(r"\lambda = \frac{h}{mv}")
    
    with col2:
        st.subheader("Атомная физика")
        st.latex(r"r_n = n^2 r_1")
        st.latex(r"E_n = \frac{E_1}{n^2}")
        st.latex(r"h\nu = E_2 - E_1")

# Нижний колонтитул
st.markdown("---")
st.markdown("📚 **Сайт создан с помощью Streamlit** • Формулы соответствуют школьной программе")


