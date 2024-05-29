import json
import pdfplumber
from sentence_transformers import SentenceTransformer


questions = json.load(open("/data/zyl/Car_Knowledge/questions.json"))
print(
    questions[0]
)  # {'question': '汽车的发动机是什么？', 'answer': '', 'reference': ''}

pdf = pdfplumber.open("/data/zyl/Car_Knowledge/初赛训练数据集.pdf")
len(pdf.pages)  # 页数
page0 = pdf.pages[0].extract_text()  # 读取第一页内容

pdf_content = []
for page_idx in range(len(pdf.pages)):
    pdf_content.append(
        {
            "page": "page_" + str(page_idx + 1),
            "content": pdf.pages[page_idx].extract_text(),
        }
    )

# 此处尝试了BGE, M3E, BCEmbedding
model = SentenceTransformer("/data/zyl/hugging_face_model/bge-small-zh-v1.5")

question_sentences = [x["question"] for x in questions]
pdf_content_sentences = [x["content"] for x in pdf_content]

question_embeddings = model.encode(question_sentences, normalize_embeddings=True)
pdf_embeddings = model.encode(pdf_content_sentences, normalize_embeddings=True)

for query_idx, feat in enumerate(question_embeddings):
    score = feat @ pdf_embeddings.T
    max_score_page_idx = score.argsort()[-1] + 1
    questions[query_idx]["reference"] = "page_" + str(max_score_page_idx)

with open("submit_bge.json", "w", encoding="utf8") as up:
    json.dump(questions, up, ensure_ascii=False, indent=4)
