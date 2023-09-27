# Simulation-Project
###
A car insurance expert center is working every day from 8 am to 6 pm. The door of the center is closed at 6:00 p.m. and only the cars that are inside the center until that moment are served until the system is empty. After the end of the working hours of the center every day, if there is a queue outside the premises, it will also disappear. In order to investigate and carry out the necessary measures, both cars (culprit and plaintiff) must be present at the same time. If one of the cars entered before the closing of the center, the second car can also enter after 6 pm. Distribution The arrival of clients is a function of snowfall and rain and the time period of arrival. Historical data shows that the distribution of arrival of clients is different in the hours of 8 to 10, 10 to 10, 13 to 15, and 15 to 18.

After entering the insurance center, if the cars are entered as a pair (culprit and plaintiff), if there is capacity, they will immediately enter the queue for taking photos. from a pair of cars follows an exponential distribution with a mean of 6 minutes. The queue of the photo booth has a limited capacity of 40 cars (20 pairs of cars) and if the queue capacity is full, the cars must wait outside the insurance area until the queue capacity is reached. be empty for them. Based on historical data, 30% of the clients arrive at the insurance center individually and have to wait for the second car. If these clients have the possibility to enter the queue of the photo taking area inside the area, according to the insurance law First, they are transferred to the waiting parking area. After the arrival of the second car, to enter the photo queue inside the area, these cars have priority over the cars outside the photo area. If a single car enters the queue outside the area and until the second car arrives, the second car will be added to the queue outside the area right behind the first car. The waiting time of a single car until its pair arrives follows an exponential distribution with an average of 30 minutes.

After the end of taking photos, the cars enter the filing department. The distance from each section to another section is assumed to be insignificant. In this part, 3 experts are working with triangular serving distribution with minimum, average and maximum of 5, 6 and 7 minutes respectively. After the end of the filing stage, the cars enter the expert queue, where 2 experts serve with an exponential distribution with an average of 9 minutes. After the examination, the review process will be different depending on whether the clients intend to file a complaint or not. If the cars do not intend to file a complaint, after the expert stage, they must enter the filing section again and complete the file. In this section, the cars that complete the case have priority over the cases that are filed. The case completion time in the second part follows a 1D probability distribution. Based on historical data, 10% of the clients of this center complain. For this purpose, after the expert stage, the cars enter the complaint registration department, where an expert is working. The duration of handling complaints has an exponential distribution with an average of 15 minutes. After filing the complaint, the cars must go through expert procedures again and then complete the case. (The service distribution of these two departments will not be different for the clients who come from the complaint registration.) Finally, after completing the case, the cars will leave the insurance center.

