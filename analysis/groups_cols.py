abm_dummies = {'policies': ['POLICIES_buy',
                            'POLICIES_rent',
                            'POLICIES_wage',
                            'POLICIES_no_policy'],
               'interest': ['INTEREST_fixed',
                            'INTEREST_real',
                            'INTEREST_nominal'],
               'acps': ['PROCESSING_ACPS_BELO HORIZONTE',
                        'PROCESSING_ACPS_FORTALEZA',
                        'PROCESSING_ACPS_PORTO ALEGRE',
                        'PROCESSING_ACPS_CAMPINAS',
                        'PROCESSING_ACPS_SALVADOR',
                        'PROCESSING_ACPS_RECIFE',
                        'PROCESSING_ACPS_SAO PAULO',
                        'PROCESSING_ACPS_JOINVILLE',
                        'PROCESSING_ACPS_CAMPO GRANDE',
                        'PROCESSING_ACPS_JUNDIAI',
                        'PROCESSING_ACPS_FEIRA DE SANTANA',
                        'PROCESSING_ACPS_IPATINGA',
                        'PROCESSING_ACPS_LONDRINA',
                        'PROCESSING_ACPS_SOROCABA',
                        'PROCESSING_ACPS_JOAO PESSOA',
                        'PROCESSING_ACPS_SAO JOSE DO RIO PRETO',
                        'PROCESSING_ACPS_MACEIO',
                        'PROCESSING_ACPS_SAO JOSE DOS CAMPOS',
                        'PROCESSING_ACPS_ILHEUS - ITABUNA',
                        'PROCESSING_ACPS_SAO LUIS',
                        'PROCESSING_ACPS_UBERLANDIA',
                        'PROCESSING_ACPS_MARINGA',
                        'PROCESSING_ACPS_VITORIA',
                        'PROCESSING_ACPS_CUIABA',
                        'PROCESSING_ACPS_BELEM',
                        'PROCESSING_ACPS_NOVO HAMBURGO - SAO LEOPOLDO',
                        'PROCESSING_ACPS_TERESINA',
                        'PROCESSING_ACPS_MANAUS',
                        'PROCESSING_ACPS_BRASILIA',
                        'PROCESSING_ACPS_ARACAJU',
                        'PROCESSING_ACPS_CAMPINA GRANDE',
                        'PROCESSING_ACPS_CAMPOS DOS GOYTACAZES',
                        'PROCESSING_ACPS_CAXIAS DO SUL',
                        'PROCESSING_ACPS_CRAJUBAR',
                        'PROCESSING_ACPS_CURITIBA',
                        'PROCESSING_ACPS_FLORIANOPOLIS',
                        'PROCESSING_ACPS_GOIANIA',
                        'PROCESSING_ACPS_JUIZ DE FORA',
                        'PROCESSING_ACPS_MACAPA',
                        'PROCESSING_ACPS_NATAL',
                        'PROCESSING_ACPS_PELOTAS - RIO GRANDE',
                        'PROCESSING_ACPS_PETROLINA - JUAZEIRO',
                        'PROCESSING_ACPS_RIBEIRAO PRETO',
                        'PROCESSING_ACPS_RIO DE JANEIRO',
                        'PROCESSING_ACPS_SANTOS',
                        'PROCESSING_ACPS_VOLTA REDONDA - BARRA MANSA'],
               'r_licenses': ['T_LICENSES_PER_REGION_False',
                              'T_LICENSES_PER_REGION_True',
                              'T_LICENSES_PER_REGION_random'],
               'days': ['STARTING_DAY_2000-01-01',
                        'STARTING_DAY_2010-01-01'],
               'r_municipal_fund': ['FPM_DISTRIBUTION_False',
                                    'FPM_DISTRIBUTION_True'],
               'r_metro_fund': ['ALTERNATIVE0_False',
                                'ALTERNATIVE0_True']}

