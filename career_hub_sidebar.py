"""
=============================================================================
MODULE: career_hub_sidebar.py (UI Controller)
AUTHOR: Kyle W. Killebrew, PhD
DESCRIPTION: 
    Centralized sidebar component for the Career Hub ecosystem.
    Imports into app.py and all pages/ scripts to ensure a uniform
    UI without duplicating code.
=============================================================================
"""

import streamlit as st
import os
from PIL import Image

def apply_global_settings(hub_title):
    """
    Sets the favicon and page title across the hub.
    """
    favicon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "documents", "Neuro-Edu_favicon_Transparent.ico")

    try:
        favicon = Image.open(favicon_path)
    except Exception:
        favicon = "🧠" 

    st.set_page_config(
        page_title=hub_title,
        page_icon=favicon,
        layout="wide",
        initial_sidebar_state="expanded"
    )

def render_sidebar():
    """
    Renders the centralized sidebar with custom CSS and navigation.
    """
    # --- 1. GLOBAL SIDEBAR CSS (Styling & Bug Fixes) ---
    st.markdown("""
        <style>
        /* Hide the default Streamlit sidebar navigation menu */
        [data-testid="stSidebarNav"] {display: none;}
        
        /* Fix the Chevron Bug: Prevent custom fonts from overriding icons */
        [data-testid="collapsedControl"] {
            font-family: sans-serif !important; 
        }

        /* Standardize Sidebar Background & STRICTLY Enforce Text Color */
        [data-testid="stSidebar"] {
            background-color: #0F172A !important; 
        }
        
        /* Prevents Streamlit's Light/Dark mode auto-detect from turning text gray */
        [data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {
            color: #F8FAFC !important;
        }
        
        /* Unique Sidebar Classes to prevent CSS leakage from main app */
        .sidebar-masthead-container {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-top: -40px; 
            margin-bottom: 30px;
        }
        .sidebar-text-container {
            line-height: 1.25;
        }
        .sidebar-name {
            font-size: 1.15rem;
            font-weight: bold;
            color: #F8FAFC !important;
            margin-bottom: 4px;
        }
        .sidebar-subtitle {
            font-size: 0.75rem; 
            color: #94A3B8 !important; 
            line-height: 1.3;
        }

        /* Add this to the bottom of the CSS block in career_hub_sidebar.py */
        .presence-bar { display: flex; gap: 15px; justify-content: center; margin-top: 30px; margin-bottom: 20px; }
        .presence-icon { color: #94A3B8; transition: color 0.3s; }
        .presence-icon:hover { color: #38BDF8; }
        .sidebar-footer { text-align: center; font-size: 0.75rem; color: #64748B; margin-top: 40px; }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # --- 2. MASTHEAD ---        
        col1, col2 = st.columns([1, 2.5], gap="small")
        
        with col1:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(base_dir, "documents", "Neuro-Edu_Logo_Transparent.png")
            
            if os.path.exists(logo_path):
                st.image(logo_path, use_container_width=True)
            else:
                st.write("🧠") 
        
        with col2:
             # Applied completely unique CSS classes to lock the size down safely
             st.markdown("""
                <div class="sidebar-text-container">
                    <div class="sidebar-name">Kyle W. Killebrew, PhD</div>
                    <div class="sidebar-subtitle">Behavioral, Cognitive, Neuro, and Data Scientist and Educational Mentor</div>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        
        # --- 3. CUSTOM NAVIGATION ---        
        # Internal Streamlit Page Links
        st.page_link("career_hub_app.py", label="Home")
        st.page_link("pages/1_academic_research_app.py", label="Academic Research")
        st.page_link("pages/2_mentorship_app.py", label="Education & Mentorship")
        
        # External Data Science Link (Opens in new tab)
        st.markdown("""
            <div style="margin-top: 5px;">
                <a href="https://data-projects.neuro-edu.io/" target="_blank" style="text-decoration: none; color: #F8FAFC; display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1rem;">Data Science Portfolio ↗</span>
                </a>
            </div>
        """, unsafe_allow_html=True)

        # --- 4. PRESENCE / SOCIAL BAR (Global Scope) ---
        presence_html = """
        <div class="presence-bar">
            <a href="https://scholar.google.com/citations?user=y-2G-voAAAAJ&hl=en" target="_blank" class="presence-icon" title="Google Scholar">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5l4.838 3.911V22.5l7.162 1.5 7.162-1.5v-9.089l2.438-1.971V18h2V8.342L12 0z"/></svg>
            </a>
            <a href="https://www.linkedin.com/in/kylewkillebrew/" target="_blank" class="presence-icon" title="LinkedIn">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
            <a href="https://orcid.org/0000-0002-9662-9844" target="_blank" class="presence-icon" title="ORCID">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.369 4.378c.525 0 .947.431.947.947s-.422.949-.947.949a.95.95 0 0 1-.949-.949c0-.516.424-.947.949-.947zm-.722 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344 5.025 0 2.578-2.016 5.025-5.325 5.025h-3.919V7.416zm1.444 1.303v7.444h2.297c3.272 0 4.022-2.484 4.022-3.722 0-2.016-1.284-3.722-4.097-3.722h-2.222z"/></svg>
            </a>
            <a href="https://github.com/kkillebrew" target="_blank" class="presence-icon" title="GitHub">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.332-5.467-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
            </a>
        </div>
        """
        st.markdown(presence_html, unsafe_allow_html=True)

        # --- 5. COPYRIGHT FOOTER ---
        st.markdown("""
            <div class="sidebar-footer">
                © 2026 Kyle W. Killebrew.<br>
                Resume and website entirely self authored.<br>
                Analysis, figures, models, and data authored and<br>
                collected by a vibrant array of professors, postdocs,<br>
                grad students, techs, professionals, and friends.<br>
                References reported for all published analysis. 
            </div>
        """, unsafe_allow_html=True)