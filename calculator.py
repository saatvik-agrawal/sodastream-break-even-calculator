import math

def calculate_break_even_bottles(soda_stream_cost, cartridge_cost, cartridge_lifespan, mix_cost_per_nine_liters, bottled_soda_cost_per_liter):
    """
    Calculates the break-even point (in 0.8L bottles) for using a SodaStream.
    The mix cost is provided per 9 liters and is converted to a cost per 0.8L bottle.
    The bottled soda cost is provided per liter and converted to a cost per 0.8L bottle.
    
    Parameters:
      - soda_stream_cost: Cost of the SodaStream machine.
      - cartridge_cost: Cost of one CO2 cartridge.
      - cartridge_lifespan: Lifespan of a cartridge in liters.
      - mix_cost_per_nine_liters: Cost of syrup mix per 9 liters.
      - bottled_soda_cost_per_liter: Cost of bottled soda per liter.
    
    Returns:
      A tuple containing:
         (number of 0.8L bottles at break-even, total SodaStream cost, total bottled soda cost)
    """
    # Convert mix cost per 9 liters to cost per 0.8 liter bottle.
    # (9 liters = 9000 ml; one bottle = 800 ml)
    mix_cost_per_800ml = mix_cost_per_nine_liters / (9000 / 800)
    
    # Convert bottled soda cost per liter to cost per 0.8 liter bottle.
    bottled_soda_cost_per_800ml = bottled_soda_cost_per_liter * 0.8

    total_bottles = 0
    cartridges_used = 0

    while True:
        total_liters = total_bottles * 0.8  # Total liters produced from the current number of bottles.
        # Calculate the number of cartridges needed using ceiling division.
        cartridges_needed = math.ceil(total_liters / cartridge_lifespan)
        cartridges_used = max(cartridges_used, cartridges_needed)
        
        co2_cost = cartridges_used * cartridge_cost
        mix_cost = total_bottles * mix_cost_per_800ml
        total_cost_sodastream = soda_stream_cost + co2_cost + mix_cost
        total_cost_bottled_soda = total_bottles * bottled_soda_cost_per_800ml
        
        # Break when the cost of using the SodaStream is less than or equal to buying bottled soda.
        if total_cost_sodastream <= total_cost_bottled_soda:
            break
        
        total_bottles += 1

    return total_bottles, total_cost_sodastream, total_cost_bottled_soda

if __name__ == "__main__":
    # Console-based testing.
    soda_stream_cost = float(input("Cost of the SodaStream machine: "))
    cartridge_cost = float(input("Cost of CO2 cartridge: "))
    cartridge_lifespan = float(input("Lifespan of a cartridge (in liters): "))
    mix_cost_per_nine_liters = float(input("Cost of mix per 9 liters: "))
    bottled_soda_cost_per_liter = float(input("Cost of bottled soda per liter: "))
    
    result = calculate_break_even_bottles(soda_stream_cost, cartridge_cost, cartridge_lifespan, mix_cost_per_nine_liters, bottled_soda_cost_per_liter)
    print(f"Break-even point: {result[0]} bottles")
    print(f"At the break-even point, SodaStream cost: ${result[1]:.2f}, Bottled Soda cost: ${result[2]:.2f}")
    