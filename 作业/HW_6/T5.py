import difflib
from sklearn.feature_extraction.text import TfidfVectorizer


def load_file(file_path):
    """
    读取文件内容
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def cosine_similarity(text1, text2):
    """
    使用TF-IDF和余弦相似度计算两份文本的相似性
    """
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    # 计算余弦相似度
    cosine_sim = (vectors[0] @ vectors[1]) / (sum(vectors[0] ** 2) ** 0.5 * sum(vectors[1] ** 2) ** 0.5)
    return cosine_sim


def compare_files(file1, file2):
    """
    比较两份文件的相似性
    """
    text1 = load_file(file1)
    text2 = load_file(file2)

    similarity = cosine_similarity(text1, text2)

    # 计算差异并显示
    diff = difflib.ndiff(text1.splitlines(), text2.splitlines())
    print("\n".join(diff))

    return similarity


file1 = 'T1.py'
file2 = 'T2.py'

similarity_score = compare_files(file1, file2)
print(f"两份作业的相似度为: {similarity_score * 100:.2f}%")
