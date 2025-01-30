from nltk.tokenize import word_tokenize

class Tokeniser:
    @staticmethod
    def tokenise(text):
        return word_tokenize(text)
    
# Example usage (to be called from main.py)
if __name__ == "__main__":
    tokeniser = Tokeniser()
    sample_text = "I am Yash."
    tokens = tokeniser.tokenise(sample_text)
    print(tokens)