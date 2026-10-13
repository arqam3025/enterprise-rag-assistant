"""Small retrieval evaluation using fictional demo policies."""
from retrieval import load_documents,retrieve

QUESTIONS=[
    ("What is the P1 response time?","sla_policy.txt"),
    ("When do we escalate P1 incidents?","sla_policy.txt"),
    ("What does Cloud Hosting Pro include?","cloud_service.txt"),
    ("How are cloud hosting backups handled?","cloud_service.txt"),
]
def evaluate(documents=None):
    documents=load_documents() if documents is None else documents
    correct=0
    details=[]
    for question,expected in QUESTIONS:
        results=retrieve(question,documents,k=1)
        predicted=results[0]["source"] if results else None
        correct+=predicted==expected
        details.append({"question":question,"expected":expected,"retrieved":predicted})
    return {"top1_accuracy":correct/len(QUESTIONS),"cases":len(QUESTIONS),"details":details}

if __name__=="__main__":
    print(evaluate())
