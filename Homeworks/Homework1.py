
#Explain your work

#Question 1


a = [1, 2, 3, 4, 5, 6]
           #Question 1: How would you define Machine Learning?
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
         #Question 2: What are the differences between Supervised and Unsupervised Learning? Specify example 3 algorithms for each of these.
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
          #Question 3:  What are the test and validation set, and why would you want to use them? 
      '''
      
      the “validation dataset” is predominately used to describe the evaluation of models 
      when tuning hyperparameters and data preparation, and the “test dataset” is predominately used to describe 
      the evaluation of a final tuned model when comparing it to other final models.
      That the notions of “validation dataset” and “test dataset” may disappear when adopting alternate resampling methods like k-fold cross validation, 
      especially when the resampling methods are nested.
      ''',
          #Question 4: What are the main preprocessing steps? Explain them in detail. Why we need to prepare our data?    
      '''
       Data preprocessing in Machine Learning is a crucial step that helps enhance 
       the quality of data to promote the extraction of meaningful insights from the data. 
       Data preprocessing in Machine Learning refers to the technique of preparing (cleaning and organizing) 
       the raw data to make it suitable for a building and training Machine Learning models. 
       In simple words, data preprocessing in Machine Learning is a data mining technique 
       that transforms raw data into an understandable and readable format. 

       Steps in Data Preprocessing in Machine Learning:

       1> Acquire the dataset. 
              To build and develop Machine Learning models, you must first acquire the relevant dataset. This dataset will be comprised of data gathered from multiple and disparate sources which are then combined in a proper format to form a dataset. 
       Dataset formats differ according to use cases. For instance, a business dataset will be entirely different from a medical dataset. While a business dataset will contain relevant industry and business data, a medical dataset will include healthcare-related data.

       2> Import all the crucial libraries. 
                 Since Python is the most extensively used and also the most preferred library by Data Scientists around the world, we’ll show you how to import Python libraries for data preprocessing in Machine Learning. Read more about Python libraries for Data Science here. 
          The predefined Python libraries can perform specific data preprocessing jobs. The three core Python libraries used for this data preprocessing in Machine Learning are:
          NumPy – NumPy is the fundamental package for scientific calculation in Python. Hence, it is used for inserting any type of mathematical operation in the code. Using NumPy, you can also add large multidimensional arrays and matrices in your code. 
          Pandas – Pandas is an excellent open-source Python library for data manipulation and analysis. It is extensively used for importing and managing the datasets. It packs in high-performance, easy-to-use data structures and data analysis tools for Python.
          Matplotlib – Matplotlib is a Python 2D plotting library that is used to plot any type of charts in Python. It can deliver publication-quality figures in numerous hard copy formats and interactive environments across platforms (IPython shells, Jupyter notebook, web application servers, etc.). 

       3> Import the dataset. 
                In this step, you need to import the dataset/s that you have gathered for the ML project at hand. However, before you can import the dataset/s, you must set the current directory as the working directory.
       
       4> Identifying and handling the missing values. 
                 In data preprocessing, it is pivotal to identify and correctly handle the missing values, failing to do this, you might draw inaccurate and faulty conclusions and inferences from the data. Needless to say, this will hamper your ML project. 
                 Basically, there are two ways to handle missing data:

          Deleting a particular row – In this method, you remove a specific row that has a null value for a feature or a particular column where more than 75% of the values are missing. However, this method is not 100% efficient, 
          and it is recommended that you use it only when the dataset has adequate samples. You must ensure that after deleting the data, there remains no addition of bias. 
          Calculating the mean – This method is useful for features having numeric data like age, salary, year, etc. Here, you can calculate the mean, median, or mode of a particular feature or column or row that contains a missing value and replace the result for the missing value. This method can add variance to the dataset, and any loss of data can be efficiently negated. Hence, it yields better results compared to the first method (omission of rows/columns). 
          Another way of approximation is through the deviation of neighbouring values. However, this works best for linear data.
       
       5> Encoding the categorical data. 
               Categorical data refers to the information that has specific categories within the dataset. In the dataset cited above, there are two categorical variables – country and purchased.
           Machine Learning models are primarily based on mathematical equations. 
           Thus, you can intuitively understand that keeping the categorical data in the equation will cause certain issues since you would only need numbers in the equations.

       6> Splitting the dataset. 
                Every dataset for Machine Learning model must be split into two separate sets – training set and test set. data preprocessing Source
            Training set denotes the subset of a dataset that is used for training the machine learning model. Here, you are already aware of the output. A test set, on the other hand, is the subset of the dataset that is used for testing the machine learning model. The ML model uses the test set to predict outcomes. 
            Usually, the dataset is split into 70:30 ratio or 80:20 ratio. This means that you either take 70% or 80% of the data for training the model while leaving out the rest 30% or 20%. The splitting process varies according to the shape and size of the dataset in question.     
       
       7> Feature scaling.
                Feature scaling marks the end of the data preprocessing in Machine Learning. 
          It is a method to standardize the independent variables of a dataset within a specific range. In other words, feature scaling limits the range of variables so that you can compare them on common grounds.    

      ''',
          #Question 5: How you can explore countionus and discrete variables?
      '''
       Continuous Variables would (literally) take forever to count. In fact, you would get to “forever” and never finish counting them. For example, take age. You can’t count “age”. Why not? Because it would literally take forever. For example, you could be:
       25 years, 10 months, 2 days, 5 hours, 4 seconds, 4 milliseconds, 8 nanoseconds, 99 picosends…and so on.
       
       For example, 
       between 62 and 82 inches, there are a lot of possibilities: one participant might be 64.03891 inches tall, and another person might be 72.67025 inches tall. 
       And, there are literally millions of other possible heights between 62 and 82 inches.So, how do you know if you've got a continuous variable? 
       In general, a continuous variable is one that is measured, not counted. Height, for example, is measured. Weight is measured. Temperature, time, distance - all are continuous variables.
        
       Discrete variables are countable in a finite amount of time. For example, you can count the change in your pocket. You can count the money in your bank account. You could also count the amount of money in everyone’s bank accounts. 
       It might take you a long time to count that last item, but the point is—it’s still countable.

       Examples: number of students present

         number of red marbles in a jar
          number of heads when flipping three coins
          students’ grade level

      ''',
         #Question 6: Analyse the plot given below. (What is the plot and variable type, check the distribution and make comment about how you can preproccess it.)
      '''
      Regression is a linear approach for modeling the relationship between two variables. The dependent variable, “y”, is the quantity we would like to predict (in this case, rental price). 
      We predict the dependent variable using the known value of the independent variable, “x”. The goal of simple linear regression is to create a function that takes the independent variable as input and outputs a prediction for the value of the dependent variable.
      ''',]

for i in range(len(b)):
  print("Answer" ,a[i], b[i])

