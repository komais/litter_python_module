import copy
def all_leaf(in_list,element_list,length):
    '''遍历所有的叶子'''
    for i in element_list:
        out_list = copy.copy(in_list)
        out_list += [i]
        if len(in_list)<length-1:
            all_leaf(out_list,element_list,length)
        else :
            print('result is ',end='')
            print("".join(out_list))
            
