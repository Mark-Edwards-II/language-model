import sys
sys.path.append("/home/codio/workspace/code/")
from language import *

def test_load_book():
    print("Testing load_book()...\n", end="")
    # We'll test with two shorts files, test1.txt and test2.txt
    # Open them up to see the contents!
    assert(load_book("data/test1.txt") == [ 
        ["hello", "and", "welcome", "to", "the", "program", "."],
        ["we're", "happy", "to", "have", "you", "."] ])
    test2 = [ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]
    # print(test2)
    # print()
    assert(load_book("data/test2.txt") == test2)
    print("... done!")

def test_get_corpus_length():
    print("Testing get_corpus_length()...\n", end="")
    assert(get_corpus_length([ 
        ["hello", "world"],
        ["hello", "world", "again"] ]) == 5)
    assert(get_corpus_length([ 
        ["hello", "and", "welcome", "to", "the", "program", "."],
        ["we're", "happy", "to", "have", "you", "."] ]) == 13)
    assert(get_corpus_length([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]) == 41)
    print("... done!")

def test_build_vocabulary():
    print("Testing build_vocabulary()...\n", end="")
    assert(sorted(build_vocabulary([ 
        ["hello", "world"],
        ["hello", "world", "again"] ])) == sorted([ "hello", "world", "again"]))
    assert(sorted(build_vocabulary([ 
        ["hello", "and", "welcome", "to", "the", "program", "."],
        ["we're", "happy", "to", "have", "you", "."] ])) == \
        sorted([ "hello", "and", "welcome", "to", "the", "program", ".", "we're", "happy", "have", "you"]))
    assert(sorted(build_vocabulary([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ])) == \
        sorted([ "this", "is", "the", "song", "that", "never", "ends", "yes", 
        "it", "goes", "on", "and", "my", "friends", "!", "some", "people", 
        "started", "singing", ",", "not", "knowing", "what", "was", 
        "now", "they", "keep", "forever", "just", "because", "." ]))
    print("... done!")

def test_count_unigrams():
    print("Testing count_unigrams()...\n", end="")
    assert(count_unigrams([ 
        ["hello", "world"],
        ["hello", "world", "again"] ]) == { "hello" : 2, "world" : 2, "again" : 1 })
    assert(count_unigrams([ 
        ["hello", "and", "welcome", "to", "the", "program", "."],
        ["we're", "happy", "to", "have", "you", "."] ]) == \
        { "hello" : 1, "and" : 1, "welcome" : 1, "to" : 2, "the" : 1, "program" : 1, 
          "." : 2, "we're" : 1, "happy" : 1, "have" : 1, "you" : 1 })
    assert(count_unigrams([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]) == \
        { "this" : 1, "is" : 1, "the" : 1, "song" : 1, "that" : 1, "never" : 1, 
          "ends" : 1, "yes" : 1, "it" : 4, "goes" : 1, "on" : 3, "and" : 2, 
          "my" : 1, "friends" : 1, "!" : 1, "some" : 1, "people" : 1, 
          "started" : 1, "singing" : 2, "," : 2, "not" : 1, "knowing" : 1, 
          "what" : 1, "was" : 1, "now" : 1, "they" : 1, "keep" : 1, 
          "forever" : 1, "just" : 1, "because" : 1, "." : 3 })
    print("... done!")

def test_make_start_corpus():
    print("Testing make_start_corpus()...\n", end="")
    assert(make_start_corpus([ 
        ["hello", "world"],
        ["hello", "world", "again"] ]) == [ ["hello"], ["hello"] ])
    assert(make_start_corpus([ 
        ["hello", "and", "welcome", "to", "the", "program", "."],
        ["we're", "happy", "to", "have", "you", "."] ]) == \
        [ ["hello"], ["we're"] ])
    assert(make_start_corpus([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]) == \
        [ ["this"], ["yes"], ["some"], ["and"] ])
    print("... done!")

