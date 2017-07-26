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
        compare_array = ["COMPARISON ", " ", " ", abs(self.GP - name.GP), abs(self.goals - name.goals),
                         abs(self.assists - name.assists), abs(self.points - name.points),
                         abs(self.plusminus - name.plusminus), abs(self.pim - name.pim), abs(self.sog - name.sog),
                         abs(self.shootpct - name.shootpct), abs(self.gwg - name.gwg), abs(self.avgtoi - name.avgtoi),
                         abs(self.ppg - name.ppg), abs(self.ppa - name.ppa), abs(self.shgoal - name.shgoal),
                         abs(self.shassist - name.shassist), abs(self.shootoutgoal - name.shootoutgoal),
                         abs(self.shootoutattempt - name.shootoutattempt)]
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
