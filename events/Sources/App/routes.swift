import Vapor

func routes(_ app: Application) throws {
    app.get { req in
        return "It works!"
    }
    
    app.get("event") { req in
        return "GET /event"
    }
    
    app.post("v1", "event") { req -> Event in
        do {
            return try createEvent(req: req)
        } catch {
            throw Abort(.internalServerError)
        }
    }
}
