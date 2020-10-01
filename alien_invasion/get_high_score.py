def get_score():
    try:
        with open("score.txt", 'r') as files:
            data = files.read()
    except Exception:
        prompt_high_score(0)
    return int(data)


def prompt_high_score(data):
    with open("score.txt", 'w') as files:
        files.write(str(data))
