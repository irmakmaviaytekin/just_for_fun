import tkinter as tk
from tkinter import messagebox
import random

adjective = ["handsome", 'thoughtful', 'hot', 'perfect', 'passionate', 'gentle', 'funny', 'smart',
             'dramatic-ass but in the best way']

noun = ["soul", "eyes", "smile", "voice", "presence", "energy", "laughter"]

memory = [
    'the time we rode bikes on the island',
    'the time we kissed in the water on the island',
    'the time we had a man on cocaine drive us',
    'the time we had our first kiss in the rain',
    'the time we drank wine in the mens bathroom',
    'the time we watched the sea in the ferry to the island',
    'the time i played guitar and sang to you',
    'the time you flew to istanbul for me',
    'the time we spent on the counter of my house..',
    'the time we cuddled and slept in your room when i had my period',
    'the time we played a tag game in my house',
    'the time you tickled me until i screamed for you to stop',
    'the time we got drunk and had a camel fight in the pool at that one party',
    'the time you did something in that bar in kadikoy before the pool party',
    'the times we spent in the judgement free zone',
    'the time i hand fed you even though you said you would never do it and you liked it'
]

promise = [
    'i will always root for your dreams',
    "i will hold you close when everything feels too loud",
    "i will never stop writing love letters for you",
    "i will always be silly and goofy and make you laugh",
    "i will always love you despite our 'heated discussions'",
    "i will always be clingy",
    "i will always be your little cherry princess",
    "i will always make you uncomfortable with my fantasies and horror stories",
    "i will always try to win you over and not take you for granted",
    "i will always try my best to respect you and treat you with kindness"
]

templates = [
    """my love,
i keep thinking about {memory1}.
i don’t think I’ll ever stop smiling when I remember it.
just wanted to remind you: {promise1}.
yours,
your menace girlfriend""",

    """my love,
i keep thinking about {memory1}.
i feel so lucky to have a million more memories like that with you.
and i pinky promise this: {promise1}.
forever on your team,
your little cherry""",

    """my love,
i keep thinking about {memory1}.
i don’t think I’ll ever stop smiling when I remember it.
just wanted to remind you: {promise1}.
yours,
your Irmak""",

    """my love,
i keep thinking about {memory1}.
i don’t think I’ll ever stop smiling when I remember it.
and just so you know: {promise1}.
yours with sticky lip gloss and a dirty mind,
your hot hot SO HOT girly"""
]


# ─────────────── LOGIC ───────────────

def generate_love_letter():
    adj1 = random.choice(adjective)
    adj2 = random.choice(adjective)
    noun1 = random.choice(noun)
    memory1 = random.choice(memory)
    promise1 = random.choice(promise)
    template = random.choice(templates)

    letter = template.format(
        adj=adj1,
        adj2=adj2,
        noun1=noun1,
        memory1=memory1,
        promise1=promise1
    )
    return letter


# ─────────────── GUI ───────────────

# Create window
root = tk.Tk()
root.title("Love Letter Generator 💌")
root.geometry("600x600")
root.configure(bg="#ffe6f0")  # soft pink bg

# Text output box
output_box = tk.Text(root, wrap="word", font=("Courier New", 12), bg="white", fg="black")
output_box.pack(padx=20, pady=20, expand=True, fill="both")


# Generate button
def show_letter():
    output_box.delete(1.0, tk.END)
    letter = generate_love_letter()
    output_box.insert(tk.END, letter)
    messagebox.showinfo("💘 letter generated!", "love love love!!!!!.")


generate_button = tk.Button(root, text="generate love letter 💘", command=show_letter,
                            font=("Helvetica", 14, "bold"), bg="#ff99cc", fg="white")
generate_button.pack(pady=10)

# Run the app
root.mainloop()
