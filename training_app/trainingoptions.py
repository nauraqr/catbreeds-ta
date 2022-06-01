from dataclasses import dataclass
from typing import Optional

@dataclass
class TrainingOptions:
    path_dir: Optional[str] = None