### VALIDAÇÃO DO CPF ###

def validar_cpf(cpf):

    cont = 0 
    # aqui ele verifica se todos os caracteres são números, 11 dígitos
    for k in range(len(cpf)): 
        if cpf[k] >= "0" and cpf[k] <= "9":
            cont += 1
           
    if len(cpf) != 11 and cont < len(cpf):
        print("O cpf preicsa ter 11 dígitos e conter apenas números reais")
        return False

    elif len(cpf) != 11:
        print("O cpf precisa ter 11 dígitos")
        return False
    
    elif cont != 11:
        print("Utilize apenas números reais")
        return False
    
    else:                                                       # a partir desse "else", acontece a verificação matemática.
        iguais=0                                                # em primeiro lugar, verifica-se se o cpf não possui todos os dígitos iguais.
        for k in range (len(cpf)):                              # em segundo lugar, é verificado o primeiro dígito de verificação.
            if cpf[k] == cpf[0]:                                # em terceiro lugar, é verificado o segundo dígito de verificação.
                iguais+=1                                       # depois, os dígitos verificadores são comparados e então validados.
        if iguais == 11:
            print("CPF inválido: números repetidos")
            return False
        else:
            soma1=0
            multiplicacao1=10
            for i in range(9):
                soma1+=int(cpf[i])*multiplicacao1               # nesta linha, a string "cpf" é convertida em número inteiro,                                                                                
                multiplicacao1-=1                               # para que possa ser multiplicada como um número.

            resto1=soma1 % 11
            if resto1 < 2:
                first_verify = 0
            else:
                first_verify= 11 - resto1
                if first_verify >= 10:
                    first_verify = 0

            #Cálculo do segundo dígito verificador
            soma2=0                                            
            multiplicacao2=11
            for i in range(9):
                soma2+=int(cpf[i])*multiplicacao2
                multiplicacao2-=1

            soma2+=first_verify*2
            resto2=soma2 % 11
            if resto2 < 2:
                second_verify = 0
            else:
                second_verify= 11 - resto2
                if second_verify >= 10:
                    second_verify = 0
             #Validação final
            if first_verify == int(cpf[9]) and second_verify == int(cpf[10]):   
                print("CPF válido!")
                return True
            else:
                print("CPF inválido: erro nos dígitos verificadores.")  
                return False


                                                                                                                                                                                     