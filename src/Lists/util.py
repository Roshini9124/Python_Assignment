def execute(l,data):
    command=data[0]
    match command:
        case 'append':
            value=int(data[1])
            l.append(value)
        case 'insert':
            ind=data[1]
            val=data[2]
            l.insert(int(ind),int(val))
        case 'print':
            print(l)
        case 'remove':
            l.remove(int(data[1]))
        case 'sort':
            l.sort()
        case 'pop':
            l.pop()
        case 'reverse':
            l.reverse()