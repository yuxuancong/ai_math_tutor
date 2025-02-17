from typing import Dict, Any, Optional
import requests
from .base_engine import BaseEngine, EngineStatus

class AIEngine(BaseEngine):
    """AI����ʵ��"""
    
    def __init__(self):
        super().__init__()
        self.api_key = None
        self.api_endpoint = None
        
    def initialize(self, config: Dict[str, Any]) -> bool:
        """��ʼ��AI����"""
        try:
            self.api_key = config.get('api_key')
            self.api_endpoint = config.get('api_endpoint')
            
            if not self.api_key or not self.api_endpoint:
                raise ValueError("Missing API configuration")
                
            self.status = EngineStatus.RUNNING
            return True
        except Exception as e:
            self.logger.error(f"AI�����ʼ��ʧ��: {str(e)}")
            self.status = EngineStatus.ERROR
            return False
    
    def generate_response(self, prompt: str) -> Optional[str]:
        """����AI��Ӧ"""
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
                self.logger.error(f"API����: {response.status_code}")
                return None
                
        except Exception as e:
            self.logger.error(f"������Ӧʧ��: {str(e)}")
            return None
            
    def evaluate_answer(self, question: str, answer: str) -> Dict[str, Any]:
        """������"""
        prompt = f"""
        ����: {question}
        ѧ����: {answer}
        ����������𰸣����������¸�ʽ:
        {{
            "correct": true/false,
            "score": 0-100,
            "feedback": "���巴��",
            "explanation": "��ϸ����"
        }}
        """
        
        response = self.generate_response(prompt)
        if not response:
            return {
                "correct": False,
                "score": 0,
                "feedback": "����ϵͳ��ʱ�޷�ʹ��",
                "explanation": "���Ժ�����"
            }
            
        try:
            # ����AI���ص��Ǹ�ʽ����JSON�ַ���
            import json
            return json.loads(response)
        except:
            return {
                "correct": False,
                "score": 0,
                "feedback": "�����������ʧ��",
                "explanation": "ϵͳ����"
            }
    
    def shutdown(self) -> bool:
        """�ر�AI����"""
        try:
            self.status = EngineStatus.STOPPED
            return True
        except Exception as e:
            self.logger.error(f"�ر�AI����ʧ��: {str(e)}")
            self.status = EngineStatus.ERROR
            return False 