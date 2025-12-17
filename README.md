# Python Prompt Framework

**Python Prompt Framework** is a modular and reusable Python framework for **creating, managing, and rendering dynamic AI prompts**. It supports structured outputs, few-shot examples, role-based prompts, and Chain-of-Thought reasoning, making it easy to build complex workflows for Large Language Models (LLMs).

---

## Features

- Single or multi-step prompt rendering
- Dynamic input variable validation using Pydantic
- Support for zero-shot, few-shot, structured outputs, and CoT (Chain-of-Thought) prompts
- Role-based prompts for teacher, expert, or user simulation
- JSON output support for structured data
- Prompt chaining for complex AI workflows
- Easy-to-extend and maintainable Python API

---

## Project Structure

python_prompt_framework/
│
├── framework/ # Main package
│ ├── init.py # Package initializer
│ ├── core.py # Prompt engine (load & render templates)
│ ├── prompt_chain.py # Handles prompt chaining
│
├── templates/ # YAML prompt templates
│ ├── zero_shot_1.yaml
│ ├── zero_shot_2.yaml
│ ├── structured_output_1.yaml
│ ├── structured_output_2.yaml
│ ├── role_based_1.yaml
│ ├── role_based_2.yaml
│ ├── few_shot_1.yaml
│ ├── few_shot_2.yaml
│ ├── chain_of_thought_1.yaml
│ └── chain_of_thought_2.yaml
│
├── examples.py # Example usage
├── requirements.txt # Python dependencies
├── pyproject.toml # Project metadata & build configuration
├── README.md # This file
└── .gitignore # Ignore unnecessary files/folders


## Installation

Clone the repository:

git clone https://github.com/N-Haritha16/python_prompt_framework.git
cd python_prompt_framework

## Install dependencies:

pip install -r requirements.txt

## Usage Example

from python_prompt_framework.core import TemplateLoader, PromptEngine
from python_prompt_framework.prompt_chain import PromptChain

 // Load templates

loader = TemplateLoader("templates")
loader.load_templates()

// Initialize engine

engine = PromptEngine(loader.templates)

// Render a single prompt

print(engine.render("sum_example.yaml", a=10, b=20))

// Run a chain of prompts

chain = PromptChain(engine)
sequence = ["sum_example.yaml", "chain_of_thought_1.yaml"]
result = chain.run_chain(sequence, {"a": 5, "b": 15})
print(result)

## Contributing

Fork the repository

Create a new branch (git checkout -b feature-name)

Make your changes

Commit your changes (git commit -m "Add feature")

Push to the branch (git push origin feature-name)

Open a Pull Request


---

# 📄 `LICENSE` (MIT – Safe for academic use)
```txt
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

