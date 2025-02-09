import pandas as pd
from imblearn.under_sampling import TomekLinks
from collections import Counter
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("M:\\Techsaksham_by_Microsoft_Project\\Project\\dataset\\parkinsons.csv")

# Assume the target column is the status variable
X = df.drop(columns=['name' , 'status'] , axis=1)
Y = df['status']

print("Before Tomek Links:", Counter(Y))

tomek = TomekLinks()
X_resampled, y_resampled = tomek.fit_resample(X, Y)

print("After Tomek Links:", Counter(y_resampled))


df_resampled = pd.DataFrame(X_resampled, columns=X.columns)
df_resampled["status"] = y_resampled  

# Save the cleaned dataset
df_resampled.to_csv("parkinsons_tomeklinks.csv", index=False)

print("Tomek Links under-sampling applied and saved as 'parkinsons_tomeklinks.csv'")


# for each csv do the same and replacethe target variables 