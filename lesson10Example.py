row_scores = ["abc","-1","101","60"]
scores,errors = [],[]
for row in row_scores:
    try:
        score = int(row)
        if not 0 <= score <= 100:
            raise ValueError("range")
        scores.append(score)
    except ValueError:
        errors.append(row)
passing = [score for score in scores if score >= 60]
print(passing,errors)