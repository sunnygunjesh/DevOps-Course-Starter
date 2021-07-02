class ViewModel:
    def __init__(self,items):
        self._items = items

    @property
    def items(self):
        return self._items

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

    # For stretch goals,no longer in use 
    # @property
    # def should_show_all_done_items(self):
    #     output=[]
    #     for item in self.items:
    #         if item.status=="Done":
    #             output.append(item)
    #     return output

    # @property
    # def recent_done_items(self):
    #     output=[]
    #     for item in self.items:
    #         if item.status=="Done":
    #             output.append(item)
    #     return output

    # @property
    # def older_done_items(self):
    #     output=[]
    #     for item in self.items:
    #         if item.status=="Done":
    #             output.append(item)
    #     return output