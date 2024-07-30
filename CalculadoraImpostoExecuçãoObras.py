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
        pis =   Total* 0.0065
        cofins = Total *0.03

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
