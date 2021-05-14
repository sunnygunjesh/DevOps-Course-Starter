class ViewModel:
    def __init__(self,items):
        self._items = items

    @property
    def items(self):
        return self.items

    @property
    def todo_items(self):
        output=[]
        for item in self.items:
            if item.status=="To Do":
                output.append(item)
        return output


    @property
    def doing_items(self):
        output=[]
        for item in self.items:
            if item.status=="Doing":
                output.append(item)
        return output

    @property
    def done_items(self):
        output=[]
        for item in self.items:
            if item.status=="Done":
                output.append(item)
        return output
