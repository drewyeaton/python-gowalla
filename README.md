#Gowalla Python Client

This python-gowalla library is a thin layer that exposes Gowalla's heretofore unconfirmed API. Although the data structure is likely to be a moving target, it hasn't changed in the past couple weeks. For now, this client only supports Gowalla's read-only methods. As these calls are largely undocumented, I've only tested the ones that I have discovered.


##Usage

See **gowallatest.py** for example usage.


##Requirements

- [Python](http://python.org/) (2.5 or greater, but not 3.x)


##Known Methods

###Get User
Returns information on a Gowalla user. Excepts username or user id.

	/users/USERNAME.FORMAT
	/users/USER_ID.FORMAT


###List User's Friends
Returns a list of the user's friends. Excepts username or user id. **This currently returns an empty list.**

	/users/USER_ID/friends.FORMAT
	/users/USERNAME/friends.FORMAT


###List User's Vaulted Items
Returns a list of the user's vaulted items. Excepts username or user id.

	/users/USER_ID/vault.FORMAT
	/users/USERNAME/vault.FORMAT


###Get Spot
Returns information on a Gowalla spot.

	/spots/SPOT_ID.FORMAT


###List Spot's Items
Returns a list of the items at a Gowalla spot.

	/spots/SPOT_ID/items.FORMAT


###List Trips
Returns a list of "official" Gowalla trips. This is likely to change as user contributed trips becomes live.

	/trips.FORMAT 


###Get Trip 
Returns information on a Gowalla trip.

	/trips/TRIP_ID.FORMAT


###Get Item
Returns information on a Gowalla item.

	/items/ITEM_ID.FORMAT


###List Items
Returns a list of all Gowalla items.

	/items.FORMAT


###List Item's Events
Returns a list of things that have "happened" to the item.

	/items/ITEM_ID/events.FORMAT