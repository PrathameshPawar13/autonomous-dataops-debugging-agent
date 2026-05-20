from datetime import datetime
from pathlib import Path


def save_markdown_report(incident_report: str) -> str:
    output_dir = Path("data/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_dir / f"incident_report_{timestamp}.md"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(incident_report)

    return str(file_path)
