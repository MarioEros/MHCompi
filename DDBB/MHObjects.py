class MHUser:
    user_id:int
    name:str
    lang:str

    def __init__(self,user_id,name,lang):
        self.user_id=user_id
        self.name=name
        self.lang=lang