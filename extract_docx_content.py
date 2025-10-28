import docx
import sys
import os

def extract_text_from_docx(file_path):
    """
    Extrai texto de um arquivo .docx
    """
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Erro ao extrair conteúdo do arquivo {file_path}: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça o caminho do arquivo .docx como argumento")
        sys.exit(1)
        
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        sys.exit(1)
        
    content = extract_text_from_docx(file_path)
    if content:
        print(content)
    else:
        print("Não foi possível extrair o conteúdo do arquivo.")