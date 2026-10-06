# 143 - Mini File Statistics Analyzer: 10 practical features
sample_text='''Python is simple and powerful.\nPython is useful for automation.\nLearning Python requires practice and projects.\nProjects improve programming skills.\n'''
# 1. Character count
def character_count(text): return len(text)
# 2. Characters without spaces
def characters_without_spaces(text): return sum(not c.isspace() for c in text)
# 3. Word count
def word_count(text): return len(text.split())
# 4. Line count
def line_count(text): return len(text.splitlines())
# 5. Longest word
def longest_word(text): return max((w.strip('.,!?;:') for w in text.split()),key=len,default='')
# 6. Count a word
def count_word(text,word): return sum(w.strip('.,!?;:').lower()==word.lower() for w in text.split())
# 7. Word frequencies
def word_frequencies(text):
    r={}
    for w in text.lower().split():
        w=w.strip('.,!?;:')
        if w:r[w]=r.get(w,0)+1
    return r
# 8. Most common words
def most_common_words(text,limit=5): return sorted(word_frequencies(text).items(),key=lambda x:(-x[1],x[0]))[:limit]
# 9. Average word length
def average_word_length(text):
    w=[x.strip('.,!?;:') for x in text.split()]; return round(sum(map(len,w))/len(w),2) if w else 0
# 10. Report
def report(text):
    print('FILE STATISTICS'); print('Characters:',character_count(text)); print('Without spaces:',characters_without_spaces(text)); print('Words:',word_count(text)); print('Lines:',line_count(text)); print('Longest:',longest_word(text)); print('Python count:',count_word(text,'Python')); print('Common:',most_common_words(text)); print('Average word length:',average_word_length(text))
if __name__=='__main__': report(sample_text)
