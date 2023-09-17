def find_toppers_and_scores(N):
    student_scores = {}  
    
    for i in range(N):
        name = input(f"")
        while True:
            try:
                score = float(input(f""))
                if 0 <= score <= 100:
                    student_scores[name] = score
                    break
                else:
                    print("")
            except ValueError:
                print("")
    max_score = max(student_scores.values())
    toppers = [name for name, score in student_scores.items() if score == max_score]
    print("")
    for topper in toppers:
        print(f"{topper}")
T = int(input(""))
if 1 <= T <= 25:
    for i in range(T):
        print(f"")
        N = int(input(f""))
        if 2 <= N <= 100:
            find_toppers_and_scores(N)
        else:
            print("")
else:
    print("")
