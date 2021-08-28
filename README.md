# Calculating-GPA-and-sorting-GPA-from-csv
In this project, you need to write a program that reads scores of different people from a csv file and performs the following tests on the scores and stores the resulting values in a file.

In this project, you need to implement 5 different tasks. The file sample source.py you need to use for submites is at the bottom of the page (file download option) click on this option to download the file.

 

Do not change the names of the functions in any way and implement all the code you want to hit in the same defs (do not code outside defs except importing libraries that you put at the beginning of the file) (use the mean method only to get average (this method is imported from the statistics library in the file below).) (None of the values are rounded) (All libraries that you want to import only once at the beginning of the file and outside of defs and do not import in defs) and complete the corresponding function for each task, and then make sure to make this file with the name (source.py) and be sure to zip (rar not just zip) and send it.

If you do not comply with any of the above points, unfortunately your score will be zeroed by the system.

Note: The online arbitration system uses Python 3.4, in this version dictionaries do not remember the order of data entry to themselves and may not achieve the desired result if they are sorted, use OrderedDict to fix this problem instead of dict, this data structure can be imported from the collections library in the app.

 

1- Calculate the average of each person and save along with each person's name, the output order of the names must be exactly the same as the order of the input file.

2- Save the GPA in ascending order with each person's name. Please note that if you are using dict, the order of GPA is not clear, please refer to this link for more information. https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries

3- Save the top three GPA with each person's name.

4. Save the bottom three GPA without each person's name.

5- Calculate and save the average averages.

Sample content of a csv file

mandana,5,7,3,15
hamid,3,9,4,20,9,1,8,16,0,5,2,4,7,2,1
sina,19,10,19,6,8,14,3
sara,0,5,20,14
soheila,13,2,5,1,3,10,12,4,13,17,7,7
ali,1,9
sarvin,0,16,16,13,19,2,17,8
 

Tesk 1 Output

mandana,7.5
hamid,6.066666666666666
sina,11.285714285714286
sara,9.75
soheila,7.833333333333333
ali,5.0
sarvin,11.375
 

Tesk II Output

ali,5.0
hamid,6.066666666666666
mandana,7.5
soheila,7.833333333333333
sara,9.75
sina,11.285714285714286
sarvin,11.375
 

Tsk III Output

sarvin,11.375
sina,11.285714285714286
sara,9.75
 

Tesk IV Output

5.0
6.066666666666666
7.5
 

5th Tsk Output

8.401530612244898
 

Note:Note that at each stage, if the average of a few people is the same, the output order must be alphabetical, for example:

hossein 16.5
mona 16.5
