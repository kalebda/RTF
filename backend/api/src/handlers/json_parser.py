import json
import os

from jinja2 import Template


class JSONParser:
    def __init__(self):
        pass

    def parse_json(self, template_str):
        cwd = os.getcwd()

        with open(f"{cwd}/src/handlers/data.json", "r") as file:
            data = json.load(file)

        for key in data:
            if isinstance(data[key], dict):
                table_data = data[key]
                print("------------->", table_data)
                if "sum" in table_data["result"]:
                    sum_value = table_data["var1"] + table_data["var2"]
                    table_data["result"] = table_data["result"].format(
                        var1=table_data["var1"], var2=table_data["var2"], sum=sum_value
                    )
                    # Convert table data to string representation
                    data[key] = "\n".join(f"{k}: {v}" for k, v in table_data.items())

        # Load template using Jinja2
        template = Template(template_str)

        result = template.render(
            image1=data["image1"], table2=data["table2"], pdf3=data["pdf3"]
        )

        return result
