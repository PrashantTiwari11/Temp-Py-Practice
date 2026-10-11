"""156 Customer Feedback Analyzer — 10 features."""
from collections import Counter
import re
feedback=[]
POS={"good","great","excellent","fast","helpful","love","easy","friendly"}
NEG={"bad","poor","slow","rude","hate","difficult","broken","late"}
def add_feedback(text,rating=None): feedback.append({"text":text.strip(),"rating":rating})
def word_count(text): return len(re.findall(r"\b\w+\b",text))
def keywords(text): return re.findall(r"\b[a-zA-Z']+\b",text.lower())
def sentiment(text):
    ws=keywords(text); score=sum(w in POS for w in ws)-sum(w in NEG for w in ws)
    return "Positive" if score>0 else "Negative" if score<0 else "Neutral"
def average_rating():
    rs=[f["rating"] for f in feedback if isinstance(f["rating"],(int,float))]
    return round(sum(rs)/len(rs),2) if rs else None
def sentiment_summary(): return dict(Counter(sentiment(f["text"]) for f in feedback))
def common_words(limit=5):
    ws=[w for f in feedback for w in keywords(f["text"]) if len(w)>2]
    return Counter(ws).most_common(limit)
def search(term): return [f for f in feedback if term.lower() in f["text"].lower()]
def low_rated(threshold=2): return [f for f in feedback if isinstance(f["rating"],(int,float)) and f["rating"]<=threshold]
def export_csv(path="feedback_report.csv"):
    import csv
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["text","rating"]); w.writeheader(); w.writerows(feedback)
if __name__=="__main__":
    add_feedback("Great service and helpful staff",5); add_feedback("Delivery was slow and late",2); add_feedback("The app is easy to use",4)
    print("1 Feedback:",feedback); print("2 Word count:",word_count(feedback[0]["text"]))
    print("3 Keywords:",keywords(feedback[0]["text"])); print("4 Sentiment:",sentiment(feedback[0]["text"]))
    print("5 Average rating:",average_rating()); print("6 Sentiment summary:",sentiment_summary())
    print("7 Common words:",common_words()); print("8 Search:",search("delivery"))
    print("9 Low-rated:",low_rated()); print("10 Export CSV with export_csv()")
