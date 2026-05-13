import streamlit as st
import asyncio
from agent import WebAutomationAgent

st.set_page_config(page_title="🤖 Web Automation Agent", layout="wide")

st.title("🕷️ Web Automation Agent")
st.markdown("**AI that shops, books, researches autonomously**")

if "agent" not in st.session_state:
    st.session_state.agent = None

goal = st.text_area("What should the agent do?", 
                   placeholder="Find best laptop under $1000 on Amazon and add to cart")

if st.button("🚀 Launch Agent", type="primary"):
    with st.spinner("Agent activating..."):
        st.session_state.agent = WebAutomationAgent()
        asyncio.run(st.session_state.agent.run_mission(goal))
    
    st.success("🎉 Mission complete!")
    st.image("step_*.png")  # Shows screenshots

# Demo video placeholder
st.video("demo_video.mp4")
