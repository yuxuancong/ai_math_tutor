from flask import Blueprint, request, jsonify
from core.services.math_problem_service import MathProblemService
from infrastructure.database.connection import get_db_session
from api.middleware.auth import auth_required

bp = Blueprint('math_problems', __name__)

@bp.route('/problems', methods=['GET'])
@auth_required
def get_problems():
    db = get_db_session()
    try:
        service = MathProblemService(db)
        problems = service.get_problems(
            skip=request.args.get('skip', 0, type=int),
            limit=request.args.get('limit', 10, type=int),
            difficulty=request.args.get('difficulty', type=int),
            category=request.args.get('category')
        )
        return jsonify([p.to_dict() for p in problems])
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

@bp.route('/problems/<int:problem_id>', methods=['GET'])
@auth_required
def get_problem(problem_id):
    db = get_db_session()
    try:
        service = MathProblemService(db)
        problem = service.get_problem_by_id(problem_id)
        if problem:
            return jsonify(problem.to_dict())
        return jsonify({"error": "Problem not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close() 