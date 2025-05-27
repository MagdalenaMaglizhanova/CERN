import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Particle collision simulation", layout="centered")
st.title("Particle Collision Simulation")
st.markdown("""
Explore how two particles behave during an elastic collision. Adjust their masses and velocities and see what happens after the collision.
""")

# Input parameters
st.sidebar.header("Particle Parameters")
m1 = st.sidebar.slider("Mass of Particle 1 (kg)", 1.0, 10.0, 5.0)
v1 = st.sidebar.slider("Velocity of Particle 1 (m/s)", -10.0, 0.0, -5.0)
m2 = st.sidebar.slider("Mass of Particle 2 (kg)", 1.0, 10.0, 5.0)
v2 = st.sidebar.slider("Velocity of Particle 2 (m/s)", 0.0, 10.0, 5.0)

st.subheader("Calculations after Collision")
v1f = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
v2f = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)

st.write(f"Velocity of Particle 1 after collision: **{v1f:.2f} m/s**")
st.write(f"Velocity of Particle 2 after collision: **{v2f:.2f} m/s**")

t = np.linspace(0, 2, 100)
x1_before = v1 * t
x2_before = v2 * t
x1_after = v1f * t + x1_before[-1]
x2_after = v2f * t + x2_before[-1]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, x1_before, label="Particle 1 (before)", color='blue')
ax.plot(t, x2_before, label="Particle 2 (before)", color='red')
ax.plot(t, x1_after, '--', label="Particle 1 (after)", color='blue')
ax.plot(t, x2_after, '--', label="Particle 2 (after)", color='red')
ax.set_xlabel("Time (s)")
ax.set_ylabel("Position (m)")
ax.set_title("Particle Motion Before and After Collision")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.subheader("Quiz: What did you learn?")
question = st.radio(
    "What happens in an elastic collision?",
    options=[
        "The total kinetic energy is conserved",
        "Momentum is lost",
        "Particles stop moving"
    ]
)

if question == "The total kinetic energy is conserved":
    st.success("Correct! Elastic collisions conserve both energy and momentum.")
else:
    st.error("Incorrect. In an elastic collision, both energy and momentum are conserved.")

st.markdown("""
---
**Learn More:**  
At CERN, scientists study proton collisions at high energies to reveal the fundamental nature of matter and forces.  
The principles of momentum and energy conservation are the basis of all experiments at the Large Hadron Collider.
""")