abm_dummies_show = {'POLICIES_buy': 'Policy: buy',
                    'POLICIES_rent': 'Policy: rent',
                    'POLICIES_wage': 'Policy: wage',
                    'POLICIES_no_policy': 'Policy: none',
                    'PROCESSING_ACPS_BELO HORIZONTE': 'Belo Horizonte',
                    'PROCESSING_ACPS_FORTALEZA': 'Fortaleza',
                    'PROCESSING_ACPS_PORTO ALEGRE': 'Porto Alegre',
                    'PROCESSING_ACPS_CAMPINAS': 'Campinas',
                    'PROCESSING_ACPS_SALVADOR': 'Salvador',
                    'PROCESSING_ACPS_RECIFE': 'Recife',
                    'PROCESSING_ACPS_SAO PAULO': 'São Paulo',
                    'PROCESSING_ACPS_JOINVILLE': 'Joinville',
                    'PROCESSING_ACPS_CAMPO GRANDE': 'Campo Grande',
                    'PROCESSING_ACPS_JUNDIAI': 'Jundiai',
                    'PROCESSING_ACPS_FEIRA DE SANTANA': 'Feira de Santana',
                    'PROCESSING_ACPS_IPATINGA': 'Ipatinga',
                    'PROCESSING_ACPS_LONDRINA': 'Londrina',
                    'PROCESSING_ACPS_SOROCABA': 'Sorocaba',
                    'PROCESSING_ACPS_JOAO PESSOA': 'João Pessoa',
                    'PROCESSING_ACPS_SAO JOSE DO RIO PRETO': 'SJRP',
                    'PROCESSING_ACPS_MACEIO': 'Maceio',
                    'PROCESSING_ACPS_SAO JOSE DOS CAMPOS': 'SJC',
                    'PROCESSING_ACPS_ILHEUS - ITABUNA': 'Ilheus-Itabuna',
                    'PROCESSING_ACPS_SAO LUIS': 'Sao Luis',
                    'PROCESSING_ACPS_UBERLANDIA': 'Uberlandia',
                    'PROCESSING_ACPS_MARINGA': 'Maringá',
                    'PROCESSING_ACPS_VITORIA': 'Vitória',
                    'PROCESSING_ACPS_CUIABA': 'Cuiabá',
                    'PROCESSING_ACPS_BELEM': 'Belém',
                    'PROCESSING_ACPS_NOVO HAMBURGO - SAO LEOPOLDO': 'NH-SL',
                    'PROCESSING_ACPS_TERESINA': 'Teresina',
                    'PROCESSING_ACPS_MANAUS': 'Manaus',
                    'PROCESSING_ACPS_BRASILIA': 'Brasília',
                    'T_LICENSES_PER_REGION_False': 'Licenses: False',
                    'T_LICENSES_PER_REGION_True': 'Licenses: True',
                    'T_LICENSES_PER_REGION_random': 'Licenses: Random',
                    'STARTING_DAY_2000-01-01': 'Jan. 2000',
                    'STARTING_DAY_2010-01-01': 'Jan. 2010',
                    'FPM_DISTRIBUTION_False': 'FPM: False',
                    'FPM_DISTRIBUTION_True': 'FPM: True',
                    'ALTERNATIVE0_False': 'Alternative0: False',
                    'ALTERNATIVE0_True': 'Alternative0: True',
                    'INTEREST_fixed': 'Interest: fixed',
                    'INTEREST_real': 'Interest: real',
                    'INTEREST_nominal': 'Interest: nominal',
                    'PROCESSING_ACPS_ARACAJU': 'Aracaju',
                    'PROCESSING_ACPS_CAMPINA GRANDE': 'Campina Grande',
                    'PROCESSING_ACPS_CAMPOS DOS GOYTACAZES': 'Campos',
                    'PROCESSING_ACPS_CAXIAS DO SUL': 'Caxias do Sul',
                    'PROCESSING_ACPS_CRAJUBAR': 'Crato',
                    'PROCESSING_ACPS_CURITIBA': 'Curitiba',
                    'PROCESSING_ACPS_FLORIANOPOLIS': 'Florianópolis',
                    'PROCESSING_ACPS_GOIANIA': 'Goiânia',
                    'PROCESSING_ACPS_JUIZ DE FORA': 'Juiz de Fora',
                    'PROCESSING_ACPS_MACAPA': 'Macapá',
                    'PROCESSING_ACPS_NATAL': 'Natal',
                    'PROCESSING_ACPS_PELOTAS - RIO GRANDE': 'Pelotas',
                    'PROCESSING_ACPS_PETROLINA - JUAZEIRO': 'Petrolina-Juazeiro',
                    'PROCESSING_ACPS_RIBEIRAO PRETO': 'Ribeirão Preto',
                    'PROCESSING_ACPS_RIO DE JANEIRO': 'Rio de Janeiro',
                    'PROCESSING_ACPS_SANTOS': 'Santos',
                    'PROCESSING_ACPS_VOLTA REDONDA - BARRA MANSA': 'Volta Redonda',
                    'all': 'All'}

