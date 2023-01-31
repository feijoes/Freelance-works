
import services

from br_nome_gen import pessoa_random



import randominfo as ri

class Person:
    def __init__(self) -> None:
        self.first_name = ri.get_first_name()
        self.last_name = ri.get_last_name()
        self.birthdate = ri.get_birthdate()



def main(v:int):
    cpfs = []
    while len(cpfs)< v:
        cpf = services.generate_cpf()
        if cpf not in cpfs: cpfs.append(cpf)
    
    
    for i in range(v+1):
        p : str = pessoa_random().nome
        while True:
            email: str = ri.get_email(Person())
            if email.endswith('.com'):
                break
        services.start()
        services.fields(cpfs[i],p,email)
        services.send()
        services.close()

main(95)
    

        
        
