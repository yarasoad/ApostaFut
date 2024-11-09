from kivymd.app import MDApp #classe da criação do app com KivyMD
from kivymd.uix.boxlayout import MDBoxLayout #importa o layout
from kivymd.uix.label import MDLabel #importa o texto
from kivymd.uix.textfield import MDTextField #importa caixa para usuario escrever
from kivymd.uix.button import MDRaisedButton #importa botao
from kivy.metrics import dp #garantir tamanho adequado

#layout da janela
class ApostaFutebol (MDBoxLayout): #criando a classe, contendo uma caixa para organizar os elementos
    def __init__(self, **kwargs): #construtor init, self referenciar objeto e kwargs substitui parametros (nome, idade, cor)
        super().__init__(orientation='vertical', padding=50, spacing=dp(15), **kwargs) #coluna vertical, espaço da borda da janela, espaço entre os campos

        #Campo do Título
        self.add_widget(MDLabel(text='Aposta Futebol', halign='center', font_style='H5'))

        #campo do "Time A" 
        self.add_widget(MDLabel(text='Time A', halign='left')) #adicionar campo e titulo 
        self.time_a=MDTextField(hint_text='Nome do Time A') #vai aparecer dentro do espaço para escrita do campo 
        self.add_widget(self.time_a) #adicionar campo dentro da caixa MDBoxLayout

        #campo do "Time B"
        self.add_widget(MDLabel(text='Time B', halign='left')) # MDLABEL - titulos de textos
        self.time_b=MDTextField(hint_text='Nome do Time B') #MDTextField - campo para o usuário escrever
        self.add_widget(self.time_b)

        #campo do "valor da aposta"
        self.add_widget(MDLabel(text="Valor da Aposta (R$):", halign="left"))
        self.valor_aposta = MDTextField(hint_text="Digite o Valor da Sua Aposta")
        self.add_widget(self.valor_aposta)

        #campo das "ODDs"
        self.add_widget(MDLabel(text="ODDs (Respectivamente do: Time A, Time B, Empate):", halign="left"))
        self.odds = MDTextField(hint_text="Ex.: 2.5, 1.8, 3.0")
        self.add_widget(self.odds)

        #campo do "tipo de aposta"
        self.add_widget(MDLabel(text="Tipo de Aposta:", halign="left"))
        self.tipo_aposta = MDTextField(hint_text="Vitória A, Vitória B ou Empate")
        self.add_widget(self.tipo_aposta)

        #botao "calcular"
        self.botao_calcular = MDRaisedButton(text="Calcular Apostas", on_release=self.calcular) #MDRaisedButton - botao interativo  // on_release=self.calcular = quando apertar o botão, calcular
        self.add_widget(self.botao_calcular)

        #resultado do botao calculo
        self.resultado = MDLabel(text="", halign="center", theme_text_color="Secondary")
        self.add_widget(self.resultado)

    #calcular ao apertar o botao
    def calcular(self,instance):
        try: #se algo falhar, ir direto para o codigo 'except'
            time_a=self.time_a.text 
            time_b=self.time_b.text
            valor_aposta=float(self.valor_aposta.text) #pega o numero digitado do valor da aposta em float=numero
            odds_texto = self.odds.text.split(',') #lista, separando os numeros digitados pela virgula
            odd_vitoria_a = float(odds_texto[0].strip()) #organiza cada odd de cada time, usando os numeros respectivamente
            odd_empate = float(odds_texto[1].strip()) #strip remove espaços em branco
            odd_vitoria_b = float(odds_texto[2].strip())
            tipo_aposta=self.tipo_aposta.text

            if tipo_aposta == "Vitória A": #se o tipo de aposta for igual a "vitoria a"
                odd_selecionada = odd_vitoria_a #aparecerá a odd de "vitoria a"
            elif tipo_aposta == "Empate":
                odd_selecionada = odd_empate
            elif tipo_aposta == "Vitória B":
                odd_selecionada = odd_vitoria_b
            else: #se não for nenhum dos 3 tipos de apostas, aparecerá invalido
                self.resultado.text = "Tipo de aposta inválido. Use: Vitória A, Empate ou Vitória B."
                return #retorna a mensagem de erro

            retorno = valor_aposta * odd_selecionada #retornar resultado calculando o valor da aposta multiplicando a odd selecionada
            lucro = retorno - valor_aposta #vai retornar o lucro usando o valor do retorno subtraindo o valor da aposta

            # Exibe os resultados
            resultado_texto = (
                f"Aposta em {time_a} x {time_b} ({tipo_aposta})\n" #aparecerá na tela o texto usando os valores 
                f"Odd Selecionada: {odd_selecionada}\n" #\n "pular pra proxima linha"
                f"Retorno Potencial: R${retorno:.2f}\n"
                f"Lucro Potencial: R${lucro:.2f}" #.2f para mostrar duas casas decimais na tela
            )
            
            self.resultado.text = resultado_texto  
        
        except ValueError: #se try der erro
            self.resultado.text = "Por favor, insira valores válidos."

#mostra o aplicativo com a interface de apostas (abre a janela)
class MeuApp(MDApp): #permite a construção de um aplicativo com KivyMD
    def build(self): #constroi interface do usuario
        return ApostaFutebol() #retorna com os valores da classe 'apostafutebol', criada inicialmente
    
MeuApp().run() #roda 