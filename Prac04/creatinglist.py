__author__ = 'jc449799'
scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
print("your highest score is ",max(scores))