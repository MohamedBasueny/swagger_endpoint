"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# System modules

# 3rd party modules
from flask import make_response, abort





# Data to serve with our API
Pets = {
    "0": [],
   
    "1": 
       [],
   
    "2": []
}





def create(pet_id,user_name,bid):
    """
    This function creates a new bid in the Pets structure
    based on the passed in Pets data
    :param  pet_id:  pet_id to pay bid on 
    :param  user_name: user name who pay a bid 
    :param  bid:  amount of bid 

    :return:        201 on success, 404 pet not found
    """
    

    # Does the person exist already?
    if pet_id in Pets:
        temp_dict={}
        temp_dict[user_name] =bid 
        Pets[pet_id].append(temp_dict)        
        return make_response(
            " amount of {bid}  successfully payed by {user}".format(bid=bid,user=user_name), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            404,
            "Pet with id {pet_id} doesn't exist".format(pet_id=pet_id),
        )




def list_bids(pet_id):
    """
    This function lists all bids made on a certain pet
    based on the passed in person data
    :param pet_id:  pet to pay bid on 
    :return:   201 on success, 404 on  pet not found
    """
    

    # Does the person exist already?
    if pet_id in Pets:
        
        
        return make_response(
            " all bids are \n {bids} ".format(bids=Pets[pet_id]), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            404,
            "Pet with id {pet_id} doesn't exist".format(pet_id=pet_id),
        )










