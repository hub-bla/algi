def check_condition(nexts):
    degrees_in =[0] * len(nexts.keys())
    degrees_out = [0] * len(nexts.keys())
    #degrees_out
    for node1 in range(len(nexts.keys())):
        degrees_out[node1]  = len(nexts[node1])
        #degrees_in
        for node2 in  range(len(nexts.keys())):
                for node3 in nexts[node2]:
                     if node3==node1:
                        degrees_in[node1] +=1
        if degrees_out[node1]!=degrees_in[node1]:
            return False
    return True

def find_euler_nexts(node, nexts, track, stack):
    w = node
    stack.append(w)
    while len(nexts[w]) != 0:
        w = nexts[w].pop(0)
        stack.append(w)
        if node==w:
            break

    w = stack.pop(-1)
    while True:
        if len(nexts[w]) == 0:
            track.append(w)
        else:
            find_euler_nexts(w, nexts, track, stack)
        w = stack.pop(-1)
        if w==node:
            break
    track.append(node)
  
       
    
    
def euler_nexts(nexts):
    copy_of_nexts = nexts.copy()
    stack = []
    track = []
    if check_condition(copy_of_nexts):
        find_euler_nexts(0, copy_of_nexts, track, stack)
        print(track)
    else:
        print("Brak cyklu")
    