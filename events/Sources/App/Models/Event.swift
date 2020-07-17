import Vapor
import Fluent
import FluentMySQLDriver

final class Event: Model, Content {
    // Name of the table or collection.
    static let schema = "event"

    // Unique identifier for this Planet.
    @ID(key: .id)
    var id: UUID?

    // The Planet's name.
    @Field(key: "effect")
    var effect: String
    
    @Field(key: "end")
    var end: String
    
    @Field(key: "name")
    var name: String
    
    @Field(key: "namespace")
    var namespace: String
    
    @Field(key: "start")
    var start: String

    // Creates a new, empty Planet.
    init() { }

    // Creates a new Planet with all properties set.
    init(id: UUID? = nil, name: String) {
        self.id = id
        self.name = name
    }
}


