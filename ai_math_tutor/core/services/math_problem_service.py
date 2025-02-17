from typing import List, Optional
from sqlalchemy.orm import Session
from core.models.math_problem import MathProblem

class MathProblemService:
    def __init__(self, db: Session):
        self.db = db

    def get_problems(
        self, 
        skip: int = 0, 
        limit: int = 10,
        difficulty: Optional[int] = None,
        category: Optional[str] = None
    ) -> List[MathProblem]:
        query = self.db.query(MathProblem)
        
        if difficulty is not None:
            query = query.filter(MathProblem.difficulty == difficulty)
        if category:
            query = query.filter(MathProblem.category == category)
            
        return query.offset(skip).limit(limit).all()

    def get_problem_by_id(self, problem_id: int) -> Optional[MathProblem]:
        return self.db.query(MathProblem).filter(MathProblem.id == problem_id).first()

    def create_problem(self, title: str, content: str, difficulty: int, category: str, solution: str) -> MathProblem:
        problem = MathProblem(
            title=title,
            content=content,
            difficulty=difficulty,
            category=category,
            solution=solution
        )
        self.db.add(problem)
        self.db.commit()
        self.db.refresh(problem)
        return problem 