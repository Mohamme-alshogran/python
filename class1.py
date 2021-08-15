class member :
    not_allowd_names =["ali","manal","abd"]
    def __init__(self,firstname , middlname,lastname,gender) :
        self.first =firstname
        self.middl = middlname
        self.last = lastname
        self.gender=gender
    def fullname (self) :
        if self.first in member.not_allowd_names:

            raise ValueError ("name not allowd")

        else:
            return f"{self.first} {self.middl} {self.last}"
    def name_with_title (self) :
        if self.gender == "male" :
          return f"hello mr {self.first}"
        elif self.gender == "famel" :
            return f"heloo miss {self.first}"
        else:
            return f"heloo {self.first}"
    def get_all_info (self):
        return f"{self.name_with_title()},your full name is : {self.fullname()}"
member1 =member('mhammed','khaled','alshogran' , "male")
member2 = member ('ali' , 'manal','abd'," ")
print(member1.fullname())
print(member1.name_with_title())
print(member1.get_all_info())
print(member2.get_all_info())