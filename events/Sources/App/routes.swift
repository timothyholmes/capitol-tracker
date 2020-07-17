import Vapor

func routes(_ app: Application) throws {
    app.get { req in
        return "It works!"
    }
    
    app.get("event") { req in
        return "GET /event"
    }
    
    
    app.on(.POST, "v1", "event", body: .collect(maxSize: "1mb")) { req -> String in
        return "POST /event"
    }
    
    app.get("hello", ":name") { req -> String in
        guard let name = req.parameters.get("name", as: String.self) else {
            throw Abort(.badRequest)
        }
        return "Hello \(name)"
    }
}
