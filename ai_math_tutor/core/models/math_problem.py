from sqlalchemy import Column, Integer, String, Text, Float
from core.models.base import Base

class MathProblem(Base):
    __tablename__ = 'math_problems'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    difficulty = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    solution = Column(Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'difficulty': self.difficulty,
            'category': self.category,
            'solution': self.solution
        } 