import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Формулы по физике",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# СТИЛИ ДЛЯ ЗАМЕТНОЙ КНОПКИ МЕНЮ (без подсказок)
st.markdown("""
<style>
    /* Делаем кнопку меню (бургер) большой и яркой */
    button[data-testid="baseButton-header"] {
        background: linear-gradient(135deg, #ff4b4b 0%, #ff6b6b 100%) !important;
        border: 3px solid white !important;
        border-radius: 50% !important;
        width: 60px !important;
        height: 60px !important;
        box-shadow: 0 0 30px rgba(255, 75, 75, 0.7) !important;
        position: fixed !important;
        top: 10px !important;
        left: 10px !important;
        z-index: 999999 !important;
        animation: pulse 2s infinite !important;
    }
    
    /* Анимация пульсации */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); box-shadow: 0 0 50px rgba(255, 75, 75, 0.9); }
        100% { transform: scale(1); }
    }
    
    /* Иконка внутри кнопки (три полоски) */
    button[data-testid="baseButton-header"] svg {
        width: 30px !important;
        height: 30px !important;
        fill: white !important;
    }
    
    /* Когда меню открыто - кнопка меняется */
    button[data-testid="baseButton-header"][aria-expanded="true"] {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%) !important;
        transform: rotate(90deg);
    }
    
    /* Для мобильных устройств */
    @media (max-width: 768px) {
        /* Само меню */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
            padding-top: 80px !important;
        }
        
        /* Кнопки в меню */
        .stRadio > div {
            gap: 15px !important;
            padding: 15px !important;
        }
        
        .stRadio label {
            background: rgba(255,255,255,0.2) !important;
            border: 2px solid rgba(255,255,255,0.3) !important;
            border-radius: 15px !important;
            padding: 20px !important;
            font-size: 22px !important;
            font-weight: bold !important;
            color: white !important;
            text-align: center !important;
            margin: 5px 0 !important;
        }
        
        /* Выбранный пункт */
        .stRadio label[data-baseweb="radio"]:has(input:checked) {
            background: #ffd700 !important;
            color: #333 !important;
            border: 2px solid white !important;
            box-shadow: 0 0 30px gold !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Заголовок
st.title("⚛️ Формулы по физике")
st.markdown("---")

# --- Сайдбар с разделами ---
st.sidebar.markdown("# РАЗДЕЛЫ ФИЗИКИ")

# Радио-кнопки для выбора раздела
section = st.sidebar.radio(
    "Выберите раздел:",
    ["Механика", "Молекулярная физика", "Электричество", "Оптика", "Квантовая физика"],
    index=0
)

# --- ОСНОВНОЙ КОНТЕНТ ---
if section == "Механика":
    st.header("Механика")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Кинематика")
        st.latex(r"v = v_0 + at")
        st.latex(r"S = v_0t + \frac{at^2}{2}")
        st.latex(r"h = \frac{gt^2}{2}")
        
        st.subheader("Динамика")
        st.latex(r"F = ma")
        st.latex(r"F_{тр} = \mu N")
        st.latex(r"F = G\frac{m_1 m_2}{R^2}")
    
    with col2:
        st.subheader("Законы сохранения")
        st.latex(r"p = mv")
        st.latex(r"E_k = \frac{mv^2}{2}")
        st.latex(r"E_p = mgh")
        
        st.subheader("Колебания")
        st.latex(r"T = 2\pi\sqrt{\frac{l}{g}}")
        st.latex(r"T = 2\pi\sqrt{\frac{m}{k}}")

elif section == "Молекулярная физика":
    st.header("Молекулярная физика")
    
    st.subheader("Газовые законы")
    st.latex(r"pV = \nu RT")
    st.latex(r"U = \frac{3}{2}\nu RT")
    
    st.subheader("Термодинамика")
    st.latex(r"\Delta U = Q - A")
    st.latex(r"\eta = \frac{Q_1 - Q_2}{Q_1}")

elif section == "Электричество":
    st.header("Электричество")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Электростатика")
        st.latex(r"F = k\frac{q_1 q_2}{r^2}")
        st.latex(r"E = \frac{F}{q}")
        st.latex(r"C = \frac{q}{U}")
    
    with col2:
        st.subheader("Цепи тока")
        st.latex(r"I = \frac{U}{R}")
        st.latex(r"A = IUt")
        st.latex(r"P = IU")

elif section == "Оптика":
    st.header("Оптика")
    
    st.subheader("Геометрическая оптика")
    st.latex(r"\frac{1}{F} = \frac{1}{d} + \frac{1}{f}")
    st.latex(r"D = \frac{1}{F}")
    
    st.subheader("Волновая оптика")
    st.latex(r"\lambda = \frac{c}{\nu}")
    st.latex(r"\Delta d = k\lambda")

elif section == "Квантовая физика":
    st.header("Квантовая физика")
    
    st.subheader("Фотоэффект")
    st.latex(r"E = h\nu")
    st.latex(r"h\nu = A_{вых} + \frac{mv^2}{2}")
    
    st.subheader("Атомная физика")
    st.latex(r"h\nu = E_2 - E_1")
    st.latex(r"\lambda = \frac{h}{mv}")

st.markdown("---")

