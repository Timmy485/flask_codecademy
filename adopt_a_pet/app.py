from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return """
  <h1>Adopt a Pet</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbit">Rabbits</a></li>
  </ul>
  """

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f'<h1>List of {pet_type}</h1>'
    for i, pet in enumerate(pets.get(pet_type, [])):
        html += f'<ul><li><a href="/animals/{pet_type}/{i}">{pet["name"]}</a></li></ul>'
    return html
  

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet_type_list = pets.get(pet_type, [])
    if pet_id < len(pet_type_list):
        selected_pet = pet_type_list[pet_id]
        pet_name = selected_pet['name']
        img = selected_pet['url']
        para = selected_pet['description']
        return f"""
        <h1>{pet_name}</h1>
        <img src={img}/>
        <p>{para}</p>
        <ul>
          <li>Breed: {selected_pet['breed']}</li>
          <li>Age: {selected_pet['age']}</li>
        </ul>
        """
    else:
        return f'<h1>Pet not found</h1>'