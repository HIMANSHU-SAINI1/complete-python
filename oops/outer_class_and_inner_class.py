#outer class and inner class

class course:
    def __init__(self,name,dur,*books):
        self.course_name=name 
        self.duration=dur
        self.books=[self.book(b) for b in books]

    def show_details(self):
        print('name:', self.course_name)
        print('duration:',self.duration)
        print('suggested books')
        for b in self.books:
            print(b)

    class book:
        def __init__(self,title):
            self.title=title

        def __str__(self):
            return self.title
    
c1=course('python',10,'learn python','python crash course')
c1.show_details()