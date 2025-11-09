import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib

df = pd.read_csv("learning_data.csv")

X = df[['disability_type']]  
y = df['content_type']

le_dis = LabelEncoder()
le_con = LabelEncoder()
X_enc = le_dis.fit_transform(X['disability_type']).reshape(-1,1)
y_enc = le_con.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X_enc, y_enc, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification report:\n", classification_report(y_test, y_pred, target_names=le_con.classes_))

joblib.dump(clf, "model.pkl")
joblib.dump(le_dis, "le_disability.pkl")
joblib.dump(le_con, "le_content.pkl")
print("Saved model.pkl, le_disability.pkl, le_content.pkl")
