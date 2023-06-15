import language_tests as test

### STAGE 1 ###

def load_book(filename):
    new_list=[]
    with open(filename, 'r') as book:
        lines = book.readlines()
        book.close()
        print(lines)
        for line in lines:
            if line == '\n':
                pass
            else:
                new_list.append(line.strip("\n").split(" "))
    return new_list

def get_corpus_length(corpus):
    corpus_length = 0
    for item in corpus:
        corpus_length+=len(item)
    return corpus_length

def build_vocabulary(corpus):
    is_unique = set()
    for subitem in corpus:
        is_unique.update(set(subitem))
    return list(is_unique)

def count_unigrams(corpus):
    unigram_counts = {}
    corpus_list = build_vocabulary(corpus)
    for item in corpus_list:
        unigram_counts[item]=0
        for sub in corpus:
            for subsub in sub:
                if subsub == item:
                    unigram_counts[item]+=1 
    print(unigram_counts)
    return unigram_counts

def make_start_corpus(corpus):
    for i in range(len(corpus)):
        corpus[i]=[corpus[i][0]]
    return corpus

def count_bigrams(corpus):
    bigrams_counter = {}
    for sentence in corpus:
        for i in range(len(sentence)-1):
            if not bigrams_counter.get(sentence[i]):
                bigrams_counter[sentence[i]] = {}
            if not bigrams_counter.get(sentence[i]).get(sentence[i+1]):
                bigrams_counter[sentence[i]][sentence[i+1]]=1
            else:
                bigrams_counter[sentence[i]][sentence[i+1]]+=1
    return bigrams_counter

### STAGE 2 ###

def build_uniform_probs(unigrams):
    return [1/len(unigrams) for item in unigrams]

def build_unigram_probs(unigrams, unigram_counts, total_count):
    """Creates a list containing the probability for each word to appear the book.

    Args:
        unigrams (list[str]): List of unique words.
        unigram_counts (dict[dict[int]]): Dictionary mapping unique unigrams to counts.
        total_count (int): Total count of all words.
    """
    return [unigram_counts[word]/total_count for word in unigrams]

def build_bigram_probs(unigram_counts, bigram_counts):
    """Takes the frequencies of single words (unigram_counts) and of pairs of words (bigram_counts) and returns a new nested dictionary.

    Args:
        unigram_counts (dict[dict[int]]): dictionary mapping of unigrams
        bigram_counts (_type_): _description_
    """
    bigram_probs = {}
    for prev_word in bigram_counts.keys():
        words = []
        probs = []
        for keys in bigram_counts[prev_word].keys():
            words.append(keys)
            probs.append(bigram_counts[prev_word][keys]/unigram_counts[prev_word])
            temp={"words":words, "probs":probs}
            bigram_probs[prev_word]=temp
    print(bigram_probs)
    return bigram_probs

def get_top_words(count, words, probs, ignore_list):
    for i in range(len(probs)-1):
        for k in range(i+1, len(probs)):
            if probs[i] < probs[k]:
                temp = probs[i]
                temp_wrd = words[i]
                probs[i]=probs[k]
                probs[k]=temp
                words[i]=words[k]
                words[k]=temp_wrd
    top_words={}
    j=0
    while len(top_words) < count and j < len(words):
        if words[j] not in ignore_list:
            top_words[words[j]]=probs[j]
        j+=1
    return top_words

from random import choices
def generate_text_from_unigrams(count, words, probs):
    return " ".join(choices(words,weights=probs,k=count))

def generate_text_from_bigrams(
    count,
    start_words,
    start_word_probs,
    bigram_probs
):
    generated_words = []
    while len(generated_words) < count:
        if len(generated_words) == 0 or generated_words[len(generated_words)-1] == ".":
            generated_words.append(choices(start_words,weights=start_word_probs,k=1)[0])
        else:
            last_word = generated_words[len(generated_words)-1]
            words = bigram_probs[last_word]["words"]
            probs = bigram_probs[last_word]["probs"]
            generated_words.append(
                choices(
                words,
                weights=probs,
                k=1
                )[0]
            )
    return " ".join(generated_words)


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # test.test_all()
    test.run()
    # test.test_load_book()
    # test.test_get_corpus_length()
    # test.test_build_vocabulary()
    # test.test_count_unigrams()
    # test.test_make_start_corpus()
    # test.test_count_bigrams()
    # test.test_build_uniform_probs()
    # test.test_build_unigram_probs()
    # test.test_build_bigram_probs()
    # test.test_get_top_words()
    # test.test_generate_text_from_unigrams()
    # test.test_generate_text_from_bigrams()
