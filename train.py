

# Load Dataset
dataset_path = "/content/drive/MyDrive/AI_Safety_App/final_dataset_big_update.parquet"
df = pd.read_parquet(dataset_path)

print(df.shape)
print(df['label'].value_counts())

## Generate Embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
embeddings = embedding_model.encode(df['text'].tolist(), show_progress_bar=True)

# Save embeddings + labels for reuse
np.save("/content/drive/MyDrive/AI_Safety_App/embeddings.npy", embeddings)
df['label'].to_csv("/content/drive/MyDrive/AI_Safety_App/labels.csv", index=False)

# Split Data for Training
X_train, X_test, y_train, y_test = train_test_split(
    embeddings, df['label'], test_size=0.2, random_state=42, stratify=df['label']
)

# Train Classifier
clf = LGBMClassifier(n_estimators=500, learning_rate=0.05)
clf.fit(X_train, y_train)

# Evaluate Prediction
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Bundle model
model_bundle = {
    "vectorizer": embedding_model,  # sentence transformer
    "model": clf
}

joblib.dump(model_bundle, "/content/drive/MyDrive/AI_Safety_App/model_bundle.pkl")
