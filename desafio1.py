entrada = input(("Enter the Azure component: "))

# Função responsável por receber um componente e retornar sua respectiva descrição.
def identificar_componente(componente):
	if componente == "Datacenters":
			return "Instalações físicas que abrigam servidores e outros recursos"
			
	# TODO: Preencha corretamente a descrição de cada componente, considerando as condições abaixo e Saídas possíveis:		
	elif componente == "Regiões do Azure":
	    return "Localizações geográficas onde os serviços são disponibilizados"
	    
	elif componente == "Assinaturas":
	    return "Unidades de faturamento que agrupam recursos e serviços do Azure"
	    	    	
	elif componente == "Zonas de Disponibilidade":
	    return "Garante alta disponibilidade ao isolar falhas"
	    
	elif componente == "Grupos de Gerenciamento":
	    return "Estruturas hierárquicas que gerenciam múltiplas assinaturas"	    

print(identificar_componente(entrada))
