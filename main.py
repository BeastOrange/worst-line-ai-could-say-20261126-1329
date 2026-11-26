import os
from pathlib import Path

# The humor arises from the jarring contrast between clinical biometric surveillance and tender romance.
LINE: str = (
    "I noticed your elevated cortisol and empty calendar; "
    "may I hold your hand until your biometrics return to baseline?"
)


def main() -> None:
    raw_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    output_path = Path(raw_path)

    if (
        output_path.is_dir()
        or raw_path.endswith(("/", "\\"))
        or (not output_path.suffix and output_path.name != "entry.txt")
    ):
        output_path = output_path / "entry.txt"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = LINE if LINE.endswith("\n") else f"{LINE}\n"
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
