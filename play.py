class Play:
    FIELDS = [
        "GAME_ID",
        "EVENTNUM",
        "EVENTMSGTYPE",
        "EVENTMSGACTIONTYPE",
        "PERIOD",
        "WCTIMESTRING",
        "PCTIMESTRING",
        "HOMEDESCRIPTION",
        "NEUTRALDESCRIPTION",
        "VISITORDESCRIPTION",
        "SCORE",
        "SCOREMARGIN",
        "PERSON1TYPE",
        "PLAYER1_ID",
        "PLAYER1_NAME",
        "PLAYER1_TEAM_ID",
        "PLAYER1_TEAM_CITY",
        "PLAYER1_TEAM_NICKNAME",
        "PLAYER1_TEAM_ABBREVIATION",
        "PERSON2TYPE",
        "PLAYER2_ID",
        "PLAYER2_NAME",
        "PLAYER2_TEAM_ID",
        "PLAYER2_TEAM_CITY",
        "PLAYER2_TEAM_NICKNAME",
        "PLAYER2_TEAM_ABBREVIATION",
        "PERSON3TYPE",
        "PLAYER3_ID",
        "PLAYER3_NAME",
        "PLAYER3_TEAM_ID",
        "PLAYER3_TEAM_CITY",
        "PLAYER3_TEAM_NICKNAME",
        "PLAYER3_TEAM_ABBREVIATION"
    ]

    def __init__(self, fields):
        self.fields = dict(zip(self.FIELDS, fields))

    def is_sub(self):
        return self.fields["EVENTMSGTYPE"] == 8

    def score(self):
        if self.fields["SCORE"]:
            return [int(s) for s in self.fields["SCORE"].split(" - ")]

    def home_control(self):
        if self.fields["HOMEDESCRIPTION"] and not self.fields["VISITORDESCRIPTION"]:
            return true
        if self.fields["VISITORDESCRIPTION"] and not self.fields["HOMEDESCRIPTION"]:
            return false

    def get_players(self):
        if self.fields["PLAYER1_ID"] and self.fields["PLAYER1_TEAM_ID"]:
            yield [self.fields["PLAYER1_ID"], self.fields["PLAYER1_TEAM_ID"]]
        if self.fields["PLAYER2_ID"] and self.fields["PLAYER2_TEAM_ID"]:
            yield [self.fields["PLAYER2_ID"], self.fields["PLAYER2_TEAM_ID"]]
        if self.fields["PLAYER3_ID"] and self.fields["PLAYER3_TEAM_ID"]:
            yield [self.fields["PLAYER3_ID"], self.fields["PLAYER3_TEAM_ID"]]
