import string
file_name= input("Faylin adini daxil edin: ")
word = input("Sozu daxil edin: ")
def search_document(word):
    indexes =[]
    with open(file_name, "r") as f:
        read = f.read().split(",")
        word = word.split(" ")
        for index,value in enumerate(read):
            allexist = True
            for i in string.punctuation:
                line = value.replace(i," ")
            for i in word:
                if i.lower() not in line.lower():
                    allexist = False
                    break
            if(allexist):
                indexes.append(index)
    print(indexes)
search_document(word)
            
                
                  
            