
class User():
    
    def __init__(self, name=None, last_name=None, age=None):
        self.name=name
        self.last_name=last_name
        self.age=age  
            
               
    def __eq__(self, other):
        '''https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes'''
        
        if isinstance(other, self.__class__):
            return self.name == other.name and self.last_name == other.last_name and self.age == other.age          
        return NotImplemented
    
    
class Agenda():
            
    def __init__(self, *args):
        '''If no args are given then agenda is empty.The only Args accepted (there is no check) is abs path to a txt agenda'''
        
        self.agenda=[] 
        if len(args) == 1:
            with open(args[0],"r") as f:
                txt_list=f.readlines()
            for line in txt_list:
                mysplit = line.split()
                myuser = User(mysplit[0], mysplit[1], mysplit[2])
                self.add_user(myuser)
        elif len(args) > 1:
            print ("Too many args given!!")
      
                    
    def __contains__(self, other):
        
        return any((x == other ) for x in self.agenda)    # Operator overloading: == --> __eq__ in User Class
        
         
    def add_user(self, user):
            
        self.agenda.append(user)
        
        
    def del_user(self, user):
        
        idx = 0
        for elem in self.agenda:
            if elem == user:            # Operator overloading: == --> __eq__ in User Class
                self.agenda.pop(idx)
            idx += 1
    
    
    def save(self, filename):
        
        with open(filename,"w") as f:
            for elem in self.agenda:
                f.write(elem.name + " " + elem.last_name + " " +  str(elem.age) + "\n" )




if __name__ == "__main__":
    
    agenda = Agenda("/home/aspera/agenda.txt")
    user = User("andrea", "spera", 49)
    agenda.add_user(user)
    user = User("valeria", "virzi", 45)
    agenda.add_user(user)
    user = User("tancredi", "spera", 2)
    agenda.add_user(user)    
    
    utente1 = User("andrea", "spera", 49)
    utente2 = User("andrea", "sper", 49)
    
    if utente1 in agenda:           # Operator overloading: in --> __contain__ in Agenda Class
        print("Presente")
    else:
        print("Assente")
    if utente2 in agenda:           # Operator overloading: in --> __contain__ in Agenda Class
        print("Presente")
    else:
        print("Assente")
        
    agenda.del_user(utente1)
    agenda.save("/home/aspera/agenda_fin.txt")