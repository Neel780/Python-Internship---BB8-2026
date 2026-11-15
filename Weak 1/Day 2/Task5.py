height_cm = "175"
weight_kg = "68.5"

height_num = float(height_cm)
weight_num = float(weight_kg)

height_m = height_num / 100

BMI = weight_num / (height_m * height_m)
print("BMI:", BMI)