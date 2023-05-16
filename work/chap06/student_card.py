class studentcard:
    school_name = 'python大学'
    def __init__(self,id,name):
        print('初期化しました')
        self.id = id
        self.name = name
        
    def print_info(self):
        print('学籍番号:', self.id)
        print('氏名:', self.name)
        
    @classmethod
    def print_name(cls):
        print(cls.school_name)

if __name__ == '__main__':
    a1 = studentcard(1234,'鈴木太郎')
    a1.print_info()
    a1.print_name()


    a2 = studentcard(1235,'佐藤花子')
    a2.print_info()
    studentcard.print_name()

print('__name__:',__name__)
