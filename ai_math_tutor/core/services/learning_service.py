from typing import Dict, List, Optional
from ..models.user import User
from ..models.progress import LearningProgress
from ..engines.teaching_engine import TeachingEngine
from ..engines.ai_engine import BaseAIEngine

class LearningService:
    """ѧϰ����"""
    def __init__(
        self, 
        teaching_engine: TeachingEngine,
        ai_engine: BaseAIEngine
    ):
        self.teaching_engine = teaching_engine
        self.ai_engine = ai_engine
        
    async def get_next_problem(
        self, 
        user_id: str,
        concept: str
    ) -> Optional[Dict[str, Any]]:
        """��ȡ��һ����ϰ��"""
        user_level = await self.get_user_level(user_id, concept)
        return self.teaching_engine.generate_problem(concept, user_level)
        
    async def evaluate_answer(
        self,
        user_id: str,
        problem_id: str,
        answer: str
    ) -> Dict[str, Any]:
        """������"""
        pass 