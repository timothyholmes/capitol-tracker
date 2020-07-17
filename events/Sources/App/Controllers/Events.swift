import Vapor

func createEvent(req: Request) throws -> Event {
    let event = try req.content.decode(Event.self)
    return event
}

