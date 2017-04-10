# put your code here.
import sys
import collections

input_file = sys.argv[1]

cnt = collections.Counter()

def get_word_count(input_file):
    """Returns word count from text file."""

    poem = open(input_file).read()

    words = poem.split(" ")

    for word in words:
        cnt[word] += 1

    return cnt

    
    #word_count = {}

    #for line in poem:
     #   line = line.rstrip()
      #  words = line.split()

       # for word in words:
        #    word = word.lower()
         #   word = word.strip("!\"@?.,/:;_")
          #  word_count[word] = word_count.get(word, 0) + 1

    #return word_count

print get_word_count(input_file)
