from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class Movie:
    id: int
    title: str
    poster_path: Optional[str]
    
    def __init__(self, **kwargs):
        # Campos obrigatórios
        self.id = kwargs['id']
        self.title = kwargs['title']
        self.poster_path = kwargs.get('poster_path')
        
        # Armazena campos adicionais
        self._extra_fields = {k: v for k, v in kwargs.items() 
                            if k not in ['id', 'title', 'poster_path']}
    
    @property
    def has_poster(self) -> bool:
        return bool(self.poster_path)
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'title': self.title,
            'poster_path': self.poster_path
        } 