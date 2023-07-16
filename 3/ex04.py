           
anos = 0
while True:

    pop1 = int(input('Qual a população da cidade 1? '))
    pop2 = int(input('Qual a população da cidade 2? '))
    taxa1 = float(input('Qual a taxa de crescimento da cidade 1? '))
    taxa2 = float(input('Qual a taxa de crescimento da cidade 2? '))  
    
    while (pop1 < pop2):
    
   
        pop1 = pop1 + (taxa1 * pop1)
        pop2 = pop2 + (taxa2 * pop2)
        anos = anos +1                
    
    print(anos)
         
        
    
    