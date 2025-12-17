
from pathlib import Path
from .core import PromptEngine
from .prompt_chain import PromptChain

# Optional: expose a default templates directory
DEFAULT_TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

__all__ = [
    "load_template",
    "render_prompt",
    "PromptChain",
    "DEFAULT_TEMPLATES_DIR"
]
