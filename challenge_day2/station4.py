def solution_station_4(x):
    if x<= OR x>58.50:
        return "True"
    else
        return "False"


#How I found the pattern:
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier, export_text

sample_input = [22, 73, 67, 89, 8, 42, 2, 21, 50, 2]
sample_output = [False, True, True, True, False, False, True, False, False, True]

df = pd.DataFrame({"input": sample_input, "output": sample_output})
    
input = df[["input"]]
output = df["output"]

tree_model = DecisionTreeClassifier()
tree_model.fit(input, output)

#tree_rules = export_text(tree_model, feature_name = ["input"])
tree_rules = export_text(tree_model)
print("Pattern found \n", tree_rules)


#OUTPUT:  
#|--- feature_0 <= 58.50
#|   |--- feature_0 <= 5.00
#|   |   |--- class: True
#|   |--- feature_0 >  5.00
#|   |   |--- class: False
#|--- feature_0 >  58.50
#|   |--- class: True







