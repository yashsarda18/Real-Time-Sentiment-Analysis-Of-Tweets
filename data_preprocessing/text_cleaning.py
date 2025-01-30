import re

class TextCleaner:
    @staticmethod
    def clean_text(text):
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        return text.lower()
    
# Example usage (to be called from main.py)
if __name__ == "__main__":
    cleaner = TextCleaner()
    sample_text = "Check this out! Visit https://example.com"
    cleaned_text = cleaner.clean_text(sample_text)
    print(cleaned_text)