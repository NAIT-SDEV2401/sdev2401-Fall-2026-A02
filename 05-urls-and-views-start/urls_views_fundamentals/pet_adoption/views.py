from django.shortcuts import render

PET_TYPES = {
    'dog': {
        'name': 'Dog',
        'traits': 'Loyal, energetic, needs space and exercise.',
        'lifestyle_fit': 'active'
    },
    'cat': {
        'name': 'Cat',
        'traits': 'Independent, cuddly, low-maintenance.',
        'lifestyle_fit': 'quiet'
    },
    'rabbit': {
        'name': 'Rabbit',
        'traits': 'Gentle, small, requires calm environment.',
        'lifestyle_fit': 'quiet'
    },
    'parrot': {
        'name': 'Parrot',
        'traits': 'Social, intelligent, needs stimulation.',
        'lifestyle_fit': 'social'
    }
}

# Create your views here.
def home_page(request):
    # we're passing in the dictionary of pets to the template
    return render(request, "pet_adoption/home_page.html", {"pet_types": PET_TYPES})

# Let's add a new view to handle the pet type details
def pet_type_details(request, pet_type):
    # context
    
    pet_data = PET_TYPES.get(pet_type, None)

    context = {
        "pet_type": pet_type, # this from the url
        "pet_data": pet_data
    }
    return render(request, "pet_adoption/pet_details.html", context)
