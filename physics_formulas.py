import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Формулы по физике",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# СУПЕР-СТИЛИ чтобы меню было видно!
st.markdown("""
<style>
    /* Делаем сайдбар ярче */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        padding: 20px 0;
    }
    
    /* Текст в сайдбаре */
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Заголовок в сайдбаре */
    .css-1aehpvj {
        font-size: 24px !important;
        font-weight: bold !important;
        text-align: center !important;
        color: white !important;
        border-bottom: 3px solid #ffd700;
        padding-bottom: 15px;
        margin-bottom: 20px;
    }
    
    /* КНОПКИ МЕНЮ - ОГРОМНЫЕ И ЯРКИЕ */
    div.row-widget.stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 15px;
        padding: 10px;
    }
    
    div.row-widget.stRadio > div > label {
        background: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        padding: 20px 25px !important;
        margin: 0 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        color: white !important;
        text-align: center;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Выбранный пункт */
    div.row-widget.stRadio > div > label[data-baseweb="radio"]:has(input:checked) {
        background: #ffd700 !important;
        border: 2px solid white !important;
        color: #333 !important;
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
    }
    
    /* При наведении */
    div.row-widget.stRadio > div > label:hover {
        background: rgba(255, 255, 255, 0.3) !important;
        transform: scale(1.02);
    }
    
    /* ФОРМУЛЫ - ещё красивее */
    .formula-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        margin: 25px 0;
        border: 1px solid #e0e0e0;
        transition: all 0.3s;
    }
    
    .formula-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.2);
    }
    
    .formula-name {
        color: #667eea;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 2px dashed #e0e0e0;
    }
    
    .formula-equation {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px !important;
        font-weight: bold;
        color: #333;
    }
    
    /* Для телефона */
    @media (max-width: 768px) {
        div.row-widget.stRadio > div > label {
            font-size: 20px !important;
            padding: 18px !important;
        }
        
        .formula-equation {
            font-size: 22px !important;
            padding: 20px;
        }
    }
    
    /* Кнопка для открытия меню на телефоне */
    button[data-testid="baseButton-header"] {
        background: #ff4b4b !important;
        border-radius: 50% !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# Заголовок с эмодзи
st.title("⚛️ **ФОРМУЛЫ ПО ФИЗИКЕ**")
st.markdown("""
<div style="text-align: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 50px; margin: 20px 0; color: white; font-size: 18px;">
    👈 Нажми на кнопку слева (три полоски) чтобы открыть меню
</div>
""", unsafe_allow_html=True)

# --- Сайдбар с навигацией ---
st.sidebar.markdown("# 📚 **ВЫБЕРИ РАЗДЕЛ**")
section = st.sidebar.radio(
    "",
    ["🔥 Механика", "🌡 Молекулярка", "⚡ Электричество", "💡 Оптика", "✨ Кванты"],
    index=0
)

# Очищаем название от эмодзи для логики
if section == "🔥 Механика":
    current_section = "Механика"
elif section == "🌡 Молекулярка":
    current_section = "Молекулярная физика и термодинамика"
elif section == "⚡ Электричество":
    current_section = "Электричество и магнетизм"
elif section == "💡 Оптика":
    current_section = "Оптика"
elif section == "✨ Кванты":
    current_section = "Квантовая физика"

# Подсказка в сайдбаре
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; text-align: center;">
    📱 <b>На телефоне:</b><br>
    Нажми ☰ сверху слева
</div>
""", unsafe_allow_html=True)

# Функция для отображения формулы
def show_formula(name, formula, description=""):
    st.markdown(f"""
    <div class="formula-card">
        <div class="formula-name">📌 {name}</div>
        <div class="formula-equation">{formula}</div>
        <div style="color: #666; margin-top: 15px; font-size: 16px; padding: 10px; background: #f8f9fa; border-radius: 10px;">
            📝 {description}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- ОСНОВНОЙ КОНТЕНТ ---
if current_section == "Механика":
    st.header("🔥 Механика")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Кинематика")
        show_formula(
            "Скорость",
            "v = v_0 + at",
            "v₀ — начальная скорость, a — ускорение, t — время"
        )
        show_formula(
            "Перемещение",
            "S = v_0t + \\frac{at^2}{2}",
            "Путь при равноускоренном движении"
        )
        show_formula(
            "Высота падения",
            "h = \\frac{gt^2}{2}",
            "g = 9.8 м/с² — ускорение свободного падения"
        )
    
    with col2:
        st.subheader("Динамика")
        show_formula(
            "Второй закон Ньютона",
            "F = ma",
            "Сила = масса × ускорение"
        )
        show_formula(
            "Сила трения",
            "F_{тр} = \\mu N",
            "μ — коэффициент трения"
        )
        show_formula(
            "Закон Гука",
            "F_{упр} = -kx",
            "k — жёсткость пружины"
        )

elif current_section == "Молекулярная физика и термодинамика":
    st.header("🌡 Молекулярная физика")
    
    show_formula(
        "Уравнение Менделеева-Клапейрона",
        "pV = \\nu RT",
        "p — давление, V — объём, ν — количество вещества, R = 8.31 Дж/(моль·К), T — температура"
    )
    show_formula(
        "Внутренняя энергия",
        "U = \\frac{3}{2} \\nu RT",
        "Для одноатомного идеального газа"
    )
    show_formula(
        "КПД теплового двигателя",
        "\\eta = \\frac{Q_1 - Q_2}{Q_1}",
        "Q₁ — тепло от нагревателя, Q₂ — тепло холодильнику"
    )

elif current_section == "Электричество и магнетизм":
    st.header("⚡ Электричество")
    
    col1, col2 = st.columns(2)
    
    with col1:
        show_formula(
            "Закон Кулона",
            "F = k\\frac{|q_1||q_2|}{r^2}",
            "k = 9×10⁹ Н·м²/Кл²"
        )
        show_formula(
            "Напряжённость",
            "E = \\frac{F}{q}",
            "Силовая характеристика поля"
        )
    
    with col2:
        show_formula(
            "Закон Ома",
            "I = \\frac{U}{R}",
            "I — сила тока, U — напряжение, R — сопротивление"
        )
        show_formula(
            "Работа тока",
            "A = IUt",
            "A = мощность × время"
        )

elif current_section == "Оптика":
    st.header("💡 Оптика")
    
    show_formula(
        "Формула тонкой линзы",
        "\\frac{1}{F} = \\frac{1}{d} + \\frac{1}{f}",
        "F — фокусное расстояние, d — расстояние до предмета, f — до изображения"
    )
    show_formula(
        "Оптическая сила",
        "D = \\frac{1}{F}",
        "Измеряется в диоптриях"
    )

elif current_section == "Квантовая физика":
    st.header("✨ Квантовая физика")
    
    show_formula(
        "Энергия фотона",
        "E = h\\nu",
        "h = 6.63×10⁻³⁴ Дж·с — постоянная Планка"
    )
    show_formula(
        "Уравнение Эйнштейна",
        "h\\nu = A_{вых} + \\frac{mv^2}{2}",
        "Энергия фотона = работа выхода + кинетическая энергия"
    )


