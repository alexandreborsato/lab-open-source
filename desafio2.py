# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input(("Enter the Azure storage component: "))

# Função responsável por receber um serviço de armazenamento e retornar sua respectiva descrição.
def identificar_servico_armazenamento(servico):
	if servico == "Arquivos do Azure":
			return "Armazenamento de arquivos compartilhados acessíveis por meio de SMB"
			
	# TODO: Preencha o serviço de acordo com a descrição, considerando as condições abaixo e Saídas possíveis:		
	elif servico == "Blob do Azure":
	    return "Armazenamento de arquivos grandes e não estruturados"
	    
	elif servico == "Fila do Azure":
	    return "Armazenamento de mensagens para comunicação entre aplicações"
	    	    	
	elif servico == "Tabelas do Azure":
	    return "Armazenamento de dados estruturados não relacionais em tabelas"
	    
	elif servico == "Disco do Azure":
	    return "Armazenamento de alto desempenho para máquinas virtuais"
	    
print(identificar_servico_armazenamento(entrada))
