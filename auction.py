'''
the script is used for Geanarlized-2nd-auction calculation
* it's assumed that pets id is already created 
* only accepted bids on existing pets
* for simplisity, 3 pets id available --> [0,1,2] 
* in production , the script will get available pets and bids made on them as
input ,   and outputs: the winning users
'''    
# Data to serve with our API
Pets_bids = {
    "0": [],
   
    "1": [],
   
    "2": []
}

count_pets_items =  {
     "0": 3,
   
    "1": 2,
   
    "2": 1
    }

def create_pets_bids(pet_id,user_name,bid):
   
    """
    This function creates a new bid in the Pets structure
    based on the passed in Pets data
    :param  pet_id:  pet_id to pay bid on 
    :param  user_name: user name who pay a bid 
    :param  bid:  amount of bid 
    """
# Does the person exist already?
    if pet_id in Pets_bids:
        Pets_bids[pet_id].append([user_name,bid])   
    else:
        print(pet_id,"Not Found")
        
        
def auction(Pets_bids,count_pets_items):
    '''
    calculates the winning users,
    takes as input : available pets and bids on them
    the auction can only be made if only :
        
        count_pets_items < num of users on a ceratain pet 

    Parameters
    ----------
    Pets : Data about pets and bids on them 
    
    count_pets_items : count of items available for each Pets
    
    Returns
    resault of the auction    '''
# =============================================================================
#Is the Auction Valid --> num of Bids > num of Pets
    for i in Pets_bids:
        assert  len(Pets_bids[i]) != count_pets_items[i] , ("Invalid auction for Pet {}".format(i))
# =============================================================================
       
# =============================================================================
#checking for pets available for auctions 
    n_pets_avail = len(Pets_bids.keys())
     
    if n_pets_avail == 0 :
        print('No Pets available for auctions')
        return None    
# =============================================================================
        
# =============================================================================
#sort bids on each pet in descending order according to amount of bid payed
# incase of equal amount of Bids (tie-breaker) --> use alphapitical order
    total_sorted = []
    for bid in Pets_bids:
        sorted_users = {bid:list(zip(*sorted(Pets_bids[bid],key=lambda x: x[1], reverse=True)))}
        # print(sorted_users)
# In case of no bids show the message No Winners
        if len(sorted_users[bid]) == 0:
            print('No Winners for Pet with id {id}'.format(id=bid))
            # return('No Winners for Pet with id {id}'.format(id=bid))

            continue
        total_sorted.append(sorted_users)
# =============================================================================

# =============================================================================
#output of the auction for each Pet
    for pet in total_sorted:
        # print(pet)
        for k,v in pet.items():
            items_avail = count_pets_items.get(k)
            # print(items_avail)
            # pet[k]=list(zip(*v))
            print("for pet {0} there are {1} items available".format(k,items_avail))
             # [print(v[0][i]," : " ,v[1][i+1]) for i in range(len(v[0]))]
            for i in range(len(v[0])):
                if items_avail >0:
                    print(v[0][i]," : " ,v[1][i+1])
                    items_avail -=1    
                else: print(v[0][i]," : " ,"Lost")
    return ""
# =============================================================================
                               
    
create_pets_bids('0','mo',10)   
create_pets_bids('0','moo',100)    
create_pets_bids('0','aoooo',10000)    
create_pets_bids('0','boooo',10000)    

create_pets_bids('1','mo',10)    
# create_pets_bids('1','moo',100)    
create_pets_bids('1','aoooo',10000)    
create_pets_bids('1','boooo',10000)   
 
create_pets_bids('2','mo',10)    
create_pets_bids('2','moo',100)    
create_pets_bids('2','aoooo',10000)    
create_pets_bids('2','boooo',10000)   


if __name__ == "__main__":
    # print(auction(Pets_bids,count_pets_items))   
   res= auction(Pets_bids,count_pets_items)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    