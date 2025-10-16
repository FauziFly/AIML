print("Dictionary Example")
our_dictionary=[
    {"id":'1',"name":'fauzi', "age":'28'},
    {"id":'2',"name":'hack', "age":'21'},
    {"id":'3',"name":'pitaou', "age":'32'},
    {"id":'4',"name":'sawey', "age":'33'} 
    ]
for k in our_dictionary:
    print(k["id"]+"->"+k["name"]+"->"+k["age"])