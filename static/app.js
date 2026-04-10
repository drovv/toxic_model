const textInput = document.getElementById("text");
const submitButton = document.getElementById("submit");
const statusNode = document.getElementById("status");
const resultNode = document.getElementById("result");
const resultTitleNode = document.getElementById("result-title");
const resultMetaNode = document.getElementById("result-meta");

function setStatus(message) {
    statusNode.textContent = message;
}

function resetResult() {
    resultNode.className = "result";
    resultTitleNode.textContent = "";
    resultMetaNode.textContent = "";
}

function showResult(item) {
    const isToxic = item.label === 1;
    resultNode.className = "result show " + (isToxic ? "toxic" : "safe");
    resultTitleNode.textContent = isToxic ? "Текст токсичный" : "Текст не токсичный";
    resultMetaNode.textContent = "Вероятность токсичности: " + (item.proba_toxic * 100).toFixed(1) + "%";
}

async function predict() {
    const text = textInput.value.trim();
    if (!text) {
        resetResult();
        setStatus("Введите текст для проверки.");
        return;
    }

    submitButton.disabled = true;
    setStatus("Проверка...");

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error("HTTP " + response.status);
        }

        const data = await response.json();
        showResult(data.predictions[0]);
        setStatus("");
    } catch (error) {
        resultNode.className = "result show toxic";
        resultTitleNode.textContent = "Не удалось получить ответ";
        resultMetaNode.textContent = "Проверьте, что API запущен и модель доступна.";
        setStatus(String(error));
    } finally {
        submitButton.disabled = false;
    }
}

submitButton.addEventListener("click", predict);
textInput.addEventListener("keydown", (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
        predict();
    }
});