# 'CONSTRUCTION_ACC_CASH_FLOW',
# 'LOT_COST',
# 'TAX_PROPERTY',
abm_params = ['HIRING_SAMPLE_SIZE',
              'LABOR_MARKET',
              'LOAN_PAYMENT_TO_PERMANENT_INCOME',
              'MARKUP',
              'MAX_LOAN_TO_VALUE',
              'MUNICIPAL_EFFICIENCY_MANAGEMENT',
              'NEIGHBORHOOD_EFFECT',
              'OFFER_SIZE_ON_PRICE',
              'PCT_DISTANCE_HIRING',
              'PERCENTAGE_ACTUAL_POP',
              'PERCENTAGE_ENTERING_ESTATE_MARKET',
              'PERCENT_CONSTRUCTION_FIRMS',
              'POLICY_COEFFICIENT',
              'POLICY_DAYS',
              'POLICY_QUANTILE',
              'PRIVATE_TRANSIT_COST',
              'PRODUCTIVITY_EXPONENT',
              'PRODUCTIVITY_MAGNITUDE_DIVISOR',
              'PUBLIC_TRANSIT_COST',
              'SIZE_MARKET',
              'STICKY_PRICES',
              'TAX_ESTATE_TRANSACTION',
              'TOTAL_DAYS']

abm_params_show = {'HIRING_SAMPLE_SIZE': 'Hiring sample size',
                   'LABOR_MARKET': 'Frequency of firms entering the labor market',
                   'LOAN_PAYMENT_TO_PERMANENT_INCOME': 'Loan/permament income ratio',
                   'MARKUP': 'Markup',
                   'MAX_LOAN_TO_VALUE': 'Maximum Loan-to-Value',
                   'MUNICIPAL_EFFICIENCY_MANAGEMENT': 'Municipal efficiency management',
                   'NEIGHBORHOOD_EFFECT': 'Neighborhood effect',
                   'OFFER_SIZE_ON_PRICE': 'Supply-demand effect on real estate prices',
                   'PCT_DISTANCE_HIRING': '% firms analyzing commuting distance',
                   'PERCENTAGE_ACTUAL_POP': '% of population',
                   'PERCENTAGE_ENTERING_ESTATE_MARKET': '% families entering real estate market',
                   'PERCENT_CONSTRUCTION_FIRMS': '% of construction firms',
                   'POLICY_COEFFICIENT': 'Policy coefficient',
                   'POLICY_DAYS': 'Policy days',
                   'POLICY_QUANTILE': 'Policy Quantile',
                   'PRIVATE_TRANSIT_COST': 'Cost of private transit',
                   'PRODUCTIVITY_EXPONENT': 'Productivity: exponent',
                   'PRODUCTIVITY_MAGNITUDE_DIVISOR': 'Productivity: divisor',
                   'PUBLIC_TRANSIT_COST': 'Cost of public transit',
                   'SIZE_MARKET': 'Perceived market size',
                   'STICKY_PRICES': 'Sticky Prices',
                   'TAX_ESTATE_TRANSACTION': 'Tax over estate transactions',
                   'TOTAL_DAYS': 'Total Days'}
