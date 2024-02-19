# Identificação de Escritor por Transformada SIFT e SVM-Linear na Língua Portuguesa

## Descrição
Este é o trabalho de conclusão de curso realizado por mim para o curso de engenharia elétrica na Universidade Federal de São Carlos.

É um modelo que se utiliza da transformada SIFT, K-mean, Bag-of-Visual-Words e SVM-Linear para identificação de autores para textos manuscritos, com a métodologia validada juntamente ao banco de cartas forenses do [Brazilian Forensic Letter Database (BFL)](https://web.inf.ufpr.br/vri/databases/brazilian-forensic-letter-database/).

## Informações
1. [Anotações da métodologia proposta se encontram](notes-Methodology-Example.ipynb)

2. [Anotações da Transformada SIFT](notes-SIFT-Transform-Example.ipynb)

3. [Arquivo da validação de dados do BFL](main.py)

## Instalação
1. Clone o repositório do projeto:
   ```
   git clone https://github.com/jplsanchez/Writer-Identification-SIFT-BoW-SVM
   ```

2. Navegue até o diretório do projeto:
   ```
   cd Writer-Identification-SIFT-BoW-SVM
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No macOS e Linux:
     ```
     source venv/bin/activate
     ```

5. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Utilização
Para a Utilização do [Arquivo da validação de dados do BFL](main.py) ou do [Notebook com o passo a passo da métodologia](notes-Methodology-Example.ipynb) é necessário adicionar as imagens do BFL a pasta [./src/assets/BFL](./src/assets/BFL).
> As imagens do BFL podem ser obtidas em: [Brazilian Forensic Letter Database (BFL)](https://web.inf.ufpr.br/vri/databases/brazilian-forensic-letter-database/)

## Contribuição
Contribuições são bem-vindas! Se você quiser contribuir para este projeto, siga estes passos:
1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit de suas alterações (`git commit -am 'Adicione uma nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Autores
- Autor: João Paulo Lopes Sanchez
- Orientador: Celso Ap. de França

## Licença
Este projeto é licenciado sob a MIT License. Consulte o arquivo LICENSE para obter mais detalhes.
