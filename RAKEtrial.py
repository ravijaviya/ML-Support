#Latest implementation of Rake using NLTK
from rake_nltk import  Rake

with open('plot_the_big_short','r') as p:

    rake = Rake()
    rake.extract_keywords_from_sentences(p)
    total_keys = 0
    for score,keyword in rake.get_ranked_phrases_with_scores():
        print(score,keyword)
        if score > 1:
            total_keys+=len(keyword.split(" "))
    print(total_keys,len(rake.get_ranked_phrases()))
