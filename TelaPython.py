from PySimpleGUI import PySimpleGUI as sg

def janela_calc():

    sg.theme('DarkAmber')    
    layout1 = [
        [sg.Text('Volume de alcool ingerido\n(copo = 190ml, shoot = 45ml)'), sg.Input(default_text = '0',key='ci', size=(10,10))],
        [sg.T('')],
        [sg.Text('Teor Alcoolico', justification='center'), sg.Input(default_text = '0',key='ta', size=(10,10))],
        [sg.T('')],
        [sg.Text('Peso', justification='center'), sg.Input(default_text = '0',key='pe',size=(10,10))],
        [sg.T('')],
        [sg.Text('Jejum', justification='center'), sg.Checkbox(text='sim',default=False,key='je')],
        [sg.T('')],
        [sg.Text('Sexo'), sg.Radio('masculino','RADIO1', default=False, key='masc'),sg.Radio('feminino','RADIO1', default=False, key='fem')],    
        [sg.T('')],
        [sg.Button('calcular')],[sg.T('')]
    ]
    
    return sg.Window('Taxa de alcool no sangue', layout1, finalize=True)

def janela_result(resultado, estagio):

    sg.theme('DarkAmber')    
    layout2 = [        
        [sg.Text('Taxa de alcool no sangue: ' + resultado + ' gramas/litro')],
        [sg.T('')],
        [sg.Text('Voce está com: ' + estagio)],
        [sg.T('')],
        [sg.Button('refazer calculo')]
    ]

    return sg.Window('Taxa de alcool no sangue', layout2, finalize = True)

janela1,janela2 = janela_calc(),None

while True:

    
    window, event, valor_calc = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1:      

        estag1 = 'Aumento do ritmo cardíaco e respiratório; diminuição da atenção;\n Comportamento incoerente ao executar tarefas;\n diminuição da capacidade de julgamento e perda de inibição;\n leve sensação de euforia, relaxamento e prazer'
        estag2 = 'Diminuição da atenção, julgamento e controle; reflexos mais lentos;\n dificuldade de coordenação e redução da força muscular;\n redução da capacidade de tomar decisões ou de discernimento sensação crescente de ansiedade e depressão'
        estag3 = 'Reflexos consideravelmente mais lentos; problemas de equilíbrio e movimento alterados;\n alteração de algumas funções visuais; dificuldade na fala;\n vômito, sobretudo se esta alcoolemia for atingida rapidamente'
        estag4 = 'Alterações graves da coordenação motora, com tendência a cambalear e a cair frequentemente;\n estado emocional exagerado (medo, aborrecimentos, aflição);\n distúrbio da sensação e da percepção às cores, formas, movimentos e dimensões;\n debilidade no equilíbrio; incoordenação muscular'
        estag5 = 'Letargia profunda; perda de consciência; estado de sedação comparável ao de uma anestesia cirúrgica'
        estag6 = 'Inconsciência; incontinência urinária e fecal; parada respiratória; morte, em geral provocada por insuficiência respiratória'
        estag0 = 'sobrio'
               
        if event=='calcular':
            try:
                calculo_massa = (int(valor_calc['ci'])*float(valor_calc['ta'])*0.8)/100
                tx_alcoolmia = calculo_massa/float(valor_calc['pe'])*1.1

                if valor_calc['masc'] == False and valor_calc['fem'] == True and valor_calc['je']==True:
                    tx_alcoolmia = calculo_massa/float(valor_calc['pe'])*0.6
                if valor_calc['fem'] == False and valor_calc['masc'] == True and valor_calc['je']==True:
                    tx_alcoolmia = calculo_massa/float(valor_calc['pe'])*0.7 

                if tx_alcoolmia<0.2:
                    janela2 = janela_result(str(round(tx_alcoolmia,2)), estag0)
                    janela1.hide()
                if tx_alcoolmia>0.2 and tx_alcoolmia<=0.5:
                    janela2 = janela_result(str(round(tx_alcoolmia,2)), estag1)
                    janela1.hide()
                if tx_alcoolmia>0.5 and tx_alcoolmia<=1.0:
                    janela2 = janela_result(str(round(tx_alcoolmia,2)), estag2)
                    janela1.hide()
                if tx_alcoolmia>1.0 and tx_alcoolmia<=1.5:
                    janela2 = janela_result(str(round(tx_alcoolmia,2)), estag3)
                    janela1.hide()
                if tx_alcoolmia>1.5 and tx_alcoolmia<=2.9:
                    janela2 = janela_result(str(round(tx_alcoolmia,2)), estag4)
                    janela1.hide()
                if tx_alcoolmia>2.9 and tx_alcoolmia<=3.9:
                    janela2 = janela_result(str(round(tx_alcoolmia,2)), estag5)
                    janela1.hide()
                if tx_alcoolmia>3.9:
                    janela2 = janela_result(str(round(tx_alcoolmia,2)), estag6)
                    janela1.hide()
            except:
                sg.PopupError( 'Digite um valor diferente de 0',title= 'Erro')

    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == 'refazer calculo':
        janela2.close()
        janela1.un_hide()
