import time
import json
import streamlit as st

from wail_runtime import WailRuntime


st.set_page_config(
    page_title="WAIL Runtime Demo",
    layout="centered"
)

st.title("WAIL Runtime Demo")
st.write("Enter a prompt and observe runtime-level execution signals.")

# ---- DEBUG: UI VERSION ----
st.caption("UI version: behaviour_signals_enabled")

prompt = st.text_area("Prompt", height=120)
run = st.button("Run")

if run and prompt.strip():
    st.divider()
    st.subheader("Execution")

    wail = WailRuntime()
    wail.start_execution()

    token_placeholder = st.empty()
    displayed_tokens = []

    tokens = prompt.split()

    for token in tokens:
        time.sleep(0.15)
        displayed_tokens.append(token)
        token_placeholder.markdown(
            "**Observed tokens:** " + " ".join(displayed_tokens)
        )
        wail.observe_token(token)

    trace = wail.end_execution()

    # ---- DEBUG: RAW SIGNALS ----
    st.divider()
    st.subheader("Debug: Raw Behaviour Signals")
    st.json(trace.behaviour_signals)

    # ---- HUMAN READABLE OUTPUT ----
    st.divider()
    st.subheader("Captured Runtime Signals")

    st.write(f"**Output ID:** {trace.execution_id[:8]}")

    signals = trace.behaviour_signals

    if isinstance(signals, dict) and signals:
        for key, value in signals.items():
            if key in ["signal_mode", "derived_from"]:
                continue
            st.write(f"• **{key}**: {value}")
    else:
        st.error("Behaviour signals not available in trace.")

    st.caption("Derived from a single execution (demo)")

    # ---- DOWNLOAD JSON ----
    trace_file = f"traces/trace_{trace.execution_id}.json"
    with open(trace_file, "w", encoding="utf-8") as f:
        json.dump(trace.to_dict(), f, indent=2)

    with open(trace_file, "r", encoding="utf-8") as f:
        st.download_button(
            label="Download execution trace (JSON)",
            data=f,
            file_name=f"trace_{trace.execution_id}.json",
            mime="application/json"
        )

elif run:
    st.warning("Please enter a prompt.")
