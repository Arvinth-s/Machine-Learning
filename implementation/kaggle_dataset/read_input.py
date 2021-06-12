import pandas
data = pandas.read_csv('heart.csv')
print(data.shape)
print(data[:1])


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

x=data[:][:-2]
print(x[:1])

x_train, x_test, y_train, y_test = train_test_split(
    x, 
)
