def catClone(listOfWords):
    if isinstance(listOfWords, list):
        catWord = ""
        for word in listOfWords:
            if not isinstance(word, str):
                raise TypeError("List contains non-string values")
            catWord += word
        return catWord