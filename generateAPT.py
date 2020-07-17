import random as r
import argparse

parser = argparse.ArgumentParser(description="Generate an APT name!", usage='generateAPT.py -count 5 -noexcuse')
parser.add_argument('-count', required=False, type=int, help='Number of APT names to generate', default=1)
parser.add_argument('-noexcuse', required=False, action='store_true', help='Provide names without excuses')

args = parser.parse_args()

adjectives = [
    "Defiant",
    "Homeless",
    "Adorable",
    "Delightful",
    "Homely",
    "Quaint",
    "Adventurous",
    "Depressed",
    "Horrible",
    "Aggressive",
    "Determined",
    "Hungry",
    "Real",
    "Agreeable",
    "Different",
    "Hurt",
    "Relieved",
    "Alert",
    "Difficult",
    "Repulsive",
    "Alive",
    "Disgusted",
    "Ill",
    "Rich",
    "Amused",
    "Distinct",
    "Important",
    "Angry",
    "Disturbed",
    "Impossible",
    "Scary",
    "Annoyed",
    "Dizzy",
    "Inexpensive",
    "Selfish",
    "Annoying",
    "Doubtful",
    "Innocent",
    "Shiny",
    "Anxious",
    "Drab",
    "Inquisitive",
    "Shy",
    "Arrogant",
    "Dull",
    "Itchy",
    "Silly",
    "Ashamed",
    "Sleepy",
    "Attractive",
    "Eager",
    "Jealous",
    "Smiling",
    "Average",
    "Easy",
    "Jittery",
    "Smoggy",
    "Awful",
    "Elated",
    "Jolly",
    "Sore",
    "Elegant",
    "Joyous",
    "Sparkling",
    "Bad",
    "Embarrassed",
    "Splendid",
    "Beautiful",
    "Enchanting",
    "Kind",
    "Spotless",
    "Better",
    "Encouraging",
    "Stormy",
    "Bewildered",
    "Energetic",
    "Lazy",
    "Strange",
    "Black",
    "Enthusiastic",
    "Light",
    "Stupid",
    "Bloody",
    "Envious",
    "Lively",
    "Successful",
    "Blue",
    "Evil",
    "Lonely",
    "Super",
    "Blue-eyed",
    "Excited",
    "Long",
    "Blushing",
    "Expensive",
    "Lovely",
    "Talented",
    "Bored",
    "Exuberant",
    "Lucky",
    "Tame",
    "Brainy",
    "Tender",
    "Brave",
    "Fair",
    "Magnificent",
    "Tense",
    "Breakable",
    "Faithful",
    "Misty",
    "Terrible",
    "Bright",
    "Famous",
    "Modern",
    "Tasty",
    "Busy",
    "Fancy",
    "Motionless",
    "Thankful",
    "Fantastic",
    "Muddy",
    "Thoughtful",
    "Calm",
    "Fierce",
    "Mushy",
    "Thoughtless",
    "Careful",
    "Filthy",
    "Mysterious",
    "Tired",
    "Cautious",
    "Fine",
    "Tough",
    "Charming",
    "Foolish",
    "Nasty",
    "Troubled",
    "Cheerful",
    "Fragile",
    "Naughty",
    "Clean",
    "Frail",
    "Nervous",
    "Ugliest",
    "Clear",
    "Frantic",
    "Nice",
    "Ugly",
    "Clever",
    "Friendly",
    "Nutty",
    "Uninterested",
    "Cloudy",
    "Frightened",
    "Unsightly",
    "Clumsy",
    "Funny",
    "Obedient",
    "Unusual",
    "Colorful",
    "Obnoxious",
    "Upset",
    "Combative",
    "Gentle",
    "Odd",
    "Uptight",
    "Comfortable",
    "Gifted",
    "Old-fashioned",
    "Concerned",
    "Glamorous",
    "Open",
    "Vast",
    "Condemned",
    "Gleaming",
    "Outrageous",
    "Victorious",
    "Confused",
    "Glorious",
    "Outstanding",
    "Vivacious",
    "Cooperative",
    "Good",
    "Courageous",
    "Gorgeous",
    "Panicky",
    "Wandering",
    "Crazy",
    "Graceful",
    "Perfect",
    "Weary",
    "Creepy",
    "Grieving",
    "Plain",
    "Wicked",
    "Crowded",
    "Grotesque",
    "Pleasant",
    "Wide-eyed",
    "Cruel",
    "Grumpy",
    "Poised",
    "Wild",
    "Curious",
    "Poor",
    "Witty",
    "Cute",
    "Handsome",
    "Powerful",
    "Worrisome",
    "Happy",
    "Precious",
    "Worried",
    "Dangerous",
    "Healthy",
    "Prickly",
    "Wrong",
    "Dark",
    "Helpful",
    "Proud",
    "Dead",
    "Helpless",
    "Putrid",
    "Zany",
    "Defeated",
    "Hilarious",
    "Puzzled",
    "Zealous"
]

animals = [
    "Coyote",
    "Liger",
    "Lynx",
    "Octopus",
    "Penguin",
    "Skunk",
    "Squirrel Monkey",
    "Starfish",
    "Tarsier",
    "Thorny Devil",
    "Tortoise",
    "Toucan",
    "Behemoth",
    "Dragon"
    "Zonkey",
    "Arctic Wolf",
    "Caiman",
    "Crocodile",
    "Grizzly Bear",
    "Hippopotamus",
    "Jaguar",
    "Killer Whale",
    "Komodo Dragon",
    "Puffer Fish",
    "Snapping Turtle",
    "Stingray",
    "Tiger",
    "Tiger Shark",
    "Bearded Collie",
    "Bearded Dragon",
    "Cat",
    "Chinchilla",
    "Cow",
    "Sasquatch ",
    "Duck",
    "Gecko",
    "Guinea Pig",
    "Hamster",
    "Irish WolfHound",
    "Norwegian Forest",
    "Antelope",
    "Arctic Fox",
    "Bengal Tiger",
    "Caracal",
    "Chameleon",
    "Cheetah",
    "Kraken",
    "Giraffe",
    "Howler Monkey",
    "Koala",
    "Lion",
    "Millipede",
    "Mountain Lion",
    "Panther",
    "Prawn",
    "Cerberus",
    "Red Panda",
    "Rhinoceros",
    "Amur Leopard",
    "Aye Aye",
    "Clouded Leopard",
    "Giant Panda Bear",
    "Ocelot",
    "Okapi",
    "Chimera",
    "Polar Bear",
    "Basilisk",
    "Proboscis Monkey",
    "River Dolphin",
    "Sloth",
    "Orangutan",
    "White Tiger"
]

excuses = [
    "Krebs said it was",
    "Forensic evidence shows it's from",
    "The cybers concluded it was",
    "Our next-gen machine learning attributed it to",
    "We have seen these IOC's before from",
    "Intense research has concluded the threat actor was",
    "@dave_daves tweeted this was done by",
    "The threat actor responsible is",
    "Evidence suggests it was",
    "A security expert on Linkedin advised us this is from",
    "A reputable source has confirmed this originated from"
]

def generate_apt():
    i = 1
    while i <= args.count:
        animal = r.choice(animals)
        adj = r.choice(adjectives)

        if args.noexcuse:
            print(f'{adj} {animal}')
        else:
            excuse = r.choice(excuses)
            print(f'{excuse} "{adj} {animal}"')
        i += 1


if __name__ == '__main__':
        generate_apt()
