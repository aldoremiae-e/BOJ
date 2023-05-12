from collections import defaultdict
def solution(tickets):
    answer = []
    names = defaultdict(list)
    names_use = defaultdict(int)
    for ticket in tickets:
        names[ticket[0]].append(ticket[1])
        names_use[ticket[0]] = 0
        
    for key in names.keys():
        names[key] = sorted(names[key], reverse=True)
    #print(names)
    stack = []
    stack.append('ICN')
    while stack:
        #print(stack)
        top = stack.pop()
        
        if top not in names.keys() or not names[top]:
            answer.append(top)
        else:
            stack.append(top)
            stack.append(names[top].pop())
        
    new = []
    while answer:
        new.append(answer.pop())
    return new