def dic_tuple(dic):
    my_list = []
    for keys,peeles in dic.iteritems():
        my_list.append(tuple([keys] + [peeles]))
    
    print my_list

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

dic_tuple(my_dict)
