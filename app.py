import streamlit as st
import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Category info
category_info = {
    "false_urgency": {
        "icon": "⏰",
        "title": "FALSE URGENCY",
        "description": "Creates artificial time pressure or fake scarcity to rush your decision.",
        "example": "Only 2 left in stock! Order now!",
        "color": "#FF6B6B",
        "tip": "Check if the timer resets when you reload the page."
    },
    "confirmshaming": {
        "icon": "😔",
        "title": "CONFIRMSHAMING",
        "description": "Guilt-trips you into accepting by making the decline option sound shameful or foolish.",
        "example": "No thanks, I don't want to save money.",
        "color": "#FF9F43",
        "tip": "You always have the right to say no without feeling ashamed."
    },
    "hidden_costs": {
        "icon": "💸",
        "title": "HIDDEN COSTS",
        "description": "Hides extra fees, taxes, or charges until the very last checkout step.",
        "example": "Service fee added at checkout.",
        "color": "#EE5A24",
        "tip": "Always scroll to the final payment screen before committing."
    },
    "trick_questions": {
        "icon": "🔀",
        "title": "TRICK QUESTIONS",
        "description": "Uses confusing double negatives or misleading checkboxes to manipulate your choices.",
        "example": "Uncheck this box if you do not want to not receive emails.",
        "color": "#A29BFE",
        "tip": "Read checkbox text twice. If it's confusing, that's intentional."
    },
    "roach_motel": {
        "icon": "🪤",
        "title": "ROACH MOTEL",
        "description": "Easy to sign up, but deliberately difficult and frustrating to cancel or leave.",
        "example": "Cancellation requires calling our support line.",
        "color": "#FD79A8",
        "tip": "Test the cancellation process before you sign up."
    },
    "not_dark_pattern": {
        "icon": "✅",
        "title": "CLEAN TEXT",
        "description": "No dark pattern detected. This text appears honest, transparent and user-friendly.",
        "example": "Cancel your subscription anytime online.",
        "color": "#00B894",
        "tip": "This is what ethical design looks like. More companies should do this."
    }
}

# Quick examples for buttons
quick_examples = [
    "Only 3 left in stock!",
    "No thanks, I hate saving money.",
    "Service fee added at checkout.",
    "Uncheck if you do not want to not receive emails.",
    "Cancellation requires calling our support line.",
    "Cancel your subscription anytime online.",
]

# Page config
st.set_page_config(
    page_title="DarkPatternWatch",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main { padding-top: 2rem; }
    .result-box {
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 5px solid;
    }
    .stat-row {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🔍 DarkPatternWatch")
st.markdown("### Detect manipulative UI text using Machine Learning")
st.markdown("Paste any website text — button labels, popups, checkout messages — and instantly find out if it's a dark pattern.")
st.markdown("---")

# Stats row
col1, col2, col3 = st.columns(3)
col1.metric("Training Examples", "400+")
col2.metric("Model Accuracy", "97.5%")
col3.metric("Dark Pattern Types", "5")

st.markdown("---")

# Quick examples
st.markdown("#### ⚡ Try a quick example:")
cols = st.columns(3)
for i, example in enumerate(quick_examples):
    if cols[i % 3].button(f'"{example[:30]}..."', key=f"ex_{i}"):
        st.session_state.input_text = example

# Input area
user_input = st.text_area(
    "🔤 Or enter your own text:",
    value=st.session_state.get("input_text", ""),
    height=100,
    placeholder="e.g. Only 2 left in stock! Order now!"
)

if st.button("🔍 Analyze Text", type="primary", use_container_width=True):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        vec = vectorizer.transform([user_input])
        prediction = model.predict(vec)[0]
        proba = model.predict_proba(vec)[0]
        confidence = round(max(proba) * 100, 2)
        info = category_info[prediction]

        st.markdown("---")
        st.markdown("### 🧠 Analysis Result")

        # Color coded result
        is_dark = prediction != "not_dark_pattern"
        bg_color = "#fff5f5" if is_dark else "#f0fff4"
        border_color = info["color"]

        st.markdown(f"""
            <div style="
                background-color: {bg_color};
                border-left: 5px solid {border_color};
                padding: 1.2rem;
                border-radius: 8px;
                margin-bottom: 1rem;
            ">
                <h3 style="color: {border_color}; margin:0;">
                    {info['icon']} {info['title']}
                </h3>
                <p style="margin: 0.5rem 0 0 0; color: #444;">
                    {info['description']}
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Confidence + tip
        col1, col2 = st.columns(2)
        col1.metric("Confidence", f"{confidence}%")
        col2.info(f"💡 **Tip:** {info['tip']}")

        # Confidence breakdown
        st.markdown("### 📊 Full Confidence Breakdown")
        classes = model.classes_
        for cls, prob in sorted(zip(classes, proba), key=lambda x: -x[1]):
            cat = category_info[cls]
            st.progress(
                int(prob * 100),
                text=f"{cat['icon']} {cat['title']}: {round(prob*100, 1)}%"
            )

# About section
st.markdown("---")
with st.expander("📖 What are Dark Patterns? Learn More"):
    for key, info in category_info.items():
        if key != "not_dark_pattern":
            st.markdown(f"""
            **{info['icon']} {info['title']}**
            {info['description']}
            > *Example: "{info['example']}"*
            ---
            """)

st.caption("Built with Python · Scikit-learn · Streamlit | DarkPatternWatch v1.0 | 400+ annotated examples")