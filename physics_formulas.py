import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Формулы по физике",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# СТИЛИ ДЛЯ ЗАМЕТНОЙ КНОПКИ МЕНЮ
st.markdown("""
<style>
    /* Делаем кнопку меню (бургер) огромной и яркой */
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
    
    /* Текст-подсказка над кнопкой */
    .menu-hint {
        position: fixed;
        top: 80px;
        left: 20px;
        background: #333;
        color: white;
        padding: 12px 20px;
        border-radius: 50px;
        font-size: 18px;
        font-weight: bold;
        z-index: 999998;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        border-left: 5px solid #ff4b4b;
        animation: slideIn 1s;
    }
    
    @keyframes slideIn {
        from { left: -200px; }
        to { left: 20px; }
    }
    
    /* Стрелка указывает на кнопку */
    .menu-hint:after {
        content: "👆";
        position: absolute;
        top: -30px;
        left: 30px;
        font-size: 40px;
        animation: bounce 1s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* Затемнение фона когда меню открыто */
    section[data-testid="stSidebar"][aria-expanded="true"] {
        box-shadow: 0 0 50px rgba(0,0,0,0.5) !important;
    }
    
    /* Для мобильных устройств */
    @media (max-width: 768px) {
        /* Само меню делаем красивее */
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
        
        .stRadio label:hover {
            background: rgba(255,255,255,0.3) !important;
            transform: scale(1.02);
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

# Подсказка для пользователя
st.markdown("""
<div class="menu-hint">
    👈 Нажми на красную кнопку чтобы открыть меню!
</div>
""", unsafe_allow_html=True)

# Заголовок
st.markdown("<h1 style='text-align: center; margin-top: 100px;'>⚛️ Формулы по физике</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- Сайдбар с разделами ---
st.sidebar.markdown("# 📚 РАЗДЕЛЫ ФИЗИКИ")

# Радио-кнопки для выбора раздела
section = st.sidebar.radio(
    "Выбери раздел:",
    ["Механика", "Молекулярная физика", "Электричество", "Оптика", "Квантовая физика"],
    index=0
)

# --- ОСНОВНОЙ КОНТЕНТ ---
if section == "Механика":
    st.header("📐 Механика")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Кинематика")
        st.markdown("**Скорость:** $v = v_0 + at$")
        st.markdown("**Перемещение:** $S = v_0t + \\frac{at^2}{2}$")
        st.markdown("**Высота:** $h = \\frac{gt^2}{2}$")
        
        st.subheader("Динамика")
        st.markdown("**2-й закон Ньютона:** $F = ma$")
        st.markdown("**Сила трения:** $F_{тр} = \\mu N$")
    
    with col2:
        st.subheader("Законы сохранения")
        st.markdown("**Импульс:** $p = mv$")
        st.markdown("**Кинетическая энергия:** $E_k = \\frac{mv^2}{2}$")
        st.markdown("**Потенциальная энергия:** $E_p = mgh$")
        
        st.subheader("Колебания")
        st.markdown("**Маятник:** $T = 2\\pi\\sqrt{\\frac{l}{g}}$")
        st.markdown("**Пружина:** $T = 2\\pi\\sqrt{\\frac{m}{k}}$")

elif section == "Молекулярная физика":
    st.header("🔥 Молекулярная физика")
    
    st.subheader("Газовые законы")
    st.markdown("**Уравнение Менделеева-Клапейрона:** $pV = \\nu RT$")
    st.markdown("**Внутренняя энергия:** $U = \\frac{3}{2}\\nu RT$")
    
    st.subheader("Термодинамика")
    st.markdown("**1-й закон:** $\\Delta U = Q - A$")
    st.markdown("**КПД:** $\\eta = \\frac{Q_1 - Q_2}{Q_1}$")

elif section == "Электричество":
    st.header("⚡ Электричество")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Электростатика")
        st.markdown("**Закон Кулона:** $F = k\\frac{q_1q_2}{r^2}$")
        st.markdown("**Напряжённость:** $E = \\frac{F}{q}$")
        st.markdown("**Ёмкость:** $C = \\frac{q}{U}$")
    
    with col2:
        st.subheader("Цепи тока")
        st.markdown("**Закон Ома:** $I = \\frac{U}{R}$")
        st.markdown("**Работа тока:** $A = IUt$")
        st.markdown("**Мощность:** $P = IU$")

elif section == "Оптика":
    st.header("💡 Оптика")
    
    st.subheader("Геометрическая оптика")
    st.markdown("**Формула линзы:** $\\frac{1}{F} = \\frac{1}{d} + \\frac{1}{f}$")
    st.markdown("**Оптическая сила:** $D = \\frac{1}{F}$")
    
    st.subheader("Волновая оптика")
    st.markdown("**Длина волны:** $\\lambda = \\frac{c}{\\nu}$")
    st.markdown("**Интерференция:** $\\Delta d = k\\lambda$")

elif section == "Квантовая физика":
    st.header("✨ Квантовая физика")
    
    st.subheader("Фотоэффект")
    st.markdown("**Энергия фотона:** $E = h\\nu$")
    st.markdown("**Уравнение Эйнштейна:** $h\\nu = A_{вых} + \\frac{mv^2}{2}$")
    
    st.subheader("Атом")
    st.markdown("**Постулат Бора:** $h\\nu = E_2 - E_1$")
    st.markdown("**Длина волны де Бройля:** $\\lambda = \\frac{h}{mv}$")

# Подвал
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    📱 Нажми на <span style='background: #ff4b4b; color: white; padding: 5px 10px; border-radius: 10px;'>🔴 красную кнопку</span> слева чтобы открыть меню
</div>
""", unsafe_allow_html=True)

