class Animal():
    def actualizarAnimal(self):
        print("Acaba de adqurir un perro!")

class Perro():

    __come="si"


    def __init__(self,raza,nombre):
        self.raza=raza
        self.nombre=nombre
        print("Perro de raza "+str(self.raza)+" con nombre "+str(self.nombre)+".")

    def sentar(self):
        print("")
        print(" El perro "+str(self.nome)+" se está sentando según tus ordenes.")
        print("   ")
        print("""    
                                                                                
                        t;                                                  
                        LLL;fLtL;L     ;i                                     
                        ffL1Lt1LL;LL1111ii;i                                  
                        ;;;Lff;LLt11LLfLL;;iL                                  
            ;LLfLL     L   LL; fL11LLftL;iiL                                  
            fLLLLtLffLLLtfftf  ;tLLLLLfLL;i;L                                  
            ffffffff;ii;iii;;11L1;;LLffLL1;;L                                  
            LttLL111;;;iiii;11111L11LLfLLLL11f                                 
            LLtL111111;;;;111111tt111LtffLLLL11L                               
            fLttL1111111111L1fttf1111LLLLLfLfft                               
            ;tLttLLLLLLLLLftttt11111LLLLLL                                   
                ;fffLLLLttttttt1LLLLLLLLLL1L                                  
                LLLLfLLfLLfLLftLLLLLLLLLL11                                 
                1fLtLfLLfLftLLttLL1LLLLLLLLLL;                           1;   
                ;fLLLLLLf; fLLtLL111LLLLLLLLLLLf                      LL1;     
                LfLLLLLf; iLLLtL11111LLLLLLLLLLLLL                  ;tLL       
                LfffLLff  fLLLLL11111LLLLLLLLttttLLL;              LLL1        
                ;ffLLLft  fLLLtL111111LLLLLLLLLL1;1LLfLt           Lt11        
                fffLL   LLLLtL11111111LLLLLf1;;;11LLLtLtL       ;LL1;ft      
                        fLLLtLLL11111111LLL1;1LLLLLLLLLttLt      LtL1;L      
                        1ftLLtLL1111;;1L11L1;1LLLLLLLLLLLtLL     ;LL11;L     
                        LLLfLLfLL111;;LLLLL1;;111111111LLtLtf    LLtL;;L     
                        fLLfffftL11;;1fLLLtf1111111111111LtLt;LfLLLL11Lt     
                        L1tLLf tL11;;LLffffLL111111111L111tLtLLfLLLLLt;      
                        L;1LtLLLLtL11;;ffffLfffL111111111L1tLLLttttLf1         
                    L1LLLLLLffLL111;1LtfL111;;;;1111111ttLLti                
                    LLLLLLfLftL11111LLfLfLL1LLLLLLLLLLttL1                   
                            ;fLLfLttLtL ;fffLLLLL;                                                                                                                                             
                                  """)

    def ladrar(self):
        print("")
        print("     /")
        print("     --  )")
        print("     \")
        print(" El perro de raza "+str(self.raza)+", con nombre "+str(self.nombre)+" está ladrando!")
    

    def __darPata(self):
        print("Solo me dá la pata en privado!")

    @staticmethod
    def saludarPrivadoStatic():
        print("woah woah!")

    def darPataIsmael(self):
        self.__darPata()

    def saludarPublico(self):
        Can.saludarPrivadoStatic()

    def comer(self):
        print("¿Come? "+str(self.__come))

    def notificarAnimal(self):
        Animal.actualizarAnimal(self)

miPerro=Perro("Pastor Belga","Rufus")
miPerro.saludarPublico()

