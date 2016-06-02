#!/usr/bin/env python

import sys, traceback, Ice

import HenryIce

class HenryPyClient(Ice.Application):
    def run(self, args):
        if len(args) > 1:
            print(self.appName() + ": too many arguments")
            return 1

        dataSvc = HenryIce.DataSvcPrx.checkedCast(\
            self.communicator().propertyToProxy('DataSvc.Proxy').ice_twoway().ice_secure(False))
        if not dataSvc:
            print(args[0] + ": invalid proxy")
            return 1

        version = dataSvc.henryVersion()
        print("Henry version=" + version)

        teams = dataSvc.teamNames(2015)
        print("Team names for 2015:")
        for team in teams:
            print(team)

        print("2015 lineup for "+teams[0])
        lineup = dataSvc.defaultLineup(teams[0],'R',2015)
        for player in lineup:
            print(player)

        return 0

app = HenryPyClient()
sys.exit(app.main(sys.argv, "config.client"))
