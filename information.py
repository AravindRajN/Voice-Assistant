import wikipedia
def question(c):
    try:
        r= wikipedia.summary(c, sentences = 1)
        return r
    except:
        r= wikipedia.summary(c.replace(" ",""), sentences = 1)
        return r
