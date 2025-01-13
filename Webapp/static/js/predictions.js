const predictionsRaw = '{{data|safe}}'
const predictions = JSON.parse(predictionsRaw)

for (predictions in predictions) {
    const predictionStr = `${predictions}:${predictions[pred]}`
    const predictionElement = document.createElement('p').appendChild(
        document.createTextNode(predictionStr)
    )
    document.getElementById('predictions').appendChild(predictionElement)
}
