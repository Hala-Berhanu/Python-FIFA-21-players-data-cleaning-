# Python-FIFA-21-players-data-cleaning-
In this project, my focus is on refining FIFA 21 player data through Python. I'll employ various data cleansing techniques, including but not limited to eliminating redundant white spaces, standardizing units within columns, splitting values, handling NaN values by replacing them with zeros, and more.

To kick off the process, I'll begin by importing the crucial libraries, namely pandas and numpy.

<img width="146" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/6ff918d2-083a-435b-8153-fbe3e07c46ba">

To initiate the cleaning process, our first step involves importing and analyzing the file to identify areas in need of attention. The dataset comprises over 18,000 rows and spans 82 columns, necessitating a thorough examination to pinpoint elements requiring cleaning.

<img width="383" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/6af42901-de82-41d2-a076-1b1ef35ab1b1">

1
The initial cleaning step will focus on the "Club" column 

<img width="167" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/da3b9b79-a5bd-4bc5-9856-ec9d1a1beefd">

which contains superfluous white spaces. Consequently, I'll proceed to eliminate these unnecessary spaces.

<img width="356" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/98b41e68-d635-41e4-a8aa-61f14e9821f7">


2
Upon reviewing the "Height" column, it's evident that the data includes measurements in both centimeters and inches. Similarly, the "Weight" column exhibits entries in both kilograms and pounds. To address this inconsistency, I will standardize the units in both columns for uniformity.

<img width="266" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/5aa219cf-d658-4dbf-aa8e-d0c427a8cafe">



Henceforth, I will convert the height values expressed in feet and inches to centimeters for uniformity across the dataset.

<img width="542" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/9d7cf9f3-92b3-45b6-b430-e772897f224a">

In the initial steps, I utilized the replace function to eliminate the "cm" and inch (") signs. Subsequently, I introduced two new columns: "feet," which captures the feet value to the right of the (') symbol, and "inch," which records the inch value to the left of the (') symbol. Here's an overview of our updated dataset.

<img width="312" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/4b914935-10c6-453b-b97c-a9e9e25e5150">

To convert the "feet" values to centimeters, a multiplication by 30.48 is applied. Simultaneously, the "inch" values are converted by multiplying them by 2.54. To ensure accuracy in the conversion, a conditional filter is employed. Specifically, values less than 10 are considered as feet, distinguishing them from centimeters. This meticulous approach ensures a precise conversion for both columns.

<img width="325" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/9404299e-7de5-4c51-a4bf-bd78179f8b3f">

3
repeat the same processes for the "weight" column

<img width="525" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/96ac5daa-031b-40f1-88ab-ff1ef5b6fc99">

4
The "Joined" column currently encompasses the date, month, and year. To enhance clarity and facilitate analysis, I will partition this column into distinct ones for date, month, and year, providing a more granular breakdown of the temporal information within the dataset.

<img width="151" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/385d09c3-746a-4d5c-a3f0-57aa7ba3a313">


<img width="427" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/4f79496b-dd28-4e6c-92ce-a6bbeaeafb46">

And the result looks like this.

<img width="94" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/02f634be-9f54-436e-badd-dc8fc675ccfc">

renaming some columns

<img width="704" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/d7a73c19-4248-45ab-a670-c806ecc770a6">


5
Upon examination of both the "Value_in_M" and "Release Clause_in_M" columns, it's apparent that certain values are expressed in millions, while others are in kilos. To ensure uniformity, I will standardize these units to be consistent across both columns.

<img width="259" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/542c23f2-b1ce-4193-b913-d5bee14c6096">


To initiate the process, I will address the "Value_in_M" column, leveraging NumPy to convert the values into millions. Subsequently, I will replicate this procedure for the "Release Clause_in_M" column, ensuring both columns uniformly express their values in millions.

<img width="536" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/0a1a5377-3a03-43f6-82e8-e2b2bfd62e35">

<img width="626" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/cfaadecb-0cb6-4cfd-b27c-aad49b97034a">

and this is the result for both columns 

<img width="271" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/f2fd83a7-68e0-490f-a4f1-90f9e8e4320d">

6
The "Hits" column exhibits NaN values, indicating a lack of data, which implies zero hits. To rectify this, I will replace these NaN values with zeros, ensuring a comprehensive and accurate representation of the dataset.

<img width="77" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/6e94a781-4114-4b83-92c8-efe910d1619c">

Therefore I will replace them with Zero

<img width="215" alt="image" src="https://github.com/Hala-Berhanu/Python-FIFA-21-players-data-cleaning-/assets/71036477/73485c34-d571-466e-8eac-9318253d22b8">














