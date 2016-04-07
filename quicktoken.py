import types
PUNCTUATION = '`~!@#$%^&*()_-+={[}]|\:;"<,>.?/}\t\n'
def remove_punctuation(words, punctuation=PUNCTUATION):
    """Remove punctuation from an iterator of words, yielding the results."""
    punctuations = list(PUNCTUATION)
    
    result = []
    
    for word in words:
        string = ""
        for letter in word:
            
                
            if letter not in punctuations:
                string= string+letter
                if len(string) == len(word):
                    result.append(string)
                    string = ""
                    continue
            else:
                result.append(string)
                string = ""
    result2 = []
    for word in result:
        if len(word) > 0:
            result2.append(word)
    result2 = (i for i in result2)
    return result2
def lower_words(words):
    """Make each word in an iterator lowercase."""
    result = []
    for word in words:
        string = ""
        for letter in word:
            x = ord(letter)
            if 65 <= x <= 90:
                x = x +32
            string = string + chr(x)
        result.append(string)
    result = (i for i in result)
    return result
def remove_stop_words(words, stop_words= None):
    """Remove the stop words from an iterator of words.
    
    stop_words can be provided as a list of words or a whitespace separated string of words.
    
    """
    if stop_words == None:
        result = [word for word in words]
        return result 
    words = list(words)
    if type(stop_words) == str:
        stop_words = stop_words.split(" ")
    
    result = [word for word in words if word not in stop_words]
    
    
    result = (i for i in result)
    return result
def tokenize_line(line, stop_words=None, punctuation=PUNCTUATION):
    """Split a string into a list of words, removing punctuation and stop words."""
   
    
    x = remove_punctuation(line.split(" "))
    
    x = list(x)
    
    x = lower_words(list(x))
    
    x = list(x)
    x = remove_stop_words(x, stop_words = stop_words )
    
    x = (i for i in x)
    
    
    
    return x

def tokenize_lines(lines, stop_words=None, punctuation=PUNCTUATION):
    """Tokenize an iterator of lines, yielding the tokens."""
    result = []
    for line in lines:
        line = str(line)
        x = tokenize_line(line, stop_words = stop_words, punctuation = punctuation)
        x = list(x)
        for i in x:
            
            result.append(i)
    result = (i for i in result)
    return result

def count_words(words):
    """Return a word count dictionary from the list of words in data."""
    result = {}
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] = result[word] + 1
    return result

def sort_word_counts(wc):
    """Return a list of 2-tuples of (word, count), sorted by count descending."""
    result = []
    
    x = ("a", -1)
    print(wc)
    while (len(result) < len(wc)):
        high = -1
        for item in wc:
            if wc[item] > high:
                high = wc[item]
                x = (item, wc[item])
        result.append(x)
        wc[x[0]] = -1
    return result
def files_to_lines(files):
    """Iterator over a sequence of filenames, yielding all of the lines in the files."""
    result = []
    for file in files:
        with open(file, "r") as textfile:
            for line in textfile.readlines():
                result.append(line)
    result = (i for i in result)
    return result


