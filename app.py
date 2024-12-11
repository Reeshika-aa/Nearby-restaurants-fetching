from flask import Flask, render_template
import random

app = Flask(__name__)

# Simulated data
village_menu = {
    "Pancakes": 8.50,
    "Omelets": 10.00,
    "Burgers": 12.00,
    "Grilled Chicken Salad": 11.50,
    "Fish Tacos": 13.00
}

restaurants = {
    "Beef 'O' Brady's": {
        "rating": 4.7,
        "menu": {"Five Cheese Burger": 12, "Chicken Wings": 9, "Funnel Fries": 5}
    },
    "Kumo Sushi & Hibachi": {
        "rating": 4.6,
        "menu": {"California Roll": 8, "Chicken Teriyaki": 14, "Spicy Tuna Roll": 10}
    },
    "TooJay’s Deli": {
        "rating": 4.3,
        "menu": {"Reuben Sandwich": 11, "Corned Beef": 12, "Matzo Ball Soup": 6}
    },
    "McGrady's Pub": {
        "rating": 4.6,
        "menu": {"Shepherd’s Pie": 14, "Fish & Chips": 13, "Scotch Eggs": 8}
    },
    "The Standard Coffee Shop": {
        "rating": 4.8,
        "menu": {"Iced Latte": 5, "Mocha Blender": 6, "Ginger Salad": 8}
    }
}

def get_weather():
    temp_kelvin = random.uniform(270, 300)
    rain_conditions = random.choice(["None", "Light Rain", "Moderate Rain", "Heavy Rain"])
    temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
    return round(temp_fahrenheit, 2), rain_conditions

@app.route("/")
def home():
    temp_f, rain_conditions = get_weather()
    is_busy = random.choice([True, False])
    predicted_prices = {}
    
    for item, price in village_menu.items():
        if temp_f < 45 or rain_conditions in ["Moderate Rain", "Heavy Rain"] or is_busy:
            predicted_prices[item] = round(price * 1.15, 2)
        else:
            predicted_prices[item] = price

    return render_template("index.html",
                           village_menu=village_menu,
                           restaurants=restaurants,
                           weather=(temp_f, rain_conditions),
                           is_busy=is_busy,
                           predicted_prices=predicted_prices)

if __name__ == "__main__":
    app.run(debug=True)
