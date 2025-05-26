import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Симулация на сблъсък на частици", layout="centered")
st.title("💥 Симулация на сблъсък на частици")
st.markdown("""
Изследвай как се държат две частици при еластичен сблъсък. Променяй масите и скоростите им и виж какво се случва след сблъсъка.
""")

# Входни параметри
st.sidebar.header("🔧 Параметри на частиците")
m1 = st.sidebar.slider("Маса на частица 1 (kg)", 1.0, 10.0, 5.0)
v1 = st.sidebar.slider("Скорост на частица 1 (m/s)", -10.0, 0.0, -5.0)
m2 = st.sidebar.slider("Маса на частица 2 (kg)", 1.0, 10.0, 5.0)
v2 = st.sidebar.slider("Скорост на частица 2 (m/s)", 0.0, 10.0, 5.0)

st.subheader("⚙️ Изчисления след сблъсъка")
v1f = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
v2f = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)

st.write(f"➡️ Скорост на частица 1 след сблъсъка: **{v1f:.2f} m/s**")
st.write(f"➡️ Скорост на частица 2 след сблъсъка: **{v2f:.2f} m/s**")

t = np.linspace(0, 2, 100)
x1_before = v1 * t
x2_before = v2 * t
x1_after = v1f * t + x1_before[-1]
x2_after = v2f * t + x2_before[-1]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, x1_before, label="Частица 1 (преди)", color='blue')
ax.plot(t, x2_before, label="Частица 2 (преди)", color='red')
ax.plot(t, x1_after, '--', label="Частица 1 (след)", color='blue')
ax.plot(t, x2_after, '--', label="Частица 2 (след)", color='red')
ax.set_xlabel("Време (s)")
ax.set_ylabel("Позиция (m)")
ax.set_title("Движение на частиците преди и след сблъсъка")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.subheader("🧪 Тест: Какво научи?")
question = st.radio(
    "Какво се случва при еластичен сблъсък?",
    options=[
        "Сумата от кинетичната енергия се запазва",
        "Импулсът се губи",
        "Частиците спират"
    ]
)

if question == "Сумата от кинетичната енергия се запазва":
    st.success("✅ Правилно! Еластичният сблъсък запазва енергията и импулса.")
else:
    st.error("❌ Не е вярно. При еластичен сблъсък се запазват както енергията, така и импулсът.")

st.markdown("""
---
**📚 Научи повече:**  
В ЦЕРН учените изследват сблъсъци между протони при високи енергии, за да разкрият какво стои в основата на материята и силите в природата.  
Тези принципи на импулс и енергия стоят в основата на всички експерименти в Големия адронен ускорител.
""")
