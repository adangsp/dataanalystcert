//How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
race_count = df['race'].value_counts()

//This will give you a Pandas series race_count with the count of each race in the dataset.
//What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
//This filters the dataset for rows where the sex is 'Male' and calculates the average age using the mean() function.

//What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100
//This filters the dataset for rows where the education is 'Bachelors' and calculates the percentage by dividing the count of such rows by the total number of rows and multiplying by 100.

//What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_higher_education = (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100
//This filters the dataset for rows where the education is 'Bachelors', 'Masters', or 'Doctorate' and calculates the percentage of those rows where the salary is '>50K'.

//What percentage of people without advanced education make more than 50K?
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_lower_education = (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100
//This filters the dataset for rows where the education is not 'Bachelors', 'Masters', or 'Doctorate' and calculates the percentage of those rows where the salary is '>50K'.

//What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()
//This calculates the minimum value of the 'hours-per-week' column.

//What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
percentage_min_workers = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100
//This filters the dataset for rows where the 'hours-per-week' is equal to the minimum number of hours, and then calculates the percentage of those rows where the salary is '>50K'.

