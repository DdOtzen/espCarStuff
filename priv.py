class PrivatKlasseTilDemo():

    def __init__( self ) :
        self.var = 33
    
    def min_metode_med_mange_ord( benny ):
        print(benny.var)
        pass

class Child( PrivatKlasseTilDemo ) :
    def __init__(self):
        super().__init__()
        
        self.var__ = "barn"

c = PrivatKlasseTilDemo()
foo = Child()
