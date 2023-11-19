from models.models import Option, Ingredient

old_options = [
    Option(
        first_option=Ingredient(
            name="Chicken",
            type="meat",
            imageLink="https://www.aldelis.com/wp-content/uploads/2017/10/beneficios-pollo.jpg"
            ), 
        second_option=Ingredient(
            name="Tofu",
            type="tofu",
            imageLink="https://www.fitforfun.de/files/images/201706/1/geschnittener-tofu-in-schuessel,251508_1x1_xl.jpg"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Indian",
            type="exotic",
            imageLink="https://i.etsystatic.com/33245026/r/il/1f9336/3612599268/il_570xN.3612599268_ccik.jpg"
            ), 
        second_option=Ingredient(
            name="Thai",
            type="exotic",
            imageLink="https://i.etsystatic.com/33245026/r/il/f13729/3660574045/il_570xN.3660574045_2s5z.jpg"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Spicy",
            type="exotic",
            imageLink="https://images.pexels.com/photos/11659382/pexels-photo-11659382.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            ), 
        second_option=Ingredient(
            name="Not spicy",
            type="not exotic",
            imageLink="https://cdn3.iconfinder.com/data/icons/food-grade-2/29/food-grade-mild-512.png"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Mushroom",
            type="mushroom",
            imageLink="https://hips.hearstapps.com/hmg-prod/images/types-of-mushrooms-1644507973.jpeg?crop=0.668xw:1.00xh;0.112xw,0&resize=640:*"
            ), 
        second_option=Ingredient(
            name="Salad",
            type="healthy",
            imageLink="https://hellolittlehome.com/wp-content/uploads/2022/08/garden-salad-recipe-2.jpg"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Hot",
            type="hot",
            imageLink="https://images.pexels.com/photos/672636/pexels-photo-672636.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            ), 
        second_option=Ingredient(
            name="Cold",
            type="cold",
            imageLink="https://images.pexels.com/photos/10902065/pexels-photo-10902065.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Vegetarian",
            type="vegetarian",
            imageLink="https://images.pexels.com/photos/4871111/pexels-photo-4871111.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            ), 
        second_option=Ingredient(
            name="Chicken",
            type="meat",
            imageLink="https://www.aldelis.com/wp-content/uploads/2017/10/beneficios-pollo.jpg"
            ),
        ),
]

new_options = [
    Option(
        first_option=Ingredient(
            name="Vegan",
            type="Vegan",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/vegan-southwest-veggie-sandos-6957f718.jpg"
            ), 
        second_option=Ingredient(
            name="Bacon",
            type="Bacon",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/58b9ac35043c3c4cc663f0b3-b5c9e4a8.png"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Cinnamon",
            type="Cinnamon",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/554a35e54dab71636c8b456b.png"
            ), 
        second_option=Ingredient(
            name="Garlic",
            type="Garlic",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/554a363df8b25e1d268b456b-15867d90.png"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Chickpeas",
            type="Chickpeas",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/554a4024f8b25e1d268b4570.png"
            ), 
        second_option=Ingredient(
            name="Shellfish",
            type="Shellfish",
            imageLink="https://images.pexels.com/photos/7636375/pexels-photo-7636375.jpeg?auto=compress&cs=tinysrgb&w=600"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Hot Sauce",
            type="Hot Sauce",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/55670feafd2cb911068b4567-46f2f18b.png"
            ), 
        second_option=Ingredient(
            name="Creamy Balsamic Dressing",
            type="Creamy Balsamic Dressing",
            imageLink="https://images.pexels.com/photos/6493568/pexels-photo-6493568.jpeg?auto=compress&cs=tinysrgb&w=600"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Pulled Pork",
            type="Pulled Pork",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/5a3ae989c288004c1b048582-81479546.png"
            ), 
        second_option=Ingredient(
            name="Vegan",
            type="Vegan",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/vegan-southwest-veggie-sandos-6957f718.jpg"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Black Beans",
            type="Black Beans",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/5550dd6bfd2cb92b1a8b4567.png"
            ), 
        second_option=Ingredient(
            name="Jasmine Rice",
            type="Jasmine Rice",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/55b7845df8b25ed9088b4567.png"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Pulled Pork",
            type="Pulled Pork",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/5a3ae989c288004c1b048582-81479546.png"
            ), 
        second_option=Ingredient(
            name="Chicken Cutlets",
            type="Chicken Cutlets",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/59c2b202c288007f56514711-21c62ba7.png"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Spicy",
            type="Spicy",
            imageLink="https://images.pexels.com/photos/11659382/pexels-photo-11659382.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            ), 
        second_option=Ingredient(
            name="Milk",
            type="Milk",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/64a4fb113223226bfd2b8b2f-5e7aee28.jpeg"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Apple",
            type="Apple",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/554a3a7cf8b25ed7288b456b.png"
            ), 
        second_option=Ingredient(
            name="Orange",
            type="Orange",
            imageLink="https://img.hellofresh.com/faktorq_auto/recipes/image/554a4033f8b25ed7288b456e.png"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Mexican Cheese Blend",
            type="Mexican Cheese Blend",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/5afc835e30006c4576393862-ffdf37af.jpg"
            ), 
        second_option=Ingredient(
            name="Belgian Waffle",
            type="Belgian Waffle",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/62cdf229bab594ff4e0b3b94-77140223.jpg"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Apple",
            type="Apple",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/554a3a7cf8b25ed7288b456b.png"
            ), 
        second_option=Ingredient(
            name="Orange",
            type="Orange",
            imageLink="https://img.hellofresh.com/q_auto/recipes/image/554a4033f8b25ed7288b456e.png"
            ),
        ),
    Option(
        first_option=Ingredient(
            name="Jalapeño",
            type="Jalapeño",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/55561153fd2cb9521f8b4568-d95ff4b4.png"
            ), 
        second_option=Ingredient(
            name="Sweet Soy Glaze",
            type="Sweet Soy Glaze",
            imageLink="https://img.hellofresh.com/q_auto/recipes/ingredient/5e04ea2c1413cb766f30181c-6c56bd3d.png"
            ),
        ),
]


options = new_options