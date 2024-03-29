function calculateBreakEven() {
    const sodaStreamCost = parseFloat(document.getElementById('sodaStreamCost').value);
    const cartridgeCost = parseFloat(document.getElementById('cartridgeCost').value);
    const cartridgeLifespan = parseFloat(document.getElementById('cartridgeLifespan').value);
    const mixCostPerBottle = parseFloat(document.getElementById('mixCostPerBottle').value);
    const bottledSodaCostPerBottle = parseFloat(document.getElementById('bottledSodaCostPerBottle').value);

    let totalBottles = 0;
    let totalCostSodaStream = sodaStreamCost;
    let cartridgesUsed = 0;

    while (true) {
        let totalLiters = totalBottles * 0.8;
        let cartridgesNeeded = Math.ceil(totalLiters / cartridgeLifespan);
        
        if (cartridgesNeeded > cartridgesUsed) {
            cartridgesUsed = cartridgesNeeded;
        }
        
        let co2Cost = cartridgesUsed * cartridgeCost;
        let mixCost = totalBottles * mixCostPerBottle;
        let totalCostSodaStream = sodaStreamCost + co2Cost + mixCost;
        let totalCostBottledSoda = totalBottles * bottledSodaCostPerBottle;
        
        if (totalCostSodaStream <= totalCostBottledSoda) {
            break;
        }
        
        totalBottles++;
    }
    
    document.getElementById('result').innerHTML = `Break-even point: ${totalBottles} bottles <br> At the break-even point, SodaStream cost: $${totalCostSodaStream.toFixed(2)}, Bottled Soda cost: $${totalCostBottledSoda.toFixed(2)}`;
}
