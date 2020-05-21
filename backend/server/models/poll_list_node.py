class PollListNode:
    """Model for Polllist Data Node"""

    subgroup = ""
    modeldate = ""
    startdate = ""
    enddate = ""
    pollster = ""
    grade = ""
    samplesize = ""
    population = ""
    weight = ""
    influence = ""
    dem = ""
    rep = ""
    adjusted_dem = ""
    adjusted_rep = ""
    multiversions = ""
    tracking = ""
    url = ""
    poll_id = ""
    question_id = ""
    createddate = ""
    timestamp = ""

    def __init__(
        self,
        subgroup,
        modeldate,
        startdate,
        enddate,
        pollster,
        grade,
        samplesize,
        population,
        weight,
        influence,
        dem,
        rep,
        adjusted_dem,
        adjusted_rep,
        multiversions,
        tracking,
        url,
        poll_id,
        question_id,
        createddate,
        timestamp,
    ):
        self.subgroup = subgroup
        self.modeldate = modeldate
        self.startdate = startdate
        self.enddate = enddate
        self.pollster = pollster
        self.grade = grade
        self.samplesize = samplesize
        self.population = population
        self.weight = weight
        self.influence = influence
        self.dem = dem
        self.rep = rep
        self.adjusted_dem = adjusted_dem
        self.adjusted_rep = adjusted_rep
        self.multiversions = multiversions
        self.tracking = tracking
        self.url = url
        self.poll_id = poll_id
        self.question_id = question_id
        self.createddate = createddate
        self.timestamp = timestamp

    def serialize(self):
        return {
            "subgroup": self.subgroup,
            "modeldate": self.modeldate,
            "startdate": self.startdate,
            "enddate": self.enddate,
            "pollster": self.pollster,
            "grade": self.grade,
            "samplesize": self.samplesize,
            "population": self.population,
            "weight": self.weight,
            "influence": self.influence,
            "dem": self.dem,
            "rep": self.rep,
            "adjusted_dem": self.adjusted_dem,
            "adjusted_rep": self.adjusted_rep,
            "multiversions": self.multiversions,
            "tracking": self.tracking,
            "url": self.url,
            "poll_id": self.poll_id,
            "question_id": self.question_id,
            "createddate": self.createddate,
            "timestamp": self.timestamp,
        }
