from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import poisson

#defining normal function
def normal_dis() :
    m_inp = float(input("Insert your mean : "))
    sd_inp = float(input("Insert your standard distribution : "))
    lvl_sig = float(input("Insert your level of significance (in decimal) : "))
    test_value = float(input("Insert your test value : "))
    taburan_normal = norm(loc = m_inp, scale = sd_inp).cdf(test_value)

    if test_value > m_inp :
        prob_oftest = 1 - taburan_normal
        print(prob_oftest)
        if prob_oftest < lvl_sig :
            print("Null hypothesis is rejected")
        elif prob_oftest > lvl_sig :
            print("Null hypothesis is accepted")
        
    elif test_value < m_inp :
        prob_oftest = taburan_normal
        print(prob_oftest)
        if prob_oftest < lvl_sig :            
            print("Null hypothesis is rejected")
        elif prob_oftest > lvl_sig :
            print("Null hypothesis is accepted")

#defining binomial distribution
#need some correction on range
def binomial_dis() :
    
    n_val = int(input("Insert your n values : "))
    p_val = float(input("Insert your p value : "))
    test_value = int(input("Insert your test value (including the last value) : "))
    lvl_sig = float(input("Insert your level of significance (in decimal): "))

    r_values = list(range(test_value + 1))
    dist = [binom.pmf(r, n_val, p_val) for r in r_values]
    print(dist)

    #getting total probability in lower tail
    total_prob = 0
    for i in dist :
        total_prob += i

    if test_value > n_val * p_val :
        prob_oftest = 1 - total_prob
        print(prob_oftest)
        if prob_oftest > lvl_sig :
            print("Null hypothesis is accepted")
        elif prob_oftest < lvl_sig :
            print("Null hypothesis is rejected")

    if test_value < n_val * p_val :
        prob_oftest = total_prob
        print(prob_oftest)
        if prob_oftest > lvl_sig :
            print("Null hypothesis is accepted")
        elif prob_oftest < lvl_sig :
            print("Null hypothesis is rejected")

#defining poisson distribution
def poisson_dis() :
    
    mu_val = float(input("Insert mean : "))
    test_val = int(input("Insert your test value : "))
    lvl_sig = float(input("Insert your level of significance (in decimal) : "))

    if test_val > mu_val :
        prob_oftest = 1 - poisson.cdf(k = test_val - 1, mu = mu_val)
        print(prob_oftest)

        if prob_oftest > lvl_sig :
            print("Null hypothesis is accepted")
        elif prob_oftest < lvl_sig :
            print("Null hypothesis is rejected")

    #error on large values compared to approximation to normal
    elif test_val < mu_val :
        prob_oftest = poisson.cdf(k = test_val, mu = mu_val)
        print(prob_oftest)

        if prob_oftest > lvl_sig :
            print("Null hypothesis is accepted")
        elif prob_oftest < lvl_sig :
            print("Null hypothesis is rejected")

#choose type of distribution
type_dis = input("Type of distribution (N/B/P) : ")

if type_dis == "N" :
    normal_dis()
elif type_dis == "B" :
    binomial_dis()
elif type_dis == "P" :
    poisson_dis()
