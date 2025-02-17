from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
from ...core.services.learning_service import LearningService
from ...core.models.user import User
from ..middleware.auth import get_current_user

router = APIRouter()

@router.get("/problems/next")
async def get_next_problem(
    concept: str,
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """获取下一个练习题"""
    try:
        problem = await learning_service.get_next_problem(
            current_user.id,
            concept
        )
        return problem
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 