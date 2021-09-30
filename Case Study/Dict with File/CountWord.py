def make_word_list(file):
  infile = open(file, 'r')
  fileLine = infile.readline().lower()
  infile.close()
  line = ""
  for ch in fileLine:
    if('a' <= ch <= 'z') or (ch == " "):
      line += ch # .split()으로 단어를 구분하기 위해 공백 또한 저장을 시켜야 한다.
  wordlist = line.split()
  return wordlist

def make_dict(L):
  freq = {}
  for word in L:
    freq[word] = 0
  for word in L:
    freq[word] = freq[word] + 1 # 여기서 단어의 출현 빈도를 Count.
  return freq

def show_word_count(D, L):
  print("The Gettysburg Address contains", len(L), "words.")
  print("The Gettysburg Address contains", len(D), "different words.")

def show_most_common(D):
  print("The most common words and their frequencies are : ")
  most_common_words = []
  for word in D.keys():
    if D[word] >= 6:
      most_common_words.append((word, D[word]))
  most_common_words.sort(key=lambda x: x[1], reverse=True)
  for item in most_common_words:
    print("  ", item[0], ':', item[1])

wordlist = make_word_list("Gettysburg.txt")
freq = make_dict(wordlist)
show_word_count(freq, wordlist)
show_most_common(freq)
