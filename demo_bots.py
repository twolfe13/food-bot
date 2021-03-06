from flask import Flask, render_template, request
import random


app = Flask(__name__)


### Endpoints ###
@app.route("/")
def index():
    return render_template('index.html')

# Used if they weren't combined on the 1st / 'home page'
"""
@app.route("/order/register", methods=['GET'])
def render_register_form():
    return render_template('register.html')
"""

@app.route("/order/register", methods=['POST'])
def register():
    meal_order=request.form['meal_order']
    DINNER_RESPONSE = ['pollo y fritas','carne y arroz', 'pasta', 'milanesa', 'nuggests', 'hamburguesas', 'chorizo / asado']
    LUNCH_RESPONSE = ['hot dogs', 'salad and fruit', 'fruit or yogurt']
    BREAKFAST_RESPONSE = ['cereal', 'waffles', 'granola']
    HOT_DRINK_RESPONSE = ['black tea', 'green tea', 'coffee']
    COLD_DRINK_RESPONSE = ['agua', 'cervesa', 'vino']
        
    if "dinner" or "Dinner" in meal_order: 
        meal_finished = define_order(DINNER_RESPONSE)
        drink_finished = define_order(COLD_DRINK_RESPONSE)
    elif "lunch" or "Lunch" in meal_order:
        meal_finished = define_order(LUNCH_RESPONSE)
        drink_finished = define_order(COLD_DRINK_RESPONSE)
    elif "breakfast" or "Breakfast" in meal_order:
        meal_finished = define_order(BREAKFAST_RESPONSE) 
        drink_finished = define_order(HOT_DRINK_RESPONSE)
    else:
        meal_finished = "Please order breakfast, lunch, or dinner :)"
        drink_finished = "Sorry, we don't have drinks for" + " " + meal_order + "!"
            
        
    return render_template('order_details.html', meal_order=meal_finished, drink_order=drink_finished)


### Internal Methods  ###
def define_order(order_items):
    return random.choice(order_items)

### Run APP ###
if __name__ == "__main__":
    app.run(port=8080)
