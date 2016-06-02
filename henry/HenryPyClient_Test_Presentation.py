#!/usr/bin/env python

#
# This is a sample Python client used to test the connection and communication
# with Henry, which is running on an Amazon cloud server. This is important because
# Henry runs complex baseball simulations that require significant computing power.
# In other words, we can install Henry on a powerful server anywhere in the cloud
# and create a web-based user interface into it. Here we used a third-party software
# called ZeroC Ice to handle the networking and bridge between Python and C++.
#

# Import the ZeroC Ice files
import sys, traceback, Ice

# Import the Python interface into Henry's C++ code
import HenryIce

# Ice requires us to inherit from their Application class
class HenryPyClient(Ice.Application):
    # Ice requires us to override the run method
	def run(self, args):

        # Get the interface or API for Henry's data service, which
		# provides higher level access to the sqlite database, meaning it
		# does all the joins etc and provides formatted reports instead of
		# raw data. Example below. 
		dataSvc = HenryIce.DataSvcPrx.checkedCast(\
            self.communicator().propertyToProxy('DataSvc.Proxy').ice_twoway().ice_secure(False))
        if not dataSvc:
            print(args[0] + ": invalid proxy")
            return 1

        # Simple function call to get the version of Henry running on the server
		version = dataSvc.henryVersion()
        print("Henry version=" + version)

        # Get the list of teams for the 2015 season, which can then be displayed
		# on the screen, e.g., in an HTML table
		teams = dataSvc.teamNames(2015)
        print("Team names for 2015:")
        for team in teams:
            print(team)

        # Now get the lineup for the first team, which returns the player's
		# name and position. Again, this info would be displayed on the screen
		print("2015 lineup for "+teams[0])
        lineup = dataSvc.defaultLineup(teams[0],'R',2015)
        for player in lineup:
            print(player)
			
		# Note, the above are just a couple of examples of how to use the dataSvc.
		# It also provides many more functions that make it easy to create web-
		# based (or other) user interfaces for displaying data and interacting with
		# Henry running on a remote (cloud) server.

        return 0

# Create the client and run it!
app = HenryPyClient()
sys.exit(app.main(sys.argv, "config.client"))
