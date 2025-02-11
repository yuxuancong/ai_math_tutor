#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Web Interface Module using Streamlit"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np
from typing import Dict, List, Any
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from ai_math_tutor.core.architecture import TeachingEngine, SystemManager, LearningProgress

class MathTutorUI:
    def __init__(self):
        st.set_page_config(
            page_title="AI Math Tutor",
            page_icon="📚",
            layout="wide"
        )
        
        self.system_manager = SystemManager()
        self.initialize_session_state()
        
    def initialize_session_state(self):
        """Initialize session state variables"""
        if 'student_id' not in st.session_state:
            st.session_state.student_id = None
        if 'current_concept' not in st.session_state:
            st.session_state.current_concept = None
        if 'practice_history' not in st.session_state:
            st.session_state.practice_history = []
            
    def render_login_page(self):
        """Render login page"""
        st.title("AI Math Tutor")
        
        with st.form("login_form"):
            student_id = st.text_input("Student ID")
            submitted = st.form_submit_button("Login")
            
            if submitted and student_id:
                st.session_state.student_id = student_id
                st.success(f"Welcome back, {student_id}!")
                st.rerun()
                
    def render_concept_selection(self):
        """Render concept selection panel"""
        st.sidebar.title("Learning Concepts")
        
        available_concepts = self.system_manager.teaching_engine.knowledge_graph.get_concepts()
        
        selected_concept = st.sidebar.selectbox(
            "Select Learning Concept",
            available_concepts,
            format_func=lambda x: x.replace("_", " ").title()
        )
        
        if selected_concept != st.session_state.current_concept:
            st.session_state.current_concept = selected_concept
            st.rerun()
            
    def render_learning_dashboard(self):
        """Render learning dashboard"""
        st.title(f"Learning Concept: {st.session_state.current_concept}")
        
        status = self.system_manager.teaching_engine.get_student_status(
            st.session_state.student_id
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            self.render_progress_card(status)
        with col2:
            self.render_weak_concepts_card(status)
        with col3:
            self.render_practice_stats_card(status)
            
    def render_progress_card(self, status: Dict[str, Any]):
        """Render progress card"""
        st.markdown("### Learning Progress")
        
        overall_mastery = status.get("overall_mastery", 0.0)
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = overall_mastery * 100,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Overall Mastery"},
            gauge = {
                'axis': {'range': [0, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 60], 'color': "lightgray"},
                    {'range': [60, 80], 'color': "gray"},
                    {'range': [80, 100], 'color': "darkgray"}
                ]
            }
        ))
        
        st.plotly_chart(fig)
        
    def render_weak_concepts_card(self, status: Dict[str, Any]):
        """Render weak concepts card"""
        st.markdown("### Concepts to Strengthen")
        
        weak_concepts = status.get("weak_concepts", [])
        if weak_concepts:
            for concept in weak_concepts:
                st.warning(f"- {concept}")
        else:
            st.success("No concepts need strengthening at the moment")
            
    def render_practice_stats_card(self, status: Dict[str, Any]):
        """Render practice statistics card"""
        st.markdown("### Practice Statistics")
        
        progress_data = status.get("detailed_progress", {})
        if progress_data:
            practice_data = {
                concept: data.practice_count 
                for concept, data in progress_data.items()
            }
            
            fig = px.bar(
                x=list(practice_data.keys()),
                y=list(practice_data.values()),
                title="Practice Distribution"
            )
            st.plotly_chart(fig)
        else:
            st.info("No practice data available")
            
    def render_practice_interface(self):
        """Render practice interface"""
        st.markdown("### Practice")
        
        problem = self.system_manager.teaching_engine.generate_problem(
            st.session_state.current_concept
        )
        
        if problem:
            with st.form("practice_form"):
                st.markdown(f"**Question**: {problem['question']}")
                user_answer = st.text_input("Your Answer")
                submitted = st.form_submit_button("Submit")
                
                if submitted:
                    self.handle_practice_submission(problem, user_answer)
                    
    def handle_practice_submission(self, problem: Dict[str, Any], user_answer: str):
        """Handle practice submission"""
        assessment_result = self.system_manager.teaching_engine.assess_answer(
            problem,
            user_answer
        )
        
        self.system_manager.teaching_engine.update_student_progress(
            st.session_state.student_id,
            st.session_state.current_concept,
            assessment_result
        )
        
        if assessment_result["correct"]:
            st.success("Correct answer!")
            st.balloons()
        else:
            st.error("Incorrect answer")
            st.markdown(f"Correct answer: {problem['solution']}")
            st.markdown(f"Explanation: {problem['explanation']}")
            
        st.session_state.practice_history.append({
            'timestamp': datetime.now(),
            'concept': st.session_state.current_concept,
            'correct': assessment_result["correct"]
        })
            
    def run(self):
        """Run the UI"""
        if not st.session_state.student_id:
            self.render_login_page()
        else:
            self.render_concept_selection()
            if st.session_state.current_concept:
                self.render_learning_dashboard()
                self.render_practice_interface()

if __name__ == "__main__":
    ui = MathTutorUI()
    ui.run()