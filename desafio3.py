# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input(("Enter the Azure security component: "))

# Função responsável por receber um serviço ou ferramenta e retornar sua respectiva descrição.
def associar_recurso(recurso):
	if recurso == "Azure Role-Based Access Control":
			return "Possibilita um gerenciamento de acesso refinado dos recursos"
			
	# TODO: Preencha corretamente a descrição de cada serviço ou ferramenta, considerando as condições abaixo e Saídas possíveis:		
	elif recurso == "Microsoft Entra ID":
	    return "Serviço de gerenciamento de identidades e acessos"
	    
	elif recurso == "Multi-Factor Authentication":
	    return "Proporciona uma camada adicional de segurança"
	    	    	
	elif recurso == "Azure Key Vault":
	    return "Permite armazenar e acessar segredos de maneira segura"
  
	elif recurso == "Azure Security Center":
			return "Oferece visibilidade e controle sobre a segurança dos recursos"

print(associar_recurso(entrada))
