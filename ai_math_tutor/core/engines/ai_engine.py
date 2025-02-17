from typing import Dict, Any, Optional
import requests
from .base_engine import BaseEngine, EngineStatus

class AIEngine(BaseEngine):
    """AI引擎实现"""
    
    def __init__(self):
        super().__init__()
        self.api_key = None
        self.api_endpoint = None
        
    def initialize(self, config: Dict[str, Any]) -> bool:
        """初始化AI引擎"""
        try:
            self.api_key = config.get('api_key')
            self.api_endpoint = config.get('api_endpoint')
            
            if not self.api_key or not self.api_endpoint:
                raise ValueError("Missing API configuration")
                
            self.status = EngineStatus.RUNNING
            return True
        except Exception as e:
            self.logger.error(f"AI引擎初始化失败: {str(e)}")
            self.status = EngineStatus.ERROR
            return False
    
    def generate_response(self, prompt: str) -> Optional[str]:
        """生成AI响应"""
        if self.status != EngineStatus.RUNNING:
            return None
            
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 1000
            }
            
            response = requests.post(
                self.api_endpoint,
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                self.logger.error(f"API错误: {response.status_code}")
                return None
                
        except Exception as e:
            self.logger.error(f"生成响应失败: {str(e)}")
            return None
            
    def evaluate_answer(self, question: str, answer: str) -> Dict[str, Any]:
        """评估答案"""
        prompt = f"""
        问题: {question}
        学生答案: {answer}
        请评估这个答案，并返回以下格式:
        {{
            "correct": true/false,
            "score": 0-100,
            "feedback": "具体反馈",
            "explanation": "详细解释"
        }}
        """
        
        response = self.generate_response(prompt)
        if not response:
            return {
                "correct": False,
                "score": 0,
                "feedback": "评估系统暂时无法使用",
                "explanation": "请稍后再试"
            }
            
        try:
            # 假设AI返回的是格式化的JSON字符串
            import json
            return json.loads(response)
        except:
            return {
                "correct": False,
                "score": 0,
                "feedback": "评估结果解析失败",
                "explanation": "系统错误"
            }
    
    def shutdown(self) -> bool:
        """关闭AI引擎"""
        try:
            self.status = EngineStatus.STOPPED
            return True
        except Exception as e:
            self.logger.error(f"关闭AI引擎失败: {str(e)}")
            self.status = EngineStatus.ERROR
            return False 