import subprocess
import os
import sys

def extract_pdf_to_text(pdf_path):
    """
    Uses the system's 'pdftotext' tool to extract content.
    Returns the text as a string.
    """
    # 1. Check if the file actually exists
    if not os.path.exists(pdf_path):
        return f"Error: File '{pdf_path}' not found."

    try:
        # 2. pdftotext <pdf_file> -
        # The '-' at the end tells it to output to stdout instead of a file.
        result = subprocess.run(
            ['pdftotext', pdf_path, '-'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error during extraction: {e}"

def main():
    # Usage: python3 pdf_extractor.py <path_to_pdf>
    if len(sys.argv) < 2:
        print("Usage: python3 pdf_extractor.py <path_to_pdf>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    text = extract_pdf_to_text(pdf_file)
    
    # Printing the full text for study
    print("-" * 20)
    print(f"FULL TEXT OF: {pdf_file}")
    print("-" * 20)
    print(text) 

if __name__ == "__main__":
    main()
