# Eletromiograma

 A eletromiografia consiste num exame que avalia a função muscular e diagnostica problemas nervosos ou musculares,
a partir dos sinais elétricos liberados pelos mesmos, recolhendo informações acerca da atividade muscular por meio de eletrodos.            
 Nessa aplicação, os dados serão obtidos via conexão UDP definida de por interface de usuário, o qual deve depois de conectar-se, acionar a leitura.
Ao receber uma mensagem válida (valor numérico inteiro), o interpretador definirá a mensagem como valor válido para o eletromiograma e o gráfico será atualizado.

* Leitura de valores enviados pelo sensor (servidor UDP)
* Plotagem gráfica dos dados recebidos em "tempo real"
* Controle de dados por arquivos de extensão .csv (chave para definir ambiente: $)
* Interpretação de comandos de entrada (Tag comando: #)


## Desenvolvimento
### Instalação de dependências

* Python Package Index (update)
> python -m pip install --upgrade pip

* PyQtGraph: Scientific Graphics and GUI Library for Python
> pip install pyqtgraph

* NumPy: Numerical and multi-dimentional array computing
> pip install numpy

* PyQt5: GUI and cool stuff
> pip install pyqt5

