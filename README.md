# Simulação de PCA para Compressão de Imagens

Este repositório contém um aplicativo em Python, desenvolvido com **PyQt5**, que permite a aplicação do **Análise de Componentes Principais (PCA)** para compressão de imagens. A interface do usuário (UI) facilita a seleção da imagem e a definição de uma nova resolução, exibindo o processo de compressão e as novas dimensões resultantes. A imagem comprimida é exibida e salva no diretório de saída.

## Funcionalidades

- Carregamento de imagem através de um diálogo de seleção.
- Exibição das dimensões e resolução originais da imagem.
- Caixa de entrada para definir a resolução desejada.
- Aplicação do **PCA** para reduzir a dimensionalidade da imagem.
- Exibição das novas dimensões da imagem comprimida e visualização da imagem resultante.
- Barra de progresso para acompanhar o processamento da compressão.
- Salvamento da imagem comprimida em um diretório `outputs`.

## Arquitetura do Projeto

- **main.py**: O ponto de entrada da aplicação, responsável por iniciar a interface gráfica e a lógica de negócios.
- **ui_module.py**: Implementa a interface gráfica usando **PyQt5**. Contém os elementos de UI, como botões, campos de texto, exibição de imagem e barra de progresso.
- **backend.py**: Contém a lógica de negócios da aplicação. Gerencia o carregamento de imagem, aplicação do PCA e atualização da interface com os resultados.
- **pca_module.py**: Contém a lógica do PCA, realizando a compressão da imagem e o ajuste de resolução baseado no PCA.

## Instalação

### Pré-requisitos

- **Python 3.x**
- Instale as dependências usando o `pip`:

```bash
pip install -r requirements.txt
