# Python-FIFA-21-players-data-cleaning-
In this project, I will be cleaning a FIFA 21 player's data using Python.
First I will start by importing the essential libraries pandas and numpy.

<img width="146" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/6ff918d2-083a-435b-8153-fbe3e07c46ba">

to start with the cleaning we must first import the file and analyze it to look out for thing that needs to be cleaned. The data has more than 18000 rows and 82 columns.

<img width="383" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/6af42901-de82-41d2-a076-1b1ef35ab1b1">

If we have a look at the Height some data are in cm while others are in each same is with the weight columns some are in kg and some are in pounds.

<img width="266" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/5aa219cf-d658-4dbf-aa8e-d0c427a8cafe">

2
Therefore I will convert the foot inch into cm.

<img width="542" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/9d7cf9f3-92b3-45b6-b430-e772897f224a">

First, I removed the cm and inch(") signs using the replace function, then I created two new columns one is feet(containing the feet number to the right of ('))
and the second is inch(contain the inch value to the left of(')) 
and this is how our data looks like 

<img width="312" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/4b914935-10c6-453b-b97c-a9e9e25e5150">

now to convert feet to cm we must multiply by 30.48 and to convert inch we multiply by 2.54.
However because in the feet column, we have both cm and feet we have to filter only the feet there for i used a conditional filter and took numbers that are less than 10 
(which means it is feet, not cm)

<img width="325" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/9404299e-7de5-4c51-a4bf-bd78179f8b3f">

3
repeat the same processes for the weight column

<img width="525" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/96ac5daa-031b-40f1-88ab-ff1ef5b6fc99">

4
The joined column contains the date month and year we will separate them into different columns 

<img width="427" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/4f79496b-dd28-4e6c-92ce-a6bbeaeafb46">






