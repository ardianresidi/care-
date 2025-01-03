function handleSubmit(event) {
    event.preventDefault();  // Prevents page reload on form submission

    // Collect form data
    let age = document.getElementById("age").value;
    let smoking = document.getElementById("smoking").value;
    let symptoms = document.getElementById("symptoms").value;
    let physicalActivity = document.getElementById("physicalActivity").value;
    let airQuality = document.getElementById("airQuality").value;

    // Create a form data object
    const formData = {
        age: parseInt(age),
        smoking: smoking,
        symptoms: symptoms,
        physicalActivity: parseInt(physicalActivity),
        airQuality: airQuality
    };

    // Display the submitted data
    displaySubmittedData(formData);

    // Generate medical advice
    const advice = generateMedicalAdvice(formData);

    // Display the advice
    displayAdvice(advice);
}

function generateMedicalAdvice(formData) {
    let riskLevel = assessRespiratoryRisk(formData);  // Assess the risk level based on inputs
    let advice = [];

    // **Low Risk**
    if (riskLevel === "Low risk for respiratory disease.") {
        advice.push("Maintain a healthy lifestyle with balanced nutrition and regular exercise.");
        advice.push("Monitor your pulmonary health regularly; consider annual check-ups.");
        advice.push("Avoid smoking and exposure to pollutants to maintain good lung function.");
    }

    // **Moderate Risk**
    if (riskLevel === "Moderate to high risk based on age." || 
        riskLevel === "High risk due to smoking history." ||
        riskLevel === "Moderate risk due to low physical activity." ||
        riskLevel === "Moderate risk based on FEV1/FVC ratio indicating mild obstruction.") {
        
        advice.push("Schedule regular check-ups with a pulmonologist, especially if you have a history of respiratory symptoms.");
        advice.push("Consider getting a spirometry test annually to monitor your lung function.");
        advice.push("Use prescribed inhalers or bronchodilators as needed, and avoid triggers like smoke and dust.");
    }

    // **High Risk**
    if (riskLevel === "High risk due to pre-existing respiratory conditions or allergies." || 
        riskLevel === "High risk based on low FEV1/FVC ratio indicating moderate to severe obstruction." ||
        riskLevel === "High risk based on frequent clinical symptoms.") {
        
        advice.push("Consult with a pulmonologist for further diagnostic tests such as spirometry and chest X-rays.");
        advice.push("Adhere strictly to prescribed treatments, including inhalers, corticosteroids, or bronchodilators.");
        advice.push("Get vaccinated for flu and pneumonia, and avoid exposure to air pollution or allergens.");
    }

    return advice;
}

function assessRespiratoryRisk(formData) {
    // Basic risk assessment based on input data
    let risk = "Low risk for respiratory disease.";

    // Example risk factors (you can modify based on your specific conditions)
    if (formData.age >= 60 || formData.smoking === "current" || formData.airQuality === "poor") {
        risk = "Moderate to high risk based on age and/or air quality.";
    }
    if (formData.smoking === "former" || formData.physicalActivity < 2) {
        risk = "Moderate to high risk due to smoking history and low physical activity.";
    }

    return risk;
}

function displaySubmittedData(formData) {
    // Show the "Your Submitted Data" section
    const submittedDataDiv = document.getElementById("submittedData");
    submittedDataDiv.style.display = "block";  // Make the section visible

    // Display the submitted details
    const submittedDetailsDiv = document.getElementById("submittedDetails");
    submittedDetailsDiv.innerHTML = `
        <p><strong>Age:</strong> ${formData.age}</p>
        <p><strong>Smoking History:</strong> ${formData.smoking}</p>
        <p><strong>Symptoms:</strong> ${formData.symptoms}</p>
        <p><strong>Physical Activity (hours/week):</strong> ${formData.physicalActivity}</p>
        <p><strong>Air Quality:</strong> ${formData.airQuality}</p>
    `;
}

function displayAdvice(advice) {
    // Get the advice output container
    const adviceOutput = document.getElementById("adviceOutput");

    // Clear any existing advice
    adviceOutput.innerHTML = "";

    // Display the new advice
    advice.forEach(item => {
        const paragraph = document.createElement("p");
        paragraph.textContent = item;
        adviceOutput.appendChild(paragraph);
    });
}
Your