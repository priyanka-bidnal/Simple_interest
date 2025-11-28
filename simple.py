import sys

if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    print("User provided values:")
else:
    principal = 1000.0  
    rate = 5.0          
    time = 2.0     
    print("No input provided — using default values:")

simple_interest = (principal * rate * time) / 100

print("\n----- SIMPLE INTEREST CALCULATOR -----")
print("Principal:", principal)
print("Rate of Interest (%):", rate)
print("Time (years):", time)
print("Simple Interest:", simple_interest)
