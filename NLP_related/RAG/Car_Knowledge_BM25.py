import json
import pdfplumber
import jieba
from rank_bm25 import BM25Okapi

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


pdf_content_words = [jieba.lcut(x["content"]) for x in pdf_content]
bm25 = BM25Okapi(pdf_content_words)

for query_idx in range(len(questions)):
    doc_scores = bm25.get_scores(jieba.lcut(questions[query_idx]["question"]))
    max_score_page_idx = doc_scores.argsort()[-1] + 1
    questions[query_idx]["reference"] = "page_" + str(max_score_page_idx)

with open("submit_bm25.json", "w", encoding="utf8") as up:
    json.dump(questions, up, ensure_ascii=False, indent=4)
