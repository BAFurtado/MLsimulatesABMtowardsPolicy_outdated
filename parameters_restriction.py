# MODEL PARAMETERS SPECIFIC RESTRICTIONS
PRODUCTIVITY_EXPONENT = {'max': 1, 'min': 0, 'distribution': 'normal'}
PRODUCTIVITY_MAGNITUDE_DIVISOR = {'max': 20, 'min': 1, 'distribution': 'normal'}
# GENERAL CALIBRATION PARAMETERS
# Order of magnitude parameter of input into municipality investment
MUNICIPAL_EFFICIENCY_MANAGEMENT = {'max': .001, 'min': .00001, 'distribution': 'normal'}
# INTEREST. Choose either: 'nominal', 'real' or 'fixed'. Default 'real'
INTEREST = {'alternatives': ['nominal', 'real', 'fixed'], 'distribution': 'choice'}
# By how much percentage to increase prices
MARKUP = {'max': .5, 'min': 0, 'distribution': 'normal'}
# Frequency firms change prices. Probability > than parameter
STICKY_PRICES = {'max': 1, 'min': 0, 'distribution': 'normal'}
# Number of firms consulted before consumption
SIZE_MARKET = {'max': 100, 'min': 1, 'distribution': 'normal'}
# Frequency firms enter the market
LABOR_MARKET = {'max': 1, 'min': 0, 'distribution': 'normal'}
# Percentage of employees firms hired by distance
PCT_DISTANCE_HIRING = {'max': 1, 'min': 0, 'distribution': 'normal'}
# Ignore unemployment in wage base calculation
WAGE_IGNORE_UNEMPLOYMENT = {'alternatives': [1, 0], 'distribution': 'choice'}
# Candidate sample size for the labor market
HIRING_SAMPLE_SIZE = {'max': 100, 'min': 1, 'distribution': 'normal'}
# TAXES
TAX_CONSUMPTION = {'max': .6, 'min': .1, 'distribution': 'normal'}
TAX_LABOR = {'max': .6, 'min': .01, 'distribution': 'normal'}
TAX_ESTATE_TRANSACTION = {'max': .01, 'min': .0001, 'distribution': 'normal'}
TAX_FIRM = {'max': .6, 'min': .01, 'distribution': 'normal'}
TAX_PROPERTY = {'max': .01, 'min': .0001, 'distribution': 'normal'}
# GOVERNMENT
ALTERNATIVE0 = {'alternatives': [1, 0], 'distribution': 'choice'}
FPM_DISTRIBUTION = {'alternatives': [1, 0], 'distribution': 'choice'}
POLICY_COEFFICIENT = {'max': .4, 'min': 0, 'distribution': 'normal'}
# Policies alternatives may include: 'buy', 'rent' or 'wage' or 'no_policy'. For no policy set to empty strings ''
# POLICY_COEFFICIENT needs to be > 0.
POLICIES = {'alternatives': ['buy', 'rent', 'wage', 'no_policy'], 'distribution': 'choice'}
POLICY_DAYS = {'max': 3600, 'min': 0, 'distribution': 'normal'}
# Size of the poorest families to be helped
POLICY_QUANTILE = {'max': 1, 'min': 0, 'distribution': 'normal'}
# HOUSING AND REAL ESTATE MARKET
# LOANS
# Maximum age of borrower at the end of the contract
MAX_LOAN_AGE = {'max': 100, 'min': 50, 'distribution': 'normal'}
# Used to calculate monthly payment for the families, thus limiting maximum loan by number of months and age
LOAN_PAYMENT_TO_PERMANENT_INCOME = {'max': 1, 'min': 0, 'distribution': 'normal'}
# Refers to the maximum loan monthly payment to total wealth
# MAX_LOAN_PAYMENT_TO_WEALTH=.4
# Refers to the maximum rate of the loan on the value of the estate
MAX_LOAN_TO_VALUE = {'max': 1, 'min': 0, 'distribution': 'normal'}
# This parameter refers to the total amount of resources available at the bank.
MAX_LOAN_BANK_PERCENT = {'max': 1, 'min': 0, 'distribution': 'normal'}
CAPPED_TOP_VALUE = {'max': 2, 'min': 1, 'distribution': 'normal'}
CAPPED_LOW_VALUE = {'max': 1, 'min': 0, 'distribution': 'normal'}
# Influence of vacancy size on house prices
# It can be True or 1 or if construction companies consider vacancy strongly it might be 2 [1 - (vacancy * VALUE)]
OFFER_SIZE_ON_PRICE = {'max': 5, 'min': 0, 'distribution': 'normal'}
# TOO LONG ON THE MARKET:
# value=(1 - MAX_OFFER_DISCOUNT) * e ** (ON_MARKET_DECAY_FACTOR * MONTHS ON MARKET) + MAX_OFFER_DISCOUNT
# AS SUCH (-.02) DECAY OF 1% FIRST MONTH, 10% FIRST YEAR. SET TO 0 TO ELIMINATE EFFECT
ON_MARKET_DECAY_FACTOR = {'max': 0, 'min': -.1, 'distribution': 'normal'}
# LOWER BOUND, THAT IS, AT LEAST 50% PERCENT OF VALUE WILL REMAIN AT END OF PERIOD, IF PARAMETER IS .5
MAX_OFFER_DISCOUNT = {'max': 1, 'min': .4, 'distribution': 'normal'}
# Percentage of households pursuing new location
PERCENTAGE_ENTERING_ESTATE_MARKET = {'max': .01, 'min': 0, 'distribution': 'normal'}
NEIGHBORHOOD_EFFECT = {'max': 5, 'min': 0, 'distribution': 'normal'}

