
def listremoveduplicates(object):
    object = set(object)
    object = list(object)
    return object

mylist = ['1','2','1','4','5','6','6','9','3']


print(listremoveduplicates(mylist))