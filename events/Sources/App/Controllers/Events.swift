import Vapor

struct Event: Content {
    var effect: String
    var end: String
    var name: String
    var namespace: String
    var start: String
}

func createEvent(req: Request) throws -> Event {
    let event = try req.content.decode(Event.self)
    return event
}
