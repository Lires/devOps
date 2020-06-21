class Animal():
    def actualizarAnimal(self):
        print("Acaba de adquirir un can!")

class Can():

    __come="si"


    def __init__(self,raza,nome):
        print("WOAH WOAH!!!")
        self.raza=raza
        self.nome=nome
        print("Raza "+str(self.raza)+" con nome "+str(self.nome)+"!!")

    def sentar(self):
        print("")
        print(" O can "+str(self.nome)+" estase sentando según túas ordes.")
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

    def cagar(self):
        print("")
        print("      ()")
        print("     (  )")
        print("    (    )")
        print(" O can de raza "+str(self.raza)+", con nombre "+str(self.nome)+" está cagando!")
    

    def __darPata(self):
        print("solo me da a pata a min!")

    @staticmethod
    def saludarPrivadoStatic():
        print("woah woah!")

    def darPataIsmael(self):
        self.__darPata()

    def saludarPublico(self):
        Can.saludarPrivadoStatic()

    def comer(self):
        print("Come? "+str(self.__come))

    def notificarAnimal(self):
        Animal.actualizarAnimal(self)

meuCan=Can("palleiro","Cobi")
meuCan.saludarPublico()

