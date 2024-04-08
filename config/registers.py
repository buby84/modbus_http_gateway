regs = {
    #GRUPPO:: dati generali
    4513 : {
        'group' : 0,
        'plcaddr' : 'MW4531',
        'tag' : 'HMI_Imp_Num_Programma_I',
        'descrizione' : 'Numero Programma',
    },
    4611 : {
        'group' : 0,
        'plcaddr' : 'MW4611',
        'tag' : 'HMI_ImpSetup_Conta_Ore_I',
        'descrizione' : 'Conta Ore',
        'log' : False,
        'display' : False,
        'valuetype' : 'time',
    },
    4610 : {
        'group' : 0,
        'plcaddr' : 'MW4610',
        'tag' : 'HMI_ImpSetup_Conta_Minuti_I',
        'descrizione' : 'Conta Minuti',
        'log' : False,
        'display' : False,
    },    
    4555 : {
        'group' : 0,
        'plcaddr' : 'MW4555',
        'tag' : 'HMI_Imp_Stato_I',
        'descrizione' : 'Stato Macchina',
        'values' :{
            0 : "Emergenza",
            1 : "Stop",
            2 : "Start",
            3 : "Con. Linea Off",
            7 : "Energy save Time 1 e 2 (velocità minima e arresto motori) attivi",
        },
        'valueDisplay' : "custom",
    },
    4517 : {
        'group' : 0,
        'plcaddr' : 'MW4517',
        'tag' : 'HMI_Imp_VelAvanz_Set_I',
        'descrizione' : 'Velocità Avanzamento Impostata [m/min/10]',
        'log' : False
    },   
    4501 : {
        'group' : 0,
        'plcaddr' : 'MX9000',
        'tag' : 'HMI_Imp_Abl_Avanzamento_X',
        'descrizione' : 'Abilitazione Avanzamento',
        'valueDisplay' : "toggle_gray_green",
        'log' : True,
    },   
    4500 : { #44501
        'group' : 0,
        'plcaddr' : 'MX9100',
        'valuetype' : 'multibit',
        'display' : False,
        'log' : False,
    },   
    20100 : {
        'group' : 0,
        'plcaddr' : 'MX20100',
        'valuetype' : 'multibit',
        'display' : False,
        'log' : False,
    },    
    20110 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_0',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    },  
    20111 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_1',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    },  
    20112 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_2',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    },  
    20113 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_3',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    }, 
    20114 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_4',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    },    
    20115 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_5',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    },    
    20116 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_6',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    },    
    20117 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_7',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    },    
    20118 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_8',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    }, 
    20119 : {
        'group' : 0,
        'plcaddr' : 'MW20110',
        'valuetype' : 'char',
        'tag' : 'MesData.sBarcodeRx_9',
        'descrizione' : 'Codice del prodotto in lavorazione',
        'display' : False,
        'log' : True,
    }, 
    8033 : {
        'group' : 0,
        'plcaddr' : 'MW8033',
        'tag' : 'I_Minuti_Produzione',
        'descrizione' : 'Minuti in lavorazione',
        'log' : False,
        'display' : False,
        'valuetype' : 'time',
    },
    8034 : {
        'group' : 0,
        'plcaddr' : 'MW8034',
        'tag' : 'I_Ore_Produzione',
        'descrizione' : 'Ore in lavorazione',
        'log' : False,
        'display' : False
    },   
    #FINE GRUPPO

    #GRUPPO:: macchina    
    4308 : {
        'group' : 1,
        'plcaddr' : 'MW4308',
        'tag' : 'Presenza_Pezzo_I',
        'descrizione' : 'Stato del sensore in entrata macchina per presenza pezzo',
        'values' :{
            0 : "Nessuna Funzione",
            1 : "Presenza Pezzo",
            2 : "Eccesso Spessore",
        },
    },   
    4360 : {
        'group' : 1,
        'plcaddr' : 'MD2180',
        'tag' : 'SollAct_DI',
        'descrizione' : 'Sollevamento Spessore Attuale [mm/100]'
    }, 
    4361 : {
        'group' : 1,
        'plcaddr' : 'MD2180',
        'tag' : 'SollAct_DI',
        'descrizione' : 'Sollevamento Spessore Attuale [mm/100]'
    },     
    4364 : {
        'group' : 1,
        'plcaddr' : 'MD2182',
        'tag' : 'SollSet_DI',
        'descrizione' : 'Sollevamento Spessore Impostato [mm/100]'
    },   
    4365 : {
        'group' : 1,
        'plcaddr' : 'MD2182',
        'tag' : 'SollSet_DI',
        'descrizione' : 'Sollevamento Spessore Impostato [mm/100]'
    },     
    4300 : {
        'group' : 1,
        'plcaddr' : 'MX8600',
        'valuetype' : 'multibit',
        'display' : False,
        'log' : False,
    },     
    4352 : {
        'group' : 1,
        'plcaddr' : 'MD2176',
        'tag' : 'Allarmi_DW ',
        'descrizione' : 'Allarmi',
        'display' : False,
        'log' : False,
    },     
    4353 : {
        'group' : 1,
        'plcaddr' : 'MD2176',
        'tag' : 'Allarmi_DW ',
        'descrizione' : 'Allarmi',
        'display' : False,
        'log' : False,
    },           
    4362 : {
        'group' : 1,
        'plcaddr' : 'MW4362',
        'tag' : 'VelAvanz_Act_I ',
        'descrizione' : 'Velocita Avanzamento Attuale [m/min/10]'
    }, 
    #FINE GRUPPO

    #GRUPPO:: Gr1      
    2500 : {
        'group' : 2,
        'plcaddr' : 'MX5000',
        'valuetype' : 'multibit',
        'display' : False,
        'log' : False,
    },   
    2502 : {
        'group' : 2,
        'plcaddr' : 'MW2502',
        'tag' : 'Gr1_Grana ',
        'descrizione' : 'Grana del nastro abrasivo / altezza spazzola attualmente selezionata'
    }, 
    2529 : {
        'group' : 2,
        'plcaddr' : 'MW2529',
        'tag' : 'Gr1_GritSetAct_I ',
        'descrizione' : 'Grit-Set (posizione del gruppo di lavoro) (posizione del gruppo di lavoro) Attuale'
    },         
    2510 : {
        'group' : 2,
        'plcaddr' : 'MW2510',
        'tag' : 'Gr1_GritSetSet_I ',
        'descrizione' : 'Grit-Set (posizione del gruppo di lavoro) Impostato'
    },                 
    2527 : {
        'group' : 2,
        'plcaddr' : 'MW2527',
        'tag' : 'Gr1_Stato_I ',
        'descrizione' : 'Stato Gruppo',
        'values' :{
            0 : "Rosso",
            1 : "Verde",
            2 : "Verde Soffiatori",
            4 : "Giallo"
        },
    },         
    2528 : {
        'group' : 2,
        'plcaddr' : 'MW2528',
        'tag' : 'Gr1_GruppoVelAct_I ',
        'descrizione' : 'Velocità attulale del gruppo (calcolata)'
    },                 
    2505 : {
        'group' : 2,
        'plcaddr' : 'MW2505',
        'tag' : 'Gr1_GruppoRefSet_I ',
        'descrizione' : 'Velocità impostata del gruppo'
    },     
    2526 : {
        'group' : 2,
        'plcaddr' : 'MW2526',
        'valuetype' : 'multibit',
        'descrizione' : 'Allarmi',
        'tag' : 'Gr1_Allarmi_W ',
        'display' : False,
        'log' : False,
    },         
    #FINE GRUPPO


    #GRUPPO:: Gr2      
    2600 : {
        'group' : 3,
        'plcaddr' : 'MX5200',
        'valuetype' : 'multibit',
        'display' : False,
        'log' : False,
    },   
    2602 : {
        'group' : 3,
        'plcaddr' : 'MW2602',
        'tag' : 'Gr2_Grana ',
        'descrizione' : 'Grana del nastro abrasivo / altezza spazzola attualmente selezionata'
    }, 
    2629 : {
        'group' : 3,
        'plcaddr' : 'MW2629',
        'tag' : 'Gr2_GritSetAct_I ',
        'descrizione' : 'Grit-Set (posizione del gruppo di lavoro) (posizione del gruppo di lavoro) Attuale'
    },         
    2610 : {
        'group' : 3,
        'plcaddr' : 'MW2610',
        'tag' : 'Gr2_GritSetSet_I ',
        'descrizione' : 'Grit-Set (posizione del gruppo di lavoro) Impostato'
    },                 
    2627 : {
        'group' : 3,
        'plcaddr' : 'MW2627',
        'tag' : 'Gr2_Stato_I ',
        'descrizione' : 'Stato Gruppo',
        'values' :{
            0 : "Rosso",
            1 : "Verde",
            2 : "Verde Soffiatori",
            4 : "Giallo"
        },
    },         
    2628 : {
        'group' : 3,
        'plcaddr' : 'MW2628',
        'tag' : 'Gr2_GruppoVelAct_I ',
        'descrizione' : 'Velocità attulale del gruppo (calcolata)'
    },                 
    2605 : {
        'group' : 3,
        'plcaddr' : 'MW2605',
        'tag' : 'Gr2_GruppoRefSet_I ',
        'descrizione' : 'Velocità impostata del gruppo'
    },     
    2626 : {
        'group' : 3,
        'plcaddr' : 'MW2626',
        'valuetype' : 'multibit',
        'descrizione' : 'Allarmi',
        'tag' : 'Gr2_Allarmi_W ',
        'display' : False,
        'log' : False,
    },         
    #FINE GRUPPO

    #GRUPPO:: Gr3      
    2700 : {
        'group' : 4,
        'plcaddr' : 'MX5400',
        'valuetype' : 'multibit',
        'display' : False,
        'log' : False,
    },   
    2702 : {
        'group' : 4,
        'plcaddr' : 'MW2702',
        'tag' : 'Gr3_Grana ',
        'descrizione' : 'Grana del nastro abrasivo / altezza spazzola attualmente selezionata'
    }, 
    2729 : {
        'group' : 4,
        'plcaddr' : 'MW2729',
        'tag' : 'Gr3_GritSetAct_I ',
        'descrizione' : 'Grit-Set (posizione del gruppo di lavoro) (posizione del gruppo di lavoro) Attuale'
    },         
    2710 : {
        'group' : 4,
        'plcaddr' : 'MW2710',
        'tag' : 'Gr3_GritSetSet_I ',   
        'descrizione' : 'Grit-Set (posizione del gruppo di lavoro) Impostato'
    },                 
    2727 : {
        'group' : 4,
        'plcaddr' : 'MW2727',
        'tag' : 'Gr3_Stato_I ',
        'descrizione' : 'Stato Gruppo',
        'values' :{
            0 : "Rosso",
            1 : "Verde",
            2 : "Verde Soffiatori",
            4 : "Giallo"
        },
    },         
    2728 : {
        'group' : 4,
        'plcaddr' : 'MW2728',
        'tag' : 'Gr3_GruppoVelAct_I ',
        'descrizione' : 'Velocità attulale del gruppo (calcolata)'
    },                 
    2705 : {
        'group' : 4,
        'plcaddr' : 'MW2705',
        'tag' : 'Gr3_GruppoRefSet_I ',
        'descrizione' : 'Velocità impostata del gruppo'
    },     
    2726 : {
        'group' : 4,
        'plcaddr' : 'MW2726',
        'valuetype' : 'multibit',
        'descrizione' : 'Allarmi',
        'tag' : 'Gr3_Allarmi_W ',
        'display' : False,
        'log' : False,
    },         
    #FINE GRUPPO
    

}