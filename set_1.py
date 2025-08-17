import math

def savings(gross_pay, tax_rate, expenses):
    return math.floor(
        (gross_pay * (1 - tax_rate)) - expenses
    )

def material_waste(total_material, material_units, num_jobs, job_consumption):
    material_wasted = total_material - (job_consumption * num_jobs)
    return f"{material_wasted}{material_units}"

def interest(principal, rate, periods):
    total_interest = principal * (rate * periods)
    return math.floor(principal + total_interest)

# for my own testing
def main():
    print(f"Savings: {savings(100000, 0.124352, 50000)}")
    print(f"Material Waste: {material_waste(100, "L", 11, 5)}")
    print(f"Interest: {interest(1000, 0.0002, 12)}")

if __name__ == "__main__":
    main()