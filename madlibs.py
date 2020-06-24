import tweepy, random
from nltk.corpus import wordnet
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

type_of_words = ["a noun", "a verb", "an adjective"]
selected_type = random.choice(type_of_words)

mentions = api.mentions_timeline(count=1)
mention = str(mentions[0].text).lower().replace("@220madlibs ", "")
print(mention)

type_of_word = wordnet.synsets(mention)[0].pos()
print(type_of_word)


noun_sentences = [
    f"Hey {mention} how are you?",
    f"One day a {mention} was walking down the road. 'This is nice' said the {mention}.",
    f"Don't you dare look at the {mention}, it will destroy you.",
    f"I really love the {mention}. The {mention} is great.",
    f"Like they always say, too many cooks spoil the {mention}."
]

adjective_sentences = [
    f"I am so {mention}",
    f"Stop trying to make {mention} happen. {mention} will never happen.",
    f"The drama teacher told me I was too {mention}",
    f"I can't believe you'd do that. That's so {mention}!",
    f"I'm a sentient bot. I'm {mention}."
]

verb_sentences = [
    f"You should {mention}",
    f"Whenever I {mention}, I'm happy.",
    f"{mention} is my favourite thing to do in the world.",
    f"Have you tried {mention}? It's so relaxing.",
    f"My boyfriend was {mention} last night, so gross."
]


if type_of_word == "n":
    api.update_status(random.choice(noun_sentences))

elif type_of_word == "a":
    api.update_status(random.choice(adjective_sentences))

elif type_of_word == "v":
    api.update_status(random.choice(verb_sentences))