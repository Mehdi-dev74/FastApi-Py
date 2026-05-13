"""
🏆 PRODUCTION Multi-Agent Research Team v2.0
Advanced features: Tools + Memory + Logging + Web UI
"""

import os
import json
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from tools.web_search import search_tool
from utils.logger import get_logger
from config import Config

load_dotenv()
config = Config()

# Initialize loggers
market_logger = get_logger("MarketAnalyst")
data_logger = get_logger("DataScientist")
report_logger = get_logger("ReportWriter")

llm = ChatOpenAI(
    model=config.MODEL_NAME,
    temperature=0.1,
    api_key=config.OPENAI_API_KEY
)

# 🛠️ ADVANCED AGENTS WITH TOOLS & MEMORY
market_analyst = Agent(
    role="Senior Market Research Analyst",
    goal="""Deliver precise market intelligence with real-time data.
    Always validate findings with external sources.""",
    backstory="""15+ years at Goldman Sachs & McKinsey. Expert in 
    competitive intelligence, financial modeling, and trend forecasting.
    Never guesses - always sources data.""",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=3
)

data_scientist = Agent(
    role="Lead Data Scientist",
    goal="Transform raw data into actionable insights and visualizations",
    backstory="""PhD from Stanford. Built ML systems at Google & OpenAI.
    Specializes in NLP, time-series, and business intelligence.""",
    llm=llm,
    verbose=True,
    max_iter=2
)

report_writer = Agent(
    role="Principal Technical Writer",
    goal="Craft executive-ready reports that drive decisions",
    backstory="""20+ years writing for Fortune 500 C-suites. 
    Transforms complex analysis into compelling narratives.""",
    llm=llm,
    verbose=True
)

# 📋 SOPHISTICATED TASKS
@st.cache_data
def create_research_crew(topic: str):
    research_task = Task(
        description=f"""
        Conduct EXHAUSTIVE market research on '{topic}'.
        
        REQUIRED ANALYSIS:
        1. Market size & growth (2024-2028)
        2. Top 5 competitors + market share
        3. Key trends & drivers
        4. SWOT analysis
        5. Risks & opportunities
        6. Pricing benchmarks
        
        ✅ USE WEB SEARCH TOOL for real-time data
        ✅ Cite ALL sources with URLs
        ✅ Include specific numbers & dates
        """,
        agent=market_analyst,
        expected_output="Comprehensive market research report with sources"
    )
    
    analysis_task = Task(
        description="""
        Analyze research findings. Extract:
        1. Key metrics & KPIs
        2. Growth projections
        3. Competitive positioning
        4. Actionable insights
        
        Create 3-5 data visualizations.
        """,
        agent=data_scientist,
        context=[research_task],
        expected_output="Data-driven insights with visualizations"
    )
    
    report_task = Task(
        description="""
        Write EXECUTIVE REPORT including:
        1. Executive Summary (3 sentences)
        2. Market Overview
        3. Competitive Landscape  
        4. Strategic Recommendations
        5. Next Steps & Timeline
        
        Format: Professional, actionable, C-suite ready
        """,
        agent=report_writer,
        context=[research_task, analysis_task],
        expected_output="Production-ready executive report (1500-2000 words)"
    )
    
    return Crew(
        agents=[market_analyst, data_scientist, report_writer],
        tasks=[research_task, analysis_task, report_task],
        process=Process.sequential,
        verbose=2,
        memory=True
    )

# 🎯 PRODUCTION RUNNER
def run_research_pipeline(topic: str, save_output: bool = True):
    """Complete production research workflow"""
    print(f"\n🚀 RESEARCH PIPELINE STARTED: {topic}")
    print("=" * 80)
    
    crew = create_research_crew(topic)
    result = crew.kickoff(inputs={"topic": topic})
    
    # Save output
    if save_output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"outputs/research_report_{timestamp}.md"
        os.makedirs("outputs", exist_ok=True)
        
        with open(filename, "w") as f:
            f.write(f"# Research Report: {topic}\n\n")
            f.write(result)
        
        print(f"\n💾 Report saved: {filename}")
    
    return result

# 🌐 STREAMLIT WEB UI
def run_streamlit():
    st.set_page_config(page_title="AI Research Team", layout="wide")
    
    st.title("🤖 AI Research Team")
    st.markdown("**Autonomous agents delivering production-grade market intelligence**")
    
    topic = st.text_input("Research topic:", "Tesla autonomous driving market")
    
    if st.button("🚀 Run Research Pipeline", type="primary"):
        with st.spinner("Agents are working..."):
            result = run_research_pipeline(topic)
            st.markdown("### 📊 Final Report")
            st.markdown(result)
            
            # Download button
            st.download_button(
                "💾 Download Report",
                data=result,
                file_name=f"research_report_{topic.replace(' ', '_')}.md"
            )

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # CLI mode
        topic = " ".join(sys.argv[1:])
        result = run_research_pipeline(topic)
        print("\n" + "="*80)
        print("🏆 FINAL EXECUTIVE REPORT")
        print("="*80)
        print(result)
    else:
        # Web UI mode
        run_streamlit()
