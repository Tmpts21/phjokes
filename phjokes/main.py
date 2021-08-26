from random import choice    
from phjokes.utils.helpers import get_jokes_by_count , get_joke_by_dialect  , pinoy_jokes  
import pprint


def get_joke( dialect : str = None , count : int  = None ,)  :                
    """ 
         returns a pinoy joke    

         args : 
        
         <count> : specify how many jokes you want , the default is 1 and must not be greater than 10  
         <dialect> : specify what type of dialect 
         
    """
    jokes = pinoy_jokes 

    if dialect is not None  :  
        jokes = get_joke_by_dialect(dialect) 

    if count is not None    :        
        return get_jokes_by_count(count , jokes ) 
    
    return choice(jokes)

def random(count : int = None )  :              
    """ 
         returns a random joke    

         args : 
        
         <count> : specify how many jokes you want , the default is 1 and must not be greater than 10 
         
    """
    if count is not None :      
        return get_jokes_by_count(count , pinoy_jokes)

    return  choice(pinoy_jokes)      



