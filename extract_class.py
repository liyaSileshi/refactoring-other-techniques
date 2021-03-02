# Extract Class


class Foods:

    def __init__(self, foods_object):
        self.foods_object = foods_object
    
    def get_name(self, key):
        print("Name:", key)

    def get_prep_time(self, prep_time):
        print("Prep time:", prep_time, "mins")

    def is_veggie(self, is_veggie):
        print("Is Veggie?", 'Yes' if is_veggie else "No")

    def get_food_type(self, food_type):
        print("Food Type:", food_type)

    def get_cuisine(self, cuisine):
        print("Cuisine:", cuisine)

    def get_ingredients(self, ingredient_arr):
        for item in ingredient_arr:
            print(item, end=', ')

    def get_recipe(self, recipe):
        print("recipe", recipe)


if __name__ == "__main__":
    foods = {'butternut squash soup':[45, True, 'soup','North African',\
        ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
            ,'1. Grill the butter squash, onion, carrot and garlic in the oven until'
            'they get soft and golden on top 2. Put all in blender with'
            'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
                '. Add coconut milk. Simmer for 5 mintues.'],
            'shirazi salad':[5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
                '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                    '4. Mixed them thoroughly'],
            'Home-made Beef Sausage': [60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
                'corriander seeds','black pepper seeds','fennel seed','paprika'],'1. In a blender,'
                    ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                    'the seasonings 2. In a bowl, mix ground beef with the'
                    'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                    "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}

    foods = Foods(foods) #initialize foods class
    for key, value in foods.foods_object.items():
        foods.get_name(key)
        foods.get_prep_time(value[0])
        foods.is_veggie(value[1])
        foods.get_food_type(value[2])
        foods.get_cuisine(value[3])
        foods.get_ingredients(value[4])
        print()
        foods.get_recipe(value[5])
        print("***")

