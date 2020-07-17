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
            throw Abort(.notFound)
        }
    }
    
    app.get("hello", ":name") { req -> String in
        guard let name = req.parameters.get("name", as: String.self) else {
            throw Abort(.badRequest)
        }
        return "Hello \(name)"
    }
}
