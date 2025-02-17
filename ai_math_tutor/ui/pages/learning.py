import streamlit as st
from ...core.services.learning_service import LearningService
from ..components.progress_chart import ProgressChart
from ..components.problem_card import ProblemCard

class LearningPage:
    def __init__(self, learning_service: LearningService):
        self.learning_service = learning_service
        
    def render(self):
        st.title("AI��ѧ����")
        
        # �������֪ʶ��ѡ��
        with st.sidebar:
            self.render_concept_selector()
            
        # ��������
        col1, col2 = st.columns([2, 1])
        
        with col1:
            self.render_problem_area()
            
        with col2:
            self.render_progress_area() 