def test_count_bigrams():
    print("Testing count_bigrams()...\n", end="")
    assert(count_bigrams([ 
        ["hello", "world"],
        ["hello", "world", "again"] ]) == \
        { "hello" : { "world" : 2 }, "world" : { "again" : 1 } })
    assert(count_bigrams([ 
        ["hello", "and", "welcome", "to", "the", "program", "."],
        ["we're", "happy", "to", "have", "you", "."] ]) == \
        { "hello" : { "and" : 1 }, "and" : { "welcome" : 1 }, "welcome" : { "to" : 1 }, 
        "to" : { "the" : 1, "have" : 1 }, "the" : { "program" : 1 }, "program" : { "." : 1 }, "we're" : { "happy" : 1 }, 
        "happy" : { "to" : 1 }, "have" : { "you" : 1 }, "you" : { "." : 1 } })
    assert(count_bigrams([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]) == \
        { "this" : { "is" : 1 }, "is" : { "the" : 1 }, "the" : { "song" : 1 }, 
          "song" : { "that" : 1 }, "that" : { "never" : 1 }, "never" : { "ends" : 1 }, 
          "yes" : { "it" : 1 }, "it" : { "goes" : 1, "," : 1, "was" : 1, "forever" : 1 }, "goes" : { "on" : 1 }, 
          "on" : { "and" : 1, "my" : 1, "singing" : 1 }, "and" : { "on" : 1, "now" : 1 }, "my" : { "friends" : 1}, 
         "friends" : { "!" : 1 }, "some" : { "people" : 1 }, "people" : { "started" : 1 }, 
         "started" : { "singing" : 1 }, "singing" : { "it" : 2 }, "," : { "not" : 1 }, 
         "not" : { "knowing" : 1 }, "knowing" : { "what" : 1 }, "what" : { "it" : 1 }, 
         "was" : { "," : 1 }, "now" : { "they" : 1 }, "they" : { "keep" : 1 }, 
         "keep" : { "on" : 1 }, "forever" : { "just" : 1 }, "just" : { "because" : 1 }, 
         "because" : { "." : 1 }, "." : { "." : 2 } })
    print("... done!")

def test_build_uniform_probs():
    print("Testing build_uniform_probs()...\n", end="")
    assert(build_uniform_probs([ "hello", "world", "again"]) == [1/3, 1/3, 1/3])
    assert(build_uniform_probs(\
        [ "hello", "and", "welcome", "to", "the", "program", ".", "we're", "happy", "have", "you"]) == \
        [ 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11 ])
    assert(build_uniform_probs(\
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", "goes", "on", 
          "and", "my", "friends", "!", "some", "people", "started", "singing", ",", "not", 
          "knowing", "what", "was", "now", "they", "keep", "forever", "just", "because", "." ]) == \
        [ 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 
          1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31 ])
    print("... done!")

def test_build_unigram_probs():
    print("Testing build_unigram_probs()...\n", end="")
    assert(build_unigram_probs(\
        [ "hello", "world", "again"],
        { "hello" : 2, "world" : 2, "again" : 1 }, 5 ) == \
        [ 2/5, 2/5, 1/5 ])
    assert(build_unigram_probs(\
        [ "hello", "and", "welcome", "to", "the", "program", ".", "we're", "happy", "have", "you"],
        { "hello" : 1, "and" : 1, "welcome" : 1, "to" : 2, "the" : 1, "program" : 1, "." : 2, 
          "we're" : 1, "happy" : 1, "have" : 1, "you" : 1 }, 13) == \
        [ 1/13, 1/13, 1/13, 2/13, 1/13, 1/13, 2/13, 1/13, 1/13, 1/13, 1/13 ])
    assert(build_unigram_probs(\
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", 
          "goes", "on", "and", "my", "friends", "!", "some", "people", "started", 
          "singing", ",", "not", "knowing", "what", "was", "now", "they", "keep", 
          "forever", "just", "because", "." ],
        { "this" : 1, "is" : 1, "the" : 1, "song" : 1, "that" : 1, "never" : 1, 
          "ends" : 1, "yes" : 1, "it" : 4, "goes" : 1, "on" : 3, "and" : 2, 
          "my" : 1, "friends" : 1, "!" : 1, "some" : 1, "people" : 1, 
          "started" : 1, "singing" : 2, "," : 2, "not" : 1, "knowing" : 1, 
          "what" : 1, "was" : 1, "now" : 1, "they" : 1, "keep" : 1, 
          "forever" : 1, "just" : 1, "because" : 1, "." : 3 }, 41) == \
        [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 2/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 2/41, 2/41, 1/41, 1/41, 1/41, 1/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41 ])
    print("... done!")

