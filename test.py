from hash import customhash

hash ={}

ingredients="daal bhaat chamal"
ingredients=ingredients.split()
for i in ingredients:
    j=customhash(i.lower())
    hash[j]=i


def search(string):
    k=customhash(string)
    if k in hash:
        print (hash[k])

search("bhaat")

