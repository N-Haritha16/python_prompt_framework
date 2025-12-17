import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from framework.core import PromptEngine
from framework.prompt_chain import PromptChain


engine = PromptEngine("templates")


print(engine.render("zero_shot_1.yaml", user_name="Haritha"))
print(engine.render("few_shot_1.yaml", a=10, b=20))
print(engine.render("structured_output_1.yaml", name="Alice", age=30))
print(engine.render("zero_shot_2.yaml", user_name="Haritha"))
print(engine.render("few_shot_2.yaml", x=7, y=9))
print(engine.render("chain_of_thought_1.yaml", a=10, b=20))
print(engine.render("chain_of_thought_2.yaml", x=7, y=9))
print(engine.render("role_based_1.yaml", user_name="John"))
print(engine.render("role_based_2.yaml", user_name="John"))
print(engine.render("structured_output_2.yaml", product_name="Aha-Bha", price=30))

chain = PromptChain(engine)

sequence1 = ["zero_shot_1.yaml", "zero_shot_2.yaml"]
print("sequence1",chain.run_chain(sequence1, {"user_name": "Haritha"}))

sequence2 = ["few_shot_1.yaml", "chain_of_thought_1.yaml"]
print("sequence2",chain.run_chain(sequence2, {"a": 10, "b": 20}))

sequence3 = ["few_shot_2.yaml", "chain_of_thought_2.yaml"]
print("sequence3",chain.run_chain(sequence3, {"x": 7, "y": 9}))

sequence4 = ["role_based_1.yaml", "role_based_2.yaml"]
print("sequence4",chain.run_chain(sequence4, {"user_name": "John"}))

sequence5 = ["structured_output_1.yaml", "structured_output_2.yaml"]
print("sequence5",chain.run_chain(sequence5, {
    "name": "Alice",
    "age": 30,
    "product_name": "Aha-Bha",
    "price": 30
}))

