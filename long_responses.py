import random

R_EATING = "I dont like being fat"


def unknown():
    response = ['Could you please rephrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response