def test_build_bigram_probs():
    print("Testing build_bigram_probs()...\n", end="")
    # since 'world' appears twice, once at the end of a sentence
    res={ "hello" : { "words" : ["world"], "probs" : [1] }, 
          "world" : { "words" : ["again"], "probs" : [0.5] } }
    print("**********************************************>\n")
    print(res)
    print("**********************************************>\n")
    assert(build_bigram_probs(\
        { "hello" : 2, "world" : 2, "again" : 1 },
        { "hello" : { "world" : 2 }, "world" : { "again" : 1 } }) == \
        res)
    assert(build_bigram_probs(\
        { "hello" : 1, "and" : 1, "welcome" : 1, "to" : 2, "the" : 1, "program" : 1, "." : 2, "we're" : 1, "happy" : 1, "have" : 1, "you" : 1 }, 
        { "hello" : { "and" : 1 }, "and" : { "welcome" : 1 }, "welcome" : { "to" : 1 }, 
          "to" : { "the" : 1, "have" : 1 }, "the" : { "program" : 1 }, "program" : { "." : 1 }, "we're" : { "happy" : 1 }, 
          "happy" : { "to" : 1 }, "have" : { "you" : 1 }, "you" : { "." : 1 } }) == \
        { "hello" : { "words" : ["and"], "probs" : [1] },
          "and" : { "words" : ["welcome"], "probs" : [1] },
          "welcome" : { "words" : ["to"], "probs" : [1] },
          "to" : { "words" : ["the", "have"], "probs" : [0.5, 0.5] },
          "the" : { "words" : [ "program" ], "probs" : [1] },
          "program" : { "words" : ["."], "probs" : [1] },
          "we're" : { "words" : ["happy"], "probs" : [1] },
          "happy" : { "words" : ["to"], "probs" : [1] },
          "have" : { "words" : ["you"], "probs" : [1] },
          "you" : { "words" : ["."], "probs" : [1] } })
    assert(build_bigram_probs(\
        { "this" : 1, "is" : 1, "the" : 1, "song" : 1, "that" : 1, "never" : 1, 
          "ends" : 1, "yes" : 1, "it" : 4, "goes" : 1, "on" : 3, "and" : 2, "my" : 1, 
          "friends" : 1, "!" : 1, "some" : 1, "people" : 1, "started" : 1, "singing" : 2, 
          "," : 2, "not" : 1, "knowing" : 1, "what" : 1, "was" : 1, "now" : 1, "they" : 1, 
          "keep" : 1, "forever" : 1, "just" : 1, "because" : 1, "." : 3 }, 
        { "this" : { "is" : 1 }, "is" : { "the" : 1 }, "the" : { "song" : 1 }, 
          "song" : { "that" : 1 }, "that" : { "never" : 1 }, "never" : { "ends" : 1 }, 
          "yes" : { "it" : 1 }, "it" : { "goes" : 1, "," : 1, "was" : 1, "forever" : 1 }, 
          "goes" : { "on" : 1 }, "on" : { "and" : 1, "my" : 1, "singing" : 1 }, 
          "and" : { "on" : 1, "now" : 1 }, "my" : { "friends" : 1}, "friends" : { "!" : 1 }, 
          "some" : { "people" : 1 }, "people" : { "started" : 1 }, "started" : { "singing" : 1 }, 
          "singing" : { "it" : 2 }, "," : { "not" : 1 }, "not" : { "knowing" : 1 },
          "knowing" : { "what" : 1 }, "what" : { "it" : 1 }, "was" : { "," : 1 },
          "now" : { "they" : 1 }, "they" : { "keep" : 1 }, "keep" : { "on" : 1 },
          "forever" : { "just" : 1 }, "just" : { "because" : 1 }, 
          "because" : { "." : 1 }, "." : { "." : 2 } }) == \
        { "this" : { "words" : ["is"], "probs" : [1] },
          "is" : { "words" : ["the"], "probs" : [1] },
          "the" : { "words" : ["song"], "probs" : [1] },
          "song" : { "words" : ["that"], "probs" : [1] },
          "that" : { "words" : ["never"], "probs" : [1] },
          "never" : { "words" : ["ends"], "probs" : [1] },
          "yes" : { "words" : ["it"], "probs" : [1] },
          "it" : { "words" : ["goes", ",", "was", "forever"], "probs" : [0.25, 0.25, 0.25, 0.25] },
          "goes" : { "words" : ["on"], "probs" : [1] },
          "on" : { "words" : ["and", "my", "singing"], "probs" : [1/3, 1/3, 1/3] },
          "and" : { "words" : ["on", "now"], "probs" : [0.5, 0.5] },
          "my" : { "words" : ["friends"], "probs" : [1] },
          "friends" : { "words" : ["!"], "probs" : [1] },
          "some" : { "words" : ["people"], "probs" : [1] },
          "people" : { "words" : ["started"], "probs" : [1] },
          "started" : { "words" : ["singing"], "probs" : [1] },
          "singing" : { "words" : ["it"], "probs" : [1] },
          "," : { "words" : ["not"], "probs" : [0.5] }, # because the total count of "," is 2, with one at the end
          "not" : { "words" : ["knowing"], "probs" : [1] },
          "knowing" : { "words" : ["what"], "probs" : [1] },
          "what" : { "words" : ["it"], "probs" : [1] },
          "was" : { "words" : [","], "probs" : [1] },
          "now" : { "words" : ["they"], "probs" : [1] },
          "they" : { "words" : ["keep"], "probs" : [1] },
          "keep" : { "words" : ["on"], "probs" : [1] },
          "forever" : { "words" : ["just"], "probs" : [1] },
          "just" : { "words" : ["because"], "probs" : [1] },
          "because" : { "words" : ["."], "probs" : [1] },
          "." : { "words" : ["."], "probs" : [2/3] } }) # because the total count is 3

    # One final test to make sure probabilities aren't always the same
    assert(build_bigram_probs(\
        { "one" : 3 }, 
        { "one" : { "a" : 1, "b" : 2 } }) == \
        { "one" : { "words" : ["a", "b"], "probs" : [1/3, 2/3] } })
    print("... done!")

