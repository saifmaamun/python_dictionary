from matplotlib.cbook import index_of
from numpy.ma.core import append

dict1 ={
    "serendipity": "The occurrence and development of events by chance in a happy or beneficial way.",
    "ephemeral": "Lasting for a very short time.",
    "ubiquitous": "Present, appearing, or found everywhere.",
    "mellifluous": "(of a voice or words) sweet or musical; pleasant to hear.",
    "quixotic": "Exceedingly idealistic; unrealistic and impractical.",
    "cacophony": "A harsh, discordant mixture of sounds.",
    "ambiguous": "Open to more than one interpretation; not having an obvious meaning.",
    "loquacious": "Tending to talk a great deal; talkative.",
    "perspicacious": "Having a ready grasp of things; shrewd; astute.",
    "garrulous": "Excessively talkative, especially on trivial matters."
}
keys=list(dict1.keys())
values= list(dict1.values())
value_len=[ len(i) for i in values]
long=max(value_len)
short= min(value_len)

# print(values[value_len.index(long)])
print("The longest word is {}".format(values[value_len.index(long)]))
print("The shortest word is {}".format(values[value_len.index(short)]))

print(value_len, long, short)