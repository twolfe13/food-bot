from flask import Flask, render_template, request
import random
import re


app = Flask(__name__)



### Endpoints ###
@app.route("/")
def index():
    return render_template('index.html')


    
DINNER_RESPONSE = ['chicken and fries','beef and rice', 'pasta', 'milanesa', 'chicken nuggets', 'burgers', 'chorizo']
LUNCH_RESPONSE = ['hot dogs', 'salad and fruit', 'fruit or yogurt']
BREAKFAST_RESPONSE = ['cereal', 'nuts','waffles', 'granola']
DINNER_DRINK_RESPONSE = ['water', 'beer', 'nuts', 'wine']
LUNCH_DRINK_RESPONSE = ['water', 'nuts' 'beer', 'wine']
BREAKFAST_DRINK_RESPONSE = ['coffee', 'black tea', 'orange juice']



@app.route("/order/register", methods=['POST'])


def register():
  #  response = respond(message)
    meal_order=request.form['meal_order']
    # Create a pattern for checking if the keywords occur
    meal_keywords = re.compile('lunch|breakfast|dinner|Dinner|Lunch|Breakfast')
    # Create a pattern for finding keywords present
    if meal_keywords.search(meal_order):
        new_words = meal_keywords.findall(meal_order)
    
    else:
    
        return render_template('order_details.html', meal_order="meal invalid!", drink_order="drink invalid!")
    
    
    if len(new_words) > 0:
            # Return the name if the keywosrds are present
        meal_finished = ''.join(new_words)
        
    if  "dinner" or "Dinner" in meal_finished:
        meal_finished = define_order(DINNER_RESPONSE)
        drink_finished = define_order(DINNER_DRINK_RESPONSE)
        
        return render_template('order_details.html', meal_order=meal_finished, drink_order=drink_finished) 
        
    elif "lunch" or "Lunch" in meal_finished:
        meal_finished = define_order(LUNCH_RESPONSE)
        drink_finished = define_order(LUNCH_DRINK_RESPONSE)
        
        return render_template('order_details.html', meal_order=meal_finished, drink_order=drink_finished) 
        
    elif "breakfast" or "Breakfas" in meal_finished:
        meal_finished = define_order(BREAKFAST_RESPONSE)
        drink_finished = define_order(BREAKFAST_DRINK_RESPONSE)
    
        return render_template('order_details.html', meal_order=meal_finished, drink_order=drink_finished) 
    
    else: 
        return render_template('order_details.html', meal_order="meal invalid!", dirnk_order="drink invalid!")
    

    
### Internal Methods  ###
def define_order(order_items):
    return random.choice(order_items)

    
@app.route("/order/register", methods=['GET'])
def render_register_form():
    return render_template('register.html')
    
    


### Run APP ###
if __name__ == "__main__":
    app.run(port=8080)
