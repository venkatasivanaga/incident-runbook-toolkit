import json
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Locate the templates directory relative to this file
TEMPLATE_DIR = Path(__file__).parent / "templates"

def generate_report(data: dict, output_format: str = "markdown") -> Path:
    """Generates a post-incident report in the specified format."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format.lower() == "json":
        output_path = Path(f"post_incident_report_{timestamp}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return output_path
        
    # Default to Markdown via Jinja2
    output_path = Path(f"post_incident_report_{timestamp}.md")
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("report.md.j2")
    
    rendered_content = template.render(**data)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_content)
        
    return output_path