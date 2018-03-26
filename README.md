# python_rest

This project is an example of a RESTful python api written using best practices.

# Context

This application is expected to act as a database facade. In a microservice system architecture, one does not expect all services (internal or external) to interact directly with the database. Instead, the data api acts as a layer separating the database and other services which need to interact with it. 

This application could alternatively be expanded upon and used as a "regular service" if the consumer is not interested in conforming to a traditional microservice architecture. Indeed, this probably represents the more common use case.
