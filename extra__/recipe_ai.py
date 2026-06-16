# import json
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Load dataset
# with open("recipes.json", "r") as f:
#     data = json.load(f)

# # Convert to DataFrame
# df = pd.DataFrame(data)

# # Combine ingredients into single string
# df["ingredients_text"] = df["Ingredients"].apply(lambda x: " ".join(x))

# # Create TF-IDF model
# vectorizer = TfidfVectorizer(stop_words="english")
# tfidf_matrix = vectorizer.fit_transform(df["ingredients_text"])
# #
# # Function to predict recipe
# def recommend_recipe(user_ingredients):
#     user_text = " ".join(user_ingredients)
    
#     user_vec = vectorizer.transform([user_text])
    
#     similarity = cosine_similarity(user_vec, tfidf_matrix)
    
#     best_index = similarity.argmax()
    
#     recipe = df.iloc[best_index]
    
#     return {
#         "name": recipe["Name"],
#         "ingredients": recipe["Ingredients"],
#         "method": recipe["Method"]
#     }

# # 🔥 Test input
# if __name__ == "__main__":
#     user_input = input("Enter ingredients (comma separated): ")
#     user_ingredients = [i.strip() for i in user_input.split(",")]
    
#     result = recommend_recipe(user_ingredients)
    
#     print("\n🍽️ Recommended Recipe:", result["name"])
#     print("\n🧾 Ingredients:")
#     for i in result["ingredients"]:
#         print("-", i)
    
#     print("\n👨‍🍳 Method:")
#     for step in result["method"]:
#         print("-", step)




import json
import pandas as pd
from tkinter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
with open("recipes.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Combine ingredients
df["ingredients_text"] = df["Ingredients"].apply(lambda x: " ".join(x))

# TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["ingredients_text"])

# Recommendation Function
def recommend_recipe():
    user_input = entry.get()

    user_ingredients = [i.strip() for i in user_input.split(",")]

    user_text = " ".join(user_ingredients)
    user_vec = vectorizer.transform([user_text])

    similarity = cosine_similarity(user_vec, tfidf_matrix)

    best_index = similarity.argmax()

    recipe = df.iloc[best_index]

    result = f"🍽 Recipe: {recipe['Name']}\n\n"

    result += "🧾 Ingredients:\n"
    for item in recipe["Ingredients"]:
        result += f"• {item}\n"

    result += "\n👨‍🍳 Method:\n"
    for step in recipe["Method"]:
        result += f"• {step}\n"

    output.delete("1.0", END)
    output.insert(END, result)

# GUI Window
root = Tk()
root.title("Recipe Recommendation System")
root.geometry("700x600")

Label(root,
      text="Recipe Recommendation System",
      font=("Arial", 18, "bold")).pack(pady=10)

Label(root,
      text="Enter Ingredients (comma separated):").pack()

entry = Entry(root, width=60)
entry.pack(pady=5)

Button(root,
       text="Recommend Recipe",
       command=recommend_recipe,
       bg="green",
       fg="white").pack(pady=10)

output = Text(root, width=80, height=25)
output.pack(pady=10)

root.mainloop()