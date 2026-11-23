import argparse,csv
from collections import Counter
from pathlib import Path
from classifier import classify
parser=argparse.ArgumentParser()
parser.add_argument("--mode",choices=["baseline","llm"],default="baseline")
args=parser.parse_args()
with (Path(__file__).parent/"data/evaluation.csv").open() as f:rows=list(csv.DictReader(f))
correct=0;review=0;matrix=Counter()
for row in rows:
    result=classify(row["text"],args.mode)
    correct+=result["label"]==row["expected"]
    review+=result["needs_review"]
    matrix[(row["expected"],result["label"])]+=1
print(f"Mode: {args.mode}; accuracy: {correct}/{len(rows)} ({correct/len(rows):.1%}); review flagged: {review}/{len(rows)}")
for (expected,actual),count in sorted(matrix.items()):print(f"{expected} -> {actual}: {count}")
