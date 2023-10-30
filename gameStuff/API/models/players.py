import json
from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class CookieScore(db.Model):
    __tablename__ = 'cookiescore'
    #Define Class Schema
    id = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    cookieScore = db.Column(db.Integer, unique=False, nullable=False)
    clickerCost = db.Column(db.Integer, unique=False, nullable=False)
    clickerCount = db.Column(db.Integer, unique=False, nullable=False)
    doubleCost = db.Column(db.Integer, unique=False, nullable=False)
    doubleCount = db.Column(db.Integer, unique=False, nullable=False)
    plusCount = db.Column(db.Integer, unique=False, nullable=False)
    rateCost = db.Column(db.Integer, unique=False, nullable=False)
    rate = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, id, ccScore, cCost, cCount, dbCost, dbCount, pCount, rCost, rate):
        self.playerID = id
        self.cookieScore = ccScore
        self.clickerCost = cCost
        self.clickerCount = cCount
        self.doubleCost = dbCost
        self.doubleCount = dbCount
        self.plusCount = pCount
        self.rateCost = rCost
        self.rate = rate

    
    def __repr__(self):
        return "CookieScore(" + str(self.playerID) + "," + str(self.cookieScore) + "," + str(self.clickerCost) + "," + str(self.clickerCount) + "," + str(self.doubleCost) + "," + str(self.doubleCount) + "," + str(self.plusCount) + "," + str(self.rateCost) + "," + str(self.rate) + ")"
    
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    def read(self):
        return {
            "playerID": self.playerID,
            "cookieScore": self.cookieScore,
            "clickerCost": self.clickerCost,
            "clickerCount": self.clickerCount,
            "doubleCost": self.doubleCost,
            "doubleCount": self.doubleCount,
            "plusCount": self.plusCount,
            "rateCost": self.rateCost,
            "rate": self.rate
        }
    
    def update(self, ccScore, cCost, cCount, dbCost, dbCount, pCount, rCost, rate):
        #Convvert values into integers
        ccScore = int(ccScore)
        cCost = int(cCost)
        cCount = int(cCount)
        dbCost = int(dbCost)
        dbCount = int(dbCount)
        pCount = int(pCount)
        rCost = int(rCost)
        rate = int(rate)

        #Check to see if values are higher than previous values
        if ccScore > self.cookieScore:
            self.cookieScore = ccScore
        if cCost > self.clickerCost:
            self.clickerCost = cCost
        if cCount > self.clickerCount:
            self.clickerCount = cCount
        if dbCost > self.doubleCost:
            self.doubleCost = dbCost
        if dbCount > self.doubleCount:
            self.doubleCount = dbCount
        if pCount > self.plusCount:
            self.plusCount = pCount
        if rCost > self.rateCost:
            self.rateCost = rCost
        if rate > self.rate:
            self.rate = rate

class BinaryScore(db.Model):
    __tablename__ = 'binaryscore'
    #Define Class Schema
    id = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    binaryScore = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, id, bScore):
        self.playerID = id
        self.binaryScore = bScore
    
    def __repr__(self):
        return "BinaryScore(" + str(self.playerID) + "," + str(self.binaryScore) + ")"
    
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    def read(self):
        return {
            "playerID": self.playerID,
            "binaryScore": self.binaryScore
        }
    
    def update(self, bScore):
        #Convvert values into integers
        bScore = int(bScore)

        #Check to see if score is higher than previous score
        if bScore > self.binaryScore:
            self.binaryScore = bScore

class GuessScore(db.Model):
    __tablename__ = 'guessscore'
    #Define Class Schema
    id = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    guessScore = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, id, gScore):
        self.playerID = id
        self.guessScore = gScore
    
    def __repr__(self):
        return "GuessScore(" + str(self.playerID) + "," + str(self.guessScore) + ")"
    
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    def read(self):
        return {
            "playerID": self.playerID,
            "guessScore": self.guessScore
        }
    
    def update(self, gScore):
        #Convvert values into integers
        gScore = int(gScore)

        #Check to see if score is higher than previous score
        if gScore > self.guessScore:
            self.guessScore = gScore

class player(db.Model):
    __tablename__= 'players'

    id = db.Column(db.Integer, primary_key=True)

    _username = db.Column(db.Text, unique=True, nullable=False)

    #Relationships between the tables
    cookiescore = db.relationship("CookieScore", cascade='all, delete', backref='players', lazy=True)
    binaryscore = db.relationship("BinaryScore", cascade='all, delete', backref='players', lazy=True)
    guessscore = db.relationship("CookieScore", cascade='all, delete', backref='players', lazy=True)

    def __init__(self, username, fullname):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username
    
    def get_id(self):
        return self.id
    
    def __str__(self):
        return json.dumps(self.read())
    
    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    #CRUD read: Read converts self to dictionary
    #Returns dictionary
    def read(self):
        return {
            "id": self.id,
            "username": self.username,
            "cookieScore": self.cookieScore,
            "binaryScore": self.binaryscore,
            "guessScore": self.guessScore
        }
    
    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, username=""):
        #only updates values with length
        if len(username) > 0:
            self.username = username
        db.session.commit()
        return self
    
    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
    
