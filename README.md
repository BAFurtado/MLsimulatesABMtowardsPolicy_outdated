# Outdated
## Machine Learning simulates Agent-based Model towards Policy-Making

https://arxiv.org/abs/2203.02576

### Proposed scheme:

![](/home/furtado/MyModels/MLsimulatesABMtowardsPolicy/text/text_images/Model_Figure_proposal.drawio.png)

### Results

![](/home/furtado/MyModels/MLsimulatesABMtowardsPolicy/text/text_images/graph_sorted_POLICIES_no_policy.png)

## Previously:
Presented at inverse Generative Social Sciences Workshop **iGSS**. 

### https://www.igss-workshop.org/abstracts#furtado

This is a development of an initial attempt, available here:
https://arxiv.org/abs/1712.04429v2 based on a new, more complete version of PolicySpace2.

Code: https://github.com/BAFurtado/PolicySpace2

Initial documentation in English: https://arxiv.org/abs/2102.11929 

### Requires:

````angular2html
numpy pandas
````

The program:

1. Reads output from an ABM model and its parameters' configuration
2. Creates a socioeconomic optimal output based on two ABM results of the modelers choice
3. Organizes the data as X and Y matrices
4. Trains some Machine Learning algorithms
5. Generates random configuration of parameters based on the mean and standard deviation of the original parameters
6. Apply the trained ML algorithms to the set of randomly generated data
7. Outputs the mean and values for the actual data, the randomly generated data and the optimal and non-optimal cases

The original database from which the 232 samples of the actual data is read is large (60.7 GB)
Thus, some pre-processed data for some pairs of optimal cases are also made available

## Running the program
`python main.py`

Output will be produced at the pre_processed folder

You may change the parameters for the targets at main.py

Or you may change the parameters of the ML in machines.py

Or the size of the sample at generating_random_conf.py

### Rules (configured by parameters)
1. PCT_DISTANCE_HIRING
2. WAGE_IGNORE_UNEMPLOYMENT
3. ALTERNATIVE0 
4. FPM_DISTRIBUTION 
5. POLICIES (most outstanding result)
6. OFFER_SIZE_ON_PRICE
7. ON_MARKET_DECAY_FACTOR ** (not enough data on runs)
8. NEIGHBORHOOD_EFFECT

### Parameters
1. PRODUCTIVITY_EXPONENT
2. PRODUCTIVITY_MAGNITUDE_DIVISOR 
3. MUNICIPAL_EFFICIENCY_MANAGEMENT
4. INTEREST
5. MARKUP
6. STICKY_PRICES
7. SIZE_MARKET
8. LABOR_MARKET
9. HIRING_SAMPLE_SIZE
10. TAX_CONSUMPTION
11. TAX_LABOR 
12. TAX_ESTATE_TRANSACTION 
13. TAX_FIRM 
14. TAX_PROPERTY 
15. POLICY_COEFFICIENT
16. POLICY_DAYS
17. POLICY_QUANTILE
18. MAX_LOAN_AGE
19. LOAN_PAYMENT_TO_PERMANENT_INCOME
20. MAX_LOAN_TO_VALUE
21. MAX_LOAN_BANK_PERCENT
22. CAPPED_TOP_VALUE 
23. CAPPED_LOW_VALUE 
24. PERCENTAGE_ENTERING_ESTATE_MARKET
25. MAX_OFFER_DISCOUNT
26. RENTAL_SHARE 
27. INITIAL_RENTAL_PRICE
28. T_LICENSES_PER_REGION
29. PERCENT_CONSTRUCTION_FIRMS 
30. CONSTRUCTION_ACC_CASH_FLOW
31. LOT_COST 
32. MARRIAGE_CHECK_PROBABILITY 
33. PRIVATE_TRANSIT_COST
34. PUBLIC_TRANSIT_COST 
35. PERCENTAGE_ACTUAL_POP  
36. PROCESSING_ACPS 
37. STARTING_DAY 

#### Note.

### Tentative only
To include validation.
1. X -> omitted_rule = 0
2. X -> One more row in X for each city with observed values (Y) por higher GDP and smaller inequality
3. Train
4. Observe output in predicted for omitted_rule


### To remember
    Windows 64-bit packages of scikit-learn can be accelerated using scikit-learn-intelex.
    More details are available here: https://intel.github.io/scikit-learn-intelex

    For example:

        $ conda install scikit-learn-intelex
        $ python -m sklearnex my_application.py
