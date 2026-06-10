import os
import sys

# Adiciona o diretório plantuml_generator ao path para importar a API
sys.path.append(os.path.join(os.path.dirname(__file__), 'plantuml_generator'))

from plantuml_client import PlantUMLClient

def gerar_imagens():
    client = PlantUMLClient()
    diagramas_dir = os.path.join(os.path.dirname(__file__), 'diagramas')
    
    if not os.path.exists(diagramas_dir):
        print(f"Diretório '{diagramas_dir}' não encontrado.")
        return

    print("*" * 50)
    print("Gerando imagens dos diagramas...")
    print("*" * 50)

    for file_name in os.listdir(diagramas_dir):
        if file_name.endswith('.puml'):
            file_path = os.path.join(diagramas_dir, file_name)
            output_filename = file_name.replace('.puml', '.png')
            output_path = os.path.join(diagramas_dir, output_filename)
            
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    plantuml_code = f.read()
                
                print(f"Gerando '{output_filename}' a partir de '{file_name}'...")
                png_content = client.fetch_diagram(plantuml_code, "png")
                
                with open(output_path, "wb") as f:
                    f.write(png_content)
                    
                print(f"Sucesso: '{output_filename}' salvo.")
            except Exception as e:
                print(f"Erro ao processar '{file_name}': {e}")
                
    print("*" * 50)
    print("Processo finalizado.")
    print("*" * 50)

if __name__ == "__main__":
    gerar_imagens()
