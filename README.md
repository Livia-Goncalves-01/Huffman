<h1 align="center">
Implementação do Código de Huffman para Compressão de Texto
</h1>

<div align="justify">
  <p>
  Este projeto implementa o algoritmo de Huffman para compressão de texto, aplicando conceitos clássicos de estruturas de dados como min-heaps, árvores binárias e codificação baseada em frequência.
  </p>

  <p>
  O programa recebe textos de entrada, identifica a frequência das palavras, constrói a árvore de Huffman correspondente e gera um código binário otimizado para cada palavra. Além disso, exporta arquivos <b>.dot</b> que permitem visualizar graficamente a árvore gerada por meio do Graphviz.
  </p>
</div>

---

## 📘 Visão Geral do Projeto

<div align="justify">
<p>
A compressão de Huffman é um método eficiente baseado na ideia de atribuir códigos mais curtos às palavras que aparecem com maior frequência. Neste projeto, a entrada é dividida em textos independentes, e para cada um deles são gerados:
</p>

- A árvore de Huffman em formato textual (output.dat)  
- O conjunto de códigos binários de cada palavra  
- A versão comprimida do texto usando os códigos  
- Um arquivo `.dot` representando graficamente a árvore de Huffman  

<p>
O objetivo é compreender a estrutura da árvore, a lógica da compressão e a visualização dos códigos.
</p>
</div>

---

## Como Executar o Projeto

### **1. Pré-requisitos**
- Python 3 instalado  
- Graphviz (opcional, mas necessário para gerar imagens)  

---

### **2. Executando o Programa**

#### **Windows**
```bash
python src\huffman.py
```

#### **Linux / macOS**
```bash
python3 src/huffman.py
```

---

## Arquivos Gerados

Após a execução, o programa cria automaticamente:

 **output.dat**  
Contém:
- Árvore de Huffman representada em forma de texto  
- Frequência das palavras  
- Códigos binários gerados  
- Texto comprimido  

 **huffman_texto_X.dot**  
Arquivos de visualização gráfica da árvore.

---

## Visualizando a Árvore de Huffman (Graphviz)

Para transformar o arquivo `.dot` em `.png`, instale Graphviz:

🔗 https://graphviz.org/download/

Depois execute:

```bash
dot -Tpng huffman_texto_1.dot -o huffman_texto_1.png
dot -Tpng huffman_texto_2.dot -o huffman_texto_2.png
dot -Tpng huffman_texto_3.dot -o huffman_texto_3.png
```

---

##  Tecnologias Utilizadas

- Python 3  
- Árvores binárias  
- Estrutura de min-heap  
- Graphviz  

---

