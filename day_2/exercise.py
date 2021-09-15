# ITP Week 4 Day 2 Exercise

#Today we will pull information from the Pokemon api, put it into a dictionary, and then put that info into a new Excel file.  We will write the pseudocode as a group in class.  Be sure to follow the pseudocode, break your problems down into smaller pieces, and consult the documentation whenever you get stuck: https://pokeapi.co/docs/v2

#PSEUDO-CODE:

#GET NAME AND ABILITY FROM API
#PUT INFO IN DICTIONARY
#ADD THE DICTIONARY TO A NEW EXCEL WORKBOOK

#https://pokeapi.co/api/v2/pokemon

## abilities into a list (name)
## ability is a dictionary
## when it's done you will have a dictionary

# imports:
    #json
    #openpyxl

# input
    #json file from pokemon api
    #workbook

#Assign response to variable

#Create workbook
    #get workbook from openpy
    #load workbook
    #assign it to a variable

#Create Worksheet
    #assign it to a variable

#Create a dictionary, assign to a variable

#Function body
    #convert response to json file
        #clean data(response)
            #json.loads(response.text)

    #iterate over response
        #for each pokemon in response
            #variable key = pokemon.name
            #variable value = pokemon.abilities
            #Append (key/value) pair to dictionary

    #iterate over dictionary
        #for each item in dictionary
            #assign dictionary values to rows & columns
                #Write name to cell
                #Write abilities to cell

# output
    #Workbook

my_pokemon = {
    bulbasaur : {
        "name":"pokemon_name",
        "abilities": ["ability1", "ability2"]
    },
    pikachu : {
        "name":"pokemon_name",
        "abilities": ["ability1", "ability2"]
    }
}