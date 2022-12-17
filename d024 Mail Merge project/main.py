names = ["Bob", "Juneseo", "Peyton", "Nathan", "Amber", "Zachary", "Zywicki"]

for name in names:
    with open(f"Letter_for_{name}.txt", mode='a') as letter:
        letter.write(f'''Dear {name},
    Here is the audio transcript of our latest session.
        ''')
        with open('copypasta.txt') as body:
            letter.write(body.read())
