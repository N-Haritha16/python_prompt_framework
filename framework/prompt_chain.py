import json 

class PromptChain:
    def __init__(self, engine):
        self.engine = engine

    def run_chain(self, sequence: list, initial_vars: dict):
        vars = initial_vars.copy()
        for template_name in sequence:
            output_json = self.engine.render(template_name, **vars)
            output_data = json.loads(output_json)
        #     vars['previous_output'] = output_data['output']
        # return vars['previous_output']
             # ✅ Handle errors safely
            if "error" in output_data:
                raise ValueError(
                    f"Error in template '{template_name}': {output_data['error']}"
                )

            # ✅ Extract rendered content
            rendered = output_data.get("output")

            if rendered is None:
                raise KeyError(
                    f"'output' missing in rendered result for template '{template_name}'"
                )

            vars["previous_output"] = rendered

        return vars["previous_output"]
