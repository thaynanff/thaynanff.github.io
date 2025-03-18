# Medical Data Visualizer

We will be working on this project with our Replit starter code.

In this project, we will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

## Data description

The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. We will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

File name: medical_examination.csv

<table>
<thead>
<tr>
<th align="center">Feature</th>
<th align="center">Variable Type</th>
<th align="center">Variable</th>
<th align="center">Value Type</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Age</td>
<td align="center">Objective Feature</td>
<td align="center"><code>age</code></td>
<td align="center">int (days)</td>
</tr>
<tr>
<td align="center">Height</td>
<td align="center">Objective Feature</td>
<td align="center"><code>height</code></td>
<td align="center">int (cm)</td>
</tr>
<tr>
<td align="center">Weight</td>
<td align="center">Objective Feature</td>
<td align="center"><code>weight</code></td>
<td align="center">float (kg)</td>
</tr>
<tr>
<td align="center">Gender</td>
<td align="center">Objective Feature</td>
<td align="center"><code>gender</code></td>
<td align="center">categorical code</td>
</tr>
<tr>
<td align="center">Systolic blood pressure</td>
<td align="center">Examination Feature</td>
<td align="center"><code>ap_hi</code></td>
<td align="center">int</td>
</tr>
<tr>
<td align="center">Diastolic blood pressure</td>
<td align="center">Examination Feature</td>
<td align="center"><code>ap_lo</code></td>
<td align="center">int</td>
</tr>
<tr>
<td align="center">Cholesterol</td>
<td align="center">Examination Feature</td>
<td align="center"><code>cholesterol</code></td>
<td align="center">1: normal, 2: above normal, 3: well above normal</td>
</tr>
<tr>
<td align="center">Glucose</td>
<td align="center">Examination Feature</td>
<td align="center"><code>gluc</code></td>
<td align="center">1: normal, 2: above normal, 3: well above normal</td>
</tr>
<tr>
<td align="center">Smoking</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>smoke</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Alcohol intake</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>alco</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Physical activity</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>active</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Presence or absence of cardiovascular disease</td>
<td align="center">Target Variable</td>
<td align="center"><code>cardio</code></td>
<td align="center">binary</td>
</tr>
</tbody>
</table>

## Tasks

Create a chart similar to Figure_1.png, where we show the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.

Use the data to complete the following tasks in medical_data_visualizer.py:

- Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
- Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
- Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. The chart should look like Figure_1.png.
- Clean the data. Filter out the following patient segments that represent incorrect data:
diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
  - height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
  - height is more than the 97.5th percentile
  - weight is less than the 2.5th percentile
  - weight is more than the 97.5th percentile
- Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle. The chart should look like examples/Figure_2.png.
- Any time a variable is set to None, make sure to set it to the correct code.