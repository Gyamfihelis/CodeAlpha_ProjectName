import re


EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def extract_emails(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        return

    emails = sorted(set(EMAIL_PATTERN.findall(text)))

    with open(output_file, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"Found {len(emails)} unique email address(es).")
    print(f"Emails saved to {output_file}")


if __name__ == "__main__":
    source = input("Enter the source .txt file path: ").strip()
    destination = input("Enter the output .txt file path: ").strip()

    if not destination:
        destination = "emails.txt"

    extract_emails(source, destination)
