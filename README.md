# Documentação do Código Python para Conversão de Fala em Texto e Tradução

Este script Python realiza a captura de áudio por meio de um microfone, converte o áudio capturado em texto, traduz o texto para o inglês e, em seguida, utiliza síntese de fala para ler o texto traduzido.

## Dependências

- `speech_recognition`: Utilizada para realizar o reconhecimento de fala.
- `pyttsx3`: Biblioteca de conversão de texto em fala offline.
- `gtts` (Google Text-to-Speech): Utilizada para conversão de texto em fala online.
- `io.BytesIO`: Usado para manipulação de fluxos de dados em memória.
- `pygame`: Biblioteca usada para manipulação e reprodução de áudios.
- `deep_translator`: Usada para realizar traduções de textos.
- `my_stt`: Módulo personalizado para reconhecimento de fala (não incluído no script original).

## Inicialização

- Inicializa a biblioteca `pyttsx3` e o mixer de áudio do `pygame`.

## Funções Principais

### Função `main()`

- **Loop Principal**: Executa continuamente a captura, tradução e leitura do áudio.
- **Captura de Áudio**: Usa a função `stt()` para capturar o áudio e convertê-lo em texto.
- **Tradução**: Traduz o texto capturado do português para o inglês.
- **Síntese de Fala**: Lê o texto traduzido em voz alta.

### Função `speak(text, language)`

- **Parâmetros**:
  - `text`: Texto a ser convertido em fala.
  - `language`: Idioma para a conversão de texto em fala.
- **Processo**:
  - Cria um objeto `BytesIO` para armazenar o áudio.
  - Utiliza o `gTTS` para gerar o áudio do texto no idioma especificado.
  - Carrega e reproduz o áudio gerado usando `pygame`.

### Função `stt()`

- **Funcionalidade**: Captura o áudio do microfone e o converte em texto.
- **Processo**:
  - Inicializa o reconhecedor de fala.
  - Ajusta o reconhecedor para o ruído ambiente.
  - Captura o áudio do microfone.
  - Utiliza o `recognize_google` para converter o áudio capturado em texto.

## Execução

- A execução do script inicia pelo bloco `if __name__ == "__main__":`, que chama a função `main()`.

## Observações

- Este script está projetado para funcionar com áudio em português brasileiro (`pt-BR`).
- A função `stt()` e a biblioteca `my_stt` são referenciadas mas não estão definidas no script fornecido.

## Observação

Por algum motivo do universo, o script só funciona no segundo loop, e por motivo de tempo, a entrega será feita com essa observação. O vídeo disponibilizado foi editado.

## Execução

Para executar o script, basta executar o comando `python3 main.py` no terminal.

## Link do Vídeo

Link Drive: https://drive.google.com/file/d/1HEWjedkAwXx-ceYJbOHHYt6LMfmR32yV/view?usp=sharing