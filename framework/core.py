import json
from pathlib import Path
import yaml
from jinja2 import Template
from pydantic import create_model, ValidationError
# from .models import PromptConfig
from pydantic import BaseModel
from typing import List, Optional

class InputVar(BaseModel):
    name: str
    type: str = "str"   # str, int, list
    required: bool = True

class PromptConfig(BaseModel):
    name: str
    description: Optional[str] = ""
    input_vars: List[InputVar]
    template: str

class PromptEngine:
    def __init__(self, templates_dir="templates"):
        self.templates_dir = Path(templates_dir)
        self.templates = {}  # optional cache

    def load_prompt(self, filename: str) -> PromptConfig:
        file_path = self.templates_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found in {self.templates_dir}")
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return PromptConfig(**data)

    def render(self, filename: str, **inputs) -> str:
        prompt = self.load_prompt(filename)

        # Dynamic Pydantic model for input validation
        fields_dict = {}
        for var in prompt.input_vars:
            typ = str
            if var.type == "int":
                typ = int
            elif var.type == "list":
                typ = list
            fields_dict[var.name] = (typ, ...) if var.required else (typ, None)

        InputModel = create_model("InputModel", **fields_dict)

        try:
            validated_data = InputModel(**inputs).model_dump()
        except ValidationError as e:
            return json.dumps({"error": e.errors()}, indent=2)

        # Render Jinja2 template
        template = Template(prompt.template)
        rendered_output = template.render(**validated_data)

        # Return structured JSON
        result = {
            "prompt_name": prompt.name,
            "description": prompt.description,
            "inputs": validated_data,
            "output": rendered_output
        }
        return json.dumps(result, indent=2)
