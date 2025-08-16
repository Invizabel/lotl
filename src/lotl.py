class lotl:
    def chain(data):
        hits = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                hits.append(data[i][j])
        return hits

    def fill(data,nth=-1):
        if isinstance(data, int):
            return [nth for i in range(data)]
        elif isinstance(data,list) or isinstance(data,tuple):
            if len(data) == 2:
                return [[nth for j in range(data[0])] for i in range(data[1])]
    
    def flatten(data,nth=-1):
        if nth == -1:
            while True:
                if any([True if isinstance(i,list) or isinstance(i,tuple) else False for i in data]):
                    add = []
                    for i in data:
                        if isinstance(i,list) or isinstance(i,tuple):
                            add += i
                        else:
                            add.append(i)
                    data = list(add[:])
                else:
                    break
        else:
            for _ in range(nth):
                if any([True if isinstance(i,list) or isinstance(i,tuple) else False for i in data]):
                    add = []
                    for i in data:
                        if isinstance(i,list) or isinstance(i,tuple):
                            add += i
                        else:
                            add.append(i)
                    data = list(add[:])
                else:
                    break
        return data

    def mean(data):
        return sum(data) / len(data)

    def nested(data):
        count = 0
        while True:
            if any([True if isinstance(i,list) or isinstance(i,tuple) else False for i in data]):
                count += 1
                add = []
                for i in data:
                    if isinstance(i,list) or isinstance(i,tuple):
                        add += i
                    else:
                        add.append(i)
                data = list(add[:])
            else:
                break
        return count

    def slope(data):
        x = [i for i in range(1,len(data)+1)]
        hits = lotl.mean([(data[i+1]- data[i]) / (x[i+1] - x[i])  for i in range(len(data)-1)])
        return hits
