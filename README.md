# NLP based Poetry Analysis and Recognition
I used bigram and unigram models to train my model. As the result, this program uses two dictionaries which represent the bigram and unigram models.
My training dataset contains three text files include peoms of three persion poets.


## Train
My test dataset contains a mixture of these three poets' poems.
* Ferdowsi: 9000 poems
* Hafez: 7700 poems
* Molavi(Rumi): 8000 poems
I created a class to store the poet's information including their Persian and English names, the address of the train set, a limit (I will explain it later), bigram and unigram models of their poems.
- limit: if limit is set a number greater than 0, the words in the unigram or bigram model which their rpeat is less than that limit will be removed.

## Test 
I used backoff model for decision making.
My test data set contains 2753 peoms.
  * In the test dataset, "1", "2", and "3" represent Ferdowsi, Hazef, and Molavi respectively.  

P(ci|ci−1 )=λ3 P(ci|ci−1 )+ λ2 P(ci)+ λ1 ϵ
* λ1+ λ2+ λ3=1
* 0<ϵ<1

The python function: 
* Test(poets ,lam1 , lam2 , eps , url , realpoet ,wprint = 0)
  - poets = a list of poets
  - lam1 = λ3
  - lam2 = λ2
  - eps = ϵ
  - url = address of test dataset
  - realpoet = a dictionary for checking the result
  - wprint: if = 1 will print the actual and decided peot. if = 0 just the accuracy will be printed.
    #### note: I used Persion to print this part if wprint == 1 for coherency.


## Test Cases
1- λ3 = 0.6, λ2 = 0.2, ϵ = 0.1
Accuracy = 60.756 %

2- λ3 = 0.6, λ2 = 0.2, ϵ = 0.7
Accuracy = 59.811 %

3- λ3 = 0.95, λ2 = 0.005, ϵ = 0.1
Accuracy = 61.737 %

4- λ3 = 0.95, λ2 = 0.005, ϵ = 0.7
Accuracy = 62.282 %
