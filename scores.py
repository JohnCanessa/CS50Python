# **** main method ****
def main():

    # **** populate list of scores ****
    # scores = []
    # scores.append(72)
    # scores.append(73)
    # scores.append(33)

    scores = [72, 73, 33]

    print(f" scores: {scores}")

    # **** compute the average score (imperative way) ****
    average = 0
    for i in range(len(scores)):
        average += scores[i]
    average /= len(scores)

    print(f"average: {average}\n")

    # *** compute the average score (pythonic way) ****
    print(f"sum(scores): {sum(scores)}")
    print(f"len(scores): {len(scores)}")
    
    print(f"    average: {sum(scores) / len(scores)}")

# **** call main method ****
main()
