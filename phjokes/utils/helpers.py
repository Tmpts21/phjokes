from random import choice      
from phjokes.jokes.jokes import pinoy_jokes


list_of_dialects = ["tagalog" , "bisaya"]   

def get_joke_by_dialect(dialect : str ) -> list :     
    """  
        returns a list of jokes based on dialect
    """  
    if dialect in list_of_dialects :  
        return [ pinoy_jokes[x] for i , x in enumerate(pinoy_jokes , 1 ) if pinoy_jokes[i]['dialect'] == dialect ]  
 
    raise Exception(f" No such dialect ")  


def get_jokes_by_count (count : int , jokes : list ) -> list :  
    """  
        flags
        returns a list of jokes based on the count 
    """  
    if count > 0 and count <= 10 : 
        return [ choice(jokes) for i in range (count)]  

    raise Exception("count must be > 0 and <= 10 ")


    

