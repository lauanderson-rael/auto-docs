## Automação para sobrescrever e salvar arquivos .docx e PDFs interativos 
### objetivo
Auxiliar a mim e aos meus colegas de trabalho com tarefas repetitivas, onde manipulavamos arquivo word e pdfs interativos, preenchendo campos e salvando os arquivos com seus respectivos nomes.
### como rodar
- pip install python-docx
- pip install fillpdf
- python main.py

### Apos a execução
 - Sera gerado duas pastas "/declarações_geradas" e "/requerimentos_gerados"
 - Dentro dessas pastas irá conter os arquivos 

### Telas

<img style="margin: 0 -32px" src="./images/image1.png" alt="image1" width="700px"><br>
<img src="./images/image2.png" alt="image1" width="700px"><br>
<img src="./images/image3.png" alt="image1" width="700px"><br>


### Converter para executavel

 - pyinstaller --noconsole --name=app app.py
