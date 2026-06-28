from ai.predict import predict_clothing

prediction, confidence = predict_clothing(
    "dataset/test/shirt/01.jpg"
)

print(prediction)
print(confidence)