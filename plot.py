import matplotlib.pyplot as plt 
  
# x-coordinates of left sides of bars  
left = [1, 2, 3] 
  
# heights of bars 
height = [72.94,88.97,92.97] 
  
# labels for bars 
tick_label = ['NB','SVM','ANN'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green']) 
  
# naming the x-axis 
plt.xlabel('Algorithms') 
# naming the y-axis 
plt.ylabel('Accuracies') 
# plot title 
plt.title('Comparative Study On Fake News Accuracy Detection') 
  
# function to show the plot 
plt.show() 
