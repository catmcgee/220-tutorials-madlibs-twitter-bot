import tweepy # best Twitter API (in my opinion!)
import random # for selecting a random sentence
from nltk.corpus import wordnet 
# wordnet is a word database and has so many capabilities! We use it for finding if a word a usually a noun, adjective, verb
# wordnet does not have some words, including swear words :(

from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# authenticating with tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# mentions_timeline gets all the tweets you are mentioned in on Twitter
# count = 1 takes only one, the most recent one
mentions = api.mentions_timeline(count=1)

# we make it all lowercase so we can remove the @ tag
mention = str(mentions[0].text).lower().replace("@220madlibs ", "")

# this wordnet function gets the types (noun/adj/verb) and selects the first
# print(wordnet.synsets(mention))
type_of_word = wordnet.synsets(mention)[0].pos()

# sentences to put our word into
# the 'f' in front makes it  a string literal, allowing us to do {mention}
noun_sentences = [
    f"Hey {mention} how are you?",
    f"One day a {mention} was walking down the road. 'This is nice' said the {mention}.",
    f"Don't you dare look at the {mention}, it will destroy you.",
    f"I really love the {mention}. The {mention} is great.",
    f"Like they always say, too many cooks spoil the {mention}."
]

verb_sentences = [
    f"You should {mention}",
    f"Whenever I {mention}, I'm happy.",
    f"{mention} is my favourite thing to do in the world.",
    f"Have you tried {mention}? It's so relaxing.",
    f"My boyfriend was {mention} last night, so gross."
]

adjective_sentences = [
    f"I am so {mention}",
    f"Stop trying to make {mention} happen. {mention} will never happen.",
    f"The drama teacher told me I was too {mention}",
    f"I can't believe you'd do that. That's so {mention}!",
    f"I'm a sentient bot. I'm {mention}."
]

# update_status posts a tweet, selecting a random sentence with the word from the mention
if type_of_word == "n":
    api.update_status(random.choice(noun_sentences))
elif type_of_word == "v":
    api.update_status(random.choice(verb_sentences))
elif type_of_word == "a":
    api.update_status(random.choice(adjective_sentences))
