## final answer

import itertools

def solve(data):

    # generate name index map
    rdx = {}
    for k,v in enumerate(data):
        rdx[v['name']] = k

    # process children
    for k,v in enumerate(data):
        if v['parent']:
            data[rdx[v['parent']]]['children'].append(v)

    r = [data[i] for i,v in enumerate(data) if v['parent'] is None]
    
    # process level
    l = 0
    a = [i for i,v in enumerate(data) if v['parent'] is None]
    while a:
        
        for i in a:
            data[i]['level'] = l

        a2=[ [rdx[j['name']]for j in data[i]['children']] for i in a]
        a = list(itertools.chain(*a2))

        l += 1
        
    for i in data:
        i['level'] = l - i['level']

    return r

def main():
    data = '''
    [
    {
        "name": "John",
        "parent": null
    },
    {
        "name": "Tom",
        "parent": null
    },
    {
        "name": "Ava",
        "parent": "John"
    },
    {
        "name": "Eric",
        "parent": "Tom"
    },
    {
        "name": "Emily",
        "parent": "John"
    },
    {
        "name": "James",
        "parent": "Emily"
    },
    {
        "name": "Lucas",
        "parent": "Emily"
    }
    ]
    '''
    import json
    data = json.loads(data)
    data = [{'name':i['name'],'level':0,'parent':i['parent'],'children':[]} for i in data]
    r = solve(data)
    print( json.dumps(r, indent=2))

if __name__ == '__main__':
    main()    