# RENTAL
RENTAL_SHARE = {'max': 1, 'min': 0, 'distribution': 'normal'}
INITIAL_RENTAL_PRICE = {'max': .01, 'min': 0, 'distribution': 'normal'}

# CONSTRUCTION
# LICENSES ARE URBANIZED LOTS AVAILABLE FOR CONSTRUCTION PER NEIGHBORHOOD PER MONTH.
# If random, it will vary between 1 and 0, otherwise an integer
T_LICENSES_PER_REGION = {'alternatives': [1, 0], 'distribution': 'choice'}
PERCENT_CONSTRUCTION_FIRMS = 0.03
# Months that construction firm will divide its income into monthly revenue installments.
# Although prices are accounted for at once.
CONSTRUCTION_ACC_CASH_FLOW = 24
# Cost of lot in PERCENTAGE of construction
LOT_COST = .15

# Families run parameters (on average) for year 2000, or no information. 2010 uses APs average data
MEMBERS_PER_FAMILY = 2.5
# Initial percentage of vacant houses
HOUSE_VACANCY = .1

MARRIAGE_CHECK_PROBABILITY = .034

PRIVATE_TRANSIT_COST = 0.25
PUBLIC_TRANSIT_COST = 0.05

PROCESSING_ACPS = ['BRASILIA']


# selecting the ACPs (Population Concentration Areas)
# ACPs and their STATES - ALL ACPs written in UPPER CASE and without  ACCENT
# STATE    -       ACPs
# ------------------------
# "AM"     -      "MANAUS"
# "PA"     -      "BELEM"
# "AP"     -      "MACAPA"
# "MA"     -      "SAO LUIS", "TERESINA"
# "PI"     -      "TERESINA"
# "CE"     -      "FORTALEZA", "CRAJUBAR" - CRAJUBAR refers to JUAZEIRO DO NORTE - CRATO - BARBALHA
# "RN"     -      "NATAL"
# "PB"     -      "JOAO PESSOA", "CAMPINA GRANDE"
# "PE"     -      "RECIFE", "PETROLINA - JUAZEIRO"
# "AL"     -      "MACEIO"
# "SE"     -      "ARACAJU"
# "BA"     -      "SALVADOR", "FEIRA DE SANTANA", "ILHEUS - ITABUNA", "PETROLINA - JUAZEIRO"
# "MG"     -      "BELO HORIZONTE", "JUIZ DE FORA", "IPATINGA", "UBERLANDIA"
# "ES"     -      "VITORIA"
# "RJ"     -      "VOLTA REDONDA - BARRA MANSA", "RIO DE JANEIRO", "CAMPOS DOS GOYTACAZES"
# "SP"     -      "SAO PAULO", "CAMPINAS", "SOROCABA", "SAO JOSE DO RIO PRETO", "SANTOS", "JUNDIAI",
#                 "SAO JOSE DOS CAMPOS", "RIBEIRAO PRETO"
# "PR"     -      "CURITIBA" "LONDRINA", "MARINGA"
# "SC"     -      "JOINVILLE", "FLORIANOPOLIS"
# "RS"     -      "PORTO ALEGRE", "NOVO HAMBURGO - SAO LEOPOLDO", "CAXIAS DO SUL", "PELOTAS - RIO GRANDE"
# "MS"     -      "CAMPO GRANDE"
# "MT"     -      "CUIABA"
# "GO"     -      "GOIANIA", "BRASILIA"
# "DF"     -      "BRASILIA"

# Percentage of actual population to run the simulation
# Minimum value to run depends on the size of municipality 0,001 is recommended minimum
PERCENTAGE_ACTUAL_POP = 0.01

# Write exactly like the list above

# Selecting the starting year to build the Agents, can be: 1991, 2000 or 2010
STARTING_DAY =