


            
class MyError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'this is self define error'   

def my_error_test():
    try:
        info=[{'name':'dahai','age':18,'sex':'男'}, 
            {'name':'dahail','age':24,'sex':'男'},
            {'name':'xialuo','age':78},
            {'name':'dahai2','age':27,'sex':'女'},
            {'name':'xishi','age':8}
            ]
        items = []
        for s in info:
            if s.get("sex") != 'None':
                for item in s.items():
                    items.append(item)
        raise MyError()
    except MyError as e:
        print('exception info: ', items)


my_error_test()