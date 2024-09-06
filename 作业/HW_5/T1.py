import requests
from collections import Counter
import string

class NovelAnalyzer:
    def __init__(self, novel_url):
        self.url = novel_url

    def download_and_analyze(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.novel_text = response.text
        except requests.RequestException as e:
            print(f"下载小说时出错: {e}")
            return

        self.preprocessed_text = self.preprocess_text(self.novel_text)

        self.word_counts = Counter(self.preprocessed_text.split())

        self.top_20_words = self.word_counts.most_common(20)

        for word, count in self.top_20_words:
            print(f"{word}: {count}")

    def preprocess_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

# Notre-Dame de Paris
if __name__ == "__main__":
    analyzer = NovelAnalyzer("https://dlr1.fcdn.sk/converted-files/297ce6289fc9c19d9f72fc2e283f33f38c40c7c772122c3639baed719589626c/txt/redirection?filename=Notre-Dame%20de%20Paris%20%28Victor%20Hugo%20Alban%20Krailsheimer%29%20%28Z-Library%29.txt&md5=yUsUtYbwy2CPE5GiulpTCg&expires=1725595126")
    analyzer.download_and_analyze()
