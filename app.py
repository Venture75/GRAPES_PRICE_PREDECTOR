import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Grapes Price Predictor",
    page_icon="🍇",
    layout="centered"
)

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #1a0033 0%, #3d0066 50%, #1a0033 100%); }
.main-title { text-align:center; font-size:2.8rem; font-weight:800; color:#e0aaff;
              text-shadow:0 0 20px rgba(224,170,255,0.5); margin-bottom:0.2rem; }
.sub-title  { text-align:center; color:#c77dff; font-size:1rem; margin-bottom:2rem; }
.result-box { background:linear-gradient(135deg,#7b2fff,#c77dff); border-radius:20px;
              padding:2rem; text-align:center; margin-top:1.5rem;
              box-shadow:0 0 40px rgba(123,47,255,0.6); }
.result-label { color:#fff; font-size:1rem; opacity:0.85; }
.result-value { color:#fff; font-size:2.8rem; font-weight:900; margin:0.3rem 0; }
.result-sub   { color:rgba(255,255,255,0.75); font-size:0.9rem; }
.stButton > button { width:100%; background:linear-gradient(90deg,#7b2fff,#c77dff);
    color:white; font-size:1.1rem; font-weight:700; border:none; border-radius:12px;
    padding:0.8rem; margin-top:1rem; }
label { color:#ddd !important; font-size:0.9rem !important; }
.footer { text-align:center; color:rgba(200,180,255,0.5); font-size:0.75rem; margin-top:2rem; }
</style>
""", unsafe_allow_html=True)

# ── Load model bundle (joblib — version-safe) ──────────────────────────────────
@st.cache_resource
def load_model_bundle():
    return joblib.load("model.pkl")

try:
    bundle      = load_model_bundle()
    model       = bundle["model"]
    encoders    = bundle["encoders"]
    scaler      = bundle["scaler"]
    feat_cols   = bundle["feature_cols"]
    cat_cols    = bundle["cat_cols"]
    num_cols    = bundle["num_cols"]
    model_ok    = True
except Exception as e:
    model_ok = False
    err_msg  = str(e)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">🍇 Grapes Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Tanzania Grapes Market · Powered by Machine Learning</div>',
            unsafe_allow_html=True)

if not model_ok:
    st.error(f"Could not load model.pkl — {err_msg}")
    st.stop()

# ── Input Form ─────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Location & Type")
    region     = st.selectbox("Region",
                    ["Dodoma","Arusha","Morogoro","Mbeya","Singida"])
    grape_type = st.selectbox("Grape Type",
                    ["Red Globe","Thompson Seedless","Muscat","Flame Seedless"])
    season     = st.selectbox("Season",
                    ["Dry Season","Wet Season"])
    quality    = st.selectbox("Quality Grade",
                    ["Grade A","Grade B","Grade C"])

with col2:
    st.subheader("📊 Farm & Market Details")
    weight    = st.slider("Weight (kg)",               0.5, 10.0,  5.0, step=0.5)
    sugar     = st.slider("Sugar Content (Brix %)",   10.0, 25.0, 18.0, step=0.5)
    farm_size = st.slider("Farm Size (hectares)",      0.5, 20.0,  5.0, step=0.5)
    distance  = st.slider("Distance to Market (km)",    5,  300,   80,  step=5)
    rainfall  = st.slider("Rainfall (mm)",             400, 1200,  700, step=50)

# ── Prediction ─────────────────────────────────────────────────────────────────
if st.button("🍇 Predict Grape Price"):
    # Build raw input DataFrame
    raw = pd.DataFrame([{
        "Region":               region,
        "Grape_Type":           grape_type,
        "Season":               season,
        "Quality_Grade":        quality,
        "Weight_kg":            weight,
        "Sugar_Content_Brix":   sugar,
        "Farm_Size_ha":         farm_size,
        "Distance_to_Market_km": distance,
        "Rainfall_mm":          rainfall
    }])

    # Encode categoricals
    for col in cat_cols:
        raw[col] = encoders[col].transform(raw[col])

    # Scale numericals
    raw[num_cols] = scaler.transform(raw[num_cols])

    # Predict
    pred = float(model.predict(raw[feat_cols])[0])
    pred = max(1000.0, min(12000.0, pred))

    grade_tag = "🥇 Premium" if quality == "Grade A" else \
                ("🥈 Standard" if quality == "Grade B" else "🥉 Economy")

    st.markdown(f"""
    <div class="result-box">
      <div class="result-label">Estimated Grapes Price</div>
      <div class="result-value">TZS {pred:,.0f}</div>
      <div class="result-sub">per kilogram · {region} · {grape_type} · {grade_tag}</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("💰 Price / kg",   f"TZS {pred:,.0f}")
    c2.metric("📦 Total Value",  f"TZS {pred * weight:,.0f}", f"{weight} kg")
    c3.metric("🌡️ Sugar Level",  f"{sugar} Brix",
              "High 🔼" if sugar > 18 else "Medium ➡")

st.markdown(
    '<div class="footer">🍇 Grapes Price Predictor · Tanzania ML Project · 2026</div>',
    unsafe_allow_html=True)
