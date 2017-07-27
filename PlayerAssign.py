from texttable import Texttable

class PlayerAssign():
    def __init__(self, name, position, team, GP, goals, assists, points, plusminus, pim, sog, shootpct, gwg, toi, ppg,
                 ppa, shgoal, shassist, shootoutgoal, shootoutattempt):

        self.name = name.string
        self.position = position.string
        self.team = team.string
        self.GP = GP.string
        self.goals = goals.string
        self.assists = assists.string
        self.points = points.string
        self.plusminus = plusminus.string
        self.pim = pim.string
        self.sog = sog.string
        self.shootpct = shootpct.string
        self.gwg = gwg.string
        self.avgtoi = toi.string
        self.ppg = ppg.string
        self.ppa = ppa.string
        self.shgoal = shgoal.string
        self.shassist = shassist.string
        self.shootoutgoal = shootoutgoal.string
        self.shootoutattempt = shootoutattempt.string

    def comparison(self, name):

        compare_array = ["Difference", str(abs(int(self.GP) - int(name.GP))), str(abs(int(self.goals) - int(name.goals))),
                         str(abs(int(self.assists) - int(name.assists))), str(abs(int(self.points) - int(name.points))),
                         str(abs(int(self.plusminus) - int(name.plusminus))), str(abs(int(self.pim) - int(name.pim))), str(abs(int(self.sog) - int(name.sog))),
                         str(abs(round(float(self.shootpct) - float(name.shootpct),2))), str(abs(int(self.gwg) - int(name.gwg))), "TBD",
                         str(abs(int(self.ppg) - int(name.ppg))), str(abs(int(self.ppa) - int(name.ppa))), str(abs(int(self.shgoal) - int(name.shgoal))),
                         str(abs(int(self.shassist) - int(name.shassist)))]
        return compare_array

    def Table(self, name):
        table = Texttable()
        table.set_cols_width([20, 8, 6, 4, 6, 8, 8, 4, 5, 5, 8, 5, 7, 5, 5, 7, 7, 13, 15])
        compare = self.comparison(name)
        table.add_rows([["NAME", "POSITION", "TEAM", "GP", "GOALS", "ASSISTS", "POINTS", "+/-", "PIM", "SOG",
                         "Shooting %", "GWG", "TOI", "PPG", "PPA", "SHG", "SHA", "SHOOTOUT GOAL", "SHOOTOUT ATTEMPT"],
                        [self.name, self.position, self.team, self.GP, self.goals, self.assists, self.points,
                         self.plusminus, self.pim, self.sog, self.shootpct, self.gwg, self.avgtoi, self.ppg, self.ppa,
                         self.shgoal, self.shassist, self.shootoutgoal, self.shootoutattempt],
                        [name.name, name.position, name.team, name.GP, name.goals, name.assists, name.points,
                         name.plusminus, name.pim, name.sog, name.shootpct, name.gwg, name.avgtoi, name.ppg, name.ppa,
                         name.shgoal, name.shassist, name.shootoutgoal, name.shootoutattempt]])
        table.add_row(compare)
        print(table.draw())
