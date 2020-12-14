from collections import Counter


def count_questions(questions):
    counts = []
    yes = set()
    for line in questions:
        if not line:
            counts.append(len(yes))
            yes = set()
        else:
            for q in line:
                yes.add(q)
    counts.append(len(yes))
    return counts


def count_everyone_yes_questions(questions):
    counts = []
    yes = Counter()
    num_people = 0
    for line in questions:
        if not line:
            everyone_yes = [q for q, c in yes.items() if c == num_people]
            counts.append(len(everyone_yes))
            yes = Counter()
            num_people = 0
        else:
            yes.update(line)
            num_people += 1
    everyone_yes = [q for q, c in yes.items() if c == num_people]
    counts.append(len(everyone_yes))
    return counts


if __name__ == "__main__":
    test_questions = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""
    counts = count_questions(test_questions.splitlines())
    print(sum(counts))

    with open("2020/inputs/day6.txt") as f:
        questions = [l.strip() for l in f.readlines()]
    print(f"Sum of counts is {sum(count_questions(questions))}")

    print(
        f"Sum of questions everyone answered yes is {sum(count_everyone_yes_questions(questions))}"
    )

