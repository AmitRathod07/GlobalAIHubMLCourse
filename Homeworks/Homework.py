print(fontsize="24" + 'Homework1')

a = [1, 2, 3, 4, 5, 6]
b = [''' -Machine Learning is an Application of Artificial Intelligence (AI) it gives devices the ability to 
      learn from their experiences and improve their self without doing any coding. For Example, 
      when you shop from any website it’s shows related search like:- People who bought also saw this.

        -Machine Learning is a subset of Artificial Intelligence. Machine Learning is 
      the study of making machines more human-like in their behaviour and decisions by giving them the ability to 
      learn and develop their own programs. This is done with minimum human intervention, 

       i.e., no explicit programming. The learning process is automated and improved based on 
      the experiences of the machines throughout the process. Good quality data is fed to the machines, 
      and different algorithms are used to build ML models to train the machines on this data. 
      The choice of algorithm depends on the type of data at hand, 
      and the type of activity that needs to be automated.
      ''', 

      '''
      #   ** Supervised learning **
 
     1] Supervised learning as the name indicates the presence of a supervisor as a teacher. 
     Basically supervised learning is a learning in which we teach or train the machine using data which is well labeled that means some data is already tagged with 
     the correct answer. After that, the machine is provided with a new set of examples(data) so that supervised learning algorithm analyses 
     the training data(set of training examples) and produces a correct outcome from labeled data. 
     
     2] Supervised learning classified into two categories of algorithms: 

   1.Classification: A classification problem is when the output variable is a category, such as “Red” or “blue” or “disease” and “no disease”.
   2.Regression: A regression problem is when the output variable is a real value, such as “dollars” or “weight”.
     
    3] Supervised learning deals with or learns with “labeled” data.Which implies that some data is already tagged with the correct answer.
    
     Types:-

         1)ression
         2)Logistic Regression
         3)Classification
         4)Naive Bayes Classifiers
         5)K-NN (k nearest neighbors)
         6)Decision Trees
         7)Support Vector Machine
    4]
Advantages:-

1. Supervised learning allows collecting data and produce  data output from the previous experiences.
2. Helps to optimize performance criteria with the help of experience.
3. Supervised machine learning helps to solve various types of real-world computation problems.


Disadvantages:-

1. Classifying big data can be challenging.
2. Training for supervised learning needs a lot of computation time.So,it requires a lot of time.
 

1) How would you define Machine Learning?
4) What are the main preprocessing steps? Explain them in detail. Why we need to prepare our data?
5) How you can explore countionus and discrete variables?
6) Analyse the plot given below. (What is the plot and variable type, check the distribution and make comment about how you can preproccess it.)


  ** Unsupervised Learning **
  
     1] Unsupervised learning is the training of machine using information that is neither classified nor labeled and allowing 
     the algorithm to act on that information without guidance. Here the task of machine is to group unsorted information according to 
     similarities, patterns and differences without any prior training of data. 

     Unlike supervised learning, no teacher is provided that means no training will be given to the machine. 
     Therefore machine is restricted to find the hidden structure in unlabeled data by our-self. 
     
     
    2] Unsupervised learning classified into two categories of algorithms: 
         > Clustering: A clustering problem is where you want to discover the inherent groupings in the data, such as grouping customers by purchasing behavior.
         > Association: An association rule learning problem is where you want to discover rules that describe large portions of your data, 
           such as people that buy X also tend to buy Y.
           
    3] Types of Unsupervised Learning:-
         
         Clustering
         >Exclusive (partitioning)
         >Agglomerative
         >Overlapping
         >Probabilistic 

          Clustering Types:-
              >Hierarchical clustering
              >K-means clustering
              >Principal Component Analysis
              >Singular Value Decomposition
              >Independent Component Analysis
      ''', 

      '''
      
      the “validation dataset” is predominately used to describe the evaluation of models 
      when tuning hyperparameters and data preparation, and the “test dataset” is predominately used to describe 
      the evaluation of a final tuned model when comparing it to other final models.
      That the notions of “validation dataset” and “test dataset” may disappear when adopting alternate resampling methods like k-fold cross validation, 
      especially when the resampling methods are nested.
      ''',

      '''
       
      ''']

for i in range(len(b)):
  print("Answer" ,a[i], b[i])
