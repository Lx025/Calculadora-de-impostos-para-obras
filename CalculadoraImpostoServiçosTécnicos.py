import tkinter as tk
from tkinter import messagebox

def calcular_impostos():
    try:
        valorVendas = float(entry_valorVendas.get())
        valorMateriais = float(entry_valorMateriais.get())
        valor_MDO = float(entry_valor_MDO.get())

        # Total
        Total = valorVendas

        # Calcular o ISS
        iss = (Total - (valorMateriais*0.70)) * 0.05
        
        # Calcular PIS e Cofins no regime cumulativo
        pis =   (Total-(valorMateriais*0.7)) * 0.0165
        cofins = (Total-(valorMateriais*0.7)) * 0.0760

        Total_Custo = valorMateriais + valor_MDO
        
        # Lucro Bruto
        lucro_bruto = Total - Total_Custo - iss - pis - cofins - (Total * 0.18)
        
        # Calcular IRPJ
        if lucro_bruto > 60000:
            irpj = (lucro_bruto * 0.15) + ((lucro_bruto - 60000) * 0.10)
        else:
            irpj = lucro_bruto * 0.15
        
        # Calcular CSLL
        csll = lucro_bruto * 0.09
        
        # Lucro Líquido
        lucro_liquido = lucro_bruto - irpj - csll
        
        # Total de impostos
        Total_impostos = iss + pis + cofins + irpj + csll
        
        # Percentual de Impostos
        percentualImposto = (Total_impostos / valorVendas) * 100
        
        # Resultados
        resultados = {
            "ISS": iss,
            "PIS": pis,
            "Cofins": cofins,
            "IRPJ": irpj,
            "CSLL": csll,
            "Total de Impostos": Total_impostos,
            "Percentual de Impostos (%)": percentualImposto,
        }
        
        # Texto explicativo
        texto = (
            "Cálculo de impostos de serviços técnicos (Projeto - Gerenciamento - Laudos) - NF 1520\n"
            "Cálculo dos impostos considerando:\n"
            "- Dedução dos materiais no ISS\n"
            "- PIS e COFINS no regime cumulativo (1,65% e 7,60%) respectivamente\n"
        )
        
        # Exibir resultados
        resultado_texto = "\n".join([f"{imposto}: R$ {valor:.2f}" if "Percentual" not in imposto else f"{imposto}: {valor:.2f}%" for imposto, valor in resultados.items()])
        messagebox.showinfo("Resultados dos Impostos", texto + "\n" + resultado_texto)
        
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira valores numéricos válidos.")

# Configurar a janela principal
root = tk.Tk()
root.title("Calculadora de Impostos")

# Criar os widgets
label_valorVendas = tk.Label(root, text="Valor das Vendas:")
label_valorVendas.grid(row=0, column=0, padx=10, pady=10)
entry_valorVendas = tk.Entry(root)
entry_valorVendas.grid(row=0, column=1, padx=10, pady=10)

label_valorMateriais = tk.Label(root, text="Valor dos Materiais:")
label_valorMateriais.grid(row=1, column=0, padx=10, pady=10)
entry_valorMateriais = tk.Entry(root)
entry_valorMateriais.grid(row=1, column=1, padx=10, pady=10)

label_valor_MDO = tk.Label(root, text="Valor da Mão de Obra:")
label_valor_MDO.grid(row=2, column=0, padx=10, pady=10)
entry_valor_MDO = tk.Entry(root)
entry_valor_MDO.grid(row=2, column=1, padx=10, pady=10)

botao_calcular = tk.Button(root, text="Calcular", command=calcular_impostos)
botao_calcular.grid(row=3, columnspan=2, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