# NEED TO FIX THIS
def test_get_top_words():
    import math
    print("Testing get_top_words()...\n", end="")
    assert(get_top_words(2, [ "hello", "world", "again"], [2/5, 2/5, 1/5], []) == \
        { "hello" : 2/5, "world" : 2/5 })
    assert(get_top_words(3, [ "hello", "world", "again"], [2/5, 2/5, 1/5], []) == \
        { "hello" : 2/5, "world" : 2/5, "again" : 1/5 })
    assert(get_top_words(2, 
        [ "hello", "and", "welcome", "to", "the", "program", ".", "we're", "happy", "have", "you"], 
        [ 1/13, 1/13, 1/13, 2/13, 1/13, 1/13, 2/13, 1/13, 1/13, 1/13, 1/13 ], []) == \
        { "to" : 2/13, "." : 2/13 })
    assert(get_top_words(1, 
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", "goes", 
          "on", "and", "my", "friends", "!", "some", "people", "started", "singing", 
          ",", "not", "knowing", "what", "was", "now", "they", "keep", "forever", "just", "because", "." ], 
        [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 2/41, 
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 2/41, 2/41, 1/41, 1/41, 1/41, 1/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41], []) == \
        { "it" : 4/41 })
    assert(get_top_words(3, 
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", "goes", 
          "on", "and", "my", "friends", "!", "some", "people", "started", "singing", 
          ",", "not", "knowing", "what", "was", "now", "they", "keep", "forever", "just", "because", "." ], 
        [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 2/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 2/41, 2/41, 1/41, 1/41, 1/41, 1/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41], []) == \
        { "it" : 4/41, "on" : 3/41, "." : 3/41 })
    assert(get_top_words(6, 
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", "goes", 
          "on", "and", "my", "friends", "!", "some", "people", "started", "singing", 
          ",", "not", "knowing", "what", "was", "now", "they", "keep", "forever", "just", "because", "." ], 
        [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 2/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 2/41, 2/41, 1/41, 1/41, 1/41, 1/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41], []) == \
        { "it" : 4/41, "on" : 3/41, "." : 3/41, "and" : 2/41, "singing" : 2/41, "," : 2/41 })
    
    words = ['though', ',', 'in', 'reviewing', 'the', 'incidents', 'of', 'my', 'administration', 'I', 'am', 'unconscious', 'intentional', 'error', 'nevertheless', 'too', 'sensible', 'defects', 'not', 'to', 'think', 'it', 'probable', 'that', 'may', 'have', 'committed', 'many', 'errors', '.', 'shall', 'also', 'carry', 'with', 'me', 'hope', 'country', 'will', 'view', 'them', 'indulgence', ';', 'and', 'after', 'forty', '-', 'five', 'years', 'life', 'dedicated', 'its', 'service', 'an', 'upright', 'zeal', 'faults', 'incompetent', 'abilities', 'be', 'consigned', 'oblivion', 'as', 'myself', 'must', 'soon', 'mansions', 'rest', 'anticipate', 'pleasing', 'expectation', 'retreat', 'which', 'promise', 'realize', 'sweet', 'enjoyment', 'partaking', 'midst', 'fellow', 'citizens', 'benign', 'influence', 'good', 'laws', 'under', 'a', 'free', 'government', 'ever', 'favorite', 'object', 'heart', 'happy', 'reward', 'trust', 'our', 'mutual', 'cares', 'labors', 'danger']
    probs = [0.006134969325153374, 0.06748466257668712, 0.018404907975460124, 0.006134969325153374, 0.05521472392638037, 0.006134969325153374, 0.06748466257668712, 0.03680981595092025, 0.006134969325153374, 0.049079754601226995, 0.012269938650306749, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.03067484662576687, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.024539877300613498, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.018404907975460124, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.024539877300613498, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.012269938650306749, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.018404907975460124, 0.006134969325153374, 0.006134969325153374, 0.018404907975460124, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.012269938650306749, 0.006134969325153374, 0.006134969325153374, 0.012269938650306749, 0.012269938650306749, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374]
    result1 = get_top_words(8, words + [], probs + [], [])
    keys1 = sorted(list(result1.keys()))
    assert(keys1 == [',', 'I', 'my', 'of', 'that', 'the', 'to', 'with'])
    assert(math.isclose(result1[','], 0.06748466257668712, rel_tol=0.0001))
    assert(math.isclose(result1['of'], 0.06748466257668712, rel_tol=0.0001))
    assert(math.isclose(result1['the'], 0.05521472392638037, rel_tol=0.0001))
    assert(math.isclose(result1['I'], 0.049079754601226995, rel_tol=0.0001))
    assert(math.isclose(result1['my'], 0.03680981595092025, rel_tol=0.0001))
    assert(math.isclose(result1['to'], 0.03067484662576687, rel_tol=0.0001))
    assert(math.isclose(result1['that'], 0.024539877300613498, rel_tol=0.0001))
    assert(math.isclose(result1['with'], 0.024539877300613498, rel_tol=0.0001))

    result2 = get_top_words(5, words + [], probs + [], [',', '.', '-', ';'])
    keys2 = sorted(list(result2.keys()))
    assert(keys2 == ['I', 'my', 'of', 'the', 'to'])
    assert(math.isclose(result2['of'], 0.06748466257668712, rel_tol=0.0001))
    assert(math.isclose(result2['the'], 0.05521472392638037, rel_tol=0.0001))
    assert(math.isclose(result2['I'], 0.049079754601226995, rel_tol=0.0001))
    assert(math.isclose(result2['my'], 0.03680981595092025, rel_tol=0.0001))
    assert(math.isclose(result2['to'], 0.03067484662576687, rel_tol=0.0001))
    
    # testing for not destructively changing ignore list
    ignore = [ ".", "hello", "and", "15-110", "we're", "have", "you"]
    result = get_top_words(3, 
        [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"], 
        [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ], 
        ignore)
    assert(ignore == [ ".", "hello", "and", "15-110", "we're", "have", "you"])
    print("... done!")

def test_generate_text_from_unigrams():
    print("Testing generate_text_from_unigrams()...\n", end="")
    # Since this is random, we can only check that it's the right length
    # and that it only uses words in the provided list.
    words = [ "hello", "world", "again" ]
    probs = [ 2/5, 2/5, 1/5 ]
    sentence = generate_text_from_unigrams(5, words, probs)
    assert(len(sentence.strip().split(" ")) == 5)
    for word in sentence.strip().split(" "):
        assert(word in words)

    words = [ "hello", "and", "welcome", "to", "the", "program", ".", "we're", "happy", "have", "you" ]
    probs = [ 1/13, 1/13, 1/13, 2/13, 1/13, 1/13, 2/13, 1/13, 1/13, 1/13, 1/13 ]
    sentence = generate_text_from_unigrams(10, words, probs)
    assert(len(sentence.strip().split(" ")) == 10)
    for word in sentence.strip().split(" "):
        assert(word in words)

    words = [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", 
              "goes", "on", "and", "my", "friends", "!", "some", "people", "started", 
              "singing", ",", "not", "knowing", "what", "was", "now", "they", "keep", 
              "forever", "just", "because", "." ]
    probs = [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 
              2/41, 1/41, 1/41, 1/41, 1/41, 1/41,  1/41, 2/41, 2/41, 1/41, 1/41, 
              1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41 ]
    sentence = generate_text_from_unigrams(20, words, probs)
    assert(len(sentence.strip().split(" ")) == 20)
    for word in sentence.strip().split(" "):
        assert(word in words)
    print("... done!")

def test_generate_text_from_bigrams():
    print("Testing generate_text_from_bigrams()...\n", end="")
    # Since we assume . is used as a stopping point, include it specifically in the test set.
    start_words = [ "hi", "dear" ]
    start_probs = [ 0.6, 0.4 ]
    bigram_probs = { 
        "hi" : { "words" : [",", "how"], "probs" : [0.8, 0.2] },
        "dear" : { "words" : [ "sir", "madam" ], "probs" : [0.5, 0.5] },
        "," : { "words" : ["what's", "sup", "yeet"], "probs" : [0.3, 0.3, 0.4] },
        "how" : { "words" : ["are"], "probs" : [1] },
        "sir" : { "words" : [".", ","], "probs" : [0.8, 0.2] },
        "madam" : { "words" : [ ".", ","], "probs" : [0.8, 0.2] },
        "what's" : { "words" : [ "up" ], "probs" : [1] },
        "sup" : { "words" : [ "." ], "probs" : [1] },
        "yeet" : { "words" : [ "!" ], "probs" : [1] },
        "are" : { "words" : [ "you", "yeet" ], "probs" : [0.9, 0.1] },
        "up" : { "words" : [ ".", "," ], "probs" : [0.5, 0.5] },
        "!" : { "words" : ["!", "."], "probs" : [0.7, 0.3] },
        "you" : { "words" : ["."], "probs" : [1] } }

    sentence = generate_text_from_bigrams(10, start_words, start_probs, bigram_probs)
    sentence_words = sentence.strip().split()
    assert(len(sentence_words) == 10)

    # Check that the order of words is legal
    for i in range(len(sentence_words)):
        if i == 0 or sentence_words[i-1] == ".":
            assert(sentence_words[i] in start_words)
        else:
            assert(sentence_words[i] in bigram_probs[sentence_words[i-1]]["words"])
    print("... done!")

def test_all():
    test_load_book()
    test_get_corpus_length()
    test_build_vocabulary()
    test_count_unigrams()
    test_make_start_corpus()
    test_count_bigrams()
    
    test_build_uniform_probs()
    test_build_unigram_probs()
    test_build_bigram_probs()
    test_get_top_words()
    test_generate_text_from_unigrams()
    test_generate_text_from_bigrams()

def run():
    print("\n-----\n")
    print("Let's try running the whole thing!")
    book = load_book("data/fairytales_clean.txt")
    length = get_corpus_length(book)
    print("\n-----\n")
    
    # Uniform Model
    print("UNIFORM MODEL")
    unique_words = build_vocabulary(book)
    uniform_probs = build_uniform_probs(unique_words)
    print("\nText generated by the Uniform Model:")
    print(generate_text_from_unigrams(100, unique_words, uniform_probs))
    print("\n-----\n")

    # Unigram Model
    print("UNIGRAM MODEL")
    unigram_counts = count_unigrams(book)
    unigram_probs = build_unigram_probs(unique_words, unigram_counts, length)
    print("\nTop 20 words in the Unigram Model:")
    print(get_top_words(20, unique_words, unigram_probs, []))
    print("\nText generated by the Unigram Model:")
    print(generate_text_from_unigrams(100, unique_words, unigram_probs))
    print("\n-----\n")
    
    # Start Words Model
    print("START WORDS MODEL")
    start_corpus = make_start_corpus(book)
    start_words = build_vocabulary(start_corpus)
    start_word_counts = count_unigrams(start_corpus)
    start_word_probs = build_unigram_probs(start_words, start_word_counts, len(book))
    print("\nTop 20 starting words in the Unigram Model:")
    print(get_top_words(20, start_words, start_word_probs, []))
    print("\n-----\n")

    # Bigram Model
    print("BIGRAM MODEL\n")
    bigram_counts = count_bigrams(book)
    bigram_probs = build_bigram_probs(unigram_counts, bigram_counts)
    print("Text generated by the Bigram Model:")
    print(generate_text_from_bigrams(100, start_words, start_word_probs, bigram_probs))